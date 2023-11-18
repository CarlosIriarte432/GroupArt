from venv import logger
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
import requests
import json
import hmac
import hashlib
from django.http import JsonResponse

from Services.models import Service


# Credenciales
api_key_prod = '50E11F7A-68F6-49BD-9F15-5F252L237FCC'
secret_key_prod = 'afc9ad0b71268e0fb47463af3053b0cd107f4610'

# Endpoint
prod_url = 'https://www.flow.cl/api'
pay_service = '/payment/create'
status_service = '/payment/getStatus'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

def make_signature(params, secret_key):
        sorted_params = sorted(params.items())
        msg = ''.join([f'{key}{value}' for key, value in sorted_params])
        secret_key_bytes = bytes(secret_key, 'utf-8')
        sig = hmac.new(secret_key_bytes, msg=bytes(msg, 'utf-8'), digestmod=hashlib.sha256).hexdigest()
        return sig
    
class Payment():
    def create_payment(request):
        print(request)
        amount = request.POST.get('amount')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        user_id = int(request.POST.get('id'))
        commerce_order = int(request.POST.get('commerce_order'))
        params = {
            'apiKey': api_key_prod,
            'commerceOrder': commerce_order,
            'subject': subject,
            'currency': 'CLP',
            'amount': amount,
            'email': email,
            'urlConfirmation': 'http://localhost:8000/services/confirm_pay',
            'urlReturn': 'http://localhost:8000/services/return_pay',
        }
        params['s'] = make_signature(params, secret_key_prod)
        url = prod_url + pay_service
        response = requests.post(url=url, data=params, headers=headers)
        jsonResp = response.json()
        url_response = ''
        if response.status_code == 200:
            token = jsonResp['token']
            url_resp = jsonResp['url']
            order = str(jsonResp['flowOrder'])
            url_response = url_resp + '?token=' + token
            try:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO payment_payment (`order`, id_user, token) VALUES (%s, %s, %s)", (order, user_id, token))
                    cursor.execute("UPDATE Services_service SET availability = 0, order_number = %s WHERE id = %s", (order, commerce_order))
            except Exception as e:
                print(f"Error en metodo create_payment de 'order' y 'token': {order}, {token}")
                print(e)

        else:
            url_response = 'error_page'
        return HttpResponseRedirect(url_response)

    def get_payment_status(token):
        params = {
        'apiKey': api_key_prod,
        'token': token
        }

        params['s'] = make_signature(params, secret_key_prod)
        url = prod_url + status_service
        response = requests.get(url=url, params=params, headers=headers)
        jsonResp = response.json()
        status = 0
        if response.status_code == 200:
            status = jsonResp['status']
        return status
    
    def update_state_order(request):
        token = request.GET.get('token')
        print(token, request.GET, request)
        status = Payment.get_payment_status(token)
        if status is not None:
            newStatus = int(status)
            with connection.cursor() as cursor:
                cursor.execute("UPDATE payment_payment SET status = %s WHERE token = %s", (newStatus, token))
        return HttpResponse(status)
    
    def return_last_user_token(request):
        user_id = int(request.GET.get('user_id'))
        token = 0

        with connection.cursor() as cursor:
            cursor.execute("SELECT token FROM payment_payment WHERE id_user = %s and status = 0 ORDER BY `order` DESC LIMIT 1", [user_id])
            result = cursor.fetchone()

        if result:
            token = result[0]

        return JsonResponse({'token': token})
    
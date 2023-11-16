document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("toggleSidebar");
    const sidebar = document.querySelector(".sidebar");

    toggleButton.addEventListener("click", function () {
        sidebar.classList.toggle("collapsed");
    });
});

function showDetails(titulo, creadoPor, fecha, descripcion, precio, disponibilidad, categoria, estado, id){
    document.getElementById("titulo").innerHTML = titulo;
    document.getElementById("subject").value = titulo;
    document.getElementById("creadoPor").innerHTML = "Creado por: " + creadoPor;
    document.getElementById("fecha").innerHTML = "Fecha: " + fecha;
    document.getElementById("descripcion").innerHTML = "Descripción: " + descripcion;
    document.getElementById("precio").innerHTML = "Precio: $" + precio;
    document.getElementById("amount").value = precio;
    document.getElementById("disponibilidad").innerHTML = "Disponibilidad: " + disponibilidad;
    document.getElementById("categoria").innerHTML = "Categoría: " + categoria;
    document.getElementById("estado").innerHTML = "Estado: " + estado;
    document.getElementById("id").innerHTML = id;
    document.getElementById("commerce_order").value = id;
    document.getElementById("details").style.display = "block";
    document.getElementById("service-boxes").style.filter = "blur(3px)";
    blockCards();
}

function closeDetails(){
    document.getElementById("details").style.display = "none";
    document.getElementById("service-boxes").style.filter = "none";
    unblockCards();
}

function blockCards(){
    var cards = document.getElementsByClassName("service-card");
    for (var i = 0; i < cards.length; i++) {
        cards[i].className += " block-card";
    }
}

function unblockCards(){
    var cards = document.getElementsByClassName("service-card");
    for (var i = 0; i < cards.length; i++) {
        cards[i].classList.remove("block-card");
    }
}

function openFlow(url){
    var left = (screen.width/2)-390;
      var top = (screen.height/2)-355;
       winConfig = "width=780,height=710, directories=no, titlebar=no, toolbar=no, location=no, status=no, menubar=no, scrollbars=no, resizable=no, top="+top+", left="+left;
       window.open(
           url,
           "Contratacion GroupArt",
           winConfig).focus();
   }

function createPayment(email){
    var precio = document.getElementById("precio").value;
    var titulo = document.getElementById("titulo").innerHTML;
    var id = document.getElementById("id").value;
    window.location.href = "/Payment/amount="+ precio+"/subject='" + titulo+"'/commerce_order="+id+"/email='"+email+"'";
}

function updateStatus(token){
    $.ajax({
        url: 'http://localhost:8000/Payment/update',  // Reemplaza con la URL correcta de tu vista
        type: 'GET',
        dataType: 'json',  // Puedes cambiar el tipo de datos según lo que esperas del servidor
        data: {
            // Si tu vista espera parámetros, los puedes enviar de esta manera
            token: token,
        },

        success: function (data) {
            // Maneja la respuesta exitosa del servidor
            console.log('Dato actualizado');
        },

        error: function (error) {
            // Maneja el error
            console.error('error');
        }
    });
}


$(document).ready(function () {
    // Ahora puedes usar $ normalmente
    updateStatus();
});
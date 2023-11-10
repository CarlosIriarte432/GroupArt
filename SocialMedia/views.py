from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

from django.contrib.auth.decorators import login_required
def wall(request):
    posts = Post.objects.all()
    return render(request, 'social/wall.html', {'posts': posts})

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('wall')  # Cambia 'home' con la URL a la que deseas redirigir después de publicar
    else:
        form = PostForm()

    return render(request, 'social/create_post.html', {'form': form})
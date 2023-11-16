from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from .forms import EditPostForm  

from django.contrib.auth.decorators import login_required
def wall(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(content__icontains=query)
    return render(request, 'social/wall.html', {'posts': posts, 'query': query})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('wall') 
    else:
        form = PostForm()

    return render(request, 'social/create_post.html', {'form': form})


def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = EditPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('wall')  
    else:
        form = EditPostForm(instance=post)

    return render(request, 'social/edit_post.html', {'form': form})


def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.user == post.user:
        if request.method == 'POST':
            post.delete()
            return redirect('wall')

        return render(request, 'social/delete_post.html', {'post': post})

    return redirect('wall')
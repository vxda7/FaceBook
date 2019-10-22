from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("posts:index")
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'posts/form.html', context)


def like(request, id):
    post = get_object_or_404(Post, id=id)
    user = request.user
    # if user in post.like_users.all():
    if user.like_posts.filter(id=id):
        user.like_posts.remove(post)
    else:
        user.like_posts.add(post)

    return redirect("posts:index")
    
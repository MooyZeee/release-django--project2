from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.utils import timezone

from .forms import PostForm
from .models import MyPost


def index(request):
    posts = MyPost.objects.filter().order_by('published_date')
    return render(request, 'blog/index.html', {'posts': posts})


def work_post(request):
    posts = MyPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/work.html', {'posts': posts})

# def category(request, catid):
#     return HttpResponse(f"<h1>Cats{catid}</h1>")
#
#
# def pageNotFound(request, exception):
#     return HttpResponseNotFound("<h1>Странциа не найдена</h1>")


def post_info(request, pk):
    post = get_object_or_404(MyPost, pk=pk)
    return render(request, 'blog/post_info.html', {'post': post})


def post_new(request, pk):
    post = get_object_or_404(MyPost, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_info', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/new_post.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(MyPost, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_info', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/new_post.html', {'form': form})


def post_draft(request):
    posts = MyPost.objects.filter(published_date__isnull=True).order_by('created_date')
    print(posts)
    return render(request, 'blog/draft.html', {'posts': posts})


def post_publish(request, pk):
    post = get_object_or_404(MyPost, pk=pk)
    post.publish()
    return redirect('post_info', pk=pk)


def post_del(request, pk):
    post = get_object_or_404(MyPost, pk=pk)
    post.delete()
    return redirect('index')

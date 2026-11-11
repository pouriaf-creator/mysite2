from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.db.models import F

# def blog_view(request):
#     posts = Post.objects.filter(status=1)
#     context = {'posts':posts}
#     return render(request,'blog/blog-home.html',context)

def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)


def blog_single(request, pid):
    posts = Post.objects.filter(status=1).order_by("id")
    post = get_object_or_404(posts, pk=pid)
    
    posts_list = list(posts)
    
    current_index = posts_list.index(post)
    
    previous_post = None
    next_post = None
    
    if current_index > 0:
        previous_post = posts_list[current_index - 1]
        
    if current_index < len(posts_list) - 1:
        next_post = posts_list[current_index + 1]
    
    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post':next_post
        }
    return render(request,'blog/blog-single.html', context)


def test(request,pid):
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post,pk=pid)
    context = {'post':post}
    return render(request,'test.html',context)
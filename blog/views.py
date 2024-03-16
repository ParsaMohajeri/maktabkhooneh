from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from django.utils import timezone
# from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# from blog.models import Comment
# from blog.forms import CommentForm
# from django.contrib import messages
# from django.urls import reverse
# from django.http import HttpResponseRedirect
from blog.models import Post
# Create your views here.
def blog_view(request):
    posts=Post.objects.filter(status=1,published_date__lte=timezone.now())
    # posts=Paginator(posts,4)
    # try:
    #     page_number=request.GET.get('page')
    #     posts=posts.get_page(page_number)
    # except PageNotAnInteger:
    #     posts=posts.get_page(1)
    # except EmptyPage :
    #     posts=posts.get_page(1)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)
def blog_single(request,pid):
    post = get_object_or_404(Post,pk=pid,status=1,published_date__lte=timezone.now())
    post.counted_views += 1
    post.save()
    previous_post = Post.objects.filter(id__lt=pid,status=1,published_date__lte=timezone.now()).order_by('-id').first()
    next_post = Post.objects.filter(id__gt=pid,status=1,published_date__lte=timezone.now()).order_by('id').first()
    context={'post':post,'previous_post': previous_post,'next_post': next_post}
    return render(request,'blog/blog-single.html',context)

def test(request,pid):
    # post=Post.objects.get(id=pid)
    # posts=Post.objects.all()
    # posts=Post.objects.filter(status=0)
    post = get_object_or_404(Post,pk=pid)
    context={'post':post}
    return render(request,'test.html',context)
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm


# Create your views here.

def post_create(request):
    form = PostForm(request.POST or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Post Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    
    context_data = {
        "form": form
    }

    return render(request, "post_form.html", context_data)

def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context_data = {
        "title": instance.title,
        "instance": instance
    }

    return render(request, "post_detail.html", context_data)

def post_list(request):
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 4)
    page_request_var = 'page'

    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context_data = {
        "object_list": queryset,
        "title": "Posts",
        "page_request_var": page_request_var
    }

    return render(request, "post_list.html", context_data)

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    
    form = PostForm(request.POST or None, instance=instance)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Post Saved")
        return HttpResponseRedirect(instance.get_absolute_url())     

    context_data = {
        "title": instance.title,
        "instance": instance,
        "form": form
    }

    return render(request, "post_form.html", context_data)

def post_delete(request, id):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Post Deleted")
    return redirect("posts:list")
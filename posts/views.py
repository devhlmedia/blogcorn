from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import PostForm
from .models import Post

# Create your views here.

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        
    # if request.method == "POST":
    #     print request.POST.get("content")
    #     print request.POST.get("title")
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)

def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "list"
    }
    return render(request, "index.html", context)
    # if request.user.is_authenticated():
    #     context = {
    #         "title": "My user list"
    #     }
    # else:
    #     context = {
    #         "title": "list"
    #     }



def post_update(request):
    return HttpResponse("<h1>Hello update!</h1>")

def post_delete(request):
    return HttpResponse("<h1>Hello delete!</h1>")

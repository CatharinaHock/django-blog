from django.shortcuts import redirect, render, get_object_or_404
from .models import Post, Tag
from django.utils import timezone, safestring
from .forms import PostForm, TagForm
#from serializers import PostSerializer, LanguageSerializer
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

# Create your views here.

def start_page(request):
    return render(request, "blog/start.html", {"display_logo": True})

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by("-published_date")
    tags = Tag.objects.all().order_by("type", "name")
    return render(request, "blog/post_list.html", {"posts": posts, "display_logo": True, "tags": tags})

def tag_post_list(request, pk):
    current_tag = get_object_or_404(Tag, pk = pk)
    tags = Tag.objects.all().order_by("type", "name")
    posts = Post.objects.filter(published_date__lte = timezone.now(), tags__exact=pk).order_by("-published_date")
    return render(request, "blog/post_list.html", {"posts": posts, 
                            "display_logo": True, "tags": tags, "current_tag": current_tag})

"""
def tag_list_post_list(request, pk_list):
    tags=[]
    posts=[]
    for pk in pk_list:
        tags.append(get_object_or_404(Tag, pk = pk))
    posts = Post.objects.filter(published_date__lte = timezone.now(), tags__exact=pk_list).order_by("-published_date")
    return render(request, "blog/post_list.html", {"posts": posts, 
                            "display_logo": True, "tags": tags, "current_tag": current_tag})
"""

def post_detail(request, pk):
    post =  get_object_or_404(Post, pk =pk)
    return render(request, "blog/post_detail.html", {"post":post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()
            post.thumbnail = form.cleaned_data["thumbnail"]
            post.save()
            post.create_brief_description()
            post.tags.set(form.cleaned_data["tags"])
            if "thumbnail" in request.FILES.keys():
                post.thumbnail =  request.FILES["thumbnail"]
            post.save()
            return redirect("post_detail", pk = post.pk)

    else:
        form = PostForm()
    return render(request, "blog/post_edit.html", {"form": form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.tags.set(form.cleaned_data["tags"])
            post.create_brief_description()
            if "thumbnail" in request.FILES.keys():
                post.thumbnail =  request.FILES["thumbnail"]
            post.save()
            return redirect('post_detail', pk=post.pk) #render(request, "blog/post_edit.html",{"form":form, "thumbnail" : post.thumbnail})#
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, "current_post": post})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("post_list")

@login_required
def tag_new(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit = False)
            tag.save()
            return redirect("post_list")
    else:
        form = TagForm()
    return render(request, "blog/tag_edit.html", {"form": form})


a_tag = Tag.objects.filter(name__exact="Fantasy")

@login_required
def tag_edit(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            tag = form.save(commit = False)
            tag.save()
            return redirect("tag_post_list", pk=tag.pk)
    else:
        form = TagForm(instance=tag)
    return render(request, "blog/tag_edit.html", {"form": form, "current_tag":tag})

@login_required
def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    tag.delete()
    return redirect("post_list")
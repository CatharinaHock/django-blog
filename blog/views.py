from django.shortcuts import redirect, render, get_object_or_404
from .models import Post, Tag
from django.utils import timezone, safestring
from .forms import PicturePostForm, PostForm, TagForm
#from serializers import PostSerializer, LanguageSerializer
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

# Create your views here.

def start_page(request):
    featured_post = Post.objects.filter(title__exact = "Epiphany")[0]
    return render(request, "blog/start.html", {"display_logo": True, "featured_post":featured_post})

def post_list(request, isTextPost=1):
    tags = Tag.objects.all().order_by("type", "name")
    if isTextPost:
        posts = Post.objects.filter(published_date__lte = timezone.now(), post_type__exact="tex").order_by("-published_date")
        temp = "blog/post_list.html"
    else:
        posts = Post.objects.filter(published_date__lte = timezone.now()).exclude(post_type__exact = "tex").order_by("-published_date")
        temp = "blog/picture_post_list.html"
    
    return render(request, temp , {"posts": posts, "display_logo": True, "tags": tags, "isTextPost":isTextPost})

def tag_post_list(request, pk, isTextPost):
    current_tag = get_object_or_404(Tag, pk = pk)
    tags = Tag.objects.all().order_by("type", "name")
    if isTextPost==1:
        posts = Post.objects.filter(published_date__lte = timezone.now(), tags__exact=pk, post_type__exact="tex").order_by("-published_date")
    else:
        posts = Post.objects.filter(published_date__lte = timezone.now(), tags__exact=pk).exclude(post_type__exact="tex").order_by("-published_date")
    return render(request, "blog/post_list.html", {"posts": posts, 
                            "display_logo": True, "tags": tags, "current_tag": current_tag,
                            "isTextPost":isTextPost})

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
    if post.post_type == "tex":
        return render(request, "blog/post_detail.html", {"post":post, "isTextPost":1,})
    else:
        return render(request, "blog/picture_post_detail.html", {"post":post, "isTextPost":0,})

@login_required
def post_new(request, isTextPost = 1):
    if request.method == "POST":
        if isTextPost==0 :
            post_type="picture-based post"
            form = PicturePostForm(request.POST)
        else:
            post_type="text-based post"
            form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()
            post.thumbnail = form.cleaned_data["thumbnail"]
            if isTextPost!=0:
                post.post_type = "tex"
            post.save()
            post.create_brief_description()
            post.tags.set(form.cleaned_data["tags"])
            if "thumbnail" in request.FILES.keys():
                post.thumbnail =  request.FILES["thumbnail"]
            post.save()
            return redirect("post_detail", pk = post.pk)

    else:
        if isTextPost==0:
            post_type="picture-based post"
            form = PicturePostForm()
        else:
            post_type="text-based post"
            form = PostForm()
    return render(request, "blog/post_edit.html", {"form": form,"post_type":post_type})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    isTextPost = 0
    if post.post_type=="tex":
        isTextPost = 1
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if isTextPost==0:
            form = PicturePostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.tags.set(form.cleaned_data["tags"])
            post.create_brief_description()
            if isTextPost!= 0:
                post.post_type = "tex"
            if "thumbnail" in request.FILES.keys():
                post.thumbnail =  request.FILES["thumbnail"]
            post.save()

            return redirect('post_detail', pk=post.pk) #render(request, "blog/post_edit.html",{"form":form, "thumbnail" : post.thumbnail})#

    else:
        form = PostForm(instance=post)
        if not isTextPost:
            form = PicturePostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, "current_post": post})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    isTextPost = post.post_type == "tex"
    post.delete()
    return redirect("post_list", isTextPost=isTextPost)

@login_required
def tag_new(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit = False)
            tag.save()
            return redirect("post_list", isTextPost = 1)
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
            return render(request, "blog/tag_edit.html", {"form": form, "current_tag":tag})#redirect("post_list", isTextPost = 1) #redirect("tag_post_list", pk=tag.pk, isTextPost=1)
    else:
        form = TagForm(instance=tag)
    return render(request, "blog/tag_edit.html", {"form": form, "current_tag":tag})

@login_required
def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    tag.delete()
    return redirect("post_list", isTextPost=1)


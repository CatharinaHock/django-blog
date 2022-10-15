from django.shortcuts import redirect, render, get_object_or_404
from .models import Post, Tag
from django.utils import timezone
from .forms import PostForm, TagForm
#from serializers import PostSerializer, LanguageSerializer
from django.contrib.auth.decorators import login_required

# Create your views here.

def start_page(request):
    return render(request, "blog/start.html", {"display_logo": True})

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by("-published_date")
    tags = Tag.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts, "display_logo": True, "tags": tags})

def tag_post_list(request, pk):
    current_tag = get_object_or_404(Tag, pk = pk)
    tags = Tag.objects.all()
    posts = Post.objects.filter(published_date__lte = timezone.now(), tags__contains=current_tag).order_by("-published_date")
    return render(request, "blog/post_list.html", {"posts": posts, 
                            "display_logo": True, "tags": tags, "current_tag": current_tag})

def post_detail(request, pk):
    post =  get_object_or_404(Post, pk =pk)
    return render(request, "blog/post_detail.html", {"post":post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid() and form.cleaned_data["tags"].filter(type="l") != []:
            post = form.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()
            post.tags.set(form.cleaned_data["tags"])
            post.save()
            return redirect("post_detail", pk = post.pk)
    else:
        form = PostForm()
    return render(request, "blog/post_edit.html", {"form": form})

"""
# not working, so nevermind
def post_new_altered(request):
    serializer = PostSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    post = serializer.save()

    for language_id in request.data.get('language'):
        try:
            language = Language.objects.get(id=tag_id)
            post.language.add(language)
        except Language.DoesNotExist:
            raise NotFound()
    
    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
"""

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid() and form.cleaned_data["tags"].filter(type="l") != []:
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.tags.set(form.cleaned_data["tags"])
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

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

@login_required
def tag_edit(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            tag = form.save(commit = False)
            tag.save()
            return redirect("post_list")
    else:
        form = TagForm()
    return render(request, "blog/tag_edit.html", {"form": form})
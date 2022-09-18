from django.shortcuts import render
from .models import Blog, Tag, Category, Comment
from .forms import CommentForm
# from django.http import JsonResponse
from django.core.paginator import Paginator
# Create your views here.

def blog_list(request, page=1):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3) # Show 3 contacts per page
    blog_list = paginator.get_page(page)
    context = {
        "blog_list" : blog_list
    }
    return render(request, "blog/blog_list.html", context)


def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    tags = Tag.objects.all().filter(blogs=blog)
    categories = Category.objects.all()
    recents = Blog.objects.all().order_by("-created_ad")[:4] 
    comments = Comment.objects.all().filter(blog=blog)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            

            new_comment = Comment(blog=blog, name=name, email=email, message=message)
            new_comment.save()
            


            
    

    context = {
        "blog": blog,
        "tags": tags,
        "recents" : recents,
        "categories" : categories,
        "comments": comments
    }

    return render(request, "blog/blog_detail.html", context)


def blog_tag(request, tag):
    blog_list = Blog.objects.filter(tags__slug = tag)
    context = {
        "blog_list" : blog_list
    }
    return render(request, "blog/blog_list.html", context)
def blog_category(request, category):
    blog_list = Blog.objects.filter(category__slug = category)
    context = {
        "blog_list" : blog_list
    }
    return render(request, "blog/blog_list.html", context)




def search(request):
    if request.method == "GET":
        d = request.GET.get("search")
    blogs = Blog.objects.all().filter(title__icontains = d)
    return render(request, "blog/blog_list.html", context={"blog_list": blogs})
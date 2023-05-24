from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post
from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView
from .forms import CommentForm
from django.urls import reverse
def get_date(post):
    return post['date']


# Create your views here.

'''
def staring_page(request):
    latest_posts=Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html",{
        "posts":latest_posts
    })
'''
class staring_page(ListView):
    template_name="blog/index.html"
    model=Post
    ordering=["-date"]
    context_object_name="posts"
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

'''
def posts(request):
    all_posts=Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts":all_posts
    })
'''
class AllPost(ListView):
    template_name="blog/all-posts.html"
    model=Post
    ordering=["-date"]
    context_object_name="all_posts"

'''
def for_each_post(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
    
'''
class for_each_post(View):
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_later = post_id in stored_posts
        else:
            is_saved_later = False
        return is_saved_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        
        context = {
            "post":post,
            "coment_form":CommentForm(),
            "comments":post.comments.all(),
            "saved_for_later":self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)

    def post(self,request, slug):
        coment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if coment_form.is_valid():
            c = coment_form.save(commit = False)
            c.post =post
            c.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
        context = {
            "post":post,
            "coment_form":CommentForm(),
            "comments":post.comments.all(),
            "saved_for_later":self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)

 # identified_post = next(post for post in all_posts if post['slug']==slug)
              #or
    #identified_post = Post.objects.get(slug=slug)
                #or

class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
          posts = Post.objects.filter(id__in=stored_posts)
          context["posts"] = posts
          context["has_posts"] = True

        return render(request, "blog/stored-post.html", context)


    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
          stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
          stored_posts.append(post_id)
        else:
          stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts
        
        return HttpResponseRedirect("/")

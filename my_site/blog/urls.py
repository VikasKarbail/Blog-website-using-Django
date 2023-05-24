from django.urls import path
from  . import views
urlpatterns = [
    path("", views.staring_page.as_view(), name="Staring-page"),
    path("posts", views.AllPost.as_view(), name="post-page"),
    path("posts/<slug:slug>", views.for_each_post.as_view(), name="post-detail-page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]
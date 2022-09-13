from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.start_page, name="start_page"),
    path("post_list", views.post_list, name="post_list"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
    #path('', include('blog.urls')),
    path("admin/", admin.site.urls),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]   
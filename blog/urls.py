from django.urls import path, include,register_converter
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from . import views, converters
from django.conf import settings
from django.conf.urls.static import static

register_converter(converters.IntListConverter, 'intlist')

urlpatterns = [
    path('start/start/', lambda req: redirect('/start/')),
    path("", lambda req: redirect("/start/")),
    path("start/", views.start_page, name="start_page"),
    path("post_list", views.post_list, name="post_list"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name="post_delete"),
    path("tag/new/", views.tag_new, name="tag_new"),
    path("tag/<int:pk>/", views.tag_post_list, name="tag_post_list"),
    #path("tag/<intlist:pk_list>/", views.tag_list_post_list, name="tag_list_post_list"),
    path("tag/<int:pk>/edit/", views.tag_edit, name="tag_edit"),
    path("tag/<int:pk>/delete/", views.tag_delete, name="tag_delete"),
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
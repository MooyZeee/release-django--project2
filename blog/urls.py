from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('work/', views.work_post, name='work_post'),
    path('post/<int:pk>/', views.post_info, name='post_info'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft, name='post_draft'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/del/', views.post_del, name='post_del'),
]

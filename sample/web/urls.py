from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('board/<int:pk>', views.BoardView.as_view(), name='board'),
    path('board/create', views.BoardCreate, name='BoardCreate'),
    path('board/<int:pk>/delete', views.BoardDelete.as_view(), name='BoardDelete'),
    path('board/<int:pk>/update', views.BoardUpdate, name='BoardUpdate'),
    # path('search/', views.IndexView.as_view(), name='search'),
    path('board/<int:pk>/comment/new', views.CommentCreate.as_view(), name='CommentCreate'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.board,name="board"),
    path('board_detail/<int:board_id>/', views.board_detail,name="board_detail"),
    path('new/', views.new,name="new"),
    path('detail/<int:board_id>/delete', views.delete, name="delete"),
    path('detail/<int:board_id>/update', views.update, name="update"),

    path('<int:board_id>/like/', views.like, name="like"),
    path('<int:board_id>/hate/', views.hate, name="hate"),

    path('detail/<int:board_id>/comment_write', views.comment_write, name="comment_write"),
    path('detail/<int:comment_id>/comment_delete', views.comment_delete, name="comment_delete"),
    path('<int:comment_id>/comment_like/', views.comment_like, name="comment_like"),
    path('<int:comment_id>/comment_hate/', views.comment_hate, name="comment_hate"),

    path('missing', views.missing, name="missing"),
    path('missing_detail/<int:missing_id>/', views.missing_detail, name="missing_detail"),
    path('missing_new/', views.missing_new, name="missing_new"),
    path('missing_detail/<int:missing_id>/missing_delete', views.missing_delete, name="missing_delete"),
    path('missing_detail/<int:missing_id>/missing_update', views.missing_update, name="missing_update"),
]
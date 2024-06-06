from django.urls import path
from posts.views import ListPostView, DeletePostView


app_name = 'posts'
urlpatterns = [
    path('', ListPostView.as_view(), name='all_post'),
    path('<int:pk>/', DeletePostView.as_view(), name='delete_post'),
]

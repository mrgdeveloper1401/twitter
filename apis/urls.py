from rest_framework.urls import path
from apis.views import PostListAPIView, CreateUserAPIView, OtpRequestView, ProfileApiView \
    ,CreatePostAPIView, RetrievePostAPIView

app_name = 'apis'
urlpatterns = [
    path('signup/', CreateUserAPIView.as_view(), name='signup'),
    path('otp_request_mobile_phone/', OtpRequestView.as_view(), name='otp_request_mobile_phone'),
    path('profile/<int:pk>', ProfileApiView.as_view(), name='profile'),
    path('all_post/', PostListAPIView.as_view(), name='all_post'),
    path('create_post/', CreatePostAPIView.as_view(), name='create_post'),
    path('details_post/<int:pk>', RetrievePostAPIView.as_view(), name='details_post'),
]

from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView,
                                       PasswordResetConfirmView)
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('password_reset/', PasswordResetView.as_view(), name='password_reset_view'),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete', PasswordResetCompleteView.as_view(), name='password_reset_complete')
]
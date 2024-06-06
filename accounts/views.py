from django.shortcuts import render
from django.views.generic import CreateView
from accounts.models import User


class CreateUserView(CreateView):
    model = User

# Create your views here.
from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from core.models import User


class UserListView(ListView):
    model = User


class UserDetail(DetailView):
    model = User


class UserCreate(CreateView):
    model = User
    success_url = '/'
    fields = ['username', 'first_name', 'last_name', 'birthday', 'random_number']


class UserUpdate(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'birthday', 'random_number']


class UserDelete(DeleteView):
    model = User
    success_url = '/'

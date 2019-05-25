# Create your views here.
from django.utils import timezone
from django.views.generic.list import ListView

from core.models import User


class UserListView(ListView):
    model = User

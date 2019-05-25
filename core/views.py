from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic.list import ListView

from core.models import User


class UserListView(ListView):
    model = User
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
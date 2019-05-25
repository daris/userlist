from django.urls import path

from core.views import UserListView

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
]

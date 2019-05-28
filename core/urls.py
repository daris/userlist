from django.urls import path

from core.views import UserListView, UserDetail, UserUpdate, UserDelete, UserCreate

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('<int:pk>', UserDetail.as_view(), name='user_detail'),
    path('create', UserCreate.as_view(), name='user_create'),
    path('<int:pk>/edit', UserUpdate.as_view(), name='user_edit'),
    path('<int:pk>/delete', UserDelete.as_view(), name='user_delete'),
]

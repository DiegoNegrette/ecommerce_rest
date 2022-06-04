# from apps.users.api.api import UserAPIView
from apps.users.api.api import user_api_view, user_detail_api_view
from django.urls import path


urlpatterns = [
    # path('user/', UserAPIView.as_view(), name='user_api')
    path('user/', user_api_view, name='user_api'),
    path('user/<int:pk>', user_detail_api_view, name='user_detail_api_view')
]

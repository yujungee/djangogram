from django.urls import path
from . import views
from djangogram.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
   path('', views.main, name='main')
]

from django.urls import path
from . import views


app_name = 'haiku'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    # path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('inquiry.html/', views.InquiryView.as_view(), name="inquiry"),
]
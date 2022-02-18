from django.urls import path
from . import views


app_name = 'haiku'

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('detail/<int:pk>/', views.DetailView.as_view(), name="detail"),
]
from django.urls import path
from . import views


app_name = 'haiku'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('detail/', views.InquiryView.as_view(), name="detail"),
    # path('inquiry.html/', views.InquiryView.as_view(), name="inquiry"),
    path('kobo_info/', views.KoboInfoView.as_view(), name="kobo_info")
]
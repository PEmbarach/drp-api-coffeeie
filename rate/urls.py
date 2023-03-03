from django.urls import path
from rate import views

urlpatterns = [
    path('rate/', views.RateList.as_view()),
]

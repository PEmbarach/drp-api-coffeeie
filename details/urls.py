from django.urls import path
from details import views

urlpatterns = [
    path('details/', views.DetailsList.as_view()),
    path('details/<int:pk>/', views.DetailsDetail.as_view())
]

from . import views
from django.urls import path

urlpatterns = [
    path('<int:pk>', views.ExpenseDetailAPIView.as_view()),
    path('', views.ExpensesAPIView.as_view())
]
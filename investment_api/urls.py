from django.urls import path
from .views import InvestmentsView
urlpatterns = [
    path('Investments',InvestmentsView.as_view())
]
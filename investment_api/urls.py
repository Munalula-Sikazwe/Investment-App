from django.urls import path

from .views import InvestmentsView, DeleteInvestmentView,Home

urlpatterns = [
    path('',Home),
    path('api/Investments', InvestmentsView.as_view()),
    path('api/Investments/<int:pk>', DeleteInvestmentView.as_view()),

]

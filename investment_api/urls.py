from django.urls import path

from .views import InvestmentsView, ModifyInvestmentView,Home

urlpatterns = [
    path('',Home),
    path('api/Investments', InvestmentsView.as_view()),
    path('api/Investments/modify/<int:pk>', ModifyInvestmentView.as_view()),

]

from django.urls import path

from .views import InvestmentsView, DeleteInvestmentView

urlpatterns = [
    path('Investments', InvestmentsView.as_view()),
    path('Investments/Delete/<int:pk>', DeleteInvestmentView.as_view()),

]

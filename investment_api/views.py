from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView
# Create your views here.
from investment_api.serializers import InvestmentSerializer
from.models import Investment

class InvestmentsView(ListAPIView):
    serializer_class = InvestmentSerializer
    queryset = Investment.objects.all()


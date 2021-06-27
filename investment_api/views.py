from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
# Create your views here.
from investment_api.serializers import InvestmentSerializer
from.models import Investment

class InvestmentsView(ListCreateAPIView):
    serializer_class = InvestmentSerializer
    queryset = Investment.objects.all()


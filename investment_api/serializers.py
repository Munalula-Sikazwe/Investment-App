from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Investment as InvestmentModel

class InvestmentSerializer(ModelSerializer):
    investmentId = serializers.ReadOnlyField(source='id')
    class Meta:
        model = InvestmentModel
        fields = ['investmentId','username','amount','duration','investmentReturns']


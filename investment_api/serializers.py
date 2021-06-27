from rest_framework.serializers import ModelSerializer
from .models import Investment as InvestmentModel

class InvestmentSerializer(ModelSerializer):
    class Meta:
        model = InvestmentModel
        fields = ['username','amount','duration','investmentReturns']

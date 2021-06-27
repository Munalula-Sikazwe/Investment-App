from rest_framework.serializers import ModelSerializer
from .models import Investment as InvestmentModel

class InvestmentSerializer(ModelSerializer):
    model = InvestmentModel
    fields = ['id','user_name','amount','duration','investment_returns']
    
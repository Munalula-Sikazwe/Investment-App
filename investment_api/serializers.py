from rest_framework.serializers import ModelSerializer, ReadOnlyField

from .models import Investment as InvestmentModel


class InvestmentSerializer(ModelSerializer):
    investmentId = ReadOnlyField(source='id')

    class Meta:
        model = InvestmentModel
        fields = ['investmentId', 'username', 'amount', 'duration', 'investmentReturns']

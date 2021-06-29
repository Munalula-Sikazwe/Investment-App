from rest_framework.generics import ListCreateAPIView, DestroyAPIView

# Create your views here.
from investment_api.serializers import InvestmentSerializer
from .models import Investment


# from rest_framework.permissions import IsAuthenticatedOrReadOnly


class InvestmentsView(ListCreateAPIView):
    serializer_class = InvestmentSerializer
    queryset = Investment.objects.all()
    # permission_classes = [IsAuthenticatedOrReadOnly]

class DeleteInvestmentView(DestroyAPIView):
    queryset = Investment.objects.all()

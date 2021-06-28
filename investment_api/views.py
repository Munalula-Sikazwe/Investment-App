from rest_framework.generics import ListCreateAPIView
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
from investment_api.serializers import InvestmentSerializer
from .models import Investment


class InvestmentsView(ListCreateAPIView):
    serializer_class = InvestmentSerializer
    queryset = Investment.objects.all()
    # permission_classes = [IsAuthenticatedOrReadOnly]

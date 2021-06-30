from rest_framework.generics import ListCreateAPIView, DestroyAPIView

# Create your views here.
from investment_api.serializers import InvestmentSerializer
from .models import Investment
from django.shortcuts import HttpResponse

# from rest_framework.permissions import IsAuthenticatedOrReadOnly


class InvestmentsView(ListCreateAPIView):
    serializer_class = InvestmentSerializer
    queryset = Investment.objects.all()
    # permission_classes = [IsAuthenticatedOrReadOnly]


class DeleteInvestmentView(DestroyAPIView):
    queryset = Investment.objects.all()

def Home(request):
    return HttpResponse("<h1>Welcome to the Investment api homepage please use the valid endpoints</h1>")
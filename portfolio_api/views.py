from portfolio.models import Portfolio

from portfolio_api.serializers import PortfolioSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsAuthorOrReadOnly
from rest_framework import permissions
# Create your views here.

class PortfolioList(ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class PortfolioDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
from django.urls import path

# from .views import PortfolioListView, PortfolioCreateView, PortfolioUpdateView, PortfolioDeleteView
from .views import PortfolioList, PortfolioDetail


urlpatterns = [
    path('<int:pk>/', PortfolioDetail.as_view(), name='api_detail'),
    path('', PortfolioList.as_view(), name='portfolio_api'),
]

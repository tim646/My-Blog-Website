from django.urls import path

from .views import PortfolioListView, PortfolioCreateView, PortfolioUpdateView, PortfolioDeleteView
# from .views import PortfolioList, PortfolioDetail


# urlpatterns = [
#     path('<int:pk>/', PortfolioDetail.as_view(), name='portfolio_detail'),
#     # path('<int:pk>/delete/', PortfolioDeleteView.as_view(), name='portfolio_delete'),
#     # path('new/',PortfolioCreateView.as_view(), name='portfolio_add'),
#     path('', PortfolioList.as_view(), name='portfolio'),
# ]


urlpatterns = [
    path('<int:pk>/edit/', PortfolioUpdateView.as_view(), name='portfolio_edit'),
    path('<int:pk>/delete/', PortfolioDeleteView.as_view(), name='portfolio_delete'),
    path('new/',PortfolioCreateView.as_view(), name='portfolio_add'),
    path('', PortfolioListView.as_view(), name='portfolio'),
 ]
from .models import Portfolio

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

# from portfolio_api.serializers import PortfolioSerializer
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.

# class PortfolioList(ListCreateAPIView):
#     queryset = Portfolio.objects.all()
#     serializer_class = PortfolioSerializer
#
#
# class PortfolioDetail(RetrieveUpdateDestroyAPIView):
#     serializer_class = PortfolioSerializer



class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio.html'


class PortfolioCreateView(CreateView):
    model = Portfolio
    template_name = 'portfolio_add.html'
    fields = ('title', 'summary', 'link')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #     user admin(superuser) ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser


class PortfolioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Portfolio
    template_name = 'portfolio_delete.html'
    success_url = reverse_lazy('portfolio')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PortfolioUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Portfolio
    fields = ('title', 'summary', 'link')
    template_name = 'portfolio_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user



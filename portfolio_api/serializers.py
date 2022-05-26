from rest_framework import serializers
from portfolio.models import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'summary', 'link', 'date', 'author')
        model = Portfolio

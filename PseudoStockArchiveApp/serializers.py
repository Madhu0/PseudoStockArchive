from PseudoStockArchiveApp.models import *
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('symbol', 'name', 'marketCap', 'sector', 'industry')


class TradingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradingData
        fields = ('timestamp', 'open', 'close', 'high', 'low', 'volume')
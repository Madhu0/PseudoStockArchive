from PseudoStockArchiveApp.models import *
from datetime import datetime, timedelta
import json


def writeDailySeriesToDb(text):
    data = json.loads(text)
    symbol = data['Meta Data']['2. Symbol']
    company = Company.objects.get(symbol=symbol)
    timeSeriesData = data["Time Series (Daily)"]
    for key in timeSeriesData.keys():
        value = timeSeriesData[key]
        timestamp=datetime.strptime(key, "%Y-%m-%d")
        results = TradingData.objects.filter(timestamp=timestamp, company__symbol=symbol)
        if not results or results.count() == 0:
            tradingData = TradingData(timestamp=timestamp, open=float(value['1. open']), close=float(value['4. close']), low=float(value['3. low']), high=float(value['2. high']), volume=float(value['5. volume']), company=company)
            print("Saving data", tradingData)
            tradingData.save()

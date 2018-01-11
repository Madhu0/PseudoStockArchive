from PseudoStockArchiveApp.serializers import *
from django.http import HttpResponse, JsonResponse
from PseudoStockArchiveApp.services import getIntraDaySeries, getDailySeries, getTechnicalIndicator
from PseudoStockArchiveApp.helpers import writeDailySeriesToDb


def getCompanies(request):
    skip = int(request.GET.get('skip', '0'))
    limit = int(request.GET.get('limit', '30'))
    try:
        companies = Company.objects.all()[skip:skip + limit]
        serializer = CompanySerializer(companies, many=True)
        response = dict()
        response['data'] = serializer.data
        response['hasNext'] = Company.objects.all().__len__() > skip+limit
        return JsonResponse(response, status=200, safe=False)
    except Exception as error:
        return HttpResponse(error, status=400)


def getTradingDataBySymbol(request):
    symbol = request.GET.get('symbol', '')
    skip = request.GET.get('skip', 0)
    limit = request.GET.get('limit', 100)
    try:
        tradingData = TradingData.objects.all().filter(company__symbol=symbol).order_by('-timestamp')[skip: skip + limit]
        serializer = TradingDataSerializer(tradingData, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
    except Exception as error:
        return HttpResponse(error, status=400)


def getIntraDaySeriesBySymbol(request):
    symbol = request.GET.get('symbol', '')
    interval = request.GET.get('interval', '1min')
    res = getIntraDaySeries(symbol, interval)
    return HttpResponse(res, status=200, content_type="application/json")


def getDailySeriesBySymbol(request):
    symbol = request.GET.get('symbol', '')
    interval = request.GET.get('interval', '1min')
    res = getDailySeries(symbol=symbol)
    writeDailySeriesToDb(res)
    return HttpResponse(res, status=200, content_type="application/json")


def getTechnicalIndicatorBySymbol(request):
    res = getTechnicalIndicator(request.GET)
    return HttpResponse(res, status=200, content_type="application/json")
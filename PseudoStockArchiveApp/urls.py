from django.conf.urls import url
from PseudoStockArchiveApp.views import *

urlpatterns = [
    url('^$', getHomePage),
    url('^get/companies$', getCompanies),
    url('^get/tradingdata', getTradingDataBySymbol),
    url('^get/intradayseries', getIntraDaySeriesBySymbol),
    url('^get/dailyseries', getDailySeriesBySymbol),
    url('^get/indicators', getTechnicalIndicator)
]
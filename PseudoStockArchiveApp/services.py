from PseudoStockArchiveApp.constants import ALPHA_VANTAGE_API_KEY, ALPHA_VANTAGE_API_URL
from requests import get, post, put


def getIntraDaySeries(symbol, interval, **kwargs):
    url = ALPHA_VANTAGE_API_URL
    params = dict()
    params['function'] = 'TIME_SERIES_INTRADAY'
    params['symbol'] = symbol
    params['apikey'] = ALPHA_VANTAGE_API_KEY
    params['interval'] = interval
    params = {**kwargs, **params}
    res = get(url, params=params)
    return res.text


def getDailySeries(**kwargs):
    url = ALPHA_VANTAGE_API_URL
    params = kwargs
    params['apikey'] = ALPHA_VANTAGE_API_KEY
    params['function'] = 'TIME_SERIES_DAILY'
    res = get(url, params=params)
    return res.text


def getTechnicalIndicator(**kwargs):
    url = ALPHA_VANTAGE_API_URL
    params = kwargs
    params['apikey'] = ALPHA_VANTAGE_API_KEY
    res = get(url, params)
    return res.text

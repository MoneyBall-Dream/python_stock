import pandas as pd
import yfinance as yf

# yfinance 정보 추출 목록
info_list = ['longBusinessSummary', # 기업 간단 소개
             'currentPrice','previousClose','open','dayLow','dayHigh', # 현재 가격, 종가, 시가, 저가, 고가
             'dividendRate','dividendYield','lastDividendValue','lastDividendDate', # 배당금 정보(연간 배당금, 배당 수익률, 최근 배당금, 날짜)
             'totalRevenue','netIncomeToCommon','ebitda','grossProfits','earningsGrowth','revenueGrowth', # 총매출, 순이익, 감가상각 전 영업이익, 이익 및 매출 성장률
             'trailingEps','forwardEps','epsForward','epsTrailingTwelveMonths', # EPS
             'trailingPE','forwardPE','priceEpsCurrentYear', # PER
             'totalDebt','totalCash','debtToEquity', # 총 부채, 현금 보유, 부채비율
             'marketCap', # 시가총액
             'recommendationKey','targetHighPrice','targetLowPrice','targetMeanPrice'] # 애널리스트 분석

# 단일 주식 정보 추출
def get_stock_data(stock_name:str) -> list:
    data = yf.Ticker(stock_name)
    stock_info = data.info
    results_list = {}
    
    for key in sorted(info_list):
        results_list[key] = stock_info.get(key, None)
        
    return results_list

# 단일 주가 데이터 추출
def get_stock_history(stock_name:str) -> pd.DataFrame:
    '''
    period: 기간 (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
    interval: 주기 (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)
    '''
    data = yf.Ticker(stock_name)
    df = data.history(period='1mo', interval='1d')
    
    return df

# 환율 데이터 추출
def get_exchange_rate():
    df = yf.download("KRW=X",
                     period='1d',
                     auto_adjust=True)
    exchange_rate = df['Close'].iloc[-1].item()
    return exchange_rate

# print(get_stock_data('MSFT'))
# print(get_stock_history('MSFT'))
# get_exchange_rate()
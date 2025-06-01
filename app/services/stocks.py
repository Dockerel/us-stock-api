import datetime as dt
import FinanceDataReader as fdr
from dateutil.relativedelta import relativedelta
import requests


def get_latest_stock(ticker):
    reps = 0
    now = dt.datetime.now()
    while reps < 10:
        try:
            date_str = now.strftime("%Y-%m-%d")
            df = fdr.DataReader(ticker, date_str)
            if len(df) == 0:
                now -= dt.timedelta(days=1)
                reps += 1
                continue

            # 간단하게: 각 컬럼을 리스트로 변환
            records = []
            for i in range(len(df)):
                record = {"Close": float(df["Close"].iloc[i]), "Date": now.isoformat()}
                records.append(record)

            return [200, records]

        except Exception as e:
            print(f"Exception: {e}")
            now -= dt.timedelta(days=1)
            reps += 1
            continue

    return [400, []]


def get_stock(ticker, fromDate, toDate):
    try:
        df = fdr.DataReader(ticker, fromDate, toDate)
        df.index.name = "Date"
        df = df.reset_index()
        return [200, df.to_dict(orient="records")]
    except Exception:
        return [400, []]


def check_stockName(ticker):
    try:
        now = dt.datetime.now()
        one_year_ago = now - relativedelta(years=1)
        date_str = one_year_ago.strftime("%Y-%m-%d")
        fdr.DataReader(ticker, date_str)
        return [200, True]
    except Exception as e:
        return [200, False]


def resolve_stockName(stockKeyword):
    try:
        url = f"https://ac.stock.naver.com/ac?target=stock%2Cipo%2Cindex%2Cmarketindicator&q={stockKeyword}"
        response = requests.get(url)
        code = response.json().get("items")[0].get("code")
        return [200, code]
    except Exception as e:
        return [400, "unknown"]

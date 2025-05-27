from fastapi import APIRouter
from services import stocks

router = APIRouter()


@router.get("/stocks/{ticker}")
def get_latest_stock(ticker: str, fromDate: str = "", toDate: str = ""):
    if fromDate == "" or toDate == "":
        return api_response(stocks.get_latest_stock(ticker))
    return api_response(stocks.get_stock(ticker, fromDate, toDate))


@router.get("/stocks/check/{ticker}")
def check_stock_ticker(ticker: str):
    return api_response(stocks.check_stock_ticker(ticker))


def api_response(result):
    return {"status": result[0], "data": result[1]}

from fastapi import APIRouter
from services import stocks

router = APIRouter()


@router.get("/stocks/{stockName}")
def get_latest_stock(stockName: str, fromDate: str = "", toDate: str = ""):
    if fromDate == "" or toDate == "":
        return api_response(stocks.get_latest_stock(stockName))
    return api_response(stocks.get_stock(stockName, fromDate, toDate))


@router.get("/stocks/check/{stockName}")
def check_stockName(stockName: str):
    return api_response(stocks.check_stockName(stockName))


@router.get("/stocks/resolve-keyword/{stockKeyword}")
def resolve_stockKeyword(stockKeyword: str):
    return api_response(stocks.resolve_stockName(stockKeyword))


def api_response(result):
    return {"status": result[0], "data": result[1]}

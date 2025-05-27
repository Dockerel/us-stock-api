from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routers import stock

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stock.router, prefix="/api/v1")


@app.get("/")
def home():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app)

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import cars

app = FastAPI()

app.include_router(cars.router)
@app.get("/")
async def root():
    return RedirectResponse(url="/cars")

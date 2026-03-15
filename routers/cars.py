from fastapi import APIRouter, Request, Form, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")
cars_db = [
    {"name": "Toyota Camry", "year": 2020},
    {"name": "BMW X5", "year": 2019},
    {"name": "Audi A6", "year": 2018},
]

@router.get("/cars", response_class=HTMLResponse)
async def get_cars(request: Request):
    return templates.TemplateResponse(
        "cars/search.html",
        {
            "request": request,
            "cars": cars_db,
            "car_name": ""
        }
    )


@router.get("/cars/search", response_class=HTMLResponse)
async def search_cars(request: Request, car_name: str = Query(default="")):

    filtered_cars = []

    if car_name:
        search = car_name.lower()

        for car in cars_db:
            if search in car["name"].lower():
                filtered_cars.append(car)

    else:
        filtered_cars = cars_db

    return templates.TemplateResponse(
        "cars/search.html",
        {
            "request": request,
            "cars": filtered_cars,
            "car_name": car_name
        }
    )


@router.get("/cars/new", response_class=HTMLResponse)
async def new_car_form(request: Request):
    return templates.TemplateResponse(
        "cars/new.html",
        {"request": request}
    )


@router.post("/cars/new")
async def create_car(name: str = Form(...), year: int = Form(...)):

    cars_db.append({
        "name": name,
        "year": year
    })

    return RedirectResponse(url="/cars", status_code=303)
from fastapi import FastAPI, Request, Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette import status
from typing import Annotated
import re

from backend.vkapi import get_user_ids_from_post, get_users_info
from backend.plots import create_plot


app = FastAPI(title="VK likes analysis")

app.mount("/frontend/media", StaticFiles(directory="frontend/media"), name="media")

templates = Jinja2Templates(directory="frontend/templates")

@app.get("/")
def base(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})

@app.get("/analyze_likes")
def analyze_likes(
    post_url: str, 
    request: Request,
    sex_checkbox: Annotated[bool, Query(alias="sex")]=False, 
    city_checkbox: Annotated[bool, Query(alias="city")]=False, 
    age_checkbox: Annotated[bool, Query(alias="age")]=False, 
    country_checkbox: Annotated[bool, Query(alias="country")]=False, 
    ):
    
    print(sex_checkbox, city_checkbox, age_checkbox,)
    url_pattern = r"https://vk\.com/(\w+)\?w=wall-(\d+)_(\d+)"
    if re.match(pattern=url_pattern, string=post_url):
        post_url = post_url[post_url.index("wall"):]
        group_id = int(post_url[post_url.index("wall")+4:post_url.index("_")])
        post_id = int(post_url[post_url.index("_")+1:])
        
        user_ids = get_user_ids_from_post(group_id, post_id)
        
        users_data = {
            "cities": {},
            "countries": {},
            "sex": {},
            "ages": {}
        }

        for iterator, user_id in enumerate(user_ids, start=1):
            print(f"{iterator}/{len(user_ids)}")
            users_data = get_users_info(user_id, users_data)
        if sex_checkbox:
            create_plot("sex", users_data["sex"].values(), users_data["sex"].keys())
        if city_checkbox:
            create_plot("cities", users_data["cities"].values(), users_data["cities"].keys())
        if country_checkbox:
            create_plot("countries", users_data["countries"].values(), users_data["countries"].keys())
        if age_checkbox:
            create_plot("ages", users_data["ages"].values(), users_data["ages"].keys())

        return templates.TemplateResponse("main.html", {"request": request, "post_url": post_url})

    else:
        return {
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "Ссылка, которую вы указали, не является валидной. Пожалуйста, проверьте корректность введенной ссылки на пост."
        }

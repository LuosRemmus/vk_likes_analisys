import re
from requests import get
from datetime import datetime

from backend.config import ACCESS_TOKEN


def get_user_ids_from_post(group_id: int, post_id: int, offset: int = 0, count: int = 1000) -> list[int]:
    user_ids = []
    params = {
        'access_token': ACCESS_TOKEN,
        'type': 'post',
        'owner_id': group_id,
        'item_id': post_id,
        'offset': offset,
        'count': count,
        'v': '5.154'
        }
    
    response = get("https://api.vk.com/method/likes.getList", params=params).json()["response"]
    user_ids += response["items"]
    if len(user_ids) == 1000:
        user_ids += get_user_ids_from_post(group_id, post_id, offset=offset+1000)

    result = list(map(lambda x: "id"+x, map(str, user_ids)))

    return result


def get_users_info(user_id: str, users_data: dict[dict]) -> dict:
    params = {
        'access_token': ACCESS_TOKEN,
        'user_ids': user_id,
        'fields': 'bdate, city, country, sex',
        'v': '5.154'
        }

    user = get("https://api.vk.com/method/users.get", params=params).json()["response"][0]
    bdate_pattern = r"(\d+)\.(\d)+\.(\d+)"

    try:
        country = user["country"]["title"]
    except KeyError:
        country = "Other"
    
    try:
        sex = "Female" if user["sex"] == 1 else "Male"
    except KeyError:
        sex = "Other"
    
    try:
        bdate = user["bdate"]
        if re.match(bdate_pattern, bdate):
            age = str((datetime.now() - datetime.strptime(bdate, "%d.%m.%Y")).days // 365)
        else:
            age = "Other"
    except KeyError:
        age = "Other"

    try:
        city = user["city"]["title"]
    except KeyError:
        city = "Other"

    users_data["cities"][city] = users_data["cities"].get(city, 0) + 1
    users_data["countries"][country] = users_data["countries"].get(country, 0) + 1
    users_data["sex"][sex] = users_data["sex"].get(sex, 0) + 1
    users_data["ages"][age] = users_data["ages"].get(age, 0) + 1

    return users_data

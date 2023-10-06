import re
import json
import time
from requests import get
from datetime import datetime

from config import ACCESS_TOKEN


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

    return list(map(str, user_ids))


def get_users_info(user_ids: str) -> list[dict]:
    params = {
        'access_token': ACCESS_TOKEN,
        'user_ids': ','.join(user_ids),
        'fields': 'bdate, city, country, sex',
        'v': '5.154'
    }
    response = get("https://api.vk.com/method/users.get", params=params).json()["response"]
    bdate_pattern = r"(\d+)\.(\d)+\.(\d+)"
    filtred_users_data = []
    for user in response:
        user_data = {
            "firs_name": user["first_name"],
            "last_name": user["last_name"]
        }
        try:
            user_data["country"] = user["country"]["title"]
        except KeyError:
            user_data["country"] = "Other"
        
        try:
            user_data["sex"] = "Female" if user["sex"] == 1 else "Male"
        except KeyError:
            user_data["sex"] = "Other"
        
        try:
            bdate = user["bdate"]
            if re.match(bdate_pattern, bdate):
                user_data["age"] = str((datetime.now() - datetime.strptime(bdate, "%d.%m.%Y")).days // 365)
            else:
                user_data["age"] = "Other"
        except KeyError:
            user_data["age"] = "Other"

        try:
            user_data["city"] = user["city"]["title"]
        except KeyError:
            user_data["city"] = "Other"


        filtred_users_data.append(user_data)

    return filtred_users_data


with open('f.json', 'w', encoding="utf-8") as file:
    user_ids = get_user_ids_from_post(-55206187, 2628)
    data = [", ".join(user_ids[i:i+20]) for i in range(0, len(user_ids), 20)]

    result = [get_users_info(i) for i in data]

    print(len(data),"=",len(result))
    json.dump({"count": len(result), "items": result}, file, ensure_ascii=False)

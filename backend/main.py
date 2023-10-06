from fastapi import FastAPI
from starlette import status
import re

from backend.vkapi import get_users_ids_from_post


app = FastAPI(title="VK likes analysis")

@app.get("/analyze_likes")
def analyze_likes(post_url: str):
    url_pattern = r"https://vk\.com/feed\?w=wall-\d+_\d+"
    if re.match(pattern=url_pattern, string=post_url):
        group_id = post_url[post_url.index("wall")+1:post_url.index("_")]
        post_id = post_url[post_url.index("_")+1:]
        
        get_users_ids_from_post(group_id, post_id)
        pass
    else:
        return {
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "Ссылка, которую вы указали, не является валидной. Пожалуйста, проверьте корректность введенной ссылки на пост."
        }

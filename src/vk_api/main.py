import requests


class VK:
    def __init__(self, service_key, version, owner_id, item_id):
        self.service_key = service_key
        self.version = version
        self.owner_id = owner_id
        self.item_id = item_id

    def get_ids(self, likes_limit=1000) -> str:
        user_ids = []
        response = requests.get('https://api.vk.com/method/likes.getList', params={
            'access_token': self.service_key,
            'v': self.version,
            'type': 'post',
            'owner_id': self.owner_id,
            'item_id': self.item_id,
            'extended': 1,
            'count': likes_limit
        }).json()['response']

        items = response['items']
        for item in items:
            user_ids.append(str(item["id"]))

        return ','.join(user_ids)

    def get_users(self, user_ids: str):
        response = requests.get('https://api.vk.com/method/users.get', params={
            'access_token': self.service_key,
            'v': self.version,
            'user_ids': user_ids,
            'fields': 'city, country, sex, bdate'
        }).json()['response']

        temp = user_ids.split(',')
        result = []

        for id_, i in enumerate(response):
            try:
                city = i["city"]["title"]
            except KeyError:
                city = None
            try:
                country = i["country"]["title"]
            except KeyError:
                country = None
            try:
                sex = i["sex"]
                if sex == 2:
                    sex = 'male'
                elif sex == 1:
                    sex = 'female'
                else:
                    sex = None
            except KeyError:
                sex = None
            try:
                bdate = i['bdate']
            except KeyError:
                bdate = None
            try:
                first_name = i['first_name']
            except KeyError:
                first_name = None
            try:
                last_name = i['last_name']
            except KeyError:
                last_name = None

            result.append([temp[id_], first_name, last_name, city, country, bdate, sex])

        return result

from src.database.database import select_data, insert_data
from src.plots.MatPlotLib import create_plot
from src.vk_api.main import VK
from src.config import SERVICE_KEY, VERSION


def format_values(data: list) -> list:
    if len(list(data)) > 10:
        to_sum = sum(list(data)[10:])
        data = list(data)[:10]
        data.append(to_sum)
    return list(data)


def format_keys(data: list) -> list:
    if len(list(data)) > 10:
        data = list(data)[:10]
        data.append("Other")
    return list(data)


def sort_dict(dct: dict) -> dict:
    sorted_values = sorted(dct.values(), reverse=True)
    sorted_dct = {}

    for i in sorted_values:
        for k in dct.keys():
            if dct[k] == i:
                sorted_dct[k] = dct[k]
                break
    return sorted_dct


def main():
    url = input("Enter post url: ").replace('w=wall', '')
    owner_id, item_id = url[url.index('?') + 1:].split('_')

    vk = VK(
        service_key=SERVICE_KEY,
        version=VERSION,
        owner_id=owner_id,
        item_id=item_id
    )

    ids = vk.get_ids()
    users = vk.get_users(ids)

    """
    for user in users:
        insert_data(user[0], user[1], user[2], user[3], user[4], user[5], user[6])
    """
    countries = select_data('country')
    cities = select_data('city')
    sex = select_data('sex')
    ages = select_data('age')
    ages.sort()

    user_data = {
        "country": {},
        "city": {},
        "sex": {},
        "age": {}
    }

    for country, city, sex, age in zip(countries, cities, sex, ages):
        user_data["country"][country] = countries.count(country)
        user_data["city"][city] = cities.count(city)
        user_data["sex"][sex] = sex.count(sex)
        user_data["age"][age] = ages.count(age)

    user_data["country"] = sort_dict(user_data["country"])
    user_data["city"] = sort_dict(user_data["city"])
    user_data["sex"] = sort_dict(user_data["sex"])
    user_data["age"] = sort_dict(user_data["age"])

    city_dk, city_dv = format_keys(list(user_data["city"].keys())), format_values(list(user_data["city"].values()))
    country_dk, country_dv = format_keys(list(user_data["country"].keys())), format_values(
        list(user_data["country"].values()))
    sex_dk, sex_dv = user_data["sex"].keys(), user_data["sex"].values()
    age_dk, age_dv = format_keys(list(user_data["age"].keys())), format_values(list(user_data["age"].values()))

    create_plot('countries', list(country_dv), list(country_dk), 'media/countries.png')
    create_plot('cities', list(city_dv), list(city_dk), 'media/cities.png')
    create_plot('ages', list(age_dv), list(age_dk), 'media/ages.png')
    create_plot('sex', list(sex_dv), list(sex_dk), 'media/sex.png')


if __name__ == '__main__':
    main()

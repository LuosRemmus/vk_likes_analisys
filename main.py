from vk_api import VK
from SQL import push, get_data
from MatPlotLib import create_plot

if __name__ == '__main__':
    service_key = 'ba504f49ba504f49ba504f49a6b9419c04bba50ba504f49d9c43417e43f8253d166b5d1'
    version = 5.131
    url = input("Enter post url: ").replace('w=wall', '')
    domain = url.replace('https://vk.com/', '')[:url.index('?')]
    owner_id, item_id = url[url.index('?') + 1:].split('_')

    vk = VK(
        service_key_=service_key,
        version_=version,
        owner_id_=owner_id,
        item_id_=item_id
    )
    ids = vk.get_ids()
    query = vk.get_users(ids)

    for data in query:
        push(data[0], data[1], data[2], data[3], data[4], data[5], data[6])

    countries = get_data('country')
    cities = get_data('city')
    sex = get_data('sex')
    ages = get_data('age')
    ages.sort()

    country_data = {}
    city_data = {}
    sex_data = {}
    age_data = {}

    for i in countries:
        country_data[i] = countries.count(i)
    for i in cities:
        city_data[i] = cities.count(i)
    for i in sex:
        sex_data[i] = sex.count(i)
    for i in ages:
        age_data[i] = ages.count(i)


    def format_values(data):
        if len(list(data)) > 10:
            to_sum = sum(list(data)[10:])
            data = list(data)[:10]
            data.append(to_sum)
        return list(data)

    def format_keys(data):
        if len(list(data)) > 10:
            data = list(data)[:10]
            data.append("Other")
        return list(data)

    def sort_dict(dct):
        sorted_values = sorted(dct.values(), reverse=True)
        sorted_dct = {}

        for i in sorted_values:
            for k in dct.keys():
                if dct[k] == i:
                    sorted_dct[k] = dct[k]
                    break
        return sorted_dct


    city_data = sort_dict(city_data)
    country_data = sort_dict(country_data)
    sex_data = sort_dict(sex_data)
    age_data = sort_dict(age_data)

    city_dk, city_dv = format_keys(city_data.keys()), format_values(city_data.values())
    country_dk, country_dv = format_keys(country_data.keys()), format_values(country_data.values())
    sex_dk, sex_dv = sex_data.keys(), sex_data.values()
    age_dk, age_dv = format_keys(age_data.keys()), format_values(age_data.values())

    create_plot('countries', list(country_dv), list(country_dk),
                'C:/Users/Pivo/Desktop/Учеба/7 сем/ZaminaloV/Semestrovaya/countries.png') #Последним параметром указывается полный путь к директории, в которую необходимо сохранить файл, а так же название самого файла
    create_plot('cities', list(city_dv), list(city_dk),
                'C:/Users/Pivo/Desktop/Учеба/7 сем/ZaminaloV/Semestrovaya/cities.png')
    create_plot('ages', list(age_dv), list(age_dk),
                'C:/Users/Pivo/Desktop/Учеба/7 сем/ZaminaloV/Semestrovaya/ages.png')
    create_plot('sex', list(sex_dv), list(sex_dk),
                'C:/Users/Pivo/Desktop/Учеба/7 сем/ZaminaloV/Semestrovaya/sex.png')

import sqlalchemy as db
from sqlalchemy import Column, Integer, UnicodeText

engine = db.create_engine('sqlite:///Users.db', connect_args={'check_same_thread': False})
connection = engine.connect()
metadata = db.MetaData()

table = db.Table('users', metadata,
                 Column('id', Integer, primary_key=True, nullable=False),
                 Column('user_id', UnicodeText, nullable=False, unique=True),
                 Column('first_name', UnicodeText),
                 Column('last_name', UnicodeText),
                 Column('city', UnicodeText),
                 Column('country', UnicodeText),
                 Column('bdate', UnicodeText),
                 Column('sex', UnicodeText)
                 )

metadata.create_all(engine)


def push(user_id, first_name, last_name, city, country, bdate, sex):
    try:
        insert_data = table.insert().values({
            'user_id': f'vk.com/id{user_id}',
            'first_name': first_name,
            'last_name': last_name,
            'city': city,
            'country': country,
            'bdate': bdate,
            'sex': sex
        })

        connection.execute(insert_data)
        print('[INFO] Data pushed successfully!')
    except:
        print('[ERROR] Error while pushing')


def get_data(param: str):
    match param:
        case "city":
            return [str(i).replace("('", "").replace("',)", "") for i in connection.execute(db.select([table.columns.city]).where(table.columns.city!=None)).fetchall()]
        case "country":
            return [str(i).replace("('", "").replace("',)", "") for i in connection.execute(db.select([table.columns.country]).where(table.columns.country!=None)).fetchall()]
        case "age":
            age = connection.execute(db.select([table.columns.bdate]).where(table.columns.bdate!=None)).fetchall()
            result = []
            for i in age:
                if len(str(i).split('.')) == 3:
                    result.append(2022-int(str(i).split('.')[2].replace("',)", "")))
            return result
        case "sex":
            return [str(i).replace("('", "").replace("',)", "") for i in connection.execute(db.select([table.columns.sex]).where(table.columns.sex!=None)).fetchall()]

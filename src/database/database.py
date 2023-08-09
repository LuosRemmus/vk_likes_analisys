from sqlalchemy import select, insert
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from src.database.models import User
from src.config import DATABASE_URL

Base: DeclarativeMeta = declarative_base()

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()


def select_data(field: str):
    match field:
        case "city":
            city = session.scalars(select(User.city).where(User.country is not None)).fetchall()
            print(f"{datetime.now()} [INFO] Selected city!")
            city = [c for c in city if c is not None]
            return city

        case "country":
            country = session.scalars(select(User.country).where(User.country is not None)).fetchall()
            print(f"{datetime.now()} [INFO] Selected country!")
            country = [c for c in country if c is not None]
            return country

        case "age":
            age = session.scalars(select(User.bdate).where(User.bdate is not None)).fetchall()
            print(f"{datetime.now()} [INFO] Selected age!")
            age = [a for a in age if a is not None]
            result = []
            for i in age:
                if len(str(i).split('.')) == 3:
                    result.append(datetime.now().year - int(str(i).split('.')[2].replace("',)", "")))

            return result

        case "sex":
            sex = session.scalars(select(User.sex).where(User.sex is not None)).fetchall()
            sex = [s for s in sex if s is not None]
            print(f"{datetime.now()} [INFO] Selected sex!")
            return sex


def insert_data(user_id: int, first_name: str, last_name: str, city: str, country: str, bdate: str, sex: str):
    user = User(
        user_id="vk.com/id" + user_id,
        first_name=first_name,
        last_name=last_name,
        city=city,
        country=country,
        bdate=bdate,
        sex=sex
    )
    session.add(user)
    session.commit()
    print(f"{datetime.now()} [INFO] Inserted user!")

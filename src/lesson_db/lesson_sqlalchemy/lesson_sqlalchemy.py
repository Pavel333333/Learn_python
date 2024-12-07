# -*- coding: utf-8 -*-
from typing import Optional
from sqlalchemy import create_engine, Date, ForeignKey, update, func, delete, engine, text
from sqlalchemy.engine import url, Engine
from sqlalchemy.orm import (DeclarativeBase, Mapped, relationship, mapped_column, sessionmaker, declarative_base)
from datetime import date
from sqlalchemy_utils import database_exists, create_database
from datetime import datetime

class CreateDB:

    @classmethod
    def create_db(cls):
        url_postgres = url.URL(
            drivername="postgresql",
            database="postgres",
            username="postgres",
            password='pavel',
            host="localhost",
            port=5432,
            query={}
        )

        # Имя базы данных, которую мы хотим проверить и создать
        db_name = 'my_shop'

        # Формируем полный URL подключения к нужной базе данных
        full_url = f"{url_postgres.drivername}://{url_postgres.username}:{url_postgres.password}@{url_postgres.host}:{url_postgres.port}/{db_name}"

        # параметр echo показывает наши запросы к БД
        # engine_postgres = create_engine(full_url, echo=True)

        # with engine_postgres.connect().execution_options(autocommit=True) as conn:
        #     conn.execute(text(f'CREATE DATABASE my_shop'))

        # Проверяем, существует ли база данных
        if not database_exists(full_url):
            # Создаем базу данных, если она не существует
            create_database(full_url)
        else:
            print(f"База данных '{db_name}' уже существует.")

        # return base_engine_my_shop, session_engine_my_shop

url_postgres = url.URL(
    drivername="postgresql",
    database="my_shop",
    username="postgres",
    password='pavel',
    host="localhost",
    port=5432,
    query={}
        )

engine_my_shop: Engine = create_engine(url_postgres, echo=True)
Base = declarative_base()
# Фабрика сессий
Session = sessionmaker(bind=engine_my_shop)

# class Base(DeclarativeBase):
#     pass

class Employees(Base):
    __tablename__ = 'employees'

    employee_id: Mapped[int] = mapped_column(primary_key=True)
    last_name: Mapped[str] = mapped_column()
    name_employee: Mapped[str] = mapped_column()
    patronymic: Mapped[str] = mapped_column()
    position: Mapped[str] = mapped_column()
    address: Mapped[str] = mapped_column()
    home_phone: Mapped[str] = mapped_column()
    birthday: Mapped[date] = mapped_column(Date)

    order = relationship('Orders', back_populates='employees')


class Goods(Base):
    __tablename__ = 'goods'

    good_id: Mapped[int] = mapped_column(primary_key=True)
    supply_id: Mapped[int] = mapped_column(ForeignKey('supplies.supply_id'))
    good_name: Mapped[str] = mapped_column()
    parametres: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    image: Mapped[Optional[bytes]]
    purchase_cost: Mapped[int] = mapped_column()
    availability: Mapped[bool] = mapped_column()
    quantity: Mapped[int] = mapped_column()
    sale_cost: Mapped[int] = mapped_column()

    order: Mapped[list['Orders']] = relationship(back_populates='goods')
    supply = relationship('Supplies', back_populates='goods')


class Orders(Base):
    __tablename__ = 'orders'

    order_id: Mapped[int] = mapped_column(primary_key=True)
    employee_id: Mapped[int] = mapped_column(ForeignKey('employees.employee_id'))
    good_id: Mapped[int] = mapped_column(ForeignKey('goods.good_id'))
    placement_date: Mapped[date] = mapped_column(Date)
    execution_date: Mapped[date] = mapped_column(Date)
    client_id: Mapped[int] = mapped_column(ForeignKey('clients.client_id'))

    employee = relationship('Employees', back_populates='orders')
    good: Mapped[list['Goods']] = relationship(back_populates='orders')
    client = relationship('Clients', back_populates='orders')


class Clients(Base):
    __tablename__ = 'clients'

    client_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    address: Mapped[str] = mapped_column()
    phone: Mapped[str] = mapped_column()

    order = relationship('Orders', back_populates='clients')


class Suppliers(Base):
    __tablename__ = 'suppliers'

    supplier_id: Mapped[int] = mapped_column(primary_key=True)
    supplier_name: Mapped[str] = mapped_column()
    representative: Mapped[str] = mapped_column()
    contact: Mapped[str] = mapped_column()
    phone: Mapped[str] = mapped_column()
    address: Mapped[str] = mapped_column()

    supply = relationship('Supplies', back_populates='suppliers')


class Supplies(Base):
    __tablename__ = 'supplies'

    supply_id: Mapped[int] = mapped_column(primary_key=True)
    supplier_id: Mapped[int] = mapped_column(ForeignKey('suppliers.supplier_id'))
    supply_date: Mapped[date] = mapped_column(Date)

    supplier = relationship('Suppliers', back_populates='supplies')
    good = relationship('Goods', back_populates='supplies')

class Commands:

    @classmethod
    def create_all_tables(cls):
        Base.metadata.create_all(engine_my_shop)

    @classmethod
    def insert_elem(cls, table: type, key_fields: list, **kwargs):
        # model_type это название класса таблицы/модели
        session = Session()

        with session.begin():
            if 'birthday' in kwargs:
                kwargs['birthday'] = datetime.strptime(kwargs['birthday'], '%Y-%m-%d').date()
            filter_kwargs = {key: value for key, value in kwargs.items() if key in key_fields}
            existing_record = session.query(table).filter_by(**filter_kwargs).first()
            if not existing_record:
                new_element = table(**kwargs)
                session.add(new_element)
                print(f'Элемент {new_element} успешно добавлен.')
            else:
                print(f'Запись с такими параметрами уже существует: {existing_record}')

    @classmethod
    def select_from_table(cls, table: type):
        session = Session()

        with session.begin():
            result = session.query(table).all()

        return result

    @classmethod
    def inner_join(cls, table: type, table2: type, column_name: str,
                   join_column1: str, join_column2: str):
        session = Session()
        with session.begin():
            col = getattr(table, column_name)
            col2= getattr(table, join_column1)
            col3 = getattr(table2, join_column2)
            result = session.query(col).join(table2, col2 == col3)
            return result.all()

    @classmethod
    def update_clients_table(cls, table: type, value: str, id: int):
        session = Session()
        with session.begin():
            result = update(table).where(Clients.client_id == id).values(name=value)
            session.execute(result)

    @classmethod
    def select_from_table_where_order_group_distinct(cls, table: type, group_by, order_by,
                                                     column, distinct=False):
        session = Session()
        with session.begin():
            result = session.query(table, column).group_by(group_by).order_by(order_by).\
                distinct(distinct)
            return result

    @classmethod
    def select_from_table_sum(cls, table: type, column: str):
        session = Session()
        with session.begin():
            col = getattr(table, column)
            result = session.query(func.sum(col)).scalar()

        return result

    @classmethod
    def select_from_table_max(cls, table: type, column: str):
        session = Session()
        with session.begin():
            col = getattr(table, column)
            result = session.query(func.max(col)).scalar()

        return result

    @classmethod
    def select_from_table_count(cls, table: type, column: str):
        session = Session()
        with session.begin():
            col = getattr(table, column)
            result = session.query(func.count(col)).scalar()

        return result

    @classmethod
    def delete_from_suppliers(cls, table: type, id: int):
        session = Session()
        with session.begin():
            result = delete(table).where(Suppliers.supplier_id == id)
            session.execute(result)


if __name__ == '__main__':
    # CreateDB.create_db()
    Commands.insert_elem(Employees, ['employee_id'], last_name='Ivanov', name_employee='Ivan',
                         patronymic='Ivanovich', position='storekeeper', address='Mayakovskogo',
                         home_phone='8-903-039-33-23', birthday='1988-04-22')









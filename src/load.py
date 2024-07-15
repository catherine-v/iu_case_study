import pandas as pd
from sqlalchemy import create_engine, inspect, Engine, Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import declarative_base
from schemas import ProductSchema


Base = declarative_base()


class FoodData(Base):
    __tablename__ = "food_data"

    product_id = Column(String, primary_key=True)
    categories_hierarchy = Column(ARRAY(String))
    product_name = Column(String)
    nutriscore_score = Column(Integer)
    quantity = Column(String)
    origins = Column(String)
    allergens = Column(String)


def connect(conn_str: str) -> Engine:
    """
    Create an SQLAlchemy engine to connect to the database.

    :param conn_str: Connection string to the database
    :return: the SQLAlchemy engine
    """
    engine = create_engine(conn_str)
    return engine


def create_table(engine) -> None:
    """
    Create `food_data` table if not exists.

    :param engine: SQLAlchemy engine
    :return: None
    """
    inspector = inspect(engine)
    if not inspector.has_table(FoodData.__tablename__):
        Base.metadata.create_all(engine)


def load(products: list[ProductSchema], conn_str: str) -> None:
    """
    Load the products data into the database.

    :param products: List of ProductSchema objects
    :param conn_str: Connection string to the database
    :return: None
    """
    # Convert the products list to a pandas DataFrame
    df = pd.DataFrame([p.model_dump() for p in products]).rename(
        columns={"id": "product_id", "generic_name": "product_name"}
    )

    conn = connect(conn_str)
    create_table(conn)

    # Save the DataFrame to the database table
    df.to_sql(
        FoodData.__tablename__,
        con=conn,
        if_exists="append",
        index=False,
        dtype={c.name: c.type for c in FoodData.__table__.columns},
    )

from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker

from database import Base, engine
from models import Product

Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/")
def get_user():
    Session = sessionmaker(bind=engine)
    session = Session()

    new_product = Product(name="Pant")
    session.add(new_product)
    session.commit()

    products = session.query(Product).all()
    for product in products:
        print(product.id, product.name)
    return products

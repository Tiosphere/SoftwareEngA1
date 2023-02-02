from dataclasses import dataclass

from extensions import db


@dataclass
class Product(db.Model):
    id: int
    name: str
    price: int

    id = db.Column("product_id", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("name", db.String(30), nullable=False, unique=True)
    price = db.Column("price", db.Integer)
    belong = db.relationship("VendingMCProduct", backref="product", lazy=True)

    def edit_product(self, name: str, price: str):
        if name != "None":
            self.name = name
        if price != "None":
            self.price = int(price)
        db.session.commit()

    @staticmethod
    def find_by_id(product_id: int) -> "Product":
        return Product.query.get(product_id)

    @staticmethod
    def find_by_name(name: str) -> "Product":
        return Product.query.filter_by(name=name).first()

    @staticmethod
    def add_product(name: str, price: int):
        product = Product.find_by_name(name)
        if product is None:
            new_product = Product(name=name, price=price)
            db.session.add(new_product)
            db.session.commit()

    @staticmethod
    def get_all() -> "Product":
        return Product.query.all()

    @staticmethod
    def delete(product_id: int):
        Product.query.filter_by(id=product_id).delete()
        db.session.commit()
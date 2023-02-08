from dataclasses import dataclass
from datetime import datetime

from flask import jsonify
from sqlalchemy import JSON

from extensions import db
from models.stocks import VendingMCProduct
import datetime as dt


@dataclass
class TimeStamp(db.Model):
    vendingMC_id: int
    product_id: int
    quantity: int
    state: JSON
    date: datetime

    id = db.Column("time_stamp_id", db.Integer, primary_key=True, autoincrement=True)
    vendingMC_id = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    state = db.Column(db.JSON, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    @staticmethod
    def add_time_stamp(vendingMc_id: int, product_id: int, quantity: int):

        db.session.add(
            TimeStamp(
                vendingMC_id=vendingMc_id,
                product_id=product_id,
                quantity=quantity,
                state=jsonify(
                    VendingMCProduct.get_all_relation_by_mc(vendingMc_id)
                ).json,
                date=dt.datetime.utcnow(),
            )
        )
        db.session.commit()

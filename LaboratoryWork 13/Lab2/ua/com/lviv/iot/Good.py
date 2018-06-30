from flask import Flask, abort
from flask_restful import Api, Resource, reqparse, fields, marshal
from flask_sqlalchemy import SQLAlchemy
from Main import db
from Lab2.ua.com.lviv.iot.Types import Types


class Good(db.Model):
    __tablename__ = "GoodPython"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.column('name', db.String(80))
    material = db.column('material', db.String(80))
    amount = db.column('amount', db.Integer)
    price = db.column('price', db.Integer)

    def __init__(self, name="unknown", material="unknown", manufacturer="unknown", price=0, amount=0):
        self.manufacturer = manufacturer
        self.name = name
        self.material = material
        self.amount = amount
        self.price = price
        self.type = Types.GOOD.name

    def to_string(self):
        return "Type:", self.type, " Name:", self.name, " Material:", self.material, " Manufacturer:", self.manufacturer, " Price:", self.price, " Amount:", self.amount

    def __repr__(self):
        return '<User %r>' % self.name



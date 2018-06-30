from tokenize import String

from flask import Flask, abort
from flask_restful import Api, Resource, reqparse, fields, marshal
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, exists, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session

app = Flask(__name__, static_url_path="")
engine = create_engine('mysql://root:root@localhost/test_db', echo=True)
Base = declarative_base()


class Contact:
    __tablename__ = "contact"

    id = Column(Integer, primary_key=True)
    f_name = Column(String)
    l_name = Column(String)
    email = Column(String)
    message = Column(String)

    # ----------------------------------------------------------------------
    def __init__(self, f_name, l_name, email, message):
        """"""
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.message = message


if __name__ == '__main__':
    Base.metadata.create_all(engine)

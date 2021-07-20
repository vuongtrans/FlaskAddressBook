import datetime

from flask_appbuilder import Model
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import relationship

class Contact(Model):
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    address = Column(Text(250), nullable=False)
    city = Column(Text(100), nullable=False)
    state = Column(Text(2), nullable=False)
    zip_code = Column(Text(5), nullable=False)

    def __repr__(self):
        return self.name

def today():
    return datetime.datetime.today().strftime("%Y-%m-%d")

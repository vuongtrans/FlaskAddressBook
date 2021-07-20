import logging

from flask import Flask, request, flash, url_for, redirect, render_template
from flask_appbuilder import AppBuilder, SQLA
from flask_sqlalchemy import SQLAlchemy
from .models import Contact

"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app)
appbuilder = AppBuilder(app, db.session)

@app.route('/show')
def show_all():
   # GET
   return render_template('show_all.html', contacts = db.session.query(Contact) )

@app.route('/add', methods = ['GET', 'POST'])
def new():
   # POST
   if request.method == 'POST':
      if not request.form['first_name'] or not request.form['last_name'] or not request.form['address'] or not request.form['city'] or not request.form['state']:
         flash('Please enter all the fields', 'error')
      else:
        contact = Contact()
        contact.first_name = request.form['first_name']
        contact.last_name = request.form['last_name']
        contact.address = request.form['address']
        contact.city = request.form['city']
        contact.state = request.form['state']
        contact.zip_code = request.form['zip_code']
        db.session.add(contact)
        db.session.commit()
        flash('Record was successfully added')
        return redirect(url_for('show_all'))
   return render_template('new.html')


"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""

from . import views

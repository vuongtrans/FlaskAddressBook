from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from . import appbuilder, db
from .models import Contact

def contacts_query():
    return db.session.query(Contact)

class ContactView(ModelView):
    datamodel = SQLAInterface(Contact)
    list_columns = ["first_name", "last_name", "address", "city", "state", "zip_code"]

    show_template = "appbuilder/general/model/show_cascade.html"

db.create_all()

appbuilder.add_view(
    ContactView, "Contacts", icon="fa-folder-open-o", category="Contacts"
)
appbuilder.add_separator("Contacts")

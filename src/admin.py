import os
from flask_admin import Admin
# V-- CORRECTION: Import the models that actually exist in models.py
from models import db, Person, Planet, Species, Films 
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='Star Wars Admin', template_mode='bootstrap3')
    
    # Add your models to the admin panel
    # V-- CORRECTION: Use the models you imported, not 'User'
    admin.add_view(ModelView(Person, db.session))
    admin.add_view(ModelView(Planet, db.session))
    admin.add_view(ModelView(Species, db.session))
    admin.add_view(ModelView(Films, db.session))
from flask import Flask

from app.blueprints import blueprints
from app.models import db

app = Flask(__name__)

for blueprint in blueprints:
    app.register_blueprint(blueprint, url_prefix=f'/api/{blueprint.name}')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'

# Supress annoying deprecation warnings.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from flask import Flask

from app.blueprints import blueprints
from app.models import db

app = Flask(__name__)

app.url_map.strict_slashes = False

for blueprint in blueprints:
    app.register_blueprint(blueprint, url_prefix=f'/api/{blueprint.name}')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'

# Suppress annoying deprecation warnings.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

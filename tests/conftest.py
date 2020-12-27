from pytest import fixture

from app import app, db


@fixture(scope='function')
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'  # :memory:

    with app.app_context():
        db.create_all()

        with app.test_client() as client:
            yield client

        db.drop_all()

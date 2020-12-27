from app.models import User, db

user_json = {
    'first_name': 'Pavlo',
    'last_name': 'Havrylov',
    'address': 'Dnipro',
}


def test_create(client):
    create_user_json = user_json.copy()

    response = client.post('/api/users', json=create_user_json)
    assert response.status_code == 201
    assert response.json == {'id': 1, **create_user_json}


def create_user():
    user = User(**user_json)
    db.session.add(user)
    db.session.commit()
    db.session.refresh(user)
    return user


def test_read_all(client):
    response = client.get('/api/users')
    assert response.status_code == 200
    assert response.json == []

    user = create_user()

    response = client.get('/api/users')
    assert response.status_code == 200
    assert response.json == [user.json()]


def test_read_one(client):
    response = client.get('/api/users/1')
    assert response.status_code == 404

    user = create_user()

    response = client.get('/api/users/1')
    assert response.status_code == 200
    assert response.json == user.json()


def test_update(client):
    response = client.delete('/api/users/1')
    assert response.status_code == 404

    user = create_user()

    update_user_json = {
        'first_name': 'Havrylov',
        'last_name': 'Pavlo',
    }

    response = client.put('/api/users/1', json=update_user_json)
    assert response.status_code == 200
    assert response.json == {**user.json(), **update_user_json}


def test_delete(client):
    response = client.delete('/api/users/1')
    assert response.status_code == 404

    create_user()

    response = client.delete('/api/users/1')
    assert response.status_code == 204

    response = client.delete('/api/users/1')
    assert response.status_code == 404

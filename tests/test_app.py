def test_create(client):
    user_json = {
        'first_name': 'Pavlo',
        'last_name': 'Havrylov',
        'address': 'Dnipro',
    }
    response = client.post('/api/users', json=user_json)
    assert response.status_code == 201
    assert response.json == {'id': 1, **user_json}

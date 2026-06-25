from http import HTTPStatus


def test_create_user(client):

    response = client.post(
        "/auth/",
        json={
            "email": "alice@example.com",
            "password": "secret",
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "email": "alice@example.com",
        "id": 1,
    }


def test_read_root(client):

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Bem vindo!"}


def test_read_user(client):

    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "email": "alice@example.com",
                "id": 1,
            }
        ]
    }


def test_delete_user(client):

    response = client.delete("/users/1")

    response.status_code == HTTPStatus.OK
    response.json() == {"message": "User deletad!"}

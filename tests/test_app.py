from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (Organização)

    response = client.get('/')  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Afirmando)
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert

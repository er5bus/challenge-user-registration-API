import pytest
import time
import re

from src.settings.mailer import fm


@pytest.mark.parametrize("data", ({
    "username": "valid_test",
    "email": "valid_test@gmail.com",
    "plainPassword": "valid_password",
    "lastName": "valid_name",
    "firstName": "valid_name"
},{
    "username": "another_valid_test",
    "email": "another_valid_test@yahoo.com",
    "plainPassword": "valid_password",
    "lastName": "valid_name",
    "firstName": "valid_name"}))
def test_given_valid_data_Expect_successfull_activation(test_app, data):
    fm.config.SUPPRESS_SEND = 1
    with fm.record_messages() as outbox:
        response = test_app.post("/api/v1/authentication/signup", json=data)
        assert response.status_code == 204
        assert len(outbox) == 1
        assert outbox[0]['To'] == data["email"]
        token = outbox[0]['Token']
        response = test_app.post(f"/api/v1/authentication/activate-account/{token}")
        assert response.status_code == 204
        response = test_app.post("/api/v1/authentication/login", data={ 'username': data['username'], 'password': data['plainPassword'] })
        assert response.status_code == 200
        assert "access_token" in response.json()


@pytest.mark.parametrize("data", ({
    "username": "valid_test",
    "email": "valid_test@gmail.com",
    "plainPassword": "valid_password",
    "lastName": "valid_name",
    "firstName": "valid_name"
},{
    "username": "another_valid_test",
    "email": "another_valid_test@yahoo.com",
    "plainPassword": "valid_password",
    "lastName": "valid_name",
    "firstName": "valid_name"}))
def test_given_duplicated_users_Expect_fail_signup(test_app, data):
    response = test_app.post("/api/v1/authentication/signup", json=data)
    assert response.status_code == 204
    response = test_app.post("/api/v1/authentication/signup", json=data)
    assert response.status_code == 400
    assert "error_code" in response.json()


@pytest.mark.parametrize("data", ({
    "username": "yet_another_valid_test",
    "email": "yet_another_valid_test@gmail.com",
    "plainPassword": "valid_password",
    "lastName": "valid_name",
    "firstName": "valid_name"
},{
    "username": "itsanother_valid_test",
    "email": "itsanother_valid_test@yahoo.com",
    "plainPassword": "valid_password",
    "lastName": "valid_name",
    "firstName": "valid_name"}))
def test_given_expired_token_Expect_fail_activation(test_app, data):
    fm.config.SUPPRESS_SEND = 1
    with fm.record_messages() as outbox:
        response = test_app.post("/api/v1/authentication/signup", json=data)
        assert response.status_code == 204
        assert len(outbox) == 1
        assert outbox[0]['To'] == data["email"]
        token = outbox[0]['Token']
        time.sleep(2)
        response = test_app.post(f"/api/v1/authentication/activate-account/{token}")
        assert response.status_code == 400
        response = test_app.post("/api/v1/authentication/login", data={ 'username': data['username'], 'password': data['plainPassword'] })
        assert response.status_code == 401
        assert "error_code" in response.json()

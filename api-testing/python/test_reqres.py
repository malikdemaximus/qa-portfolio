import requests

def test_create_user():
    response = requests.post(
        "https://reqres.in/api/users",
        json={"name": "morpheus", "job": "leader"}
    )
    assert response.status_code == 201
    assert response.json()["job"] == "leader"

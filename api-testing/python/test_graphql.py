def test_graphql():
    query = """
    query {
      user(id: 1) {
        name
        email
      }
    }
    """
    response = requests.post("https://api.example.com/graphql", json={'query': query})
    assert response.json()["data"]["user"]["name"] == "John Doe"

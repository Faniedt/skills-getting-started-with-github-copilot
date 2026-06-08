def test_get_activities(client):
    # Arrange: client fixture

    # Act
    resp = client.get("/activities")

    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_signup_success(client):
    # Arrange
    email = "testuser@example.com"
    activity = "Chess Club"

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 200
    activities = client.get("/activities").json()
    assert email in activities[activity]["participants"]


def test_signup_duplicate(client):
    # Arrange
    email = "dup@example.com"
    activity = "Chess Club"

    # Act - first registration
    r1 = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert r1.status_code == 200

    # Act - duplicate registration
    r2 = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert r2.status_code == 400


def test_remove_participant(client):
    # Arrange
    email = "remove@example.com"
    activity = "Programming Class"
    client.post(f"/activities/{activity}/signup", params={"email": email})

    # Act
    r = client.delete(f"/activities/{activity}/participants/{email}")

    # Assert
    assert r.status_code == 200
    activities = client.get("/activities").json()
    assert email not in activities[activity]["participants"]


def test_remove_nonexistent_participant(client):
    # Arrange
    email = "noexist@example.com"
    activity = "Programming Class"

    # Act
    r = client.delete(f"/activities/{activity}/participants/{email}")

    # Assert
    assert r.status_code == 404

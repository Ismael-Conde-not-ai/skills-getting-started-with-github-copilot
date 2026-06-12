import pytest


class TestActivities:
    def test_get_activities(self, client):
        # Arrange
        # Act
        response = client.get("/activities")
        # Assert
        assert response.status_code == 200
        activities = response.json()
        assert isinstance(activities, dict)
        assert "Chess Club" in activities

    def test_signup_for_activity(self, client):
        # Arrange
        email = "teststudent1@mergington.edu"
        activity = "Tennis Club"
        # Act
        response = client.post(f"/activities/{activity}/signup", params={"email": email})
        # Assert
        assert response.status_code == 200
        assert email in response.json().get("message", "")

    def test_signup_duplicate_student(self, client):
        # Arrange
        email = "michael@mergington.edu"
        activity = "Chess Club"
        # Act
        response = client.post(f"/activities/{activity}/signup", params={"email": email})
        # Assert
        assert response.status_code == 400

    def test_delete_participant(self, client):
        # Arrange
        email = "lucas@mergington.edu"
        activity = "Tennis Club"
        # Act
        response = client.delete(f"/activities/{activity}/participants", params={"email": email})
        # Assert
        assert response.status_code == 200

    def test_delete_nonexistent_participant(self, client):
        # Arrange
        email = "nonexistent@mergington.edu"
        activity = "Chess Club"
        # Act
        response = client.delete(f"/activities/{activity}/participants", params={"email": email})
        # Assert
        assert response.status_code == 404

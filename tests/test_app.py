from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    activity = "Chess Club"
    email = "newstudent@mergington.edu"

    response = client.post(f"/activities/{activity}/signup?email={email}")
    assert response.status_code == 200

    delete_response = client.delete(f"/activities/{activity}/participants?email={email}")
    assert delete_response.status_code == 200

    activities = client.get("/activities").json()
    assert email not in activities[activity]["participants"]


def test_unregister_missing_participant_returns_404():
    response = client.delete("/activities/Chess Club/participants?email=ghost@mergington.edu")
    assert response.status_code == 404

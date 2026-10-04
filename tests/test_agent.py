from fastapi.testclient import TestClient
from agentx.main import app
client = TestClient(app)

def test_run_and_refuse():
    payload = client.post("/agent/run", json={"goal": 'draft a rollback literature note', "payload": {}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["roles"][0] == "supervisor" and "writer" in payload["roles"]
    refused = client.post("/agent/run", json={"goal": 'publish this to the internet'}).json()
    assert refused["refused"] is True

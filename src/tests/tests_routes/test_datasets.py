from fastapi.testclient import TestClient
from fastapi import status

def test_datasets(client: TestClient):    
    response = client.get("/datasets/namespace-name", headers={"X-Token": "hailhydra"})
    assert response.status_code == status.HTTP_200_OK
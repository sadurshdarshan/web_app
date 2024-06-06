import pytest
from web_app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_ip(client):
    response = client.get('/')
    response_text = response.data.decode('utf-8')
    


    

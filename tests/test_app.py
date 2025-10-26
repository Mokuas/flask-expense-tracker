import pytest
from app import app, db, MyCategories, MyExpenses

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_homepage_loads(client):
    resp = client.get('/')
    assert resp.status_code == 200

def test_add_category(client):
    client.post('/', data={'form_type': 'category', 'content': 'Food'})
    with app.app_context():
        cat = MyCategories.query.filter_by(category='Food').first()
        assert cat is not None

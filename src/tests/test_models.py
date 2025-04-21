import pytest
from database import db, Member, Technology
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()
    
    with app.app_context():
        db.create_all()
        
    yield client
    
    with app.app_context():
        db.drop_all()

def test_member_creation(client):
    with app.app_context():
        member = Member(name="Test Member", role="Test Role")
        db.session.add(member)
        db.session.commit()
        
        assert Member.query.count() == 1
        assert Member.query.first().name == "Test Member"

def test_member_api(client):
    with app.app_context():
        # Primera prueba (RED)
        response = client.get('/api/members')
        assert response.status_code == 200
        assert len(response.json) == 0  # No hay miembros inicialmente
        
        # Agregar miembro (GREEN)
        member = Member(name="API Test", role="Tester")
        db.session.add(member)
        db.session.commit()
        
        response = client.get('/api/members')
        assert len(response.json) == 1
        assert response.json[0]['name'] == "API Test"
        
        # REFACTOR: Podríamos extraer esto a una función helper

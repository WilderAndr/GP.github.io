from flask import Flask, render_template, jsonify
from database import db, Member, Technology

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../grupoa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()
    # Datos iniciales
    if not Member.query.first():
        initial_members = [
            Member(name="Wilder", role="Desarrollador Frontend", 
                  portfolio_url="https://wilderandr.github.io/PortafolioW.github.io/",
                  bio="Especializado en desarrollo frontend y experiencia de usuario."),
            # ... otros miembros
        ]
        db.session.add_all(initial_members)
        db.session.commit()
    
    if not Technology.query.first():
        initial_tech = [
            Technology(name="GitHub", category="Control de versiones", 
                      description="Plataforma de colaboración y control de versiones"),
            # ... otras tecnologías
        ]
        db.session.add_all(initial_tech)
        db.session.commit()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/members')
def api_members():
    members = Member.query.all()
    return jsonify([member.to_dict() for member in members])

@app.route('/api/technologies')
def api_technologies():
    techs = Technology.query.all()
    return jsonify([tech.to_dict() for tech in techs])

if __name__ == '__main__':
    app.run(debug=True)

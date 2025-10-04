from flask import Flask,request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portafolio.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class opinion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    mensaje = db.Column(db.Text, nullable=False)

@app.route("/")
def index ():
    return render_template("index.html")

@app.route("/opiniones", methods=["GET", "POST"])
def opiniones ():
    #traemos los datos del formulario
    nombre = request.form.get("nombre")
    correo = request.form.get("correo")
    mensaje = request.form.get("mensaje")
    fecha_actual = datetime.now()

    #creamos nueva opinion
    nueva_opinion = opinion(
        nombre=nombre,
        correo=correo,
        fecha=fecha_actual,
        mensaje=mensaje
    )
    #insertar y guardar la opinion 
    db.session.add(nueva_opinion)
    db.session.commit()
    return render_template ("index.html")

#ruta de los projectos
@app.route("/projectos")
def projectos ():
    return render_template("projectos.html")

@app.route("/sobremi")
def sobremi ():
    return render_template("sobremi.html")

if __name__ =="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

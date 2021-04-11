# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 18:30:36 2021
@author: sebas
"""
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
  
app = Flask(__name__)
app.secret_key = "cairocoders-ednalan-06300131"
#aqui configuramos la conexion a nuestra base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin@localhost:5432/Crud"                                      #mysql+pymysql://username:passwd@host/databasename 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  
db = SQLAlchemy(app)
  
#creamos nuestro modelo de usuarios para hacer las operaciones CRUD 
class users(db.Model):
    cedula = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))
    email = db.Column(db.String(100))
    direccion = db.Column(db.String(100))

    def __init__(self, cedula, nombre, email, direccion):
        self.cedula = cedula
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
  
#aqui ademas de cargar el inicio se valida que no existan problemas con el servidor ya que lanzara un error al usuario
#de lo contrario si todo va bien iniciara nuestra interfaz de inicio para la gestion de usuarios
@app.route('/')
def Index():
    try:
        all_data = users.query.all()
        return render_template("index.html", employees = all_data)
    except exc.OperationalError :
        message ="Lo sentimos El servidor no se encuentra disponible"
        return redirect(url_for("show_error_post",message=message))

#aqui planteamos una url especificamente para renderizar errores
@app.route('/errorServer/<message>')
def show_error_post(message = None):
    return render_template("error.html", message = message)
#metodo de insercion a la base de datos
@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        try:
            cedula = request.form['cedula']
            nombre = request.form['nombre']
            email = request.form['email']
            direccion = request.form['direccion']
            my_data = users(cedula,nombre, email, direccion)
            db.session.add(my_data)
            db.session.commit()
            flash("Usuario registrado correctamente")    
            return redirect(url_for('Index'))
        except exc.IntegrityError:
            message ="Lo sentimos este usuario ya esta registrado"
            flash(message)
            return redirect(url_for('Index'))
        except exc.OperationalError :
            message ="Lo sentimos El servidor no se encuentra disponible"
            return redirect(url_for('show_error_post',message=message))

#metodo de actualizacion de datos 
@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = users.query.get(request.form.get('cedula'))
        my_data.cedula = request.form['cedula']
        my_data.nombre = request.form['nombre']
        my_data.email = request.form['email']
        my_data.direccion = request.form['direccion']
        db.session.commit()
        flash("Cliente actualizado correctamente")
        return redirect(url_for('Index'))
  
#metodo para borrar datos
@app.route('/delete/<cedula>/', methods = ['GET', 'POST'])
def delete(cedula):
    my_data = users.query.get(cedula)
    db.session.delete(my_data)
    db.session.commit()
    flash("Cliente borrado correctamente")
    return redirect(url_for('Index'))
  
if __name__ == "__main__":
    app.run()
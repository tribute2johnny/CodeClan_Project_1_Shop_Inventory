from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.manufacturer import Manufacturer

from repositories import manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", all_manufacturers = manufacturers)

@manufacturers_blueprint.route("/show/<id>")
def show(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template("/manufacturers/show.html", manufacturer=manufacturer)

@manufacturers_blueprint.route('/manufacturers/<id>/delete', methods=['POST'])
def delete(id):
    manufacturer_repository.delete(id)
    return redirect('/manufacturers')

@manufacturers_blueprint.route('/manufacturers/new')
def new_manufacturer():
    return render_template("manufacturers/new.html")

@manufacturers_blueprint.route('/manufacturers', methods=['POST'])
def create_manufacturer():
    name = request.form['name']
    description = request.form['description']
    manufacturer = Manufacturer(name, description)
    manufacturer_repository.save(manufacturer)
    return redirect('/manufacturers')


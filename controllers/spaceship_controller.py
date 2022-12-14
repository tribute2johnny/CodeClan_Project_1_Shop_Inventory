from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.spaceship import Spaceship

from repositories import spaceship_repository, manufacturer_repository

from repositories.manufacturer_repository import select_all


spaceships_blueprint = Blueprint("spaceships", __name__)

#get method redirects to a page showing a list of all items in inventory
@spaceships_blueprint.route("/spaceships")
def spaceships():
    all_manufacturers = select_all()
    spaceships = spaceship_repository.select_all()
    return render_template("spaceships/index.html", all_spaceships = spaceships, all_manufacturers = all_manufacturers)


@spaceships_blueprint.route("/view/<id>")
def view(id):
    all_manufacturers = select_all()
    spaceship = spaceship_repository.select(id)
    return render_template("/spaceships/view.html", spaceship = spaceship, all_manufacturers = all_manufacturers)

@spaceships_blueprint.route('/spaceships/<id>/delete', methods=['POST'])
def delete(id):
    spaceship_repository.delete(id)
    return redirect('/spaceships')

@spaceships_blueprint.route("/spaceships/add")
def add_spaceship():
    manufacturers = manufacturer_repository.select_all()
    return render_template("spaceships/add.html", all_manufacturers = manufacturers)

@spaceships_blueprint.route("/spaceships", methods=['POST'])
def create_spaceship():
    model = request.form['model']
    type = request.form['type']
    manufacturer_id = request.form['manufacturer_id']
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    manufacturer = manufacturer_repository.select(manufacturer_id)
    spaceship = Spaceship(model, type, manufacturer, description, stock_quantity, buying_cost, selling_price)
    spaceship_repository.save(spaceship)
    return redirect('/spaceships')

@spaceships_blueprint.route('/spaceships/<id>/edit')
def edit_spaceship(id):
    spaceship = spaceship_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template('spaceships/edit.html', spaceship = spaceship, all_manufacturers = manufacturers)

@spaceships_blueprint.route('/spaceships/<id>', methods=['POST'])
def update_spaceship(id):
    model = request.form['model']
    type = request.form['type']
    manufacturer_id = request.form['manufacturer_id']
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    manufacturer = manufacturer_repository.select(manufacturer_id)
    spaceship = Spaceship(model, type, manufacturer, description, stock_quantity, buying_cost, selling_price, id)
    spaceship_repository.update(spaceship)
    return redirect('/spaceships')


@spaceships_blueprint.route('/spaceships/type/<type>')
def view_by_type(type):
    all_manufacturers = select_all()
    spaceships = spaceship_repository.get_products_by_type(type)
    return render_template('/spaceships/index.html', all_spaceships = spaceships, all_manufacturers=all_manufacturers)

@spaceships_blueprint.route('/spaceships/manufacturers', methods=['POST'])
def view_by_manufacturer():
    id = request.form['manufacturer_id']
    all_manufacturers = select_all()
    spaceships = spaceship_repository.get_products_by_manufacturer(id)
    return render_template('/spaceships/index.html', all_spaceships = spaceships, all_manufacturers=all_manufacturers)

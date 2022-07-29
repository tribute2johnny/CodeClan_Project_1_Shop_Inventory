from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.spaceship import Spaceship

from repositories import spaceship_repository

spaceships_blueprint = Blueprint("spaceships", __name__)

#get method redirects to a page showing a list of all items in inventory
@spaceships_blueprint.route("/spaceships")
def spaceships():
    spaceships = spaceship_repository.select_all()
    return render_template("spaceships/index.html", all_spaceships = spaceships)


@spaceships_blueprint.route("/view/<id>")
def view(id):
    spaceship = spaceship_repository.select(id)
    return render_template("/spaceships/view.html", spaceship=spaceship)

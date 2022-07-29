from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.spaceship import Spaceship

from repositories import spaceship_repository, manufacturer_repository

spaceships_blueprint = Blueprint("spaceships", __name__)

@spaceships_blueprint.route("/spaceships")
def spaceships():
    spaceships = spaceship_repository.select_all()
    return render_template("spaceships/index.html", all_spaceships = spaceships)
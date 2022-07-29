from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.manufacturer import Manufacturer

from repositories import spaceship_repository, manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", all_manufacturers = manufacturers)

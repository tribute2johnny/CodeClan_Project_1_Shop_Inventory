from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.manufacturer import Manufacturer

from repositories import spaceship_repository, manufacturer_repository

manufacturer_blueprint = Blueprint("manufacturers", __name__)



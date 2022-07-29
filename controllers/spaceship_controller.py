from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.spaceship import Spaceship

from repositories import spaceship_repository, manufacturer_repository

spaceship_blueprint = Blueprint("spaceships", __name__)
from db.run_sql import run_sql

from models.spaceship import Spaceship
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

def save(spaceship):
    sql = "INSERT INTO spaceships ( model, type, manufacturer_id, description, stock_quantity, buying_cost, selling_price) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [spaceship.model, spaceship.type, spaceship.manufacturer.id, spaceship.description, spaceship.stock_quantity, spaceship.buying_cost, spaceship.selling_price]
    results = run_sql(sql, values)
    id = results[0][id]
    spaceship.id = id
    return spaceship
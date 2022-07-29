from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.spaceship import Spaceship

def save(manufacturer):
    sql = "INSERT INTO manufacturers ( name, description ) VALUES (%s, %s) RETURNING *"
    values = [ manufacturer.name, manufacturer.description]
    results = run_sql(sql, values)
    id = results[0][id]
    manufacturer.id = id
    return manufacturer
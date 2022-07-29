from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.spaceship import Spaceship

def save(manufacturer):
    sql = "INSERT INTO manufacturers ( name, description ) VALUES (%s, %s) RETURNING *"
    values = [ manufacturer.name, manufacturer.description]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id
    return manufacturer


def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        manufacturer = Manufacturer[result['name'], result["description"], result['id']]
    return manufacturer
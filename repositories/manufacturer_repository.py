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
        manufacturer = Manufacturer(result['name'], result["description"], result['id'])
    return manufacturer

def select_all():
    manufacturers = []
    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(row['name'], row['description'], row['id'] )
        manufacturers.append(manufacturer)
    return manufacturers

def spaceships(manufacturer):
    spaceships = []

    sql = "SELECT * FROM spaceships WHERE manufacturer_id = %s"
    values = [manufacturer.id]
    results = run_sql(sql, values)

    for row in results:
        spaceship = Spaceship(row['model'], row['type'], manufacturer, row['description'], row['stock_quantity'], row['buying_cost'], row['selling_price'], row['id'] )
        spaceships.append(spaceship)
    return spaceships

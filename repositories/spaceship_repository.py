from db.run_sql import run_sql

from models.spaceship import Spaceship
import repositories.manufacturer_repository as manufacturer_repository

def save(spaceship):
    sql = "INSERT INTO spaceships ( model, type, manufacturer_id, description, stock_quantity, buying_cost, selling_price) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [spaceship.model, spaceship.type, spaceship.manufacturer.id, spaceship.description, spaceship.stock_quantity, spaceship.buying_cost, spaceship.selling_price]
    results = run_sql(sql, values)
    id = results[0]['id']
    spaceship.id = id
    return spaceship


def select_all():
    spaceships = []

    sql = "SELECT * FROM spaceships"
    results = run_sql(sql)

    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        spaceship = Spaceship(row['model'], row['type'], manufacturer, row['description'], row['stock_quantity'], row['buying_cost'], row['selling_price'], row['id'] )
        spaceships.append(spaceship)
    return spaceships

def select(id):
    spaceship = None
    sql = "SELECT * FROM spaceships WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        manufacturer = manufacturer_repository.select(result['manufacturer_id'])
        spaceship = Spaceship(result['model'], result['type'], manufacturer, result['description'], result['stock_quantity'], result['buying_cost'], result['selling_price'], result['id'])
    return spaceship

def delete_all():
    sql = "DELETE  FROM spaceships"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM spaceships WHERE id = %s"
    values = [id]
    run_sql(sql, values)


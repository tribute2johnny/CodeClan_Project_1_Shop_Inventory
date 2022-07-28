DROP TABLE IF EXISTS manufacturers;
DROP TABLE IF EXISTS spaceships;


CREATE TABLE spaceships(
    id SERIAL PRIMARY KEY,
    model VARCHAR(255),
    type VARCHAR(255),
    description VARCHAR(255)
    stock_quantity INT,
    buying_cost INT,
    selling_price INT
)


CREATE TABLE manufacturers(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT
)


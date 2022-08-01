DROP TABLE IF EXISTS spaceships;
DROP TABLE IF EXISTS manufacturers;


CREATE TABLE manufacturers(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    active BOOLEAN
);

CREATE TABLE spaceships(
    id SERIAL PRIMARY KEY,
    model VARCHAR(255),
    type VARCHAR(255),
    manufacturer_id INT REFERENCES manufacturers(id),
    description TEXT,
    stock_quantity INT,
    buying_cost INT,
    selling_price INT
);

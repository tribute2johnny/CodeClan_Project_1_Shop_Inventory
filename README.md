# CodeClan_Project_1_Shop_Inventory

A spaceship shop back end that sellers can interact with, updating products and adding ships and manufacturers.

Unittest has been added to test classes. To run unittest open the terminal and enter python_3 run_tests.py.
These tests just test the functionality of the classes in spaceship.py and manufacturer.py.

To test the controllers and repositories you can run the console file by entring into the terminal. python3 console.py

To run the app: 1. Create a database called ship ship_emporium
                2. To drop and create the tables in the terminal enter psql -d ship_emporium -f db/ship_emporium.sql
                3. To populate the tables enter into the terminal python3 console.py
                4. To run the server cd into the Galactic_Ship_Emporium and enter flask run

The app can be navigated through the nav menu under the header. The app lets the user add, update and delete products.
And lets you add, update and activate/deactivate manufacturers. Deactivated manufacturers cannot be added to new products.
They can be activated again from the edit feature. We can also view all ships by manufacturer via the drop down menu on
the navigation bar. And all ships by class via the link next to the ship type.

Technologies used HTML/CSS, Python, Flask, PostgreSQL and psycopg2
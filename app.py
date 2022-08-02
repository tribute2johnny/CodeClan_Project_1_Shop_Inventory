from flask import Flask, render_template
from controllers.spaceship_controller import spaceships_blueprint
from controllers.manufacturer_controller import manufacturers_blueprint
from repositories.manufacturer_repository import select_all

app = Flask(__name__)

app.register_blueprint(spaceships_blueprint)
app.register_blueprint(manufacturers_blueprint)


@app.route('/')
def home():
    all_manufacturers = select_all()
    return render_template('index.html', all_manufacturers = all_manufacturers)

if __name__ == '__main__':
    app.run(debug=True)

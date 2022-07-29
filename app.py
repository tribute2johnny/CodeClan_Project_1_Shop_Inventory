from flask import Flask, render_template
from controllers.spaceship_controller import spaceship_blueprint
from controllers.manufacturer_controller import manufacturer_blueprint

app = Flask(__name__)

app.register_blueprint(spaceship_blueprint)
app.register_blueprint(manufacturer_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

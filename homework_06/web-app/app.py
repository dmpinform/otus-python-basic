from flask import Flask, request, render_template
from flask_migrate import Migrate, upgrade

from web_app.models import db
from web_app.views.products import products_app

app = Flask(__name__)

app.config.from_object("config.DevelopmentConfig")

app.register_blueprint(products_app)

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about/")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)

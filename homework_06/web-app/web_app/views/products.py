from flask import Blueprint, request, jsonify, render_template, url_for, redirect
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError

from ..models import db
from ..models import Product

products_app = Blueprint("products_app", __name__)


@products_app.route("/", endpoint="list")
def list_products():
    products = Product.query.all()
    return render_template("index.html", products=products)


@products_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def product_add():
    if request.method == "GET":
        return render_template("add.html")

    product_name = request.form.get("product-name")
    product_description = request.form.get("product-description")

    if not product_name or not product_description:
        raise BadRequest("Field product-name and product_description is required!")

    product = Product(name=product_name, description=product_description)
    db.session.add(product)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise InternalServerError(f"Could not save product with name {product_name!r}")

    url = url_for("index")
    return redirect(url)

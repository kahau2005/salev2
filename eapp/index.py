from flask import Flask, render_template, request
from eapp import app, dao

@app.route('/')
def index():
    categories = dao.load_categories()
    products = dao.load_products(request.args.get("category_id"), request.args.get("kw"))
    return render_template('index.html', categories=categories, products=products)


if __name__ == '__main__':
    app.run(debug=True)

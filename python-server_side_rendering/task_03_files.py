#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    with open('products.json') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    id_filter = request.args.get('id', type=int)
    error = None
    products = []

    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    else:
        error = "Wrong source"

    if not error:
        if id_filter is not None:
            products = [p for p in products if int(p['id']) == id_filter]
            if not products:
                error = "Product not found"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)


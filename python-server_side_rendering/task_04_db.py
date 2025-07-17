#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

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

def read_sql(id_filter=None):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    if id_filter:
        cursor.execute("SELECT id, name, category, price FROM Products WHERE id = ?", (id_filter,))
    else:
        cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()
    products = []
    for row in rows:
        products.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        })
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
    elif source == 'sql':
        products = read_sql(id_filter)
        if id_filter and not products:
            error = "Product not found"
    else:
        error = "Wrong source"

    if not error and source in ['json', 'csv'] and id_filter is not None:
        filtered = [p for p in products if int(p['id']) == id_filter]
        if filtered:
            products = filtered
        else:
            error = "Product not found"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)


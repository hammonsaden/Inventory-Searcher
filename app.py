import sqlite3
from bottle import run, route, redirect, response, request, template
from datetime import datetime

# Main Page
@route('/', method='GET')
def index():
    return template('views/index')

# Inventory Viewer
@route('/Inventory', method='GET')
def inventory():
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("SELECT name, quantity, priceeach FROM inventory")
    data = cur.fetchall()
    conn.close()

    return template('views/inventory', rows=data)


# Order Submitter
@route('/SubmitOrder', method=['GET', 'POST'])
def submit_order():
    if request.method == "GET":
        return template("views/submitorder")
    else:
        item_name = request.forms.get('item_name')
        ordered = request.forms.get('ordered')

        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        cur.execute("SELECT priceeach FROM inventory WHERE name=?", (item_name,))
        r = cur.fetchone()
        if r:
            priceeach = r[0]
            total = round(float(ordered) * priceeach, 2)

            cur_datetime = datetime.now().strftime('%Y-%m-%d')

            # Putting Order into the DB
            cur.execute("INSERT INTO orders (datetime, name, ordered, priceeach, total) VALUES (?, ?, ?, ?, ?)",
                        (cur_datetime, item_name, ordered, priceeach, total))

            # Updating the overall quantity in stock value
            cur.execute("UPDATE inventory SET quantity = quantity + ? WHERE name = ?", (ordered, item_name))
            
            conn.commit()
            conn.close()

            redirect('/ViewOrders')

# Open Order Viewer
@route('/ViewOrders', method='GET')
def view_orders():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute("SELECT datetime, name, ordered, priceeach, total FROM orders")
    data = cur.fetchall()

    return template('views/vieworder', rows=data)







if __name__ == "__main__":
    run(debug=True, reloader=True)
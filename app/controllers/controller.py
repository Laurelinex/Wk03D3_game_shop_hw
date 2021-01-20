from flask import render_template
from app import app
from app.models.order_list import orders
# from app.models.indie_games_list import games

@app.route('/')
def index():
    return render_template('index.html', title='Home', orders=orders)

@app.route('/orders/<index>')
def get_order(index):
    chosen_order = orders[int(index)]
    return render_template('order.html', order=chosen_order)
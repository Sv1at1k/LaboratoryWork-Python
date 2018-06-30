from app import app
from flask import request
from app import db
from Good import Good

@app.route('/')
def index():
    firstmember = Good.query.first()
    return '<h1> Here you can find good list! </h1>'

@app.route('/good')
def view():
    good = Good.query.first()
    if device is not None:
        return str('First member name \n' + good.to_string())
    else:
        return "Device with this id does not exist"

@app.route('/device/<id>')
def get_good(id):
    good = good.query.get(id)
    if good is not None:
        return good.to_string()
    else:
        return "Good with this id does not exist"

@app.route('/good', methods=['POST'])
def add_good():
    id = request.json['id']
    name = request.json['name']
    material = request.json['amoubt']
    amount = request.json['amount']
    price = request.json['price']

    new_good = Good()
    new_good.id = id
    new_good.name = name
    new_good.material = material
    new_good.amount = amount
    new_good.price = price
    db.session.add(new_good)
    db.session.commit()

    return str(new_good.to_string())

@app.route('/good/<id>', methods=['PUT'])
def good_update(id):
    name = request.json['name']
    material = request.json['amoubt']
    amount = request.json['amount']
    price = request.json['price']

    new_good = Good.query.get(id)
    new_good.id = id
    new_good.name = name
    new_good.material = material
    new_good.amount = amount
    new_good.price = price

    db.session.commit()

    return new_device.to_string()

@app.route('/good/<id>', methods=['DELETE'])
def device_delete(id):
    good = good.query.get(id)
    db.session.delete(good)
    db.session.commit()

    return str("Deleting succssesful")
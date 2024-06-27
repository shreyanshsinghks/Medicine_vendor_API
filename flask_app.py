from arrow import get
from flask import Flask, render_template, request, jsonify

from create import createTables, createUser
from GetUsers import getAllusers, getSpecificUsers, getAllProducts
from UserOperation import updateUserAccess

# Adding extra
from create import createProduct



app= Flask(__name__)


@app.route('/createUser',methods = ['POST'])
def create_user():

    name =  request.form['name']
    password= request.form['password']
    email = request.form['email']
    address= request.form['address']
    phone = request.form['phone']
    pincode  = request.form['pincode']
    dbReb = createUser(name=name, email=email, address=address, phone=phone,password=password,pincode=pincode)
    if dbReb:
        return jsonify({"message":"success", "status":200})
    else:
        return jsonify({"message":"failed", "status":400})
    

# Adding the code for inserting product by myself
@app.route('/createProduct',methods = ['POST'])
def create_product():
    name =  request.form['name']
    price = request.form['price']
    category = request.form['category']
    stock = request.form['stock']
    dbReb = createProduct(name=name, price=price, category=category, stock=stock)
    if dbReb:
        return jsonify({"message":"success", "status":200})
    else:
        return jsonify({"message":"failed", "status":400})
    
# Adding the code for getting all the products
@app.route('/getAllProducts',methods = ['GET'])
def get_all_products():
    products = getAllProducts()
    return products


@app.route('/getAllUsers',methods = ['GET'])
def getAllUsers():
    return getAllusers()

@app.route('/getSpecificUser',methods = ['GET'])
def getSpecificUser():
    userId = request.form['userId']
    return getSpecificUsers(userId = str(userId))

@app.route('/updateUserAccess',methods = ['PATCH'])
def update_user_access():
    userId = request.form['userId']
    approved = request.form['approved']
    blocked = request.form['blocked']
    updateUserAccess(id = userId,approved = approved,blocked = blocked)
    return "Access updated successfully"


@app.route('/', methods=['GET'])
def hello():
    return "Hello"


if __name__ == "__main__":
    # createTables()
    app.run()

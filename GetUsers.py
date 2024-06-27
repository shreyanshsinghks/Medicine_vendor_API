import sqlite3
import json
from webbrowser import get

def getAllusers():
    conn=sqlite3.connect("my_medicalShop.db")
    cursor= conn.cursor()
    cursor.execute("SELECT * FROM User")
    users = cursor.fetchall()
    conn.close()
    
    userJson = []
    for user in users:
        tempUser = {
            "id": user[0],
            "user_id": user[1],
            "password": user[2],
            "Level": user[3],
            "DateOfAccountCreation": user[4],
            "approved": user[5],
            "Block": user[6],
            "name": user[7],
            "Address": user[8],
            "email": user[9],
            "phone": user[10],
            "PinCode": user[11]
        }
        userJson.append(tempUser)
    return json.dumps(userJson)


def getSpecificUsers(userId):
    conn=sqlite3.connect("my_medicalShop.db")
    cursor= conn.cursor()
    cursor.execute("SELECT * FROM User WHERE user_id = ?", (userId,))
    users = cursor.fetchall()
    conn.close()
    
    userJson = []
    for user in users:
        tempUser = {
            "id": user[0],
            "user_id": user[1],
            "password": user[2],
            "Level": user[3],
            "DateOfAccountCreation": user[4],
            "approved": user[5],
            "Block": user[6],
            "name": user[7],
            "Address": user[8],
            "email": user[9],
            "phone": user[10],
            "PinCode": user[11]
        }
        userJson.append(tempUser)
    return json.dumps(userJson)


# Adding function for getting all the products
def getAllProducts():
    conn=sqlite3.connect("my_medicalShop.db")
    cursor= conn.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    conn.close()
    
    productJson = []
    for product in products:
        tempProduct = {
            "Product_id": product[0],
            "name": product[1],
            "price": product[2],
            "category": product[3],
            "stock": product[4],
            "isActive": product[5]
        }
        productJson.append(tempProduct)
    return json.dumps(productJson)


def getAllOrders():
    conn=sqlite3.connect("my_medicalShop.db")
    cursor= conn.cursor()
    cursor.execute("SELECT * FROM Orders")
    orders = cursor.fetchall()
    conn.close()
    
    orderJson = []
    for order in orders:
        tempOrder = {
            "id": order[0],
            "date": order[1],
            "itemId": order[2],
            "quantity": order[3],
            "venderId": order[4],
            "isApproved": order[5]
        }
        orderJson.append(tempOrder)
    return json.dumps(orderJson)

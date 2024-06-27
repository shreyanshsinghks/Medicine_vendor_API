import sqlite3
from datetime import date


def updateUserAccess(id, approved, blocked):

    conn=sqlite3.connect("my_medicalShop.db")
    cursor= conn.cursor()

    cursor.execute("""
UPDATE User SET approved = ?, Block = ? WHERE id = ?
""", (approved, blocked, id))
    
    conn.commit()
    conn.close()
    return True

# Update order isApproved status
def updateOrderAccess(id, approved):

    conn=sqlite3.connect("my_medicalShop.db")
    cursor= conn.cursor()

    cursor.execute("""
UPDATE Orders SET isApproved = ? WHERE id = ?
""", (approved, id))
    
    conn.commit()
    conn.close()
    return True


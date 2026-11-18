import os
import sqlite3
DB_PATH=os.path.join(os.path.dirname(__file__),"hotel.db")
def create_table():
    conn=sqlite3.connect(DB_PATH)
    try:
        with conn:
            conn.execute("""
                         CREATE TABLE IF NOT EXISTS rooms(
                         room_id INTEGER PRIMARY KEY AUTOINCREMENT,
                         room_number TEXT UNIQUE,
                         price REAL,
                        customer_name TEXT
                        )
                        """)
    except sqlite3.Error as e:
        print("Database error :",e)
    finally:
        conn.close()
def add_room(room_number,price,customer_name):
    conn=sqlite3.connect(DB_PATH)
    try:
        with conn:
           conn.execute("INSERT INTO rooms (room_number,price,customer_name) VALUES(?,?,?)",
                        (room_number,price,customer_name))
           print(f"Room '{room_number}' add succcessfully!")
    except sqlite3.Error as e:
        print("DataBase Error",e)
    finally:
        conn.close()
def view_all_rooms():
    conn=sqlite3.connect(DB_PATH)
    try:
        cur=conn.execute("SELECT room_id, room_number,price,customer_name FROM rooms")
        rows=cur.fetchall()
        if not rows:
            print("No room found.")
            return
        else:
            for row in rows:
                print(f"ROOM_ID :{row[0]},ROOM_NUM :{row[1]},PRICE:{row[2]},CUSTOMER_NAME:{row[3]}")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()
def view_rooms_by_id(room_id):
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.execute(
            "SELECT room_id,room_number,price,customer_name FROM rooms WHERE room_id = ?", (room_id,)
        )
        row = cur.fetchone()

        if not row:
            print(f"No room found with ID {room_id}.")
            return

        print(f"ROOM_ID :{row[0]},ROOM_NUM :{row[1]},PRICE:{row[2]},CUSTOMER_NAME:{row[3]}")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()

def search_rooms_by_customer(customer_name):
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.execute(
            "SELECT room_id,room_number,price,customer_name FROM rooms WHERE customer_name = ?", (customer_name)
        )
        rows = cur.fetchall()

        if not rows:
            print(f"No rooms found by customer '{customer_name}'.")
            return

        print(f"\n--- Rooms by customer: {customer_name} ---")
        for row in rows:
            print(f"ROOM_ID :{row[0]},ROOM_NUM :{row[1]},PRICE:{row[2]},CUSTOMER_NAME:{row[3]}")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()
def update_room_num(room_id,new_room_num):
    conn = sqlite3.connect(DB_PATH)
    try:
        with conn:
            cur = conn.execute(
                "UPDATE rooms SET room_num = ? WHERE room_id = ?", (new_room_num, room_id)
            )
            if cur.rowcount == 0:
                print(f"No room found with ID {room_id}.")
            else:
                print(f"Room ID {room_id} title updated to '{new_room_num}'.")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()


def delete_room(room_id):
    conn = sqlite3.connect(DB_PATH)
    try:
        with conn:
            cur = conn.execute("DELETE FROM rooms WHERE room_id = ?", (room_id))
            if cur.rowcount == 0:
                print(f"No room found with ID {room_id}.")
            else:
                print(f"Room ID {room_id} deleted successfully.")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()


def main():
    create_table()

    while True:
        print("\n=== HOTEL Management System ===")
        print("1. View All Rooms")
        print("2. Add New Room")
        print("3. View Room by ID")
        print("4. Search Rooms by Customer")
        print("5. Update Room Num")
        print("6. Delete Room")
        print("0. Exit")

        choice = input("Enter your choice (0-7): ").strip()
        if choice=="1":
            view_all_rooms()
        elif choice=="2":
            room_num= input("Enter room number : ").strip()
            try:
                room_no= int(room_num)
            except ValueError:
                print("Invalid ID. Please enter numbers only.")
                continue
            customer_name=input("Enter Customer Name :").strip()
            if not customer_name:
                print("No customer name found.")
                continue
            price= input("Enter room price : ").strip()
            try:
                room_price= int(price)
            except ValueError:
                        print("Invalid ID. Please enter numbers only.")
                        continue
            
            add_room(room_no,room_price,customer_name)
        elif choice == "3":
            id_input = input("Enter room ID: ").strip()
            try:
                room_id = int(id_input)
            except ValueError:
                print("Invalid ID. Please enter numbers only.")
                continue

            view_rooms_by_id(room_id)

        elif choice == "4":
            customer_name = input("Enter customer name to search: ").strip()
            search_rooms_by_customer(customer_name)

        elif choice == "5":
            id_input = input("Enter room ID to update: ").strip()
            try:
                room_no_id = int(id_input)
            except ValueError:
                print("Invalid ID. Please enter numbers only.")
                continue

            new_room_number = input("Enter new title: ").strip()
            if not new_room_number:
                print(" Room number cannot be empty.")
                continue

            update_room_num(room_id, new_room_number)

        elif choice == "6":
            id_input = input("Enter room ID to delete: ").strip()
            try:
                room_id = int(id_input)
            except ValueError:
                print("Invalid ID. Please enter numbers only.")
                continue

            delete_room(room_id)

        elif choice == "0":
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid selection. Please choose an option from 0 to 6.")


if __name__ == "__main__":
    main()





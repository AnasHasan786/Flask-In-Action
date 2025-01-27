from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (like a database)
data = [
    {"id": 1, "name": "Pizza", "price": 10},
    {"id": 2, "name": "Burger", "price": 8},
    {"id": 3, "name": "Pasta", "price": 12},
]

@app.route('/')
def home():
    return "<p>Hi, I am learning about APIs with JSON in Flask</p>"

# API to fetch all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)     # Convert list to JSON and return

# API to fetch a single item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    for item in data:
        if item["id"] == item_id:
            return jsonify(item)
        
    return jsonify({"error": "Item not found"}), 404

# API to add a new item (using POST request)
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.get_json()   # Getting JSON data from the request
    data.append(new_item)
    return jsonify({"message": "Item added successfully!", "data": new_item}), 201

# API to delete an item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    for item in data:
        if item["id"] == item_id:
            data.remove(item)
            return jsonify({"message": "Item deleted successfully!"})
    
    return jsonify({"error": "Item not found"}), 404
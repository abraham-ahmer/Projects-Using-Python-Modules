# Build a program that reads a JSON file of product data (name, price, quantity) and prints the total inventory value.

import json

with open("data.json", "r") as f:
    data = json.load(f)
    inventory_number = 0

for i in data:
    inventory_number += 1
    while True:
        try:
            actual_price = i["price"] * i["quantity"]
            print(f"Product name: {i["name"]}. Has {i["quantity"]} packets, each worth {i["price"]} PKR. Total inventory value: {actual_price} PKR")
            break
        except Exception as e:
            print(f"Some issues detected in that inventory number {inventory_number}")
            break
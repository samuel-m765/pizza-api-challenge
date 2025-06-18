# pizza-api-challenge

A simple Flask REST API for managing restaurants, pizzas, and restaurant-pizza associations.

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone the repository
cd pizza-api-challenge
2. Create and Activate Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Or if you're using Pipenv:

bash
Copy
Edit
pipenv install
pipenv shell
 Run the App
Set the Flask app and run the server:

bash
Copy
Edit
export FLASK_APP=server:create_app
flask run
 Database Migration & Seeding
Initialize Migrations (first time only):
bash
Copy
Edit
flask db init
Create Migration Script:
bash
Copy
Edit
flask db migrate -m "Initial migration"
Apply Migration:
bash
Copy
Edit
flask db upgrade
(Optional) Seed the Database
You can use Flask shell to manually create records:

bash
Copy
Edit
flask shell
Then:

python
Copy
Edit
from server import db
from server.models import Restaurant, Pizza

r1 = Restaurant(name="Domino's", address="123 Pizza St")
p1 = Pizza(name="Margherita", ingredients="cheese, tomato, basil")

db.session.add_all([r1, p1])
db.session.commit()
 Routes Summary
Method	Endpoint	Description
GET	/restaurants/	Get all restaurants
GET	/restaurants/<id>/	Get a single restaurant
POST	/restaurants/	Create a new restaurant
GET	/pizzas/	Get all pizzas
POST	/restaurant_pizzas/	Link a pizza to a restaurant

 Example Requests & Responses
 Create a Restaurant
POST /restaurants/

Request JSON:

json
Copy
Edit
{
  "name": "Pizza Planet",
  "address": "456 Cheese Rd"
}
Response:

json
Copy
Edit
{
  "id": 1,
  "name": "Pizza Planet",
  "address": "456 Cheese Rd"
}
✅ Get All Restaurants
GET /restaurants/

Response:

json
Copy
Edit
[
  {
    "id": 1,
    "name": "Pizza Planet",
    "address": "456 Cheese Rd"
  },
  ...
]
Validation Rules
name and address are required for restaurants.

price for restaurant_pizza must be between 1 and 30.

Only existing pizza_id and restaurant_id can be used when linking in /restaurant_pizzas/.

Using Postman
Open Postman

Set the method (GET, POST, etc.)

Use the appropriate URL, e.g., http://127.0.0.1:5000/restaurants/

For POST requests:

Go to Body > raw

Choose JSON

Paste your JSON payload (see examples above)

Click Send
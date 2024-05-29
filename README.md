# Product Inventory Management API
This project is a Django-based web application that provides CRUD (Create, Read, Update, Delete) APIs for managing a product inventory. It allows users to perform operations such as adding, retrieving, updating, and deleting products from the inventory.

## Features
CRUD APIs: Provides endpoints for managing products, including creating new products, retrieving all products, updating existing products, and deleting products by ID.
Product Model: Defines a Product model with attributes such as ID, name, category, and price to represent products in the inventory.
SQLite Database: Uses SQLite as the database backend for storing product data. SQLite is lightweight and suitable for small-scale deployments.
Dockerized: The application is containerized using Docker, making it easy to deploy and run in different environments.
API Documentation: Provides documentation for the available APIs, including URL patterns and descriptions.

## Usage
To run the project locally, follow these steps:

Clone the repository:
git clone https://github.com/your_username/product-inventory.git

Navigate to the project directory:
cd product-inventory

Build and run the Docker containers:
docker-compose up --build

Access the application in your web browser at http://localhost:8000.

## API Endpoints
GET /api/products/: Retrieve a list of all products.
GET /api/products/{id}/: Retrieve a specific product by ID.
POST /api/products/: Create a new product.
PUT /api/products/{id}/: Update an existing product by ID.
DELETE /api/products/{id}/: Delete a product by ID.
For detailed documentation of API endpoints and usage examples, refer to the API documentation provided with the application.

## Author
Madhav

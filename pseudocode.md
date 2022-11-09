# Backend Bistro
## Roger Mullins

## Basic Requirements
- Store the following data in your PostgreSQL database and implement models for READ only operations for the following data:
    - Menu Items
        -Title
        -Description
        -Price
        -Spicy Level
        -FK to Category
        -FK to Cuisine
    - Category (Appetizer, Dessert, Main Dish, etc.)
    - Cuisine (American, Thai, etc.)

- Create views to send JSON data back to a GET request for a list of all menu items with the category and cuisine labels nested in the data.
- Create routes to use the views created in the previous step.
- Change the URL in the React Restaurant Code with the gitpod url of your running backend code only. (NOTE: We shouldn’t be writing any React code for basic requirements)
- Example view functions
    - /api/menu-items/
        - Read: view full list of menu item information
    - Build more routes as needed for your project if you finish early (Create, Read, Update, Delete)
- Additional Requirements
    - Use the tools and technologies covered in class to complete your api.
    - Your repo should be public so that others can see your code and comment on it. 	
        - Remember to push to GitHub!
- Stretch Goals
    - Handle exceptions with error messaging on front end and/or back end.
    - Additional CRUD functionality
    - Add a sale price or special price for items for the restaurant with new fields on the models.
    - Add a custom field(s) to the API that improves the functionality of the restaurant front end
    - Add a check for the current date and time to filter the list of items sent back to the frontend. 
- If you finish early
    - Add info to your projects README.md

# Endpoint(s)
First iteration: /api/json (to return list of all data)
Definition:
- dish
    - FK category
        - title
    - title
    - description
    - price
    - spice_level
    - FK cuisine
        - title

![db-diagram]('Backend Bistro.png')
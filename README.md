# Flask-In-Action 🚀  
_A comprehensive repository to learn and practice Flask by exploring various fundamental and advanced topics._

## **About This Repository**  

<p align="justify">
  This repository is a collection of Flask scripts that I’ve created while learning Flask. It covers a wide array of concepts, ranging from the basics to advanced features, to help you gain hands-on experience 
  with the Flask web framework.  
  
  Each topic is organized and well-documented, making it easy for anyone to follow and understand. Whether you’re a beginner or an intermediate learner, this repository is designed to be your one-stop resource 
  for mastering Flask.
</p>

<p align="center">
  <img src="https://i.imgur.com/tvnriz5.png" alt="Flask" width="900" height="300">
</p>

---

## **Table of Contents**  
1. [Getting Started](#getting-started)  
2. [Folder Structure](#folder-structure)  
3. [Topics Covered](#topics-covered)  
   - [Routing and URL Building](#1-routing-and-url-building)  
   - [Templates and Rendering](#2-templates-and-rendering)  
   - [Sessions and Cookies](#3-sessions-and-cookies)  
   - [Working with Databases](#4-working-with-databases)  
   - [Blueprints and Views](#5-blueprints-and-views)  
   - [Authentication](#6-authentication)  
   - [File Uploads](#7-file-uploads)  
   - [APIs and JSON](#8-apis-and-json)  
   - [Redirects and Error Handling](#9-redirects-and-error-handling)  
4. [How to Use This Repository](#how-to-use-this-repository)  
5. [Requirements](#requirements)   

---

## **Getting Started**  

**Clone this repository to your local system:**

```bash
git clone https://github.com/your-username/Flask-In-Action.git
cd Flask-In-Action
```

**Set up the virtual environment:**

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

---

## **Folder Structure**

```bash
Flask-In-Action/
│
├── blog/                # Contains a demo blog app for exploring Blueprints and views
├── templates/           # HTML templates for rendering
├── uploads/             # Directory for file uploads (e.g., images, documents)
├── user/                # User-related functionalities (authentication, sessions, etc.)
│
├── apis_with_json.py    # Example of building APIs and returning JSON
├── authentication.py    # User authentication using sessions and hashed passwords
├── blueprints_and_views.py  # Demonstrates the use of Blueprints and views
├── cookies.py           # Examples of using cookies in Flask
├── file_upload.py       # Demonstrates handling file uploads
├── hello.py             # A simple "Hello, World!" Flask app
├── http_methods.py      # Explores HTTP methods (GET, POST, etc.)
├── redirects_and_errors.py # Redirects and custom error pages
├── rendering_templates.py  # Examples of rendering Jinja2 templates
├── routing.py           # Basic routing and URL-building examples
├── sessions.py          # Managing user sessions
├── unique_urls.py       # Demonstrates unique URL generation
├── url_building.py      # Working with `url_for` to build dynamic URLs
├── variable_rules.py    # Demonstrates Flask's variable rules in routes
├── working_with_databases.py # Interacting with SQLite using Flask-SQLAlchemy
└── .gitignore           # Ignores unnecessary files from being committed
```

---

## **Topics Covered**

<p align="justify">
  <strong>1. Routing and URL Building</strong>
  
  Learn how to create dynamic routes and use Flask's `url_for` function to generate URLs dynamically.
  Example: `routing.py`, `url_building.py`
  
  **2. Templates and Rendering**
  
  Understand how to use Jinja2 templates for dynamic content rendering.
  Example: `rendering_templates.py`, `templates/`
  
  **3. Sessions and Cookies**
  
  Manage user sessions and leverage cookies for storing client-side data.
  Example: `sessions.py`, `cookies.py`
  
  **4. Working with Databases**
  
  Use Flask-SQLAlchemy to interact with a database. Covers creating tables, adding data, and querying.
  Example: `working_with_databases.py`
  
  **5. Blueprints and Views**
  
  Learn how to modularize your Flask application using Blueprints for better structure.
  Example: `blueprints_and_views.py`
  
  **6. Authentication**
  
  Implement user authentication, including login, logout, and password hashing for security.
  Example: `authentication.py`
  
  **7. File Uploads**
  
  Handle file uploads securely, including saving files and validating their types.
  Example: `file_upload.py`
  
  **8. APIs with JSON**
  
  Build RESTful APIs and return JSON responses to clients.
  Example: `apis_with_json.py`
  
  **9. Redirects and Error Handling**
  
  Implement URL redirection and custom error pages for better user experience.
  Example: `redirects_and_errors.py`
</p>

---

## **How to Use This Repository**

1. Explore each `.py` file to understand the concept and its implementation.
2. Run the Flask app for a particular topic and test it in the browser. For example:

```bash
flask --app routing.py run --debug
```

3. Check the `templates/` folder for HTML files used in template rendering.

---

## **Requirements**

- Python 3.8 or higher
- Flask
- Flask-SQLAlchemy
- Jinja2

Install the dependencies using:

```bash
pip install -r requirements.txt
```


Thank you for exploring this repository.

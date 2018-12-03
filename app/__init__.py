import os
from flask import Flask, jsonify
import psycopg2
from flask_bcrypt import Bcrypt

# Initialize application
app = Flask(__name__)

# Initialize Bcrypt
app.config['SECRET_KEY'] = '12345678'
bcrypt = Bcrypt(app)

conn = psycopg2.connect(database = "testdb")

# Import the application views
from app.views.user_views import GetAuthUrls
from app.views.menu_views import GetMenuUrls
from app.views.orders_views import GetOrderUrls
GetAuthUrls.fetch_urls(app)
GetMenuUrls.fetch_urls(app)
GetOrderUrls.fetch_urls(app)
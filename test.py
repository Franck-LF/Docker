from flask import Flask
import redis
import os

# Create a Flask application instance
app = Flask(__name__)

# Retrieve Redis host and port from environment variables or use default values
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = os.getenv("REDIS_PORT", 6379)

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Define a route for the home page
@app.route('/')
def welcome():
    return "Welcome to my visitor counter app!"

# Define a route for counting visits
@app.route('/count')
def count():
    # Increment the visit count in Redis
    r.incr('page_views')
    # Retrieve the current visit count from Redis
    current_count = r.get('page_views')
    print(f'Current page views: {current_count.decode("utf-8")}')
    return f'Current page views: {current_count.decode("utf-8")}'

# Run the app if this file is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
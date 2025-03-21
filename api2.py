from flask import Flask
import redis
import os

# Create a Flask application instance
app = Flask(__name__)

# Retrieve Redis host and port from environment variables or use default values
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = os.getenv("REDIS_PORT", 6379)

# Connect to the Redis database
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

# Define a route for the home page
@app.route('/')
def welcome():
    return "Welcome to my visitor counter app!"

# Define a route for counting visits
@app.route('/count')
def count():
    # Increment the visit count in Redis
    redis_client.incr('visit_count')
    # Retrieve the current visit count from Redis
    count = redis_client.get('visit_count')
    return f"Visit count: {count}"

# Run the app if this file is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
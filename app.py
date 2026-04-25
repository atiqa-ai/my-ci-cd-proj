from flask import Flask
import redis
import os

app = Flask(__name__)

# Redis server ka naam 'redis' hai (jo docker-compose mein define hoga)
# Environment variable se host lena ya default 'redis'
redis_host = os.environ.get('REDIS_HOST', 'redis')
cache = redis.Redis(host=redis_host, port=6379)

@app.route('/')
def hello():
    try:
        # Counter barhao
        count = cache.incr('hits')
        return f'Hello! Ye page {count} baar dekha gaya hai. (Database Connected)'
    except Exception as e:
        return f"Error connecting to Redis: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

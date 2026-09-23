from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

redis_host = os.environ.get("REDIS_HOST", "redis")
redis_port = int(os.environ.get("REDIS_PORT", 6379))
cache = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)


@app.route("/")
def home():
    count = cache.incr("visits")
    return jsonify({
        "message": "Hello from Flask + Redis!",
        "visits": count
    })


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

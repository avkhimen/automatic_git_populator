import redis

def make_redis_client():
    # Create a Redis client
    redis_host = 'localhost'  # Change to your Redis server's host
    redis_port = 6379         # Change to your Redis server's port
    redis_db = 0              # Change to the desired Redis database index
    redis_client = redis.Redis(host=redis_host, port=redis_port, db=redis_db)
    return redis_client
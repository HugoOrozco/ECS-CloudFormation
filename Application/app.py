import redis
from flask import (Flask, send_file, request)
from flask import render_template
import os

app = Flask(__name__)
cache = redis.Redis(host=os.environ.get('REDIS_HOST'), port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello! I have been seen {} times.\n'.format(count)

@app.route('/health', endpoint='healthCheck')
def healthCheck():
    return 'I am healthy!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
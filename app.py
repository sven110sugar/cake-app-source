from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    version = os.environ.get('APP_VERSION', 'v0.1.2')
    return f'Hello from GitOps! Version: {version}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

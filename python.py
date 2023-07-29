# python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'
@app.route('/your-custom-endpoint', methods=['GET'])
def your_custom_endpoint():
    # your custom logic goes here
    return 'Custom endpoint response'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)


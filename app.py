from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! This is my Flask web application running on EC2.'

if __name__ == '__main__':
    # Change the port number to your desired port
    port_number = 9000
    app.run(host='0.0.0.0', port=port_number)

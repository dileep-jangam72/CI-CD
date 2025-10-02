from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, People ! This is a DevOps demo app running on Kubernetes!"
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_public_ip():
    user_ip = request.remote_addr
    return f"My IP address : {user_ip}"

if __name__ == "__main__":
    app.run(debug=True)

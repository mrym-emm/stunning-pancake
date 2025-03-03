from flask import Flask

# an app is simply an object of the class Flask
app = Flask(__name__)

# everything after the domain name (github/) is the path or route
# so if someone goes to the homepage, aythign below the decorator will run
@app.route("/")
def hello_world():
    return "Hello, mrym!"
# def add_numbers():
#   return str(1+2) # can only be strings apparently


# to run website
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)
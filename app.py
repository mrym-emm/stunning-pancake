from flask import Flask, render_template

# an app is simply an object of the class Flask
app = Flask(__name__)

PLACES = [
  # making dictionary inside of list
  # to make this appear on website, pass it tru the render website
  {'id': 1,
   'name': "The Nook",
   'location': "Tamarind Square",
   'price_range': "RM10"
  },

  {'id': 2,
   'name': "Soufflé Dessert Cafe",
   'location': "Damansara Utama",
   'price_range': "RM18"
  },

  {'id': 3,
   'name': "Flufff",
   'location': "Ipoh"
  }
]


# everything after the domain name (github/) is the path or route
# so if someone goes to the homepage, aythign below the decorator will run
@app.route("/")
def hello_pancakes():
  return render_template("home.html", 
                         places = PLACES) # this will render the html file

 



# def hello_world():
#     return "Hello, mrym!"
# def add_numbers():
#   return str(1+2) # can only be strings apparently


# to run website
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)
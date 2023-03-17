from flask import Flask ,jsonify
app = Flask(__name__)

@app.route('/income/<int:n>')
def salary(n): 
      tax = 0
      cess = 0
      ttax = tax+cess
      if (n <= 250000):
          tax = 0 
          result = {
            "income tax":tax,
            "health and education cess":cess,
            "total":ttax
        }
      elif (n <= 500000):
          tax = (n - 250000)*0.05
          result = {
            "income tax":tax,
            "health and education cess":cess,
            "total":ttax
        }
      elif (n <= 750000):
          tax = (n - 500000)*0.10 + 12500
          result = {
            "income tax":tax,
            "health and education cess":cess,
            "total":ttax
        }
      elif (n <= 1000000):
          tax = (n - 750000)*0.15 + 37500 
          result = {
            "income tax":tax,
            "health and education cess":cess,
            "total":ttax
        }
      elif (n <= 1250000):
          tax = (n - 100000)*0.20 + 75000 
          result = {
            "income tax":tax,
            "health and education cess":cess,
            "total":ttax
        }
      elif (n <= 1500000):
          tax = (n - 1250000)*0.25 + 125000 
          result = {
            "income tax":tax,
            "health and education cess":cess,
            "total":ttax
        }
      else:
          tax = (n - 1250000)*0.30 + 187000 
          cess = tax*0.04
          ttax = tax+cess
          result = {
            "income tax":tax,
            "health and education cess":cess,
            "total":ttax
        }

      return jsonify(result)

if __name__ ==  "__main__":
    app.run(debug=True)
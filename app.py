# importing Flask and other modules 
from flask import Flask, request, render_template, jsonify 
from flask_cors import CORS
from flask_ngrok import run_with_ngrok

# Flask constructor 
app = Flask(__name__)  
run_with_ngrok(app)  
cors = CORS(app, allow_headers='*')
# A decorator used to tell the application 
# which URL is associated function 
@app.route('/login', methods =["GET", "POST"]) 
def gfg(): 
    if request.method == "POST": 
       # getting input with name = fname in HTML form 
       
       data = request.json
       print(data)
       data = request.form.to_dict()
       print(data)
      #  print(request.form.get("fname"))
       first_name = request.args.get("fname")
       print(first_name)
       # getting input with name = lname in HTML form  
       last_name = request.args.get("lname")
       print(last_name)
             
      #  return "Your name is "+first_name + last_name 
       
       return jsonify(data)
    return render_template("form.html") 

@app.route('/user', methods =[ "POST"]) 
def user(): 
    if request.method == "POST": 
       # getting input with name = fname in HTML form 
       d = request.data
       data = request.form.to_dict()
      #  first_name = request.form.get("fname") 
      #  # getting input with name = lname in HTML form  
      #  last_name = request.form.get("lname")  
      #  return "Your name is "+first_name + last_name 
       print(data)
       print('dasd', d)
       return jsonify({'ABC': 1, 'CVB':2}) 



# if __name__=='__main__': 
app.run() 

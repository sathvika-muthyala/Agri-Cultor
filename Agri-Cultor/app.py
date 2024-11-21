from predict import prediction
from flask import Flask, render_template, request
import sys
import time
import predict

from flask.helpers import get_flashed_messages
app = Flask(__name__)

@app.route('/',methods=['post','get'])
def load():
    return render_template('index.html')

@app.route('/products', methods=['post', 'get'])
def products():
    return render_template('shop.html')


@app.route('/predict', methods=['post', 'get'])
def predict():
    return render_template('login.html')

@app.route('/vedic', methods=['post', 'get'])
def vedic():
    return render_template('vedic.html')

@app.route('/swaps', methods=['post', 'get'])
def swaps():
    return render_template('healthyswaps.html')    

@app.route('/earthenware', methods=['post', 'get'])
def earthenware():
    return render_template('earthenware.html')    

@app.route('/ancientroutine', methods=['post', 'get'])
def ancientroutine():
    return render_template('ancientroutine.html')   
       
@app.route('/login', methods =["GET", "POST"])
def login():
    if request.method == "POST":

       # getting input with name = fname in HTML form
       Username = request.form.get("username")
       Username1 = Username
       Contact = request.form.get("contact")       
       Email = request.form.get("email")
       Gender = request.form.get("gender")
       Gender1 = Gender
       Age = request.form.get("age") 
       Age1 = Age
       Height = request.form.get("height")
       Height1 = Height
       Weight = request.form.get("weight")
       Weight1 = Weight
       Disease = request.form.get("disease")
       Disease1 = Disease
       Bp = request.form.get("bp")
       Bp1=Bp
       Diet = request.form.get("diet")
       Diet1 = Diet
      

       if Gender1 == '1':
           Gender1 = 'Male'
       else:
           Gender1 = 'Female'
    
       if Age1 == '1':
           Age1 = '< 20'
       elif Age1 == '2':
           Age1 = '21 - 40'
       elif Age1 == '3':
           Age1 = '41 - 60'
       elif Age1 == '4':
           Age1 = '61 - 80'
       else:
           Age1 = '> 80'
        
       if Height1 == '1':
           Height1 = "4'1 - 4'12"
       elif Height1 == '2':
           Height1 = "5'1 - 5'6"
       elif Height1 == '3':
           Height1 = "5'7 - 5'12"
       else:
           Height1 = "> 6'0"
    
       if Weight1 == '1':
           Weight1 = '< 55 kg'
       elif Weight1 == '2':
           Weight1 = '56 - 80 kg'
       elif Weight1 == '3':
           Weight1 = '81 - 100 kg'
       else:
           Weight1 = '> 100 kg'
        
       if Disease1 == '1':
           Disease1 = 'Diabetes'
       elif Disease1 == '2':
           Disease1 = 'Kidney Issue'
       elif Disease1 == '3':
           Disease1 = 'Heart Disease'
       elif Disease1 == '4':
           Disease1 = 'Liver Issue'
       elif Disease1 == '5':
           Disease1 = 'Joint Pains'
       elif Disease1 == '6':
           Disease1 = 'Thyroid'     
       else:
           Disease1 = 'No history of disease'
        
       if Bp1 == '1':
           Bp1 = 'Low'
       elif Bp1 == '2':
           Bp1 = 'Moderate'
       elif Bp1== '3':
            Bp1 = 'High'
       else:
           Disease1 = 'No BP Selected'
         
       if Diet1 == '1':
           Diet1 = 'Building'
       elif Diet1 == '2':
           Diet1 = 'Lifestyle'
       elif Diet1 == '3':
           Diet1 = 'Healing'
       elif Diet1 == '4':
           Diet1 = 'Happy Disease'            
       else:
            Diet1 = 'No Diet Plan Selected'
      

       lis = []
       lis.append(Gender)
       lis.append(Age)
       lis.append(Height)
       lis.append(Weight) 
       lis.append(Disease)
       lis.append(Bp)
       lis.append(Diet)
       str = prediction(lis)

       return render_template("response.html",mess=str,name=Username1,gender=Gender1,age=Age1,height=Height1,weight=Weight1,disease=Disease1,bp=Bp1,diet=Diet1)
    else:
        return render_template("questions.html")

@app.route('/article1', methods =["GET","POST"])
def article1():
    return render_template("blog-detail1.html")

@app.route('/article2', methods =["GET","POST"])
def article2():
    return render_template("blog-detail2.html")

@app.route('/article3', methods =["GET","POST"])
def article3():
    return render_template("blog-detail3.html")

@app.route('/article4', methods =["GET","POST"])
def article4():
    return render_template("blog-detail4.html")


if __name__ == '__main__':
    app.run(debug=True)
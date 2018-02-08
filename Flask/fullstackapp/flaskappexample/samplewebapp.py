from flask import Flask
from flask import render_template
from flask import flash
from flask import request
from flask import redirect
from flask import url_for
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
#This import is required for the wtf import in showmap.html to work
from flask_bootstrap import Bootstrap
import urllib3
from bs4 import BeautifulSoup
import json

#flask instance stored in app
app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = 'myflaskapp'
bootstrap = Bootstrap(app)
#request hooks and g contexts to store data common for all view functions
#template contains the text of a response with the variables whose values will be known in the request
#deorator for the main page
#view functions
@app.route("/")
def indexing():
    #This is a GET REQUEST to changedatainjs

    #A GET request with render_tempate
    #here by just returning it is the response object that is returned
    print("root")
    return('<h1>hello world</h1>')

    #returns from back end to front end
    #return "just started"

#Route decorator
#pass param in url that is picke up from client side and gets <addr> value in the backend
@app.route('/address/<addr>')
def showaddress(addr):
    return('<h1>The address is {} </h1>'.format(addr))

#now you want a template generating this response since you do not want to add html code here
#adding request with actual values and getting the final response string is called rendering

#from client request picking it up and showing it again on another client
#the variable in the app route, shoild be the same as the parameter passed here and same as the return address

@app.route('/addresstemplate/<address>')
def showaddressthroughtemplate(address):
    print(address)
    #return address

    #YOU HAve tp pass address to the new url
    #the left same as in the html and the right same as in the addr - param in url

    return render_template('changedatainjs.html', addressatcg=address)

#now pass data through submit

class SubmitAddressForm(Form):
    address = StringField('Enter current address', validators=[DataRequired()])
    submitButton =  SubmitField('Submit')


@app.route('/showmap', methods=['GET', 'POST'])
def showmap():
    address = None
    print("show map func")
    form = SubmitAddressForm()
    finList = []
    if request.method == 'POST':
        address = form.address.data
        print("addr on the server side=  " + address)
        form.address.data = ''
        flash('your address is  ' + address)

        GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json?'
        addP = "address=" + address.replace(" ", "+", -1)
        apikey = 'AIzaSyCI2tEqnQfGLFEEsvO4xjOppywbXtYdutw'
        GeoUrl = GOOGLE_MAPS_API_URL + addP + "&key=" + apikey
        print("inside POST")
        http = urllib3.PoolManager()

        response = http.request('GET', GeoUrl)
        print("Received response")
        jsonRaw = response.data.decode('utf-8')
        print(jsonRaw)

        jsonData = json.loads(jsonRaw)
        print(jsonData)

        if jsonData['status'] == 'OK':
            results = jsonData['results'][0]
            finList = [results['formatted_address'], results['geometry']['location']['lat'], results['geometry']['location']['lng']]
            print(finList)

    return render_template('showmap.html', form=form, address=finList)


#you just sent data to javascript
#decorator for another page
#@app.route("/showmap/<name>")
#def showmapofcountry(name):
#    print("should show showmap.html")
#    return name

#POST is required to post from here to showmap.html
#@app.route("/showmap",methods= ['GET', 'POST'])
#def showmapcountry():
#    print("should show showmap.html")
#    return render_template('showmap.html')


#not working
#@app.route("/changeinjs2", methods= ['POST'])
#def changedatainjs2():
#           jsdata = request.form
           #can also call render_template to call another html and pass a parameter
           #return  jsdata
#           return render_template("postdatafromserverthroughget.html", value=jsdata)

#@app.route("/getlocation", methods=['GET', 'POST'])
#def getaddressofuser():
#    if(request.method == 'POST'):
#        print("came back to get location from javascript")
#        jslocdata = request.form['data']
#        print(jslocdata)
        #render - to redirect
#        return redirect(url_for('showmapcountry'))
        #this page getlocation is posting data to another page showmap.html
        #return render_template('showmap.html', countryname=jslocdata)
 #   else:
 #       print("getlocation form being displayed")
 #       return render_template("acceptaddress.html")


#@app.route("/changedatainjs")
#def changedatainjs():
    #the string used in the url before = sign
    #address = request.args.get('address')
    #print(address)
 #   print("am in change data in js view function")
   # address = "Curiositygym,Fort"
    #passing data from back end to front end using a query string

    #directly render html

  #  return #'''<h1> the address is {}</h1>'''.format(address)




if __name__ == "__main__":
    app.run()

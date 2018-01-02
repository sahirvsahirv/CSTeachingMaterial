from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

#flask instance stored in app
app = Flask(__name__)

#deorator for the main page
@app.route("/")
def hello():
    return render_template("changedatainjs.html")

#you just sent data to javascript
#decorator for another page
@app.route("/showmap/<countryname>")
def showmapofcountry(countryname):
    print("should show showmap.html")
    return render_template('showmap.html', name = countryname)

#POST is required to post from here to showmap.html
@app.route("/showmap",methods= ['GET', 'POST'])
def showmapcountry():
    print("should show showmap.html")
    return render_template('showmap.html')

@app.route("/changedatainjs/<jsdata>")
def changedataandsenditbacktopython(jsdata):
    print("in changedataandsenditbacktopython")
    return jsdata
#not working
@app.route("/changeinjs2", methods= ['POST'])
def changedatainjs():
           jsdata = request.form
           #can also call render_template to call another html and pass a parameter
           #return  jsdata
           return render_template("postdatafromserverthroughget.html", value=jsdata)

@app.route("/getlocation", methods=['GET', 'POST'])
def getaddressofuser():
    if(request.method == 'POST'):
        print("came back to get location from javascript")
        jslocdata = request.form['data']
        print(jslocdata)
        #render - to redirect
        return redirect(url_for('showmapcountry'))
        #this page getlocation is posting data to another page showmap.html
        #return render_template('showmap.html', countryname=jslocdata)
    else:
        print("getlocation form being displayed")
        return render_template("acceptaddress.html")
                
if __name__ == "__main__":
    app.run()

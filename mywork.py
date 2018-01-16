from flask import Flask, render_template, request
from wtforms import Form, StringField, validators

import Processing

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/uobrewardtrending')
def uobrewardtrending():
    return render_template('uobrewardtrending.html')

@app.route('/uobrewardtrendingpt')
def uobrewardtrendingpt():
    return render_template('uobrewardtrendingpt.html')

@app.route('/uobrewardall')
def uobrewardall():
    return render_template('uobrewardall.html')

@app.route('/uobrewardallpt')
def uobrewardallpt():
    return render_template('uobrewardallpt.html')

@app.route('/uobrewardretail')
def uobrewardretail():
    return render_template('uobrewardretail.html')

@app.route('/uobrewardretailpt')
def uobrewardretailpt():
    return render_template('uobrewardretailpt.html')

@app.route('/uobrewarddining')
def uobrewarddining():
    return render_template('uobrewarddining.html')

@app.route('/uobrewarddiningpt')
def uobrewarddiningpt():
    return render_template('uobrewarddiningpt.html')

@app.route('/uobrewardleisure')
def uobrewardleisure():
    return render_template('uobrewardleisure.html')

@app.route('/uobrewardleisurept')
def uobrewardleisurept():
    return render_template('uobrewardleisurept.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/alldecredemption')
def alldecredemption():
    return render_template('alldecredemption.html')

@app.route('/uobdecredemption')
def uobdecredemption():
    return render_template('uobdecredemption.html')

@app.route('/ocbcdecredemption')
def ocbcdecredemption():
    return render_template('ocbcdecredemption.html')

@app.route('/dbsdecredemption')
def dbsdecredemption():
    return render_template('dbsdecredemption.html')

@app.route('/allnovredemption')
def allnovredemption():
    return render_template('allnovredemption.html')

@app.route('/uobnovredemption')
def uobnovredemption():
    return render_template('uobnovredemption.html')

@app.route('/ocbcnovredemption')
def ocbcnovredemption():
    return render_template('ocbcnovredemption.html')

@app.route('/dbsnovredemption')
def dbsnovredemption():
    return render_template('dbsnovredemption.html')

@app.route('/allredemption')
def allredemption():
    allredemptionList = []
    allredemptionList = Processing.processallredemption()
    return render_template('allredemption.html', allredemptions=allredemptionList)

@app.route('/alluobredemption')
def alluobredemption():
    return render_template('alluobredemption.html')

@app.route('/allocbcredemption')
def allocbcredemption():
    return render_template('allocbcredemption.html')

@app.route('/alldbsredemption')
def alldbsredemption():
    return render_template('alldbsredemption.html')

@app.route('/updateuobrewardretail')
def updateuobrewardretail():
    return render_template('updateuobrewardretail.html')

@app.route('/updateuobrewarddining')
def updateuobrewarddining():
    return render_template('updateuobrewarddining.html')

@app.route('/updatepart2uobdining')
def updatepart2uobdining():
    return render_template('updatepart2uobdining.html')

@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/trying')
def trying():
    uob_currentpts = Processing.processpoints()
    uob_allitems = Processing.processallitems
    uob_retialitems = Processing.processretailitems()
    uob_diningitems = Processing.processdiningitems()
    uob_leisureitems = Processing.processleisureitems()
    return render_template('trying.html', uobcurrentpts=uob_currentpts, uoballitems = uob_allitems,uobretialitems=uob_retialitems, uob_diningitems=uob_diningitems, uobleisureitems=uob_leisureitems)

if __name__ == '__main__':
    app.run()



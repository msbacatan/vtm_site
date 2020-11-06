from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/estimate')
def estimate():
    return render_template('estimate.html')

class Tank:
    def __init__(self, radius, height):
        self.tankRadius = radius
        self.tankHeight = height
        self.piCalc = 3.14
        self.materialCost = 25
        self.laborCost = 15
        self.topArea = piCalc * (tankRadius)**2
        self.sideArea = (piCalc * (tankRadius * tankHeight))
        self.totalArea = 0
        self.totalMaterialCost = 0
        self.totalLaborCost = 0
        self.totalCost = 0

    def totalArea(self):
        return self.totalArea

    def calcTotalArea(self):
        self.totalArea = (self.topArea + self.sideArea)/144 #convert from sq in to sq ft

    def totalMaterialCost(self):
        return self.totalMaterialCost

    def calcMaterialCost(self):
        self.totalMaterialCost = (self.totalArea * self.materialCost)

    def totalLaborCost(self):
        return self.totalLaborCost

    def calcLaborCost(self):
        self.totalLaborCost = (self.totalArea * self.laborCost)

    def calculateTotalCost(self):
        self.calcTotalArea()
        self.calcLaborCost()
        self.calcMaterialCost()
        self.totalCost = self.calcLaborCost() + self.calcMaterialCost()

    def getTotalEstimate(self):
        return self.totalCost

@app.route('/totalEstimate', methods=['POST'])
def totalEstimate():
    if request.method == 'POST':
        form = request.form
        radius = float(form['tankRadius'])
        height = float(form['tankHeight']) 

        tank = Tank(radius, height)

        tank.calculateTotalCost()

        totalCost = tank.getTotalEstimate()
        totalCost = ("The estimated total cost for this tank is ${0:,.2f}").format(totalCost)

        print(totalCost)

        return render_template('estimate.html', totalEstimate = totalCost)

    return render_template('estimate.html')

if __name__ == '__main__':
    app.run(debug=True)

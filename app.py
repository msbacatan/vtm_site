from flask import Flask
from flask import render_template

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
    def __init__(self, tankRadius, tankHeight):
    self.tankRadius = tankRadius
    self.tankHeight = tankHeight

@app.route('/totalEstimate', methods=['POST'])
def totalEstimate():
    if request.method == 'POST':
        form = request.form
        radius = float(form['tankRadius'])
        height = float(form['tankHeight']) 

        print(radius)
        print(height)

        PI = 3.14
        MATERIALCOST = 25
        LABORCOST = 15
        
        topArea = PI * radius**2
        sideArea = (2 * (PI * (radius * height)))
        totalAreaSqFt = (topArea + sideArea)/144 #convert from square inches to square feet
        # print(topArea)
        # print(sideArea)
        # print(totalAreaSqFt)
        
        totalMaterialCost = totalAreaSqFt * MATERIALCOST
        totalLaborCost = totalAreaSqFt * LABORCOST
        # print(totalMaterialCost)
        # print(totalLaborCost)

        totalCost = totalMaterialCost + totalLaborCost
        totalEstimate = totalCost
        print(totalEstimate)

        return render_template('estimate.html', totalEstimate = totalCost)

    return render_template('estimate.html')

if __name__ == '__main__':
    app.run(debug=True)

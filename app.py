from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle="About VTM")

@app.route('/estimate', methods=['POST'])
def estimate():
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

        totalEstimate = totalMaterialCost + totalLaborCost
        print(totalEstimate)
    return render_template('estimate.html', pageTitle="VTM Cost Estimator")

if __name__ == '__main__':
    app.run(debug=True)

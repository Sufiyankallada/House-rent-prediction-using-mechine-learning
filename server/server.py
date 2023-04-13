from flask import Flask,request,jsonify
import util
app = Flask(__name__)

@app.route('/get_furnishing_method')
def get_furnishing_method():
    response = jsonify({
        "furnishing":util.get_furnishing_method()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/predict_rent_amount', methods=['POST'])
def predict_rent_amount():
    bathroom = int(request.form['bathroom'])
    area=float(request.form['area'])
    floor_number = int(request.form['floor_number'])
    parking = int(request.form['parking'])

    power_backup = int(request.form['power_backup'])
    #deposite = int(request.form['deposite'])
    total_rooms = int(request.form['total_rooms'])
    furnishing = request.form['furnishing']
    available_for = request.form['available_for']
    property_age = request.form['property_age']
    wheelchairavailability = request.form['wheelchairavailability']
    pets_allowed = request.form['pets_allowed']
    floor_type = request.form['floor_type']
    place = request.form['place']



    response = jsonify({
        'estimated_price': util.get_estimated_price(bathroom,area,floor_number,parking,power_backup,total_rooms,furnishing,available_for,property_age,wheelchairavailability,pets_allowed,floor_type,place)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ =="__main__":
    print("starting flask from miniproject")
    util.load_saved_artifacts()
    print(util.get_estimated_price(
        3, 1500, 3, 1, 1, 4, "furnished", "family only", "1 to 5 year old", "wheelchairavailable",
        "petavailable", "marble","b"
        ))
    app.run()
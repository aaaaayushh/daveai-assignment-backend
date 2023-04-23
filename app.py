from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import flask
import flask_sqlalchemy
import flask_cors
print(flask.__version__)
print(flask_sqlalchemy.__version__)
print(flask_cors.__version__)
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ungcchve:1nuOTJufZacnUr1zDwZh442v7zcySpzy@lallah.db.elephantsql.com/ungcchve'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Float, nullable=False)
    age = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    waist = db.Column(db.Float, nullable=False)


@app.route('/measurements', methods=['GET'])
def get_measurements():
    print(request)
    height = request.args.get('height')
    age = request.args.get('age')
    weight = request.args.get('weight')
    measurements = Data.query.filter(
        Data.height >= float(height) - 5,
        Data.height <= float(height) + 5,
        Data.age >= float(age) - 2,
        Data.age <= float(age) + 2,
        Data.weight >= float(weight) - 5,
        Data.weight <= float(weight) + 5
    )

    waist_measurements = [measurement.waist for measurement in measurements]
    result = list(set(waist_measurements))
    print(len(result))
    return jsonify({'waist_measurements': result})

@app.route('/measurements', methods=['POST'])
def add_measurement():
    height = request.json['height']
    age = request.json['age']
    weight = request.json['weight']
    waist = request.json['waist']
    measurement = Data(height=height, age=age, weight=weight, waist=waist)
    db.session.add(measurement)
    db.session.commit()
    return jsonify({'message': 'Measurement added successfully'})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from surprise.dump import load
import os
import numpy as np

app = Flask(__name__)

Model = load('RecommendationModel.pkl')[1]


@app.route("/", methods = ['GET'])
def Welcome_Message():
    return 'Welcome to my first REST API', 200

@app.route("/predict", methods = ['POST'])
def flask_predict():
    print(request.headers)
    if request.is_json: #Verify data is in json format
        data = request.get_json()
        print(data)
        user_id = str(data['user_id'])
        item_id = str(data['item_id'])
        
        prediction = Model.predict(user_id, item_id)
        
        return jsonify(prediction), 201
    return {"error": "Request must be JSON"}, 415
    
if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = int(os.environ.get("PORT", 5000)))
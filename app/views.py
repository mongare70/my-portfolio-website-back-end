from app import app, mail
from flask import json, request, jsonify
from flask_cors import cross_origin
from flask_mail import Message

# API test route
@app.route("/api", methods=["GET", "POST"])
@cross_origin()
def apiTest():
    return "<h1>Test Success</h1>"
    

#Send Mail route
@app.route("/api/sendEmail", methods=["GET", "POST"])
@cross_origin()
def sendEmail():
    request_data = json.loads(request.data)

    msg = Message('Hire Me from Portfolio', recipients=["hillarymongare70@gmail.com"], sender=request_data["email"])
    msg.body=f""" The sent message is:

    {request_data["message"]}

    From: {request_data["name"]} : {request_data["email"]}
    
    """
    try:
        mail.send(msg)
        return jsonify({"sent": True})
    except:
        return jsonify({"sent": False})
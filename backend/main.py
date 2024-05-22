from flask import request, jsonify
from config import app, db
from models import Contact


@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify({"contacts": [contact.to_json() for contact in contacts]}),200

@app.route("/create_contacts", methods=["POST"])
def create_contact():
    try:
        first_name=request.json["firstName"]
        last_name=request.json["lastName"]
        email=request.json["email"]

        if not first_name or not last_name or not email:
            return jsonify({"message": "All fields are required"}), 400

        new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
        
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({"message": "Contact created successfully"}), 201

    except Exception as e:
        return jsonify({"message": str(e)}), 400
    



@app.route("/update_contact/<int:id>", methods=["PUT"])
def update_contact(id):
    contact = Contact.query.get(id)
    if not contact:
        return jsonify({"message": "Contact not found"}), 404

    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if first_name:
        contact.first_name = first_name
    if last_name:
        contact.last_name = last_name
    if email:
        contact.email = email

    try:
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "Contact updated successfully"}), 200


@app.route("/delete_contact/<int:id>", methods=["DELETE"])
def delete_contact(id):
    contact = Contact.query.get(id)
    if not contact:
        return jsonify({"message": "Contact not found"}), 404

    try:
        db.session.delete(contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "Contact deleted successfully"}), 200

    

if __name__=="__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
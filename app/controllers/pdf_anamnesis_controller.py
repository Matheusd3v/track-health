from flask import jsonify, render_template, make_response
import pdfkit
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.pdf_anamnesis_services import get_anamnesis

@jwt_required()
def create_pdf():
    user = get_jwt_identity()
    anamnesis = get_anamnesis(user["id"])

    rendered = render_template("anamnesis.html", anamnesis=anamnesis, name=user["name"], )
    pdf = pdfkit.from_string(rendered, False)

    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = f"attachment; filename=DKJSAKJD.pdf"



    print(anamnesis)
    return response
    # return jsonify(anamnesis)
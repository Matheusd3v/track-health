from flask import render_template, make_response
import pdfkit
from flask_jwt_extended import jwt_required

@jwt_required()
def create_pdf(name):

    rendered = render_template("anamnesis.html", name="guga")
    pdf = pdfkit.from_string(rendered, False)

    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = f"attachment; filename={name}.pdf"




    return response
    # return render_template("anamnesis.html")
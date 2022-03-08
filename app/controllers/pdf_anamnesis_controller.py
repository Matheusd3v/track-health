from http import HTTPStatus
from flask import jsonify, render_template, make_response
import pdfkit
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user_model import User
import os, sys, subprocess, platform
from app.services.pdf_anamnesis_services import get_anamnesis
from app.services.user_services import serializing_all_fields

@jwt_required()
def create_pdf():

    def _get_pdfkit_config():
     if platform.system() == 'Windows':
         return pdfkit.configuration(wkhtmltopdf=os.environ.get('WKHTMLTOPDF_BINARY', 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'))
     else:
         WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf')], stdout=subprocess.PIPE).communicate()[0].strip()
         return pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)

    config = _get_pdfkit_config()
    
    try:    
        user = get_jwt_identity()
        user = User.query.filter_by(id = user["id"]).first()
        user = serializing_all_fields(user.asdict()) 

        anamnesis = get_anamnesis(user["id"])

        rendered = render_template("anamnesis.html", anamnesis=anamnesis, name=user["name"], user=user)
        pdf = pdfkit.from_string(rendered, False, configuration=config)


        response = make_response(pdf)
        response.headers["Content-Type"] = "application/pdf"
        response.headers["Content-Disposition"] = f"attachment; filename=DKJSAKJD.pdf"



        return response

    except IndexError:
        return {"msg":"The user doenst have an anamnesis"}, HTTPStatus.NOT_FOUND
from flask import Blueprint

from app.controllers.pdf_anamnesis_controller import create_pdf

bp = Blueprint("bp_pdf_anamnesis", __name__, url_prefix="/pdf")

bp.get("/")(create_pdf)
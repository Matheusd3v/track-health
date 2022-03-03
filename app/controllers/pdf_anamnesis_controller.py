from flask import render_template, make_response
import pdfkit


def create_pdf():

    rendered = render_template("anamnesis.html")
    pdf = pdfkit.from_string(rendered, False)

    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "attachment; filename=aoba.pdf"




    return response
    # return render_template("anamnesis.html")
from flask import Blueprint
from app.controllers import address_controler

bp_address = Blueprint("bp_address", __name__, url_prefix="/address")

bp_address.post('')(address_controler.create_address)
bp_address.get('')(address_controler.get_address)
bp_address.patch('')(address_controler.patch_address)
bp_address.delete('')(address_controler.delete_address)
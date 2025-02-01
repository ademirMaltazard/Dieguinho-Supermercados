from flask import Blueprint, jsonify
from repositories.person_repository import PersonRepository

home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET'])
def get_person():
    return jsonify({
        'its working?' : 'True'
    })
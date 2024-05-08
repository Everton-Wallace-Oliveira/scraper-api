from flask import Blueprint
from controller.scraper_controller import get_google_info

google_routes = Blueprint('google_routes', __name__)

@google_routes.route('/api/google-info', methods=['GET'])
def get_info():
    return get_google_info()


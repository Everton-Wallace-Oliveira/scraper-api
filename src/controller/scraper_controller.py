from flask import request, jsonify
from services.scraper_service import ScraperService
from exceptions.custom_exceptions import NotFoundError

scraper_service = ScraperService()

def get_google_info():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400
    
    try:
        results = scraper_service.get_google_info(query)
        return jsonify(results)
    except NotFoundError as e:
        return jsonify({'error': str(e)}), 404
from flask import Flask
from routes.scraper_routes import google_routes

app = Flask(__name__)
app.register_blueprint(google_routes)

if __name__ == '__main__':
    app.run(debug=True, port=8080)

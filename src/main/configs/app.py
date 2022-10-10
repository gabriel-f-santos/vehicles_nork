from flask import Flask
from src.infra.config import DBConnectionHandler, Base
from flask_cors import CORS
from src.main.routes import api_routes_bp

app = Flask(__name__)
CORS(app)
db_conn = DBConnectionHandler()
engine = db_conn.get_engine()
Base.metadata.create_all(engine)

app.register_blueprint(api_routes_bp)

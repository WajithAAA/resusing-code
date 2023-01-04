from app.main import main
from config import Config

@main.route("/")
def home():
    return "test data"

@main.route("/test")
def test_data():
    return "test data"

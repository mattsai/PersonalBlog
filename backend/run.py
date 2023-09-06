import os

from flask_cors import CORS
from app import create_app

app = create_app()
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get("BLOG_PORT"))

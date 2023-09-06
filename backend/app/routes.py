from flask import Blueprint, render_template


bp_routes = Blueprint('routes', __name__)


@bp_routes.route('/',methods=('GET',))
def index():
    return "Yes WOrking2"

from db_connect import db

from flask import (Blueprint, Flask, abort, g, jsonify, make_response,
                   redirect, render_template, request, session, url_for)

newspage = Blueprint('newspage', __name__)
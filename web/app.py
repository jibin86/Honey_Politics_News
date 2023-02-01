# from db_connect import db

from flask import (Blueprint, Flask, abort, g, jsonify, make_response,
                   redirect, render_template, request, session, url_for)

app = Flask(__name__)

# newspage_api와 연결
from newspage_api import newspage
app.register_blueprint(newspage)

# # DB config
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@127.0.0.1:3306/honey_news'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db.init_app(app)


@app.route('/')
def home():
    # portal 페이지가 메인 페이지
    return render_template('portal.html')


if __name__ == '__main__':
    app.run(debug=True)

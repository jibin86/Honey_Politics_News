# from db_connect import db

from flask import (Blueprint, Flask, abort, g, jsonify, make_response,
                   redirect, render_template, request, session, url_for)
import pandas as pd
import database

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
    newslist0 = database.newslist0[:9]
    newslist1 = database.newslist1[:9]
    newslist2 = database.newslist2[:9]
    newslist3 = database.newslist3[:9]
    newslist4 = database.newslist4[:9]
    
    return render_template('portal.html', newslist0=newslist0, newslist1=newslist1, newslist2=newslist2, newslist3=newslist3, newslist4=newslist4)


if __name__ == '__main__':
    app.run(debug=True)

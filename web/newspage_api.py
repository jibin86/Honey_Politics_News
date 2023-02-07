from flask import (Blueprint, Flask, abort, g, jsonify, make_response,
                   redirect, render_template, request, session, url_for)
import database
from portal_recommend import portal_recommend

newspage = Blueprint('newspage', __name__)

@newspage.route('/news/<int:number>/')
def news(number):
    news = database.df.iloc[number].tolist()
    rec_news_list = portal_recommend.get_rec_index(number)
    return render_template('news.html', news=news, rec_news_list=rec_news_list)
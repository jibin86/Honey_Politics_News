from flask import (Blueprint, Flask, abort, g, jsonify, make_response,
                   redirect, render_template, request, session, url_for)
import database

newspage = Blueprint('newspage', __name__)

@newspage.route('/news/<int:number>/')
def news(number):
    news = database.df.iloc[number].tolist()
    return render_template('news.html', news=news)
import json

from flask import Flask, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from hashids import Hashids

# instantiate the app
app = Flask(__name__)
CORS(app)
app.config.from_object('config.DevelopmentConfig')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from models import *


# sanity check route
@app.route('/', methods=['POST'])
def add_url():
    response_object = {'status': 'success'}
    original_url = json.loads(request.data)['originalUrl']
    try:
        link = ShortUrl.query.filter_by(original_url=original_url).first()
        if link is None:
            short_url_ = ShortUrl(original_url=original_url)
            db.session.add(short_url_)
            db.session.commit()
            hashids = Hashids(min_length=4, salt=os.environ.get('SECRET_KEY'))
            short_url = hashids.encode(short_url_.id)
            short_url_.short_url = short_url
            db.session.commit()
        else:
            short_url = link.short_url
        response_object['short_url'] = request.host_url + short_url
        return jsonify(response_object)
    except Exception as e:
        return str(e)


@app.route('/<short_url>')
def redirect_url(short_url):
    original_url = ShortUrl.query.filter_by(short_url=short_url).first_or_404()
    return redirect(original_url.original_url, 302)


@app.errorhandler(404)
def page_not_found(e):
    return 'Oops, I cant reach this link', 404


if __name__ == '__main__':
    app.run()

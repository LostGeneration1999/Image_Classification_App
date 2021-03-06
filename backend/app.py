# render_template：参照するテンプレートを指定
# jsonify：json出力
from flask import Flask, render_template, jsonify, request, make_response

# CORS：Ajax通信するためのライブラリ
# from flask_cors import CORS
from flask_restful import Api, Resource
#as been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.
from flask_cors import CORS 
from random import *
from PIL import Image
from pathlib import Path
from io import BytesIO
import base64
import os

# static_folder：vueでビルドした静的ファイルのパスを指定
# template_folder：vueでビルドしたindex.htmlのパスを指定
app = Flask(__name__, static_folder = "./../frontend/dist/static", template_folder="./../frontend/dist")
#http://tarhashi.hatenablog.com/entry/2017/05/21/143253
app.config['JSON_AS_ASCII'] = False
#CORS=Ajaxで安全に通信するための規約
api = Api(app)
CORS(app)

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 任意のリクエストを受け取った時、index.htmlを参照
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")

class Spam(Resource):
    def get(self):
        return { 'id': 18,
                'name' : 'Daisuke Miura', 
                'team' : 'Yokohama Baystars', 
                'song' : 'ゴーゴーレッツゴー　跳ねろマウンド三振奪取　決まってるぜ　リーゼント　勝利だ三浦'}
api.add_resource(Spam, '/api/spam')

@app.route('/classification', methods=['POST'])
def uploadImage():
    if request.method == 'POST':
        base64_png =  request.form['image']
        code = base64.b64decode(base64_png.split(',')[1]) 
        image_decoded = Image.open(BytesIO(code))
        image_decoded.save(Path(app.config['UPLOAD_FOLDER']) / 'image.png')
        return make_response(jsonify({'result': 'success'}))
    else: 
        return make_response(jsonify({'result': 'invalid method'}), 400)

# app.run(host, port)：hostとportを指定してflaskサーバを起動
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
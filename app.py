from flask import Flask, request, jsonify
import requests
import yaml
from lib.decision_engine import DecisionEngine

app = Flask(__name__)
CONFIG_PATH = './config/db.yaml'
CONFIG = yaml.load(open(CONFIG_PATH))
CONFIG_DATA = yaml.load(open(CONFIG['config_path']))


@app.route('/')
def get():
    return jsonify({"app": "Decision engine",
                    "version": "1.0",
                    "env": CONFIG_DATA['env']})


@app.route('/recommended/<product>/<userid>')
def top_ten(product, userid):
    url = CONFIG_DATA['url']
    dc = DecisionEngine(app=app, config=CONFIG_DATA[CONFIG_DATA['env']])
    recommended_articles=requests.get(url.format(userid=userid, product=product)).json()
    recommended_articles['rules'] = dc.get_rules()
    return jsonify(recommended_articles)


@app.route('/decision-engine/slot/update/<int:slot_no>')
def update_slot(slot_no):
    article = request.args.get('articles')
    cross_products = request.args.get('cross_products')
    ad = request.args.get('ad')
    insert = request.args.get('insert')
    if not insert:
        insert = 0
    else:
        insert = 1
    dc = DecisionEngine(app=app, config=CONFIG_DATA[CONFIG_DATA['env']])
    data = dc.update_rule(slot_no, article, cross_products, ad, insert=insert)
    return jsonify({'status': data})


@app.route('/decision-engine/slot/list/')
def get_slot():
    dc = DecisionEngine(app=app, config=CONFIG_DATA[CONFIG_DATA['env']])
    data = dc.get_rules()
    return jsonify({'slots_list': data})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

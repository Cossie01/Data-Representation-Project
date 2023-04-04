from flask import Flask, jsonify


app = Flask(__name__, static_url_path='', static_folder='static')

teas = [
    {'name':'Barrys'},
    {'name':'Lyons'},
    {'name':'PJ Tips'},
    ]

@app.route('/tea', methods = ['GET'])
def getAllTeas():
    return jsonify(teas)

@app.route('/vote/<teaname>', methods = ['POST'])
def voteforTeas(teaname):
    return jsonify({'name':teaname})

@app.route('/vote/<teaname>', methods = ['GET'])
def getCountForTeas(teaname):
    return '9999'

@app.route('/vote', methods = ['GET'])
def getAllCountForTeas():
    return jsonify({'name':'test','count':9999})

@app.route('/vote/all', methods = ['DELETE'])
def deleteAllVotes():
    return jsonify({'done':True})

if __name__ == "__main__":
    app.run(debug=True)
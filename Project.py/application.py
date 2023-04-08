from flask import Flask, jsonify, abort, request
from voteDAO import voteDAO

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
    ip_address = request.remote_addr
    data = (teaname, ip_address)
    newid= voteDAO.create(data)
    
    return jsonify({'id':newid})

@app.route('/vote/<teaname>', methods = ['GET'])
def getCountForTeas(teaname):
    count =voteDAO.countvotes(teaname)
    return jsonify({teaname:count})

@app.route('/vote', methods = ['GET'])
def getAllCountForTeas():
    allcounts =[]
    for tea in teas:
        teaname=teas['name']
        count = voteDAO.countvotes(teaname)
        allcounts.append({teaname:count})
    return jsonify(allcounts)

@app.route('/vote/all', methods = ['DELETE'])
def deleteAllVotes():
    return jsonify({'done':True})

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify, abort, request, render_template
from voteDAO import voteDAO
import requests
from flask_limiter import Limiter

app = Flask(__name__, static_url_path='', static_folder='static')

#Limiter
def get_remote_address():
    return request.remote_addr

limiter = Limiter(app)
limiter.key_func = get_remote_address

teas = [
    {'name':'Barrys'},
    {'name':'Lyons'},
    {'name':'PG Tips'},
    {'name':'Tetleys'},
    ]
#External Api
@app.route('/external-teas', methods=['GET'])
def getExternalTeas():
    try:
        api_url = 'https://boonakitea.cyclic.app/api/teas'
        response = requests.get(api_url)
        response.raise_for_status()  
        teas = response.json()
        for tea in teas:
            print(teas)
        return render_template('externalApi.html', teas=teas)
    except requests.exceptions.RequestException as e:
        abort(500, f"An error occurred while retrieving teas from the external API: {e}")

#Internal Api
@app.route('/tea', methods = ['GET'])
@limiter.limit("10/minute")
def getAllTeas():
    return jsonify(teas)

@app.route('/vote/<teaname>', methods = ['POST'])
@limiter.limit("1/minute")
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
        teaname=tea['name']
        count = voteDAO.countvotes(teaname)
        allcounts.append({teaname:count})
    return jsonify(allcounts)

@app.route('/vote/all', methods = ['DELETE'])
def deleteAllVotes():
    return jsonify({'done':True})

@app.route('/tea/<teaname>', methods = ['PUT']) 
def updateTea(teaname):
    new_tea_name = request.json.get('new_tea_name')

    for tea in teas:
        if tea['name'] == teaname:
            # Update the name
            tea['name'] = new_tea_name
            return jsonify(tea)
    
    abort(404, f"Tea with name {teaname} not found")


if __name__ == "__main__":
    app.run(debug=True)
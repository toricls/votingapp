import os

from flask import Flask
from flask_cors import CORS, cross_origin
from random import randrange
import simplejson as json
import boto3
from multiprocessing import Pool
from multiprocessing import cpu_count

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"Access-Control-Allow-Origin": "*"}})

ddb = boto3.resource('dynamodb', region_name="us-west-2")
ddbtable = ddb.Table('restaurants')

cpustress = os.getenv('CPUSTRESS', 0)
memstress = os.getenv('MEMSTRESS', 0)
cpustressfactor = os.getenv('CPUSTRESSFACTOR', 1)
memstressfactor = os.getenv('MEMSTRESSFACTOR', 1)

print("The cpustress variable is set to: " + str(cpustress))
print("The memstress variable is set to: " + str(memstress))
memeater=[]
memeater = [0 for i in range(10000)] 

## https://gist.github.com/tott/3895832
def f(x):
    for x in range(1000000 * cpustressfactor):
        x*x


def readvote(restaurant):
    response = ddbtable.get_item(Key={'name': restaurant})
    # this is required to convert decimal to integer 
    normilized_response = json.dumps(response)
    json_response = json.loads(normilized_response)
    votes = json_response["Item"]["restaurantcount"]
    return str(votes)

def updatevote(restaurant, votes):
    ddbtable.update_item(
        Key={
            'name': restaurant
        },
        UpdateExpression='SET restaurantcount = :value',
        ExpressionAttributeValues={
            ':value': votes
        },
        ReturnValues='UPDATED_NEW'
    )
    return str(votes)


@app.route("/api/outback")
def outback():
    string_votes = readvote("outback")
    votes = int(string_votes)
    votes += 1
    string_new_votes = updatevote("outback", votes)
    return string_new_votes 

@app.route("/api/bucadibeppo")
def bucadibeppo():
    string_votes = readvote("bucadibeppo")
    votes = int(string_votes)
    votes += 1
    string_new_votes = updatevote("bucadibeppo", votes)
    return string_new_votes 

@app.route("/api/ihop")
def ihop():
    string_votes = readvote("ihop")
    votes = int(string_votes)
    votes += 1
    string_new_votes = updatevote("ihop", votes)
    return string_new_votes 

@app.route("/api/chipotle")
def chipotle():
    string_votes = readvote("chipotle")
    votes = int(string_votes)
    votes += 1
    string_new_votes = updatevote("chipotle", votes)
    return string_new_votes 

@app.route("/api/getvotes")
def getvotes():
    string_outback = readvote("outback")
    string_ihop = readvote("ihop")
    string_bucadibeppo = readvote("bucadibeppo")
    string_chipotle = readvote("chipotle")
    string_votes = '[{"name": "outback", "value": ' + string_outback + '},' + '{"name": "bucadibeppo", "value": ' + string_bucadibeppo + '},' + '{"name": "ihop", "value": '  + string_ihop + '}, ' + '{"name": "chipotle", "value": '  + string_chipotle + '}]'
    if memstress == "1":
      print("the MEMSTRESS variable is set to " + memstress + ". I am eating 100MB at every getvotes request")
      memeater[randrange(10000)] = bytearray(1024 * 1024 * 100 * memstressfactor) # eats 100MB * memstressfactor
    if cpustress == "1":
      processes = cpu_count()
      print 'utilizing %d cores\n' % processes
      pool = Pool(processes)
      pool.map(f, range(processes))
      print("the CPUSTRESS variable is set to " + cpustress + ". I am eating some cpu at every getvotes request")
    return string_votes
    
if __name__ == '__main__':
   app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
   app.debug =True
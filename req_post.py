import json
# import requests
import urllib2

GLASSES_IP = "192.168.71.50"
base_url = "http://" + GLASSES_IP

test_msg = "hello"

# response = requests.post("http://192.168.71.50", data={"msg" : test_msg})
# print("status_code : " + str(response.status_code))
# print("res_msg : " + response.txt)

def post_request(api_action, data=None):
    url = base_url + api_action
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    data = json.dumps(data)
    response = urllib2.urlopen(req, data)
    data = response.read()
    json_data = json.loads(data)
    print(json_data)
    return json_data

post_request("/api/system/conf")

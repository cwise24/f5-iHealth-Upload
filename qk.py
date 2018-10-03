#!/usr/bin/env python

import json, cookielib, requests

url='https://api.f5.com/auth/pub/sso/login/ihealth-api'
headers = {'content-type': 'application/json', 'user-agent':'FSE_QKapi'}
payload = {'user_id':'<user id>', 'user_secret':'<password>'}
session = requests.session()
r_token = session.post(url, headers=headers, data=json.dumps(payload))

print "Auth Token ", r_token.status_code

url1 = 'https://ihealth-api.f5.com/qkview-analyzer/api/qkviews'
headers1 = {'Accept': 'application/vnd.f5.ihealth.api', 'user-agent':'FSE_QKapi'}
payload1 = {'visible_in_gui': 'True'}
fvar = {'qkview': open('support.qkview', 'rb')}
r_Up = session.post(url1, headers=headers1, files=fvar, data=payload1)

print "Upload Status ",r_Up.status_code

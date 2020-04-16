import requests
import json
import os
 
webhook_url = os.environ['WEBHOOK_URL']






requests.post(webhook_url,json.dumps(main_content),headers={'Content-Type': 'application/json'})
  
  
  
  

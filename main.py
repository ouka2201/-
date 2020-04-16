import requests
import json
 
webhook_url = 'https://discordapp.com/api/webhooks/700232080885284904/ppHjyZ98WH7mgtHk7K-NCZ9e-udgzsJ7BYDPr0Vh5kYWiNiz3uUBM_rukslWXIVzTWUc'






requests.post(webhook_url,json.dumps(main_content),headers={'Content-Type': 'application/json'})
  
  
  
  

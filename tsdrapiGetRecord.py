from __future__ import print_function

from Plumage import plumage 
import json

def lambda_handler(event, context):
   t = plumage.TSDRReq()
   t.getTSDRInfo(str(event['params']['num']), str(event['params']['numtype']))   # get info on reg. no 2,564,831
   tsdrdata=t.TSDRData

   if tsdrdata.TSDRMapIsValid:
      try:
         event['params']['record-key']
      except KeyError:
         responseBody = "{\"TSDRSingle\": " + json.dumps(tsdrdata.TSDRSingle,ensure_ascii=False) + ", \"TSDRMulti\": " + json.dumps(tsdrdata.TSDRMulti,ensure_ascii=False) + "}"
         return responseBody
      else:
         try:
            singleDump = json.dumps(tsdrdata.TSDRSingle[str(event['params']['record-key'])],ensure_ascii=False)
            return singleDump
         except:
            try:
               multiDump = json.dumps(tsdrdata.TSDRMulti[str(event['params']['record-key'])],ensure_ascii=False)
               return multiDump
            except:
               return "JSON key reference does not exist"
   else:
      return "Could not parse trademark file. Please check status manually."

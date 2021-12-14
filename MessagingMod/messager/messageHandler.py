"""
this class is for handling full Messaging capabilitys for Notifing the user during import situations in program
TODO: Get Custom Textbelt Gateway to work so i dont have to charge users to use this program
"""

import requests
from utils import consoleLog

default_endpoint ='https://textbelt.com/text'

# this Sends and checks to see if the endpoint works
def checkEndpoint(phoneNum,apikey):
    phone = str("'")+str(phoneNum)+str("'")
    key = str(apikey)
    resp =  requests.post('https://textbelt.com/text', {
    'phone': phone,
    'message': 'Hello world This is A Test Message from SecuServe UwU',
    'key': key,
    })
    
    print(resp.json()['success'])
    consoleLog.info("Responce from Textbelt"+ "  "+ "Enpoint Checking  "+" "+"Was Sent"+"  "+ str(resp.json()['success']))

# this is for handling sending all the messages UwU
def _message(endpoint,apikey,phoneNum,message):

    phone = str(phoneNum)
    msg = str(message)
    apikey = str(apikey)

    consoleLog.PipeLine_Ok("textbelt request:"+"   "+ phone+ "   "+ msg+ "  "+ apikey)

    resp = requests.post(endpoint, {
    'phone': phone,
    'message': msg,
    'key': apikey,
    })
    consoleLog.Warning("Responce from Textbelt"+ "  "+ str(message)+" "+"Was Sent"+"  "+ str(resp.json()['success']))
    consoleLog.PipeLine_Ok("Responce from Textbelt"+ "  "+ str(message)+" "+"Was Sent"+"  "+ str(resp.json()['success']))
    
    # if the custom endpoint fails, Use Default one
    if(resp.json()['success'] == False):
        consoleLog.Warning("Faild to send message via the first endpoint now sending it with the Default one")
        print("textbelt request:"+"   "+ phone+ "   "+ msg+ "  "+ apikey)

        phone = str(phoneNum)
        msg = str(message)
        apikey =str(apikey)
        resp = requests.post('https://textbelt.com/text', {
        'phone': phone,
        'message': msg,
        'key': apikey,
        })
        print("Responce from Textbelt"+ "  "+ str(message)+" "+"Was Sent"+"  "+ str(resp.json()['success'])+ "   "+ "error:"+"  "+str(resp.json()['error']))
        consoleLog.info("Responce from Textbelt"+ "  "+ str(message)+" "+"Was Sent"+"  "+ str(resp.json()['success'])+ "   "+ "error:"+"  "+str(resp.json()['error']))


# this checks the ballance of the api key 
def _balence(endpoint,apikey,phoneNum,message):

    phone = str(phoneNum)
    msg = str(message)
    apikey = str(apikey)
    print("textbelt request:"+"   "+ phone+ "   "+ msg+ "  "+ apikey)

    resp = requests.post(endpoint, {
    'phone': phone,
    'message': msg,
    'key': apikey,
    })
    consoleLog.Warning("Responce from Textbelt"+ "  "+ str(message)+" "+"Was Sent"+"  "+ str(resp.json()['success']))
    print("Responce from Textbelt"+ "  "+ str(message)+" "+"Was Sent"+"  "+ str(resp.json()['success']))
    print("Qutoa left:"+" "+ str(resp.json()['quotaRemaining']))

# Sends life threating Info
def sendWarnMessage(message,phoneNum,api):
    _message(default_endpoint,api,phoneNum,"[SECU-SERVE]"+ str(" ")+"WARNING! WARNING! WARNING!"+str("  ")+str(message))

# Sends Debug  Info
def sendDebugMessage(message,phoneNum,api):
    _message(default_endpoint,api,phoneNum,"[SECU-SERVE]"+ str(" ")+"debug"+str("  ")+str(message))


# Sends Warning threating Info
def sendMessage(message,phoneNum,api):
    _message(default_endpoint,api,phoneNum,"[SECU-SERVE]"+str("  ")+str(message))

# Sends a caputued image to the user
def sendCapturedImageMessage(message,phoneNum,url,api):
    _message(default_endpoint,apikey=api,phoneNum=phoneNum,message="[SECU-SERVE-CAPUTURED]"+str("  ")+str(message)+" "+str(url))

# checks the balance to the calls bakie
def checkbalRemaining(phoneNum,api):
    _balence(default_endpoint,apikey=api,phoneNum=phoneNum,message="checking bal")
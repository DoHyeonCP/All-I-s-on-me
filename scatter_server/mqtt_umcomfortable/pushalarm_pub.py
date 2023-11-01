import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
from firebase_admin import datetime

cred_path = "scatter-41f74-firebase-adminsdk-rkm4o-783d482b9a.json"
cred = credentials.Certificate(cred_path)
default_app = firebase_admin.initialize_app(cred)

# 안드로이드에서 토큰 전송 받도록 해야함

def pushalarm(area, firebasetoken):
    registration_token = str(firebasetoken)
    print (registration_token)
    message = messaging.Message(
            notification=messaging.Notification(
                    title= '위험',
                    body = f'사람이 많은 ${area} 근처입니다.',
            ),
            token = registration_token,
        )

    response = messaging.send(message)
    # Response is a message ID string.
    print ('Successfully sent message:', response)




# pushalarm("롯데월드")
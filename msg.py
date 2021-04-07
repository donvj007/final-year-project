from twilio.rest import Client
import datetime
def message():
   

    x = datetime.datetime.now()
    y=x.strftime("%c") + " "+x.strftime("%p")
    account = "AC9e2e644ad97a41c382fe63a5927c6639"
    token = "a6cd4080884d4bf9f2cf647b36596dbf"

    client = Client(account, token)

    message = client.messages.create(to="+917010440985", from_="+12055498665",
                                 body="somebody found!!!\n at "+str(y)+" \n Test msg by Vijay :)")
    #print response back from Twilio
    print ("message sent")

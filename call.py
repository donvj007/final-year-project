from twilio.rest import Client as Call
import msg
def calling():
    print("in Call module")
    From_Number = "+12055498665"
    To_Number = "+917010440985"
    #Src_Path = "https://demo.twilio.com/docs/voice.xml"
    Src_Path = "https://anti-theft-cctv.firebaseapp.com/voice.xml"

    #Client = Call("AC9e2e644ad97a41c382fe63a5927c6639","a6cd4080884d4bf9f2cf647b36596dbf")
    client = Call("AC9e2e644ad97a41c382fe63a5927c6639","a6cd4080884d4bf9f2cf647b36596dbf")

    print("Call Started")
    client.calls.create(to=To_Number, from_=From_Number, url = Src_Path, method = 'GET')
    print("call registered")
    print("Messaging proceed...")
    #msg.message()

import serial
import time
import tweepy
import sys

#Serial communication
try:
    ser = serial.Serial('COM4', 9600, timeout=0)
except Exception:
    print "Could not connect to 'COM4' serial port"
    exit()

#Estados de umidade
SECO = 0
MODERADO = 1
UMIDO = 2

#twitter application credentials
consumer_key="CONSUMER_KEY"
consumer_secret="CONSUMER_SECRET"

#twitter user credentials
access_token="ACCESS_TOKEN"
access_token_secret="ACCESS_TOKEN_SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

tweepyapi = tweepy.API(auth)

while 1:
    try:
        BYTE_READ = ser.read()
        if(BYTE_READ != ''):
            BYTE_READ = int(BYTE_READ)
            LOCAL_TIME = str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min) + ":" + str(time.localtime().tm_sec)
            if BYTE_READ == SECO:
                print("Solo em umidade baixa");
                #tweepyapi.update_status('Estado de umidade atual da terra: SECO. "HELP!!! :(" ')
                tweepyapi.update_status('Estado de umidade atual da terra: SECO. "HELP!!! :(" ' + LOCAL_TIME)
            elif BYTE_READ == MODERADO:
                print("Solo em umidade moderada");
                #tweepyapi.update_status('Estado de umidade atual da terra: MODERADO. "Nothing bad!!!" ')
                tweepyapi.update_status('Estado de umidade atual da terra: MODERADO. "Nothing bad!!!" ' + LOCAL_TIME)
            elif BYTE_READ == UMIDO:
                print("Solo em umidade alta");
                #tweepyapi.update_status('Estado de umidade atual da terra: UMIDO. "Everything great! :)"' )
                tweepyapi.update_status('Estado de umidade atual da terra: UMIDO. "Everything great! :)"' + LOCAL_TIME)
    except Exception as e:
        #print "Connection closed."
        print(e)
        #exit()
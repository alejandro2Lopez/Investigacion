from traceback import print_tb
from flask import Flask, jsonify, request
import tweepy

import mysql.connector

cnx = mysql.connector.connect(user='root', password='123p',
                              host='127.0.0.1',
                              database='PRUEBA')
cursor = cnx.cursor()
cursor.execute("SELECT * FROM Persona")
print(cursor.fetchall()) 
cnx.close()
app = Flask(__name__)
# Authenticate to Twitter
auth = tweepy.OAuthHandler("S8WH0kA1pl10TYefROTCd4hbb", "EDH4CMjriRmlkqKDtNYNZiYNyk8mIa0Hq437FBIYtKTwhXA9c9")
auth.set_access_token("1533245440761679873-Z50i6rMd0Dy7stKuU37KFSpvlEi8iU", "xJqyspTvnLSBmrJL6py8QKQWevHOahST5wmlgHm6dU1Ak")

ap2i = tweepy.API(auth)

try:
    ap2i.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")



@app.route('/', methods=['GET'])

def hello():
    user = ap2i.get_user(screen_name='Ale79013')

    for follower in user.followers():
        print(follower.name)
        
    user1= {'name': user.name, 'descripcion':user.description, 'location': user.location}
  
    return jsonify({'nombre': user1})

user = ap2i.get_user(screen_name='NavasKeylor')
for follower in user.followers():
    print(follower.name)






if __name__ == '__main__':
    app.run(debug=True, port=8000)
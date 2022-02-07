import json
from tweepy import OAuthHandler, Stream, StreamListener
from datetime import datetime

# Cadastro das chaves de acesso
consumer_Key = "xxxxx"
consumer_secret = "xxxxx"
access_token = "xxxxx"
access_token_secret = "xxxxx"

# Define um arquivo de saída para armazenar os tweets coletados
data_hoje = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
out = open(f"collected_tweets_{data_hoje}.txt", "w")

# Implementa uma classe para conexão com o Twitter
class MyListener(StreamListener):

    def on_data(self, data):
        itemString = json.dumps(data)
        out.write(itemString + "\n")
        return True

    def on_error(self, status):
        print(status)

# Implementa a função MAIN
if __name__ == '__main__':
    l = MyListener()
    auth = OAuthHandler(consumer_Key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    Stream = Stream(auth, l)
    Stream.filter(track=["Bolsonaro"])

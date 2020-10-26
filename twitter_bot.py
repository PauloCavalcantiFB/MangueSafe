import tweepy

#Autentica para o twitter
auth = tweepy.OAuthHandler("Xrpbldbdq0BEqMZjcYEfKqdmr", "jo7q2PViLfUzpfyRnwQlNDdG3L07HmBk6m2z047WduXqW7rg7i")
auth.set_access_token("1048807349434155008-wPDPwnTPm5EmOOKZEeidQFFK9MUwZc", "0cG1uvk2Xd5JwEIA6aUyFuzc1hQzJz4Yf3FBuX91BZO2F")

#Cria um objeto API
api = tweepy.API(auth)

#Cria um tweet
api.update_status("Hello Tweepy, teste!")

try:
    api.verify_credentials()
    print("Autenticação OK.")
except:
    print("Ocorreu algum erro.")


#API key: Xrpbldbdq0BEqMZjcYEfKqdmr

#API key secret: jo7q2PViLfUzpfyRnwQlNDdG3L07HmBk6m2z047WduXqW7rg7i

#Bearer token: AAAAAAAAAAAAAAAAAAAAADKaJAEAAAAA9cpScEHW7LSlDY90eDGDH6g3Ink%3DQEry3DKyQhtJ4XRCqUWtxXzBcIsxjw1BMaBWohYU8XNa0i2nli

#Access Token: 1048807349434155008-wPDPwnTPm5EmOOKZEeidQFFK9MUwZc

#Access token secret: 0cG1uvk2Xd5JwEIA6aUyFuzc1hQzJz4Yf3FBuX91BZO2F
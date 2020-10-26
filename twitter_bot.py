import tweepy

#Autentica para o twitter
auth = tweepy.OAuthHandler("Xrpbldbdq0BEqMZjcYEfKqdmr", "jo7q2PViLfUzpfyRnwQlNDdG3L07HmBk6m2z047WduXqW7rg7i")
auth.set_access_token("1048807349434155008-wPDPwnTPm5EmOOKZEeidQFFK9MUwZc", "0cG1uvk2Xd5JwEIA6aUyFuzc1hQzJz4Yf3FBuX91BZO2F")

#Cria um objeto API
api = tweepy.API(auth)

#Cria um tweet
original_tweet = api.update_status('teste de thread3')
txt_thread = 'Reply update_satus original.'
api.update_status(status=txt_thread, in_reply_to_status_id = original_tweet.id, auto_populate_reply_metadata=True)

#try:
#    api.verify_credentials()
#    print("Autenticação OK.")
#except:
#    print("Ocorreu algum erro.")
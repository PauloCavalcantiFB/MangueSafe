import tweepy

#Teste de atualização mamaquinho

#Autentica para o twitter
auth = tweepy.OAuthHandler("Xrpbldbdq0BEqMZjcYEfKqdmr", "jo7q2PViLfUzpfyRnwQlNDdG3L07HmBk6m2z047WduXqW7rg7i")
auth.set_access_token("1048807349434155008-wPDPwnTPm5EmOOKZEeidQFFK9MUwZc", "0cG1uvk2Xd5JwEIA6aUyFuzc1hQzJz4Yf3FBuX91BZO2F")

#Cria um objeto API
api = tweepy.API(auth)

raw = input("Insert the text: ")
input_raw = list(raw)
commit = []
tweets = []
temp = ''
flag = True
contador = 0

for c in range(len(input_raw)):
	if c == 0:
		commit.append(input_raw[c])
	elif c % 130 != 0:
		commit.append(input_raw[c])
	elif c % 130 == 0 and flag == False:
		commit.append(input_raw[c])
		temp = temp.join(commit)
		#print(temp)
		tweets.append(api.update_status(status=temp, in_reply_to_status_id=tweets[contador].id, auto_populate_reply_metadata=True))
		contador += 1
		commit.clear()
		temp = ''
	elif c % 130 == 0 and flag == True:
		commit.append(input_raw[c])
		temp = temp.join(commit)
		#print(temp)
		tweets.append(api.update_status(temp))
		commit.clear()
		temp = ''
		flag = False
temp = temp.join(commit)
tweets.append(api.update_status(status=temp, in_reply_to_status_id=tweets[contador].id, auto_populate_reply_metadata=True))

#if len(tweets) > 1:
#	original = api.update_status(tweets[0])
#	for i in range(len(tweets)):
#		original = api.update_status(tweets[i + 1], in_reply_to_status_id=original.id, auto_populate_reply_metadata=True)

#Cria um tweet
#original_tweet = api.update_status('teste de thread3')
#txt_thread = 'Reply update_satus original.'
#api.update_status(status=txt_thread, in_reply_to_status_id = original_tweet.id, auto_populate_reply_metadata=True)

#try:
#    api.verify_credentials()
#    print("Autenticação OK.")
#except:
#    print("Ocorreu algum erro.")

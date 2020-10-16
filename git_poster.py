import praw, os, creds

reddit = praw.Reddit(client_id=creds.client_id,
                     client_secret=creds.client_secret,
                     password=creds.password,
                     user_agent='/r/Houston headline bot by /u/thecravenone',
                     username=creds.username)

stream=os.popen('git log --pretty=%h:\ %s -n1')
subject = stream.read().rstrip()

stream=os.popen('git log --pretty=%b -n1')
body = stream.read().rstrip()


try:
	the_thread = reddit.subreddit('HoustonHeadlineBot').submit(subject, selftext=body)
except Error as error:
	print(error)
else:
	id = the_thread.id
	print("Succesfully posted commit thread to https://redd.it/" + id)
	try:
		the_thread.mod.lock()
	except Error as error:
		print(error)
	else:
		print("Successfully locked thread.")

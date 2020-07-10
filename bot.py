from datetime import datetime
import praw, re, requests, html, sys, creds, hhb_regexes

reddit = praw.Reddit(client_id=creds.client_id,
                     client_secret=creds.client_secret,
                     password=creds.password,
                     user_agent='/r/Houston headline bot by /u/thecravenone',
                     username=creds.username)

def complain(submission, headline, title):
	message = "Detected bad submission at https://redd.it/" + submission + "\n\nOriginal headline: " + headline + "\n\nOP's headline: " + title
	reddit.redditor('thecravenone').message('Bot checking in!', message)
	this_submission = reddit.submission(id=submission)
	this_submission.reply('Original headline:\n>#' + headline)

def log(input):
	stamp = str(datetime.now())
	print(stamp + " " + input)

regexes = hhb_regexes.regexes
url_regex = "(?<=\/\/).*?(?=\/)"



log("Run begining.")

runtime = int(datetime.now().timestamp())

for submission in reddit.subreddit('houston').new(limit=10):
	subtime = submission.created_utc
	if subtime > runtime - 300:
		if not submission.is_self:
			url = submission.url
			thread_id = str(submission)
			domain = re.findall(url_regex, url)[0]
			if not domain == "i.redd.it":	# Reduce comparisons by 
											# eliminating the most common
											# domain we won't be using
				if domain in regexes:
					# Handle needing a different regex for chron.com slideshows:
					# TODO: A more elegant and extensible way to handle such things
					if domain == "www.chron.com" and bool(re.match(r".*\/slideshow\/.*", url)):
						domain = "chron slideshow"

					title = submission.title.rstrip()
					log("Submission: https://redd.it/" + thread_id)
					log("Title: " + title)
					log("Fetching...")
					site_content = requests.get(url).text
					headline = html.unescape(re.findall(regexes[domain], site_content)[0].rstrip())
						#Get the regex's result, strip trailing whitespace and convert HTML entities to characters
					log("Detected headline: " + headline)
					if headline != title:
						log("***** DETECTED BAD HEADLINE *****")
						log("ORIGINAL: " + headline)
						log("OP      : " + title)
						complain(thread_id, headline, title)
					else:
						log("Headline good!")
				else:
					log("Unknown domain: " + domain + " submission: https://redd.it/" + thread_id)
	else:				
		log("All further submissions are > 5 minutes old")
		sys.exit()	# Submissions are returned in order from newest to oldest.
					# Therefore any further submissions are too old and do not
					# need to be evaluated

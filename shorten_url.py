import urllib.request

def shortenUrl(text):
	if (len(text.split()) != 1):
		return "/shortenUrl must take only 1 arguement"
	url = urllib.request.urlopen("http://tinyurl.com/api-create.php?url=" + text);
	contents = url.read()
	return contents
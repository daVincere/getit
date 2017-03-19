from django.shortcuts import render

# Create your views here.
def main(request):
	site_list = {
		"https://techcrunch.com/",
		"https://www.wired.com/about/rss_feeds/",
		"http://www.techrepublic.com/rssfeeds/",
		"https://www.cnet.com/rss/",	
	}

	for site in site_list:
		
	context = {

	}
	return render(request, "index.html", context)
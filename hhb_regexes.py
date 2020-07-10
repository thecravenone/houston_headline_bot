regexes = {
	"www.houstonchronicle.com":"(?<=\"\>)(.*?)(?=<\/h1>)",
	"www.khou.com":"(?<=\"article__headline\"\>)(.*?)(?=<\/h1>)",
	"www.houstonpublicmedia.org":"(?<=\>)(.*?)(?=<\/h1>)",
	"www.click2houston.com":"(?<=\"headline\":\")(.*?)(?=\",\"description\")",
	"www.chron.com":"(?<=og:title\" content=\")(.*)(?=\"\ +\/>)",
	"chron slideshow":"(?<=og:title\" content=\")(.*)(?=\"\/><meta property=\"og:description)",
	"abc13.com":"(?<=class=\"headline\">)(.*)(?=<\/h1>)",
	"spacecityweather.com":"(?<=<h1 class=\"amp-wp-title\">)(.*?)(?=</h1>)"
}
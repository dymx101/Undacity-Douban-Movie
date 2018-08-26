"""
SPEC - https://github.com/dymx101/cn-python-foundation/tree/master/best%20movie
"""
import requests
import  expanddouban

"""
return a string corresponding to the URL of douban movie lists given category and location.
"""
def getMovieUrl(category, location):
    url = None
    if category:
        url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,{}".format(category)
    if location:
        url = "{},{}".format(url, location)
    return url

url = getMovieUrl("剧情","美国")
print(url)
# response = requests.get(url)
# html = response.text

html = expanddouban.getHtml(url)

print(html)
from BeautifulSoup import BeautifulSoup
myfile = open("user_details.txt", "r")
html = myfile.read()

print BeautifulSoup(html).prettify()
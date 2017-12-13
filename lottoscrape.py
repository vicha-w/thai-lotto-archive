from bs4 import BeautifulSoup
from urllib.request import urlopen

#metaurl = "http://news.sanook.com/lotto/archive/page/{}/"
# http://lottery.kapook.com/2560/2017-01-17.html
metaurl = "http://lottery.kapook.com/{}/{}-{:02d}-{:02d}.html"

'''
for num in range(1, 28):
    page = urlopen(metaurl.format(num)).read().decode("utf-8")
    soup = BeautifulSoup(page, "html.parser")
    for div in soup.findAll(class_="archive--lotto__body"): 
        links.append(div.a['href'])

links = links[1:]
'''

links = []
for year in range(2012, 2018):
    for month in range(1, 13):
        for day in [1, 16]:
            eday = day
            emonth = month
            if day == 1 and month == 1:
                eday = 30
                emonth = 12
            elif day == 16 and month == 1 and year >= 2016: eday = 17
            elif day == 1 and month == 5: eday = 2
            elif day == 1 and month == 6 and year == 2015: eday = 2
            elif day == 16 and month == 12 and year == 2015: eday = 17
            links.append(metaurl.format(year+543, year, emonth, eday))

for link in links:
    pagename = link.split('/')[-1].replace('.html', '')
    [year, month, day] = [int(string) for string in pagename.split('-')]
    try:
        page = urlopen(link).read()
    except Exception as e:
        print("WARNING: "+link+" cannot be scraped with exception "+str(e)+". Skipping.")
        continue
    soup = BeautifulSoup(page, "html.parser")
    first = soup.find(id="no1").string
    three_first = [soup.find(id="d3:{}".format(i)).string for i in [1, 2]]
    three_last = [soup.find(id="d3:{}".format(i)).string for i in [3, 4]]
    two = soup.find(id="d2").string
    near_first = [soup.find(id="no1nr:{}".format(i)).string for i in [1, 2]]
    second = [soup.find(id="no2:{}".format(i)).string for i in range(1, 6)]
    third = [soup.find(id="no3:{}".format(i)).string for i in range(1, 11)]
    fourth = [soup.find(id="no4:{}".format(i)).string for i in range(1, 51)]
    fifth = [soup.find(id="no5:{}".format(i)).string for i in range(1, 101)]

    outfile = open("lottonumbers/"+pagename+".txt", 'w')
    outfile.write(link+'\n')
    outfile.write("FIRST "+str(first)+'\n')
    if (year > 2015) or (year == 2015 and month > 8):
        outfile.write("THREE_FIRST "+str(three_first[0])+' '+str(three_first[1])+'\n')
        outfile.write("THREE_LAST "+str(three_last[0])+' '+str(three_last[1])+'\n')
    else:
        outfile.write("THREE "+str(three_first[0])+' '+str(three_first[1])+' '+str(three_last[0])+' '+str(three_last[1])+'\n')
    outfile.write("TWO "+str(two)+'\n')
    outfile.write("NEAR_FIRST "+str(near_first[0])+' '+str(near_first[1])+'\n')

    prizes = [second, third, fourth, fifth]
    names = ["SECOND", "THIRD", "FOURTH", "FIFTH"]

    for i in range(4):
        outfile.write(names[i]+' ')
        for num in prizes[i]: outfile.write(str(num)+' ')
        outfile.write('\n')

    outfile.close()

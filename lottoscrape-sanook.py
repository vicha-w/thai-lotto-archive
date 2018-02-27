from bs4 import BeautifulSoup
from urllib.request import urlopen

links = [
    #"http://news.sanook.com/lotto/check/16022556/",
    #"http://news.sanook.com/lotto/check/01062557/",
    #"http://news.sanook.com/lotto/check/16062557/",
    #"http://news.sanook.com/lotto/check/01072557/",
    #"http://news.sanook.com/lotto/check/16072556/",
    #"http://news.sanook.com/lotto/check/16112556/",
    #"http://news.sanook.com/lotto/check/16072557/",
    #"http://news.sanook.com/lotto/check/16072559/"
    "http://news.sanook.com/lotto/check/16022561/"
    #"http://news.sanook.com/lotto/check/16072553/",
    #"http://news.sanook.com/lotto/check/01102553/",
    #"http://news.sanook.com/lotto/check/30122550/",
    #"http://news.sanook.com/lotto/check/16042551/",
    #"http://news.sanook.com/lotto/check/01082551/"
]

'''
metaurl = "http://news.sanook.com/lotto/check/{:02d}{:02d}{}/"

links = []
for year in range(2007, 2012):
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
            links.append(metaurl.format(eday, emonth, year+543))
links.append("http://news.sanook.com/lotto/check/30122549/")
'''

for link in links:
    print("Scraping numbers from link {}".format(link))
    try:
        pagename = link.split('/')[-2]
        pagename = '-'.join([str(int(pagename[4:8])-543), pagename[2:4], pagename[0:2]])
        [year, month, day] = [int(string) for string in pagename.split('-')]
        page = urlopen(link).read()
        soup = BeautifulSoup(page, "html.parser")
        numbers = [num.string for num in soup.findAll(class_="lotto__number")]
        first = numbers[0]
        three_first = numbers[1:3]
        three_last = numbers[3:5]
        two = numbers[5]
        near_first = numbers[6:8]
        second = numbers[8:13]
        third = numbers[13:23]
        fourth = numbers[23:73]
        fifth = numbers[73:173]

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
            for num in prizes[i]: outfile.write(num.strip()+' ')
            outfile.write('\n')

        outfile.close()
        print("Scraped data from {} into lottonumbers/{}.txt".format(link, pagename))
    except Exception as e:
        print("WARNING: "+link+" cannot be scraped with exception "+str(e)+". Skipping.")
        continue

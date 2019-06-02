# thai-lotto-archive
Archive of winning Thai lottery numbers since 2007. All data are sourced from kapook.com, sanook.com, and other sources.

## File structure
Each file in `lottonumbers` directory consist of winning numbers from each lotto drawing days, shown in a file name. The first line is a URL of website as a source for winning numbers data on the corresponding day. *On some lottery drawing days, data can not be properly scraped from either kapook.com or sanook.com, so they are recorded by hand from other sources.* One string precedes each line from the second line onwards, which labels other numbers on the line to each corresponding prize as follows:

* `FIRST`: 1st prize, 1 number
* *(Prior to 1 September 2015)* `THREE`: Prize matching last 3 digits, 4 numbers
* *(1 September 2015 onwards)* `THREE_FIRST`: Prize matching first 3 digits, 2 numbers
* *(1 September 2015 onwards)* `THREE_LAST`: Prize matching last 3 digits, 2 numbers
* `TWO`: Prize matching last 2 digits, 1 number
* `NEAR_FIRST`: Prize with numbers close to 1st prize (see section [Some information about Thai lottery](#some-information-about-thai-lottery)), 2 numbers
* `SECOND`: 2nd prize, 5 numbers
* `THIRD`: 3rd prize, 10 numbers
* `FOURTH`: 4th prize, 50 numbers
* `FIFTH`: 5th prize, 100 numbers

## `lottoscraper.py` and `lottoscraper-sanook.py`
This repo also contains two python scripts which I used to scrape all data from lottery checking pages at [kapook.com](http://lottery.kapook.com/) and [sanook.com](http://news.sanook.com/lotto/), and put them in a nice format under the directory `lottonumbers`. `lottoscraper.py` is tailored for web page format seen in kapook.com, while `lottoscraper-sanook.py` is for web page format seen in sanook.com. You will need Python 3 and [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) in order to run the scripts.

## Archive in other formats
* pandas DataFrame containing winning numbers can be obtained via `lottodataframe.py` (made by [@kittinan](https://github.com/kittinan) -- thank you!). To obtain the DataFrame: 
    ```python
    import lottodataframe
    lottodataframe.get_lotto_df()
    ```
    *Winning numbers in this DataFrame will only include first prize winning number, as well as last two winning digits, first three winning digits, and last three winning digits.*
* If you would like to provide code for other formats, you may submit a pull request with provided code. Please keep in mind that the code must be able to generate the latest winning numbers according to the archive.

## Some information about Thai lottery
Thailand's Government Lottery Office draws winning lottery numbers on the 1st and 16th of every month, with a few exceptions as follows:

* Lottery drawings on 1 January (New year's day) are scheduled on 30 December, two days before the 1 January.
* Lottery drawings on 16 January (Teacher's day) are scheduled on 17 January.
* Lottery drawings on 1 May (Labour day) are scheduled on 2 May.
* Lottery drawing on 1 June 2015 was held on 2 June on the same year, since 1 June 2015 was Visakha Bucha day as Thai official holiday.
* Lottery drawing on 16 December 2015 was held on 17 December, since the funeral for Somdet Phra Yannasangwon, Supreme Patriarch of Thailand took place on that day.
* Lottery drawing on 1 March 2018 was held on 2 March, since 1 March 2018 was Makha Bucha day as Thai official holiday.

Each Thai lottery contains six digits, resulting in one million combinations in total. A list of prizes are as follows:

* **1st prize** with 1 winning number.
* **Close numbers to 1st prize** which is an increment or decrement of the winning number of the 1st prize by 1, comprising of 2 winning numbers. For example, if the 1st prize winning number is 123456, the numbers belonging to this prize will be 123455 and 123457.
* **2nd prize** with 5 winning numbers.
* **3rd prize** with 10 winning numbers.
* **4th prize** with 50 winning numbers.
* **5th prize** with 100 winning numbers.
* (Prior to 1 September 2015) **Matching last 3 digits** with 4 winning numbers.
* (1 September 2015 onwards) **Matching *first* 3 digits** with 2 winning numbers.
* (1 September 2015 onwards) **Matching *last* 3 digits** with 2 winning numbers.
* **Matching last 2 digits** with 1 winning number.

For more information, see https://th.wikipedia.org/wiki/%E0%B8%AB%E0%B8%A7%E0%B8%A2%E0%B9%83%E0%B8%99%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B9%80%E0%B8%97%E0%B8%A8%E0%B9%84%E0%B8%97%E0%B8%A2 (Thai Wikipedia)

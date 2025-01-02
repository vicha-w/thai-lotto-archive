# thai-lotto-archive
Archive of winning Thai lottery numbers since 2007. All data are sourced from kapook.com, sanook.com, and other sources.

## File structure
Each file in `lottonumbers` directory consist of winning numbers from each lotto drawing days, shown in a file name. The first line is a URL of website as a source for winning numbers data on the corresponding day. *On some lottery drawing days, data can not be properly scraped from either kapook.com or sanook.com, so they are recorded by hand from other sources.* One string precedes each line from the second line onwards, which labels other numbers on the line to each corresponding prize as follows:

* `FIRST`: First Prize, 1 number
* *(Prior to 1 September 2015)* `THREE`: Three Digit Suffix 4 numbers
* *(1 September 2015 onwards)* `THREE_FIRST`: Three Digit Prefix, 2 numbers
* *(1 September 2015 onwards)* `THREE_LAST`: Three Digit Suffix, 2 numbers
* `TWO`: Two Digit Suffix, 1 number
* `NEAR_FIRST`: First Prize Neighbours (see section [Some information about Thai lottery](#some-information-about-thai-lottery)), 2 numbers
* `SECOND`: Second Prize, 5 numbers
* `THIRD`: Third Prize, 10 numbers
* `FOURTH`: Fourth Prize, 50 numbers
* `FIFTH`: Fifth Prize, 100 numbers

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
Thailand's Government Lottery Office (GLO) draws winning lottery numbers on the 1st and 16th of every month, with a few exceptions as follows:

* Lottery drawings on 1 January (New year's day) are scheduled on 30 December, two days before the 1 January.
* Lottery drawings on 16 January (Teacher's day) are scheduled on 17 January.
* Lottery drawings on 1 May (Labour day) are scheduled on 2 May.

Each Thai lottery contains six digits, resulting in one million combinations in total. A list of prizes are as follows:

* **First Prize** with 1 winning number.
* **First Prize Neighbours** which are an increment or decrement of the winning number of the First Prize by 1, comprising of 2 winning numbers. For example, if the First Prize winning number is 123456, the numbers belonging to this prize will be 123455 and 123457.
* **Second Prize** with 5 winning numbers.
* **Third Prize** with 10 winning numbers.
* **Fourth Prize** with 50 winning numbers.
* **Fifth Prize** with 100 winning numbers.
* (Prior to 1 September 2015) **Three Digit Suffix** with 4 winning numbers.
* (1 September 2015 onwards) **Three Digit *Prefix*** with 2 winning numbers.
* (1 September 2015 onwards) **Three Digit *Suffix*** with 2 winning numbers.
* **Two Digit Suffix** with 1 winning number.

For more information, see https://th.wikipedia.org/wiki/หวยในประเทศไทย (Thai Wikipedia)

## Extraordinary rescheduling of lottery drawing dates
Some lottery drawing dates are postponed due to several reasons, most commonly being the drawing date coincide with Thai Buddhist holiday, which is based on lunar calendar and not the same date on Gregorian calendar every year. Here are the lottery drawing dates that are postponed in the past or being rescheduled.

* Lottery drawing on 1 June 2015 was held on 2 June on the same year, since 1 June 2015 was Visakha Bucha day as Thai official holiday.
* Lottery drawing on 16 December 2015 was held on 17 December, since the funeral for Somdet Phra Yannasangwon, Supreme Patriarch of Thailand took place on that day.
* Lottery drawing on 1 March 2018 was held on 2 March, since 1 March 2018 was Makha Bucha day as Thai official holiday.
* Lottery drawing on 16 July 2019 was held on 15 July, since 16 July 2019 was Asalaha Bucha day as Thai official holiday, and 17 July 2019 was Buddhist Lent day as another Thai official holiday.
* Lottery drawing on 1 April 2020 was held on 16 May. Due to concerns regarding COVID-19 outbreak, GLO postponed lottery drawing on 1 April to 16 May, and no lottery tickets for 16 April, 1 May, and 16 May lottery drawings are sold.
* Lottery drawing on 16 February 2022 was held on 17 February, since 16 February 2022 was Makha Bucha day as Thai official holiday.
* Lottery drawing on 30 December 2024 was postponed by GLO to 2 January 2025.
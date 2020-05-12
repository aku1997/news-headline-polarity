#####################################
# This program finds and performs and
# displays the sentiment analysis of
# all of the headlines from Borneo 
# Bulletin,a news media of Brunei.
#
# It also displays the percentage of 
# positive, negative, and neutral
# headlines as a pie chart.
#####################################

#####################################
# Modules Used:
# 'BeautifulSoup' for Web Scraping
# 'TextBlob' for Sentiment Analysis
# 'matplotlib' for plotting a pie chart
#####################################

import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import matplotlib.pyplot as plt

# Percentage Calculator
def calculatePercentage(part,whole):
    return format((100 * float(part)/float(whole)), '.2f')
# Percentage Calculator END

response = requests.get("https://borneobulletin.com.bn/")
soup = BeautifulSoup(response.content, "html.parser")

urls = []
# getting the headlines
for h3_tags in soup.find_all("h3"):
    a_tags = h3_tags.find("a")
    urls.append(a_tags.string)

i=1
positive = 0
negative = 0
neutral = 0

# running sentiment analysis on each of the headlines
for titles in urls:
    print(i,titles)
    analysis = TextBlob(titles)
    print(analysis.sentiment)
    if analysis.sentiment.polarity > 0:
        positive+=1
    elif analysis.sentiment.polarity < 0:
        negative+=1
    else:
        neutral+=1
    i+=1

numberOfHeadlines = positive + negative + neutral

# percentage calculation
positive = calculatePercentage(positive,numberOfHeadlines)
negative = calculatePercentage(negative,numberOfHeadlines)
neutral = calculatePercentage(neutral,numberOfHeadlines)

# output in percentage
print("-------------------------")
print("Positive: ",positive,"%")
print("Negative: ",negative,"%")
print("Neutral: ",neutral,"%")
print("-------------------------")

# Pie Chart
plt.style.use("fivethirtyeight")

slices = [positive,negative,neutral]
labels = ['Positive','Negative','Neutral']
explode = [0.1,0,0]

plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=90, autopct="%1.1f%%")
plt.title("Borneo Bulletin Headlines")
plt.tight_layout()

plt.show()

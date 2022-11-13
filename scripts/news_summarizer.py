import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')

url = 'https://www.cnn.com/2019/09/25/tech/singapore-water-technology-innovative-cities/index.html'

article = Article(url)

article.download()
article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Date Published: {article.publish_date}')
print(f'Summary: {article.summary}')
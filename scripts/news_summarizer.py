import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')

# Article Summary
url = 'https://www.cnn.com/2019/09/25/tech/singapore-water-technology-innovative-cities/index.html'

article = Article(url)

article.download()
article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Date Published: {article.publish_date}')
print(f'Summary: {article.summary}')

# Sentiment Analysis
analysis = TextBlob(article.text)
print(analysis.polarity)
print(f'Sentiment: {"positve" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

# GUI
root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

alabel = tk.Label(root, text="Author(s)")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

plabel = tk.Label(root, text="Date Published")
plabel.pack()

published = tk.Text(root, height=1, width=140)
published.config(state='disabled', bg='#dddddd')
published.pack()

slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

salabel = tk.Label(root, text="Sentiment Analysis")
salabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

btn = tk.Button(root, text="Summarize")
btn.pack()

root.mainloop()
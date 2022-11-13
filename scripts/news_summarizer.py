import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')

# Article Summary

def summarize():
    url = utext.get('1.0', "end").strip()

    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    published.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    published.delete('1.0', 'end')
    published.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    # Sentiment Analysis
    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positve" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    published.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')
    
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

btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

root.mainloop()
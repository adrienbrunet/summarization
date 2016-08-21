# coding: utf-8

from newspaper import Article, nlp

"""Hypthesis:
- we treat english articles only for now.
  newspaper can handle other languages as well,
  further work could be done to achieve this.
  It should work as is though.
- we treat article one by one, i.e. one url = one article
  newspaper also provide a more violent scrapper that could be used
  to batch articles with async operations.
- A lot more extraction could be achieved using newspaper... rtfm
"""


def get_twittable_sentences_from_url(url):
    article = Article(url)
    article.download()
    article.parse()
    best_sentences = nlp.summarize(title=article.title, text=article.text)
    return [s for s in best_sentences if len(s) < 140]


if __name__ == '__main__':
    # print('\n'.join(get_twittable_sentences_from_url('www.example.com/article1')))
    pass


# TODO:
# - newspaper gives a summary of 5 sentences. It's hardcoded.
# - Each sentences respects len(sentence) > 10, we could enforce < 140 in nlp
# - if the article is only made of big-ass sentences,
#   we won't get any twittable sentences. Could we do smth about it? Should we?

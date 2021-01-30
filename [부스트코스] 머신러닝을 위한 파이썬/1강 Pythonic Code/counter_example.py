from collections import Counter

c = Counter()
c = Counter('gallahad')
print(c)
'''
Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})
'''

c = Counter({'red': 4, 'blue': 2})
print(c)
print(list(c.elements()))
'''
Counter({'red': 4, 'blue': 2})
['red', 'red', 'red', 'red', 'blue', 'blue']
'''

c = Counter(cats=4, dogs=8)
print(c)
print(list(c.elements()))
'''
Counter({'dogs': 8, 'cats': 4})
['cats', 'cats', 'cats', 'cats', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs']
'''

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)  # c- d
print(c)
'''
Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
'''

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
print(c + d)
print(c & d)
print(c | d)
'''
Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2})
Counter({'b': 2, 'a': 1})
Counter({'a': 4, 'd': 4, 'c': 3, 'b': 2})
'''

text = """A press release is the quickest and easiest way to get free publicity. If well written, a press release can result in multiple published articles about your firm and its products. And that can mean new prospects contacting you asking you to sell to them. Talk about low-hanging fruit!
What's more, press releases are cost effective. If the release results in an article that (for instance) appears to recommend your firm or your product, that article is more likely to drive prospects to contact you than a comparable paid advertisement.
However, most press releases never accomplish that. Most press releases are just spray and pray. Nobody reads them, least of all the reporters and editors for whom they're intended. Worst case, a badly-written press release simply makes your firm look clueless and stupid.
For example, a while back I received a press release containing the following sentence: "Release 6.0 doubles the level of functionality available, providing organizations of all sizes with a fast-to-deploy, highly robust, and easy-to-use solution to better acquire, retain, and serve customers."
Translation: "The new release does more stuff." Why the extra verbiage? As I explained in the post "Why Marketers Speak Biz Blab", the BS words are simply a way to try to make something unimportant seem important. And, let's face it, a 6.0 release of a product probably isn't all that important.
As a reporter, my immediate response to that press release was that it's not important because it expended an entire sentence saying absolutely nothing. And I assumed (probably rightly) that the company's marketing team was a bunch of idiots.""".lower().split()
print(Counter(text))
print(Counter(text)["a"])
'''
Counter({'a': 12, 'to': 10, 'the': 9, 'and': 9, 'press': 8, 'release': 8, 'that': 7, 'of': 5, 'your': 4, 'in': 3, 'firm': 3, 'you': 3, 'releases': 3, 'are': 3, 'all': 3, 'i': 3, 'is': 2, 'way': 2, 'if': 2, 'can': 2, 'about': 2, 'new': 2, 'prospects': 2, 'an': 2, 'article': 2, 'more': 2, 'most': 2, 'for': 2, 'simply': 2, '6.0': 2, 'as': 2, 'important.': 2, 'was': 2, 'quickest': 1, 'easiest': 1, 'get': 1, 'free': 1, 'publicity.': 1, 'well': 1, 'written,': 1, 'result': 1, 'multiple': 1, 'published': 1, 'articles': 1, 'its': 1, 'products.': 1, 'mean': 1, 'contacting': 1, 'asking': 1, 'sell': 1, 'them.': 1, 'talk': 1, 'low-hanging': 1, 'fruit!': 1, "what's": 1, 'more,': 1, 'cost': 1, 'effective.': 1, 'results': 1, '(for': 1, 'instance)': 1, 'appears': 1, 'recommend': 1, 'or': 1, 'product,': 1, 'likely': 1, 'drive': 1, 'contact': 1, 'than': 1, 'comparable': 1, 'paid': 1, 'advertisement.': 1, 'however,': 1, 'never': 1, 'accomplish': 1, 'that.': 1, 'just': 1, 'spray': 1, 'pray.': 1, 'nobody': 1, 'reads': 1, 'them,': 1, 'least': 1, 'reporters': 1, 'editors': 1, 'whom': 1, "they're": 1, 'intended.': 1, 'worst': 1, 'case,': 1, 'badly-written': 1, 'makes': 1, 'look': 1, 'clueless': 1, 'stupid.': 1, 'example,': 1, 'while': 1, 'back': 1, 'received': 1, 'containing': 1, 'following': 1, 'sentence:': 1, '"release': 1, 'doubles': 1, 'level': 1, 'functionality': 1, 'available,': 1, 'providing': 1, 'organizations': 1, 'sizes': 1, 'with': 1, 'fast-to-deploy,': 1, 'highly': 1, 'robust,': 1, 'easy-to-use': 1, 'solution': 1, 'better': 1, 'acquire,': 1, 'retain,': 1, 'serve': 1, 'customers."': 1, 'translation:': 1, '"the': 1, 'does': 1, 'stuff."': 1, 'why': 1, 'extra': 1, 'verbiage?': 1, 'explained': 1, 'post': 1, '"why': 1, 'marketers': 1, 'speak': 1, 'biz': 1, 'blab",': 1, 'bs': 1, 'words': 1, 'try': 1, 'make': 1, 'something': 1, 'unimportant': 1, 'seem': 1, 'and,': 1, "let's": 1, 'face': 1, 'it,': 1, 'product': 1, 'probably': 1, "isn't": 1, 'reporter,': 1, 'my': 1, 'immediate': 1, 'response': 1, "it's": 1, 'not': 1, 'important': 1, 'because': 1, 'it': 1, 'expended': 1, 'entire': 1, 'sentence': 1, 'saying': 1, 'absolutely': 1, 'nothing.': 1, 'assumed': 1, '(probably': 1, 'rightly)': 1, "company's": 1, 'marketing': 1, 'team': 1, 'bunch': 1, 'idiots.': 1})
12
'''

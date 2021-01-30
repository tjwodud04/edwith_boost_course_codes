# Reference from
# https://dongyeopblog.wordpress.com/2016/04/08/python-defaultdict-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0/

from collections import defaultdict
from collections import OrderedDict

d = dict()
#print(d["first"]) error

d = defaultdict(object)
d = defaultdict(lambda: 1)
print(d["first"])
'''
1
'''

text = """A press release is the quickest and easiest way to get free publicity. If well written, a press release can result in multiple published articles about your firm and its products. And that can mean new prospects contacting you asking you to sell to them. Talk about low-hanging fruit!
What's more, press releases are cost effective. If the release results in an article that (for instance) appears to recommend your firm or your product, that article is more likely to drive prospects to contact you than a comparable paid advertisement.
However, most press releases never accomplish that. Most press releases are just spray and pray. Nobody reads them, least of all the reporters and editors for whom they're intended. Worst case, a badly-written press release simply makes your firm look clueless and stupid.
For example, a while back I received a press release containing the following sentence: "Release 6.0 doubles the level of functionality available, providing organizations of all sizes with a fast-to-deploy, highly robust, and easy-to-use solution to better acquire, retain, and serve customers."
Translation: "The new release does more stuff." Why the extra verbiage? As I explained in the post "Why Marketers Speak Biz Blab", the BS words are simply a way to try to make something unimportant seem important. And, let's face it, a 6.0 release of a product probably isn't all that important.
As a reporter, my immediate response to that press release was that it's not important because it expended an entire sentence saying absolutely nothing. And I assumed (probably rightly) that the company's marketing team was a bunch of idiots.""".lower().split()

print(text)
'''
['a', 'press', 'release', 'is', 'the', 'quickest', 'and', 'easiest', 'way', 'to', 'get', 'free', 'publicity.', 'if', 'well', 'written,', 'a', 'press', 'release', 'can', 'result', 'in', 'multiple', 'published', 'articles', 'about', 'your', 'firm', 'and', 'its', 'products.', 'and', 'that', 'can', 'mean', 'new', 'prospects', 'contacting', 'you', 'asking', 'you', 'to', 'sell', 'to', 'them.', 'talk', 'about', 'low-hanging', 'fruit!', "what's", 'more,', 'press', 'releases', 'are', 'cost', 'effective.', 'if', 'the', 'release', 'results', 'in', 'an', 'article', 'that', '(for', 'instance)', 'appears', 'to', 'recommend', 'your', 'firm', 'or', 'your', 'product,', 'that', 'article', 'is', 'more', 'likely', 'to', 'drive', 'prospects', 'to', 'contact', 'you', 'than', 'a', 'comparable', 'paid', 'advertisement.', 'however,', 'most', 'press', 'releases', 'never', 'accomplish', 'that.', 'most', 'press', 'releases', 'are', 'just', 'spray', 'and', 'pray.', 'nobody', 'reads', 'them,', 'least', 'of', 'all', 'the', 'reporters', 'and', 'editors', 'for', 'whom', "they're", 'intended.', 'worst', 'case,', 'a', 'badly-written', 'press', 'release', 'simply', 'makes', 'your', 'firm', 'look', 'clueless', 'and', 'stupid.', 'for', 'example,', 'a', 'while', 'back', 'i', 'received', 'a', 'press', 'release', 'containing', 'the', 'following', 'sentence:', '"release', '6.0', 'doubles', 'the', 'level', 'of', 'functionality', 'available,', 'providing', 'organizations', 'of', 'all', 'sizes', 'with', 'a', 'fast-to-deploy,', 'highly', 'robust,', 'and', 'easy-to-use', 'solution', 'to', 'better', 'acquire,', 'retain,', 'and', 'serve', 'customers."', 'translation:', '"the', 'new', 'release', 'does', 'more', 'stuff."', 'why', 'the', 'extra', 'verbiage?', 'as', 'i', 'explained', 'in', 'the', 'post', '"why', 'marketers', 'speak', 'biz', 'blab",', 'the', 'bs', 'words', 'are', 'simply', 'a', 'way', 'to', 'try', 'to', 'make', 'something', 'unimportant', 'seem', 'important.', 'and,', "let's", 'face', 'it,', 'a', '6.0', 'release', 'of', 'a', 'product', 'probably', "isn't", 'all', 'that', 'important.', 'as', 'a', 'reporter,', 'my', 'immediate', 'response', 'to', 'that', 'press', 'release', 'was', 'that', "it's", 'not', 'important', 'because', 'it', 'expended', 'an', 'entire', 'sentence', 'saying', 'absolutely', 'nothing.', 'and', 'i', 'assumed', '(probably', 'rightly)', 'that', 'the', "company's", 'marketing', 'team', 'was', 'a', 'bunch', 'of', 'idiots.']
'''

word_count = {}

for word in text:
    if word in word_count.keys():
        word_count[word] += 1
    else:
        word_count[word] = 0
print(word_count)
'''
{'a': 11, 'press': 7, 'release': 7, 'is': 1, 'the': 8, 'quickest': 0, 'and': 8, 'easiest': 0, 'way': 1, 'to': 9, 'get': 0, 'free': 0, 'publicity.': 0, 'if': 1, 'well': 0, 'written,': 0, 'can': 1, 'result': 0, 'in': 2, 'multiple': 0, 'published': 0, 'articles': 0, 'about': 1, 'your': 3, 'firm': 2, 'its': 0, 'products.': 0, 'that': 6, 'mean': 0, 'new': 1, 'prospects': 1, 'contacting': 0, 'you': 2, 'asking': 0, 'sell': 0, 'them.': 0, 'talk': 0, 'low-hanging': 0, 'fruit!': 0, "what's": 0, 'more,': 0, 'releases': 2, 'are': 2, 'cost': 0, 'effective.': 0, 'results': 0, 'an': 1, 'article': 1, '(for': 0, 'instance)': 0, 'appears': 0, 'recommend': 0, 'or': 0, 'product,': 0, 'more': 1, 'likely': 0, 'drive': 0, 'contact': 0, 'than': 0, 'comparable': 0, 'paid': 0, 'advertisement.': 0, 'however,': 0, 'most': 1, 'never': 0, 'accomplish': 0, 'that.': 0, 'just': 0, 'spray': 0, 'pray.': 0, 'nobody': 0, 'reads': 0, 'them,': 0, 'least': 0, 'of': 4, 'all': 2, 'reporters': 0, 'editors': 0, 'for': 1, 'whom': 0, "they're": 0, 'intended.': 0, 'worst': 0, 'case,': 0, 'badly-written': 0, 'simply': 1, 'makes': 0, 'look': 0, 'clueless': 0, 'stupid.': 0, 'example,': 0, 'while': 0, 'back': 0, 'i': 2, 'received': 0, 'containing': 0, 'following': 0, 'sentence:': 0, '"release': 0, '6.0': 1, 'doubles': 0, 'level': 0, 'functionality': 0, 'available,': 0, 'providing': 0, 'organizations': 0, 'sizes': 0, 'with': 0, 'fast-to-deploy,': 0, 'highly': 0, 'robust,': 0, 'easy-to-use': 0, 'solution': 0, 'better': 0, 'acquire,': 0, 'retain,': 0, 'serve': 0, 'customers."': 0, 'translation:': 0, '"the': 0, 'does': 0, 'stuff."': 0, 'why': 0, 'extra': 0, 'verbiage?': 0, 'as': 1, 'explained': 0, 'post': 0, '"why': 0, 'marketers': 0, 'speak': 0, 'biz': 0, 'blab",': 0, 'bs': 0, 'words': 0, 'try': 0, 'make': 0, 'something': 0, 'unimportant': 0, 'seem': 0, 'important.': 1, 'and,': 0, "let's": 0, 'face': 0, 'it,': 0, 'product': 0, 'probably': 0, "isn't": 0, 'reporter,': 0, 'my': 0, 'immediate': 0, 'response': 0, 'was': 1, "it's": 0, 'not': 0, 'important': 0, 'because': 0, 'it': 0, 'expended': 0, 'entire': 0, 'sentence': 0, 'saying': 0, 'absolutely': 0, 'nothing.': 0, 'assumed': 0, '(probably': 0, 'rightly)': 0, "company's": 0, 'marketing': 0, 'team': 0, 'bunch': 0, 'idiots.': 0}
'''

word_count = defaultdict(object)
word_count = defaultdict(lambda: 0)

for word in text:
    word_count[word] += 1

for i, v in OrderedDict(sorted(
        word_count.items(), key=lambda t: t[1], reverse=True)).items():
    print(i, v)
'''
a 12
to 10
the 9
and 9
press 8
release 8
that 7
of 5
your 4
in 3
firm 3
you 3
releases 3
are 3
all 3
i 3
is 2
way 2
if 2
can 2
about 2
new 2
prospects 2
an 2
article 2
more 2
most 2
for 2
simply 2
6.0 2
as 2
important. 2
was 2
quickest 1
easiest 1
get 1
free 1
publicity. 1
well 1
written, 1
result 1
multiple 1
published 1
articles 1
its 1
products. 1
mean 1
contacting 1
asking 1
sell 1
them. 1
talk 1
low-hanging 1
fruit! 1
what's 1
more, 1
cost 1
effective. 1
results 1
(for 1
instance) 1
appears 1
recommend 1
or 1
product, 1
likely 1
drive 1
contact 1
than 1
comparable 1
paid 1
advertisement. 1
however, 1
never 1
accomplish 1
that. 1
just 1
spray 1
pray. 1
nobody 1
reads 1
them, 1
least 1
reporters 1
editors 1
whom 1
they're 1
intended. 1
worst 1
case, 1
badly-written 1
makes 1
look 1
clueless 1
stupid. 1
example, 1
while 1
back 1
received 1
containing 1
following 1
sentence: 1
"release 1
doubles 1
level 1
functionality 1
available, 1
providing 1
organizations 1
sizes 1
with 1
fast-to-deploy, 1
highly 1
robust, 1
easy-to-use 1
solution 1
better 1
acquire, 1
retain, 1
serve 1
customers." 1
translation: 1
"the 1
does 1
stuff." 1
why 1
extra 1
verbiage? 1
explained 1
post 1
"why 1
marketers 1
speak 1
biz 1
blab", 1
bs 1
words 1
try 1
make 1
something 1
unimportant 1
seem 1
and, 1
let's 1
face 1
it, 1
product 1
probably 1
isn't 1
reporter, 1
my 1
immediate 1
response 1
it's 1
not 1
important 1
because 1
it 1
expended 1
entire 1
sentence 1
saying 1
absolutely 1
nothing. 1
assumed 1
(probably 1
rightly) 1
company's 1
marketing 1
team 1
bunch 1
idiots. 1
'''
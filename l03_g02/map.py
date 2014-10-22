#!/usr/bin/python3
#@author: stifterm13, mayerhfl13

print("Sorting Example Starts!\n")

words = """Some things in life are bad
They can really make you mad
Other things just make you swear and curse.
When you're chewing on life's gristle
Don't grumble, give a whistle
And this'll help things turn out for the best...

    And...always look on the bright side of life...
    Always look on the light side of life...  """



def longwords (w):
	return len(w)>5
	
longwords("hallo")

longwords("hallihallo")
filter(longwords, words)

list(filter(longwords, words))
map(str.upper, words)

list(map(str.upper, words))
list(map(len, words))

def stars(w):
	return "*" * len(w)

list(map(stars, words))

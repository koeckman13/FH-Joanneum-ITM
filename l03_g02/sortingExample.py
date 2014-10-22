#!/usr/bin/python3
#@author: stifterm13, mayerhfl13

print("Sorting Example Starts!\n")

lyrics = """Some things in life are bad
They can really make you mad
Other things just make you swear and curse.
When you're chewing on life's gristle
Don't grumble, give a whistle
And this'll help things turn out for the best...

    And...always look on the bright side of life...
    Always look on the light side of life...  """

print(lyrics)
words=lyrics.split()
words.sort(key=str.lower)
print("Sorted:\n",words)
print("Example finished")
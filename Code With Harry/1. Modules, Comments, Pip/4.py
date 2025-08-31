"""
Purpose: To convert text into speech using 
Author: Anurag Yadav
Created: 27-07-2025
Language: Python (3.11.9)
Library: os (built-in)
Status: Final
"""

# pip install gtts

from gtts import gTTS

language = "ja"

text = """An engineer so keen and bright,
Studies circuits late at night.
With glasses thick upon his nose,
And where his social life went, no one knows.

He speaks a language, strange and new,
Of Python, C, and Java too.
He calculates the stress and strain,
While coffee percolates his brain.

His diet's mostly instant ramen,
A culinary sad specimen.
His laundry pile, a fearsome beast,
Has not been touched for weeks, at least.

He dreams in code, a strange affair,
With loops and functions everywhere.
A "for" loop runs to grab a beer,
An "if" statement conquers fear.

He'll build a bridge or write a script,
From common sense, he's gently slipped.
But ask him how to boil an egg?
A blank stare's all you'll get, I beg.

So raise a glass, a rusty wrench,
To heroes of the lab and bench!
They'll build the world, for me and you,
Just... don't ask them to tie a shoe."""


speech = gTTS(text=text, lang=language, slow=False, tld="com.au")
speech.save(r"C:\code_purgatory\DS_AIML\Code With Harry\1. Modules, Comments, Pip\output.mp3")
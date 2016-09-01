#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright 2016 David Lougheed

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from flask import Flask
from random import randint

# A constant referring to the dictionary to use.
WORD_FILE = "./words.txt"

# Initialize the Flask app.
app = Flask(__name__)

# The main and only route.
@app.route("/")
def main():
	with open(WORD_FILE, "r") as words:
		word_list = list(filter(None, words.read().split("\n")))
		random_word = word_list[int(randint(0, len(word_list) - 1))]
		return "{} boi".format(random_word)

if __name__ == "__main__":
	main()

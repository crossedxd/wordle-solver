#!/usr/bin/env python3

import argparse
from collections import Counter
from pprint import pprint as print
import string


def get_wordlist():
    wordlist = set()
    with open("/usr/share/dict/words") as f:
        for row in f.read().splitlines():
            if "'" not in row and len(row) == 5:
                wordlist.add(row.upper())
    return wordlist


def check_word_length(word):
    if len(word) == 10:
        return word
    raise argparse.ArgumentTypeError("Word length must be 10")


def filter_wordlist(wordlist, mask):
    temp = set()

    filter_gg = mask[:5]
    filter_y = mask[5:]

    for word in wordlist:
        keep = True

        # Green/grey filter
        for i in range(5):
            if filter_gg[i] == " ":  # Skip empty spaces
                continue
            elif filter_gg[i].isupper():  # Green
                if filter_gg[i] != word[i]:
                    keep = False
            elif filter_gg[i].islower():  # Gray
                if filter_gg[i].upper() == word[i]:
                    keep = False

        # Yellow filter
        for c in filter_y:
            if c != " " and c not in word.lower():
                keep = False

        if keep:
            temp.add(word)

    return temp


def score_wordlist(wordlist):
    # next , alphabetically and positionally count all the letters of the remaining words
    counts = [Counter() for _ in range(5)]
    for word in wordlist:
        for i in range(5):
            counts[i][word[i]] += 1

    # then, score each word based on those counts, storing the score
    scoredwords = dict()
    for word in wordlist:
        score = 0
        for i in range(5):
            score += counts[i][word[i]]
        scoredwords[word] = score

    return scoredwords


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Wordle Solver",
        description="Attempts to find the best word choice based on nothing in particular",
    )
    """
    If I had to characterize this methodology, I'd call it the "Guess Who?" technique,
    wherein you seek out words that are likely to eliminate the greatest number of
    possibilities in a single pass.  So this approach selects words that tend to have
    some of the most popular/common letters in each position of the word.
    
    Note that this leads to cases where it prefers to start with SALES instead of other
    more popular options, but it's still managed to successfully complete every Wordle
    I've thrown at it so far.
    """
    parser.add_argument("guesses", type=check_word_length, nargs="*")
    args = parser.parse_args()

    wordlist = get_wordlist()

    # Prefilter the wordlist using user-provided green/grey/yellow masks
    for guess in args.guesses:
        mask = "".join([i if i in string.ascii_letters else " " for i in guess])
        wordlist = filter_wordlist(wordlist, mask)

    # Score the words based on some arbitray bullshit
    scoredwords = score_wordlist(wordlist)

    # Output some results
    print(f"{len(wordlist)} words")
    i = 10
    for word in sorted(scoredwords, key=scoredwords.get, reverse=True):
        print(f"{word} {scoredwords[word]}")
        i -= 1
        if i == 0:
            break


# TODO implement a way to select the best word for an arbitrary number of simultaneous wordles (Octordle)
# this is mostly a parsing issue on the frontend, and is just a meta-list issue on the backend

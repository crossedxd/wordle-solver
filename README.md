# wordle-solver

## Prerequisites
This script was originally written to work on Ubuntu, but it should work with Python on other platforms as long as you point get_wordlist() to any dictionary (newline-separated word lists).

## How to Use
This script is used during the solving process, as it works by winnowing down the list of likely and available words as other options are eliminated.

Once you've submitted a starter word*, you can pass that word and the Wordle's feedback into the script in the following way,

  $ python3 wordle.py 'xxxxxyyyyy'

where 'xxxxx' is the starter word with lowercase letters in gray/yellow spaces and uppercase letters in green spaces, and
where 'yyyyy' is the starter word with letters ONLY in yellow spaces.

Here is an example of the script in operation:
- I input 'CRANE' into the puzzle, and get gray/gray/gray/yellow/yellow back.  I invoke the script as follows:
  - $ python3 wordle.py 'crane   ne'
- The script responds with some top options; I try 'MENES', which returns gray/green/yellow/gray/gray.  I then rerun the script like so (adding to the previous inputs):
  - $ python3 wordle.py 'crane   ne' 'mEnes  n  '
- I now try 'RERAN'.  It comes back with gray/green/gray/gray/yellow.
  - $ python3 wordle.py 'crane   ne' 'mEnes  n  ' 'rEran    n'
- 'NEWLY'? Nope, green/green/gray/gray/gray:
  - $ python3 wordle.py 'crane   ne' 'mEnes  n  ' 'rEran    n' 'NEwly     '
- Couple options left, so we try 'NEIGH'.  And that's correct!

So overall, the script just kinda 'works' in a "Guess Who?" sort of fashion.

*the script like SALES, but there are plenty of discussions about that elsewhere

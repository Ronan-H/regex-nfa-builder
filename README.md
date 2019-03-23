
# Regex NFA Builder

## What is this?
This is a Python 3 project that uses [nondeterministic finite automata](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton) to parse [regular expressions](https://en.wikipedia.org/wiki/Regular_expression). It was completed for a 3rd year software development graph theory assignment.

## What are the notable files in the repo and what do they do?
* **main.py:** Main Python file, run this to run the program
* **nfa.py:** Class representing an NFA (not specific to this project, could be used elsewhere)
* **nfa_utils:** Has functions for joining NFAs in varoius ways (ie. concatenate, union,...) and also the recursive function to build an NFA from the given regular expression string. Does most of the hard work of the project.
* **tests.py:** Has test cases for various functions. If all these tests pass, it's a good indication that the project is functioning properly.
* **research.txt:** Contains the research I did to help me with the project, including references, and also just some of my thoughts about how I was planning to tackle certain problems.

## How does it work?
NFAs are represented as objects, in a way that is as close as possible to their mathematical definition (_see nfa.py_).

NFAs are built recursivly using [Thompson's construction](https://en.wikipedia.org/wiki/Thompson%27s_construction).

The regular expression is never converted to postfix notation, it operates on infix notation. No stack is explicitly used either, instead the algorithm uses the call stack.

## How do I run the program?
You need Python 3 to run this project.
Clone the repo and run *python3 main.py* from inside.

## How do I use the program?
Follow the instructions provided when you run the program:

_Set the regular expression by typing regex=(regex here)_

_Example: regex=011010_

_You can give input text to test against that regex by just typing it in by itself._

Also, you can type _exit_ to exit the program.

## What does the output mean?
When you create an NFA using _regex=..._, a breakdown/visualization of the recursive algorithm will be printed as the NFA is built.

The program will report whether or not a given input string is accepted or rejected by the currently set regex when you give it an input string.

It will also report some information on how much time was taken for an NFA to build, or how long it took to check if an input string is accepted or rejected.

## What special symbols are supported?
**Concatenation operation:** . (dot character)

**Union operator:** | (pipe character)

**Kleene star:** * (asterisk)

**One-or-more-of operator:** + (plus)

**Zero-or-one-of operator:** ? (question mark)

## What order of precedence do those operations follow?
**Order:** ? + * . |

Left to right, where '?' is done first, and '|' is done last.

## What alphabet symbols are supported?
Anything that isn't recognized as a special character.

Internally, there are no preset alphabet characters. They are based on whatever input you give it.

## Examples?
**p.y.t.h.o.n** or **python** - Matches only the word "python"

**python|java|C#** - Matches any one of "python", "java" or "C#"

**o+k then** or **o\*ok then** - Matches "ok then", "ooook then", "ooooooook then", etc...

**c?loud** - Matches "cloud" and "loud"

**H?A?h?a?*!\*|H?E?h?e?\*!\*** - Accepts a wide range of laughs, including "Ha", "heh", "Haha", and "AAAAAAAAAAHAHAHAHAHA!!"

## How do I run the test cases?
_python3 -m unittest discover ._ seems to work, although I've been running the tests from within Pycharm.

## Why didn't you use postfix notation, or store NFAs on a stack etc?
It's probably a better idea but I had more fun figuring it out on my own.

The main drawback of my approach seems to be that adding support for parenthesis would be very messy and difficult.

# CS50’s Introduction to Programming with Python

This repository contains code created for "[CS50’s Introduction to Programming with Python](https://cs50.harvard.edu/python/2022/)" course by Harvard Open OpenCourseWare. The course consists of nine problem sets with 4-5 pre-defined tasks in each, and a final project of the students' choosing. The following chapters describes the topic of each problem set and details assignments in it. Documentation on the final project can be found [here](https://github.com/VikSil/CS50Python/tree/trunk/final_project).

## Problem Set 0 - Functions, Variables

* [Indoor Voice](https://cs50.harvard.edu/python/2022/psets/0/indoor/) - program prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespaces are output unchanged.
* [Playback Speed](https://cs50.harvard.edu/python/2022/psets/0/playback/) - program prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).
* [Making Face](https://cs50.harvard.edu/python/2022/psets/0/faces/) - program implements a function called `convert` that accepts a `str` as input and returns that same input with any `:)` converted to 🙂 (otherwise known as a slightly smiling face) and any `:(` converted to 🙁 (otherwise known as a slightly frowning face). All other text is returned unchanged.
* [Einstein](https://cs50.harvard.edu/python/2022/psets/0/einstein/) - program prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. 
* [Tip Calculator](https://cs50.harvard.edu/python/2022/psets/0/tip/) - program implements two functions: `dollars_to_float`, which accepts a `str` as input (formatted as `$##.##`, wherein each `#` is a decimal digit), removes the leading `$`, and returns the amount as a `float`, and `percent_to_float`, which accepts a `str` as input (formatted as `##%`, wherein each `#` is a decimal digit), removes the trailing `%`, and returns the percentage as a float.

## Problem Set 1 - Conditionals

* [Deep Thought](https://cs50.harvard.edu/python/2022/psets/1/deep/) - program prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting `Yes` if the user inputs `42` or (case-insensitively) `forty-two` or `forty two`. Otherwise the output is `No`.
* [Bank](https://cs50.harvard.edu/python/2022/psets/1/bank/) - program prompts the user for a greeting. If the greeting starts with “hello”, the progam outputs `$0`. If the greeting starts with an “h” (but not “hello”), output is `$20`. Otherwise, output is `$100`. User's greeting is treated case-insenitevely and any leading whitespace in the user’s greeting are ignored.
* [File Extensions](https://cs50.harvard.edu/python/2022/psets/1/extensions/) - program prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes: `.gif`, `.jpg`, `.jpeg`, `.png`, `.pdf`, `.txt`, `.zip`
* [Math Interpreter](https://cs50.harvard.edu/python/2022/psets/1/interpreter/) - program prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. It assumes that the user’s input will be formatted as `x y z`, with one space between `x` and `y` and one space between `y` and `z`, wherein: `x` is an integer, `y` is `+`, `-`, `*`, or `/` and `z` is an integer.
* [Meal Time](https://cs50.harvard.edu/python/2022/psets/1/meal/) - program prompts the user for a time and outputs whether it’s `breakfast time`, `lunch time`, or `dinner time`. If it’s not time for a meal, it does not output anything at all. It assumes that the user’s input will be formatted in 24-hour time as `#:##` or `##:##`. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

## Problem Set 2 - Loops

* [camelCase](https://cs50.harvard.edu/python/2022/psets/2/camel/) - program prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. It assumes that the user’s input will indeed be in camel case.
* [Coke Machine](https://cs50.harvard.edu/python/2022/psets/2/coke/) -  program prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has input at least 50 cents, it outputs how many cents in change the user is owed. It assumes that the user will only input integers, and ignores any integer that isn’t an accepted denomination of 5, 10 or 25 cents.
* [Just setting up my twttr](https://cs50.harvard.edu/python/2022/psets/2/twttr/) - program prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether input in uppercase or lowercase.
* [Vanity Plates](https://cs50.harvard.edu/python/2022/psets/2/plates/) - program prompts the user for a vanity plate and then outputs `Valid` if the plate meets the following requirements:

     * All vanity plates must start with at least two letters.
     * Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
     * Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.
     * No periods, spaces, or punctuation marks are allowed.

     Otherwise program outputs `Invalid`. It assumes that any letters in the user’s input will be uppercase.
* [Nutrition Facts](https://cs50.harvard.edu/python/2022/psets/2/nutrition/) - program prompts users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s recommendations for fruits. It ignores any input that isn’t a fruit.

## Problem Set 3 - Exceptions

* [Fuel Gauge](https://cs50.harvard.edu/python/2022/psets/3/fuel/) - program prompts the user for a fraction, formatted as `X/Y`, wherein each of `X` and `Y` is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, it outputs `E` instead to indicate that the tank is essentially empty. And if 99% or more remains, it outputs `F` instead to indicate that the tank is essentially full. If, though, `X` or `Y` is not an integer, `X` is greater than `Y`, or `Y` is `0`, th eprogram prompts the user again. 
* [Felipe’s Taqueria](https://cs50.harvard.edu/python/2022/psets/3/taqueria/) -  program enables a user to place an order, prompting them for food items, one per line, until the user inputs control-d. After each  item, it displays the total cost of all items input thus far, prefixed with a dollar sign ($) and formatted to two decimal places. User’s input is treated case insensitively. Any input that isn’t an item is ignored.
* [Grocery List](https://cs50.harvard.edu/python/2022/psets/3/grocery/) - program prompts the user for items, one per line, until the user inputs control-d. Then it outputs the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user input that item. User’s input is treated case insensitively and items are not pluralised.
* [Outdated](https://cs50.harvard.edu/python/2022/psets/3/outdated/) - program prompts the user for a date, anno Domini, in month-day-year order, formatted like `9/8/1636` or `September 8`, 1636, and then outputs the same data in `YYYY-MM-DD` format. If the user’s input is not a valid date in either format, the program prompts the user again. The program assumes that every month has 31 days.

## Problem Set 4 - Libraries

* [Emojize](https://cs50.harvard.edu/python/2022/psets/4/emojize/) -  program prompts the user for a str in English and then outputs the “emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji.
* [Frank, Ian and Glen’s Letters](https://cs50.harvard.edu/python/2022/psets/4/figlet/) - program transforms input text into ascii art. It expects zero or two command-line arguments:

    * Zero if the user would like to output text in a random font.
    * Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
    
    It then prompts the user for a `str` of text and outputs that text in the desired font.

* [Adieu, Adieu](https://cs50.harvard.edu/python/2022/psets/4/adieu/) - program prompts the user for names, one per line, until the user inputs control-d. It assumes that the user will input at least one name. It then bids adieu to those names, using `and` to separate the last two names, and a comma to separate all other names, for example:  `Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl`.
* [Guessing Game](https://cs50.harvard.edu/python/2022/psets/4/game/) - program prompts the user for a level n. 

    * If the user does not input a positive integer, the program prompts again.
    * If the level is a positive number, it randomly generates an integer between 1 and n, inclusive, using the random module.

    The program then prompts the user to guess that integer and outputs `Too small!`, `Too large!` or `Just right!` until the user successfully guesses the random number.

* [Little Professor](https://cs50.harvard.edu/python/2022/psets/4/professor/) - program emulates the children educational game-tool called "Little Professor". It generates ten simple maths problems for the user and keeps score of how many of the problems the user has solved correctly. After the user inputs the answer to the last problem, the problem outputs the score: number of correct answers out of 10.
* [Bitcoin Price Index](https://cs50.harvard.edu/python/2022/psets/4/bitcoin/) - program expects the user to specify as a command-line argument the number of Bitcoins `n` that they would like to buy. If that argument cannot be converted to a `float`, the program exits with an error message. Given a correct input value, the program 1ueries the API for the CoinDesk Bitcoin Price Index at `https://api.coindesk.com/v1/bpi/currentprice.json` and outputs the current cost of `n` Bitcoins in USD to four decimal places, using `,` as a thousands separator.

## Problem Set 5 - Unit Tests

* [Testing my twttr](https://cs50.harvard.edu/python/2022/psets/5/test_twttr/) - the program implements tests for "Just setting up my twttr" program from Problem Set 2.
* [Back to the Bank](https://cs50.harvard.edu/python/2022/psets/5/test_bank/) - the program implements tests for "Bank" program from Problem Set 1.
* [Re-requesting a Vanity Plate](https://cs50.harvard.edu/python/2022/psets/5/test_plates/) - the program implements tests for "Vanity Plates" program from Problem Set 2.
* [Refueling](https://cs50.harvard.edu/python/2022/psets/5/test_fuel/) - the program implements tests for "Fuel Gauge" program from Problem Set 3.

## Problem Set 6 - File I/O

* [Lines of Code](https://cs50.harvard.edu/python/2022/psets/6/lines/) - program expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines.
* [Pizza Py](https://cs50.harvard.edu/python/2022/psets/6/pizza/) - program  expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate.
* [Scourgify](https://cs50.harvard.edu/python/2022/psets/6/scourgify/) - program  expects the user to provide two command-line arguments:

    * the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house.
    * the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.

The program converts that input to that output, splitting each name into a first name and last name. 

* [CS50 P-Shirt](https://cs50.harvard.edu/python/2022/psets/6/shirt/) -  program expects two command-line arguments:
    * the name (or path) of a JPEG or PNG to read (i.e., open) as input.
    * the name (or path) of a JPEG or PNG to write (i.e., save) as output.

The program then overlays [shirt.png](https://cs50.harvard.edu/python/2022/psets/6/shirt/shirt.png) (which has a transparent background) on the input after resizing and cropping the input to be the same size, saving the result as its output.

## Problem Set 7 - Regular Expressions

* [NUMB3RS](https://cs50.harvard.edu/python/2022/psets/7/numb3rs/) - program implements a function that expects an IPv4 address as input as a str and then returns True or False, respectively, if that input is a valid IPv4 address or not.
* [Watch on YouTube](https://cs50.harvard.edu/python/2022/psets/7/watch/) - program implements a function that expects a `str` of HTML as input, extracts any YouTube URL that’s the value of a `src` attribute of an `iframe` element therein, and returns its shorter, shareable `youtu.be` equivalent as a `str`.
* [Working 9 to 5](https://cs50.harvard.edu/python/2022/psets/7/working/) - program implements a function that expects a `str` in either of the following 12-hour formats: `9:00 AM to 5:00 PM` or `9 AM to 5 PM`. It returns the corresponding str in 24-hour format (i.e., `9:00 to 17:00`).
* [Regular, um, Expressions](https://cs50.harvard.edu/python/2022/psets/7/um/) - program implements a function that expects a line of text as input as a `str` and returns, as an `int`, the number of times that “um” appears in that text, case-insensitively, as a word unto itself, not as a substring of some other word. For instance, given text like `hello, um, world`, the function should return `1`. Given text like `yummy`, though, the function should return `0`.
* [Response Validation](https://cs50.harvard.edu/python/2022/psets/7/response/) - program prompts the user for an email address via input and then prints `Valid` or `Invalid`, respectively, if the input is a syntatically valid email address or not.

## Problem Set 8 - Object Oriented Programming

* [Seasons of Love](https://cs50.harvard.edu/python/2022/psets/8/seasons/) - program prompts the user for their date of birth in `YYYY-MM-DD` format and then prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals, without any `and` between words. Since a user might not know the time at which they were born, the program assumes, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date and that the current time is also midnight.
* [Cookie Jar](https://cs50.harvard.edu/python/2022/psets/8/jar/) - program implements a class called Jar with these methods:
    * `__init__` initializes a cookie jar with the given `capacity`, which represents the maximum number of cookies that can fit in the cookie jar. If `capacity` is not a non-negative `int`, though, `__init__`  raises a ValueError.
    * `__str__` returns a str with `n` 🍪, where `n` is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, it returns "🍪🍪🍪"
    * `deposit` adds `n` cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, deposit raises a `ValueError`.
    * `withdraw` removes `n` cookies from the cookie jar. If there aren’t that many cookies in the cookie jar, `withdraw` raises a ValueError.
    * `capacity` returns the cookie jar’s capacity.
    * `size` returns the number of cookies actually in the cookie jar, initially `0`.
* [CS50 Shirtificate](https://cs50.harvard.edu/python/2022/psets/8/shirtificate/) - program prompts the user for their name and outputs, using [fpdf2](https://pypi.org/project/fpdf2/), a CS50 shirtificate in a file called `shirtificate.pdf` similar to [this one for John Harvard](https://cs50.harvard.edu/python/2022/psets/8/shirtificate/jharvard.pdf).

## Final Project

Final project is stored separately from the problem sets and a separate README file is available [here](https://github.com/VikSil/CS50Python/tree/trunk/final_project).  




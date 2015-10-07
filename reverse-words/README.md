reverse-words
=========================

Description
----------------------

This directory contains a C++ source file and a corresponding makefile:

* **reverse-words.cc** - the source code to reverse the order of the words in
a string while still allowing individual words to be read normally

This code was developed and tested on Linux using GNU tools. Your mileage may
vary on other platforms.


Requirements
----------------------

Given a string, reverse the words, so that the last word becomes the 
first word, but each word still reads normally.

**INPUTS:**

* A string containing words separated by a single space

**OUTPUT:**

* A string with the order of the words reversed, but each word is
still readable normally.

**CONSTRAINTS:**

Do not use large amounts of extra storage.  Very limited local scope
variables are OK, but you can't do things like buffer up chunks
of the string or allocate a new list of the words for reversal.

**EXAMPLE:**

    "The pen is red" becomes "red is pen The"

Building and Execution
----------------------

Assuming that you have the appropriate GNU tools installed, set your
working directory to this project's source directory and type the following
at the terminal prompt:

    make
    reverse-words

Alternatively, you can compile link and execute the program by typing the
the following at the terminal prompt:

    ../tools/gg reverse-words.cc

Support
----------------------

If you have any questions, problems, or suggestions, please submit an
[issue](../../issues)

Copyright and License
----------------------

Copyright 2015 Dean Stevens

Licensed under the MIT License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://opensource.org/licenses/MIT

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

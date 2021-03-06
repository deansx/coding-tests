coding-tests
=========================

Introduction / Description
----------------------

Over the years, we've all been subjected to (or subjected others to) the
dreaded "coding test".  Since I have a bunch of these laying around, I decided
to throw them up on GitHub so that others could laugh at my feeble attempts.

Each of the sub-directories in this repo contains a solution, or group of 
solutions to a coding problem that was presented in a real interview.

Tests
----------------------
* [replace-words](./replace-words) - write a program that takes groups of
words that each map
to a specific replacement word. Then process a sentence replacing words in
the sentence that match a word in one of the groups with the corresponding
mapped word.  Also include documentation and tests.  I did this one in both
[C++](./replace-words/cpp) and [Python](./replace-words/python) for the test.
Both results are included. I later added a [Rust](./replace-words/rust)
implementation just for fun

* [reverse-words](./reverse-words) - given a string, reverse the words, so
that the last word becomes the first word, but each word still reads normally.
I used C++ for this one.

* [display-tree-by-level](./display-tree-by-level) - given a tree data
structure, print the tree one level at a time, without using extensive
secondary storage. The implementation uses Python

* [parse-dict-file](./parse-dict-file) - Parse a data file provided as part of
the test and then extract specified data from the resulting collection.

* more coming soon

Support
----------------------

If you have any questions, problems, or suggestions, please submit an
[issue](../../issues)

License & Copyright
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


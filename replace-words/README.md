replace-words/
=========================

Description
----------------------
This is a straightforward coding exercise. The sub directories
[Python](./Python/) and [C++](./cpp/) contain sample implementations in their
respective languages

Requirements
----------------------

Create two (2) objects with accompanying documentation and test cases.

* **List_Object** - holds one or more groups of words. The object must support
mapping each group of words to a single string.  For example: {"Bob", "Carol",
"Ted", "Alice"} => NAME

* **Mapped_Sentence_Object** - given an input string containing at least one
word, with each component word separated by a single space as input, this
object must convert the input string to all lower case and then generate
four (4) new strings:

1. The original input string
2. A string containing a space separated list of the words from the input
string that were recognized (tagged) by the List_Object
3. A string containing a space separated list of the words from the input
string that were NOT recognized by the List_Object
4. A new version of the original input string with all of the recognized words
replaced with the corresponding mapped strings from the List_Ojbect

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
parse.py
=========================

Description
----------------------

This directory contains a Python source file and a test data file:

* **parse.py** - the main python code to implement this test
* **testdata.txt** - data file provided for this test. *As per the
written instructions, this data file must not be modified
in any way*

If a Python interpreter is installed, parse.py can be run on the linux
command line.  Note that line endings are linux style, which might cause
a problem in Windows.

This code was developed using Python3 and tested on Linux using GNU tools.
Due to an unwritten requirement, it was also tested on Python2.7. Your 
mileage may vary on other platforms.


Discussion
----------------------
I fixed a few of the potentially misleading typos that I found in the
original instructions. I wasn't sure
whether the typos were just there to see if I was paying attention, but...

The email that accompanied this seemed to suggest that they wanted me to write
a parser. This seemed like a waste of effort, since the sample data was
easily parsed using
[ast.literal_eval()](https://docs.python.org/2/library/ast.html).
With the time constraints of the test in mind, I used the library function,
so this isn't the place
to see how to write a JSON parser in Python, although I'm not sure why you'd 
[want to do that](https://docs.python.org/2/library/json.html).


# Instructions:
----------------------

Write a program (parse.py) in python that will parse the given testdata.txt.

**Do not change testdata.txt under any circumstance.**

Provide all source code and workspaces.

Usage from command line should be the following:

    python parse.py testdata.txt

## Output of the program should be the following:

A list of all organs with a "central" attribute

    [“heart", "liver", "stomach", "intestine", "esophagus”]

A dictionary of key-value pair of all the "things in my head”

    {"childhood memories": 500, "adolescent memories": 150, "forgotten memories": 6640, "new memories": 13}

An ordered (by alpha) sort of all items at the upper level

    "box1": {"item1": "this is the first item in box 1", "item2": "this is the second item in box 1"}
    "container": "container key says 'hi'"
    "item type": "brain"
    "memory counter": "000000"
    "organCounter": "0x1E"
    "organs": [{"heart": "central", "lifeCycleState": 1}, {"filter": "True", "liver": "central", "lifeCycleState": 2, "cellCount": "0xDEADBEEF", "bloodType": "A-", "source": "chicken"}, {"stomach": "central", "lifeCycleState": 2}, {"digestive": "True", "intestine": "central", "lifeCycleState": 2, "full": "False", "length": "0x15", "content": None}, {"esophagus": "central", "lifeCycleState": 7}, {"filter": "True", "kidney": "left", "lifeCycleState": 2, "cellCount": "0xFACEFACE", "bloodType": "A-", "source": "chicken"}, {"filter": "True", "kidney": "right", "lifeCycleState": 2, "cellCount": "0xFACEFACE", "bloodType": "A-", "source": "chicken"}, {"optic": "True", "eye": "left", "lifeCycleState": 1, "functional": "True", "used": "True", "blind": "False”}]
    "things in my head": {"childhood memories": 500, "adolescent memories": 150, "forgotten memories": 6640, "new memories": 13}
    "versionNumber": [48]

Execution
----------------------

As specified in the Instructions section, you can run the script (assuming that
you have an appropriate Python interpreter installed) as:

    python parse.py testdata.txt

You should also be able to run it directly in the console as:

    parse.py testdata.txt

Support
----------------------

If you have any questions, problems, or suggestions, please submit an
[issue](../../../issues)

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

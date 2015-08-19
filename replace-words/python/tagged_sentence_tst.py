#!/usr/bin/env python
"""tagged_sentence_tst.py is the executable module for the testing the
   TaggedSentence class for replace-words coding test.
   
   This module creates a TaggedSentence instance, and feeds it a test
   sentence.  The tag sets are pre-defined for the object, tag sets are
   tested separately by another test script.  The results are compared with
   expected values for pass/fail determination.

   Prints a Pass/Fail summary


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
  
    CODER:   Dean Stevens
    STATUS:  Sample
    VERSION: 0.1
"""
# Note: symbolic link so we can treat replace-words as a module
from replace_words import *


if __name__ == '__main__':
    p = 0
    f = 0
    ts = TaggedSentence()
    ors = "This is Jill she has fOUr or FivE dogs and THREE cats or more cats"
    ts.orig_sentence = ors

    # compare a string against a reference, prints OK, if they're equal and
    # increments the pass counter.  Otherwise prings FAIL and increments the
    # fail counter.
    def cmp_val(s1, ref):
        global p
        global f
        if s1 == ref:
            print("OK: {0}".format(s1))
            p+= 1
        else:
            print("FAIL: {0} != {1}".format(ref, s1))
            f+=1
    
    # Check values in the object
    cmp_val(ts.orig_sentence, ors)
    cmp_val(ts.tagged, "jill four five three")
    cmp_val(ts.untagged, "this is she has or dogs and cats or more cats");
    cmp_val(ts.classtagged, 
          "this is NAME she has NUM or NUM dogs and NUM cats or more cats");

    print("Passed: {0}\nFailed: {1}".format(p,f))
    

#!/usr/bin/env python
"""wordmap_tst.py is the executable module for the testing the
    MapList and WordMap classes for replace-words coding test.
   
    This module creates a MapList instance, and populates it with test WordMap
    objects.  Then, the new MapList/WordMap(s) combination is tested both for
    checking the "taggedness" of objects, and also to ensure that the WordMap
    sets and mapped_word match what was expected.

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

def TstMapList():
    """TstMapList is a utility function to populate the MapList with the
       data for this evaluation
    """
    # Tests adding information to the WordMap and MapList objects
    ml = MapList()
    nam = WordMap()
    nam.mapped_word = "WIERD"
    nam.add_to_set(["foo", "bar"])
    ml.maps_.append(nam);
    num = WordMap()
    num.mapped_word = "FOOD"
    num.add_to_set(["fries", "cheese", "milk", "bread", "pizza", "beer", 
                    "meat"])
    ml.maps_.append(num);
    return ml

if __name__ == '__main__':
    p = 0
    f = 0
    ml = TstMapList()

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
    
    # Check the mapped words
    cmp_val(ml.maps_[0].mapped_word, "WIERD")
    cmp_val(ml.maps_[1].mapped_word, "FOOD")

    # Check the sets
    w_ref = "bar foo"
    f_ref = "beer bread cheese fries meat milk pizza"
    l = list(ml.maps_[0].words_)
    l.sort()
    cmp_val(' '.join(l), w_ref)
    l = list(ml.maps_[1].words_)
    l.sort()
    cmp_val(' '.join(l), f_ref)

    # Tries to use the MapList.tagged() member to look up words that
    # might be tagged.  If the word is tagged, the corresponding mapped
    # word will be returned.  Otherwise, and empty string is returned.
    # This function can test successfully both for a word that should be
    # tagged and one that shouldn't (ref == "") 
    def fnd_tst(word, ref):
        global p
        global f
        if ml.tagged(word) == ref:
            print("Correct look-up for \"{0}\"".format(word))
            p+=1
        else:
            print("Incorrect look-up for \"{0}\"".format(word))
            f+=1
    # Test a group of words, some will show as tagged, some not.
    fnd_tst("foo", "WIERD")
    fnd_tst("zing", "")
    fnd_tst("pizza", "FOOD")
    fnd_tst("sandwich", "")

    print("Passed: {0}\nFailed: {1}".format(p,f))
    

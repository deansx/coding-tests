#!/usr/bin/env python
"""replace-words.py is the main executable module for the coding test that
demonstrates simple minded tokenization and some simple data structures.

    Process a given sentence into single "word" tokens that can be checked
        against a list of many-to-one word maps to see whether any words in
        the sentence  map to a "replacement" mapped word.
     
    Supports:
       - Returning the original input sentence
       - Returning a string containing the "untagged" words
       - Returning a string containing the "tagged" words
       - Returning a sentence with the "tagged" words replaced by their mapped
         values


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
"""

__author__ = "Dean Stevens"
__status__ = "Sample"
__version__ = "0.1.0"


class WordMap(object):
    """WordMap manages a set of words that "map" to a specified word.
       Supports:
        - adding new words to the match set
        - searching for a word in the match set,
        - producing the mapped word
    """
    def __init__(self):
        self.words_ = set()
        self.mapped_word_ = ""
    
    # See whether the specified "word" is in this map's set.
    # Returns true if the given word is present.  false otherwise
    def find_word(self, word):
        return word in self.words_
    # Add another word to the set of words that are the basis of this object
    def add_to_set(self, wordlst):
        for ele in wordlst:
            self.words_.add(ele)
    
    # The word "mapped to" by the set in this object
    @property
    def mapped_word(self):
        return self.mapped_word_
    @mapped_word.setter
    def mapped_word(self, mword):
        self.mapped_word_ = mword

class MapList(object):
    """MapList manages an arbitrary list of WordMaps and supports searching
       all of the managed maps for a specified word.
       Supports:
          - searching all of the lists for a specified word, and then returning
            the mapped word for the successful set.
    """
    def __init__(self):
        self.maps_ = [];

    # Search the managed maps to see if the specified word maps to any of
    #   the "tagged words"
    # Returns the mapped word, if it finds a match.  Otherwise returns an
    #   empty string. This lets us directly make the substitution for the
    #   class tagged case.
    def tagged(self, word):
        # initialize the return value
        retval = ""
        # iterate through the maps, looking for the specified word, if it's
        # found, set retval to the mapped word and break the search
        for amap in self.maps_:
            if amap.find_word(word):
                retval = amap.mapped_word
                break
        return retval

def MakeMapList():
    """MakeMapList is a utility function to populate the MapList with the
       data for this evaluation
    """

    ml = MapList()
    nam = WordMap()
    nam.mapped_word = "NAME"
    nam.add_to_set(["jack", "jill"])
    ml.maps_.append(nam);
    num = WordMap()
    num.mapped_word = "NUM"
    num.add_to_set(["one", "two", "three", "four", "five", "six", 
                    "seven", "eight", "nine"])
    ml.maps_.append(num);
    return ml

class TaggedSentence(object):
    """TaggedSentence processes a given sentence into single "word" tokens
       that can be checked against a list of objects to see whether any words
        map to a "replacement" mapped word.
        Supports:
          - Returning the original input sentence
          - Returning a string containing the "untagged" words
          - Returning a string containing the "tagged" words
          - Returning a sentence with the "tagged" words replaced by their
            mapped values
    """
    def __init__(self):
        self.orig_sentence_ = ""
        self.tokens_ = []
        self.tagged_ = []
        self.untagged_ = []
        self.classtagged_ = ""
        self._x = None
        self.maplist_ = MakeMapList()
    
    # The original sentence
    @property
    def orig_sentence(self):
        return self.orig_sentence_
    
    # When the orig_sentence is set, the evaluation progresses
    @orig_sentence.setter
    def orig_sentence(self, sentence):
        self.orig_sentence_ = sentence
        # convert the phrase to lower case, and split it into individual
        # words at the spaces
        self.tokens_ = sentence.lower().split(' ')
        # temporary list to hold the Class Tag words
        cls_tag_tmp = []
        
        # Empty the lists, in case this object is being reused
        del self.tagged_[:]
        del self.untagged_[:]
        
        # Iterate through the list of words from the original sentence.
        # If a given word was tagged, add it to the "tagged" list and
        #    replace it with the "mapped" word in the Class Tag list.
        # If the word was not tagged, add it to the untagged list and place
        #    it directly into the Class Tag list.
        
        for word in self.tokens_:
            tagged = self.maplist_.tagged(word)
            if tagged:
                self.tagged_.append(word)
                cls_tag_tmp.append(tagged)
            else:
                self.untagged_.append(word)
                cls_tag_tmp.append(word)

        # Produce the Class Tagged string by joining the words, now
        self.classtagged_ = ' '.join(cls_tag_tmp)
    
    @property
    def tagged(self):
        # Produce the string containing the tagged words by joining the list
        #   elements.
        return ' '.join(self.tagged_)
    
    @property
    def untagged(self):
        # Produce the string containing the tagged words by joining the list
        #   elements.
        return ' '.join(self.untagged_)
    
    @property
    def classtagged(self):
        return self.classtagged_


if __name__ == '__main__':
    ts = TaggedSentence()
    ts.orig_sentence = "I'm Jack and I'm three years old"
    print("Original phrase: {0}".format(ts.orig_sentence))
    print("Untagged words   {0}".format(ts.untagged))
    print("Tagged words:    {0}".format(ts.tagged))
    print("Class Tagged:    {0}".format(ts.classtagged))
    

/*****************************************************************************
*   DESCRIPTION:
*     Create a system that can map a specified set of words to a given word.
*     This system is then applied to a sentence to generate a new sentence
*     with each of the listed words replaced by the word that they're mapped
*     to.
*     
*     INPUTS:
*       > A string containing one or more words, each separated by a single
*         blank space
*       > One or more lists of words where each list will map to a specified
*         replacement word
*         Examples:
*           {jack, jill} => NAME - both "jack" and "jill" map to "NAME"
*           {one, two, three, …, nine} => NUM - the words representing
*                                                  integers one through nine
*                                                  map to "NUM"
*     
*     OUTPUT:
*       > Original string
*       > string containing the words from the original that were not mapped
*       > string containing the words from the original that were mapped
*       > string containing a new sentence with the tagged words replaced by
*         their respective mapped words.
* 
*     TESTS:
*       > A set of self tests is included in the main() block.
*
*   Copyright 2015 Dean Stevens
*
*   Licensed under the MIT License (the "License");
*   you may not use this file except in compliance with the License.
*   You may obtain a copy of the License at
*   
*       http://opensource.org/licenses/MIT
*   
*   Unless required by applicable law or agreed to in writing, software
*   distributed under the License is distributed on an "AS IS" BASIS,
*   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
*   See the License for the specific language governing permissions and
*   limitations under the License.
* 
*   CODER:   Dean Stevens
*   STATUS:  Sample
*   VERSION: 0.1
*
*****************************************************************************/

#include <cstdlib>
#include <string>
#include <iostream>
#include <unordered_set>
#include <list>
#include <sstream>
#include <vector>
#include <iterator>
#include <locale>

//
// WordMap manages a set of words that "map" to a specified word.
// Supports:
//   - adding new words to the match set
//   - searching for a word in the match set,
//   - producing the mapped word
//
class WordMap {
  
 public:
  WordMap(std::string mapped_word) : mapped_word_(mapped_word) {}

  // Return the word mapped by this object
  std::string get_mapped_word() { return mapped_word_; }

  // Add another word to the set of words that are the basis of this object
  void add_to_set(const std::string new_word) {
    words_.insert(new_word);
  }

  // Dump the state of this object
  void dump() {
    std::cout << "WordMap for " << mapped_word_ << ":\n";
    for (auto wd : words_) {
      std::cout << wd << std::endl;
    }
  }

  // See whether the specified "word" is in this map's set.
  // Returns true if the given word is present.  false otherwise
  bool find_word(std::string word) {
    return (words_.count(word) > 0)? true : false;
  }

  // Returns the word that this object maps to
  std::string mapped_word() {
    return mapped_word_;
  }

 private:
  // Set of words recognized by this object.
  std::unordered_set<std::string> words_;
  // Word mapped to by this object
  std::string mapped_word_;

};

//
// SetList manages an arbitrary list of WordMaps and supports searching
//   all of the managed maps for a specified word.
// Supports:
//   - searching all of the lists for a specified word, and then returning
//     the mapped word for the successful set.
//
class SetList {
 public:
  SetList() {
    // For this exercise, hard coded the data.  Could easily be
    //   extended by adding other input methods.  If done, will need
    //   to ensure that the same word isn't added to multiple maps.
    //   Set functionality ensures that only one occurrence of each word
    //   will be present.
    WordMap name("NAME");
    name.add_to_set("jack");
    name.add_to_set("jill");
    maps_.push_back(name);
    WordMap num("NUM");
    num.add_to_set("one");
    num.add_to_set("two");
    num.add_to_set("three");
    num.add_to_set("four");
    num.add_to_set("five");
    num.add_to_set("six");
    num.add_to_set("seven");
    num.add_to_set("eight");
    num.add_to_set("nine");
    maps_.push_back(num);
  }
 
  // Search the managed maps to see if the specified word maps to any of
  //   the "tagged words"
  // Returns the mapped word, if it finds a match.  Otherwise returns an
  //   empty string. This lets us directly make the substitution for the
  //   class tagged case.
  std::string tagged(std::string word) {
    // initialize the empty string, will be returned if we don't find
    //   anything
    std::string temp;
    // iterate through the maps and look for the specified word in each
    //   map
    for (auto &map :  maps_ ) {
      if (map.find_word(word)) {
        // the set contained the word, return the "mapped" word.
        temp = map.mapped_word();
      }
    }
    return temp;
  }

 private:
    std::list<WordMap> maps_;
};

//
// Process a given sentence into single "word" tokens that can be checked
//   against a list of objects to see whether any words map to a "replacement"
//   mapped word.
// Supports:
//   - Returning the original input sentence
//   - Returning a string containing the "untagged" words
//   - Returning a string containing the "tagged" words
//   - Returning a sentence with the "tagged" words replaced by their mapped
//     values

class TaggedSentence {
 public:
  // The constructor takes the original sentence, converts it to lowercase
  //   in a locale friendly way, and then tokenizes it.
  TaggedSentence(std::string original_sentence) : 
                 original_sentence_(original_sentence) {

    // Take care of the conversion to lowercase
    std::locale loc;
    std::string::size_type len = original_sentence.length();
    char v[len+1];
    for (std::string::size_type i=0; i<len; ++i) {
      v[i] = std::tolower(original_sentence[i], loc);
    }
    v[len] = '\0';

    // Tokenize the input string. istringstream will work, since ' ' is the
    // only token separator.
    std::istringstream iss(v);
    // Initialize with an initializer_list and move the resulting vector to
    // this object's member variable
    tokens_ = {std::istream_iterator<std::string>{iss}, 
               std::istream_iterator<std::string>{}};
  }

  // Returns the original input stream
  std::string original() {
    return original_sentence_;
  }

  // NOTE:  I considered cacheing each of these results in member variables
  //        and adding a process() member function, but I did it this way
  //        in the interest of trying to hit the 2 hour window.

  // Returns a string containing the words that were not tagged
  std::string untagged() {
    std::string tmpstr;
    // iterate through the tokens, checking to see if each word is tagged.
    //   if it's not tagged, add it to the return string.
    for (auto &t : tokens_) {
      std::string s = set_list_.tagged(t);
      if (s.length() == 0) {
        tmpstr.append(t);
        tmpstr.append(" ");
      }
    }
    return tmpstr;
  }

  // Returns a string containing the words that were tagged
  std::string tagged() {
    std::string tmpstr;
    // iterate through the tokens, checking to see if each word is tagged.
    //   if it is tagged, add it to the return string.
    for (auto &t : tokens_) {
      std::string s = set_list_.tagged(t);
      if (s.length() != 0) {
        tmpstr.append(t);
        tmpstr.append(" ");
      }
    }
    return tmpstr;
  }

  // Returns a string containing a variation of the original sentence that
  //   has each of the tagged words replaced by their mapped value.
  std::string class_tagged() {
    std::string tmpstr;
    // iterate through the tokens, checking to see if each word is tagged.
    //   if it is tagged, then add the respective mapped word to the
    //     return string.
    //   if it is not tagged, then add it directly to the return string.
    for (auto &t : tokens_) {
      std::string s = set_list_.tagged(t);
      if (s.length() != 0) {
        // It is tagged, add the mapped word.
        tmpstr.append(s);
      } else {
        // It's not tagged, add the original word
        tmpstr.append(t);
      }
      tmpstr.append(" ");
    }
    return tmpstr;
  }

  void dump() {
    std::cout << "Original sentence: " << original_sentence_ << std::endl;
    for (auto &t : tokens_) {
      std::cout << t << " | ";
    }
    std::cout << std::endl;
  }

 private:
  std::string original_sentence_;
  std::vector<std::string> tokens_;
  SetList set_list_; 

};

// Helper functions to run tests on the wordmap object

// Returns true if the specified word is in the set for the specified object
//   false otherwise
bool find_word(WordMap &wm, std::string word) {
  bool retval = false;
  if (wm.find_word(word)) {
    std::cout << "\"" << word << "\" is in WordMap \"" << wm.get_mapped_word()
              << "\"\n";
    retval = true;
  } else {
    std::cout << "\"" << word << "\" is NOT in WordMap \""
              << wm.get_mapped_word() << "\"\n";    
  }
  return retval;
}

// Returns pass and fail counts
void test_word(WordMap &wm, std::string word, bool should_it,
               int &pass, int &fail) {

  if (find_word(wm, word) == should_it) {
    pass++;
  } else {
    fail++;
  }
}

// Tests the WordMap object.  Returns pass/fail counts
void test_wordmap(int &p, int &f) {

  p = 0;
  f = 0;
  WordMap wm("FOO");
  wm.add_to_set("bar");
  wm.add_to_set("zing");
  wm.add_to_set("zap");
  wm.dump();
  test_word(wm, "bar", true, p, f);
  test_word(wm, "tang", false, p, f);
  test_word(wm, "zing", true, p, f);
  test_word(wm, "zap", true, p, f);

  std::cout << "WordMap Results:  Pass: " << p << "; Fail: " << f << std::endl;
}

// Compares strings generated by the test TaggedSentence object,
//   Returns pass/fail counts
void test_tagged(std::string ref, std::string tst, int &pass, int &fail) {
  if (ref.compare(tst) == 0) {
    std::cout << ref <<": PASSED\n";
    pass++;
  } else {
    std::cout << ref << "!=\n" << tst << ": FAILED\n";
    fail++;
  }
}

// Tests the TaggedSentence object. Returns pass/fail counts.
void test_tagged_sentence(int &p, int &f) {
  p = 0;
  f = 0;
  std::string origsent("Hello, Jill is not Jack, she's three or 4 or nine");
  std::string cltag("hello, NAME is not jack, she's NUM or 4 or NUM ");
  std::string tag("jill three nine ");
  std::string ntag("hello, is not jack, she's or 4 or ");
  TaggedSentence ts(origsent);
  ts.dump();

  test_tagged(origsent, ts.original(), p, f);
  test_tagged(cltag, ts.class_tagged(), p, f);
  test_tagged(tag, ts.tagged(), p, f);
  test_tagged(ntag, ts.untagged(), p, f);
  
  std::cout << "Tagged Sentence Results:  Pass: " << p 
            << "; Fail: " << f << std::endl;
}

int main(int argc, char *argv[]) {

  std::cout << "***** TESTS ****\n";
  int wp, wf, tp, tf;
  test_wordmap(wp, wf);
  test_tagged_sentence(tp, tf);

  std::cout << "***** END  TESTS ****\n\n\n";

  if ((wf + tf) > 0) {
    std::cout << "ERROR: Self test failed.  Exiting...\n";
    return EXIT_FAILURE;
  }

  TaggedSentence tagged("I'm Jack and I'm three years old");
  
  std::cout << "\n\nFINAL RESULTS:\n";
  std::cout << "  Original sentence: " << tagged.original() << std::endl;
  std::cout << "  Class Tagged: " << tagged.class_tagged() << std::endl;
  std::cout << "  Just Tagged: " << tagged.tagged() << std::endl;
  std::cout << "  Not Tagged: " << tagged.untagged() << std::endl;

  return EXIT_SUCCESS;
}

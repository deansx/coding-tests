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
*           {one, two, three, ..., nine} => NUM - the words representing
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
*   VERSION: 0.1.0
*
*****************************************************************************/
use std::collections::HashMap;
use std::collections::HashSet;
use std::fmt;
use std::ascii::AsciiExt;
//use std::process;

//
// WordMap manages sets of words that each "map" to a specified specified
// word.  Note: Does not directly support retrieving the original match
// sets.
// Supports:
//    - adding new words to the match set
//    - searching for a word in the match set,
//    - producing the mapped word
// NOTE:
//    - Public so that the struct can be accessed by the test module

pub struct WordMap<'a> {
    map:HashMap<&'a str, &'a str>,
}

impl<'a> WordMap<'a> {

    // Initializes object with an empty HashMap
    // Returns:
    //    The new object
    fn new() -> WordMap<'a> {
        WordMap{map:HashMap::new()}
    }

    // Add a new "mapping." In this context, a mapping is a group of keys
    // that map to a single word
    // Args:
    //   new_keys - a str ref that contains a space separated list of words
    //               that represent the "keys" for new_val
    //   new_val - a str ref representing the single word mapped by new_keys
    fn add_map(&mut self, new_keys: &'a str, new_val: &'a str) {
        let sstr = new_keys.split(' ');
        let svec = sstr.collect::<Vec<_>>();
        for k in svec.iter() {
            self.map.insert(k, new_val);
        }
    }

    // Attempt to retrieve the word that is mapped by the given argument.
    // Args:
    //   word - a str ref representing the word to look up
    // Returns:
    //   Option(mapped_value) - If the "word" is in the map, will return a
    //      Some() containing a str ref with the word that was mapped to.
    fn get(&self, word: &str) -> Option<&str> {
        match self.map.get(word) {
            Some(subst) => {
                Some(subst)
            },
            None => {
                None
            },
        }        
    }

    // Test method that runs the specified sentence through the mapper
    // Args:
    //   the_str - a str ref representing the sentence to run through
    // Returns:
    //   String containing a version of the original phrase, in which mapped
    //   words have been replaced by their mapped value.
    #[cfg(test)]
    fn run_map(&self, the_str: &str) -> String {
        let svec = the_str.split(' ').collect::<Vec<_>>();
        let substr: Vec<_> = svec.iter().map(|w| {
            match self.map.get(w) {
                Some(subst) => {
                    *subst
                },
                None => {
                    *w
                },
            }
        }).collect();

        substr.join("+")
    }

}

//
// Map sentence is really just an artifact of the requirements for the
// exercise. The functionality could easily have been provided in a function.
// This object is initialized with a "sentence" a str ref containing 
// sequences of ASCII characters separated by single spaces. It uses the
// services and mapping information loaded into the WordMap object to replace
// words in the input str with mapped words. Note that, as per the
// requirements, the input str is converted to an all lowercase
// representation before mapping is performed.
//
// The input_str is provided at initialization and maintained as a data
// member of the object.
//
// After mapping, the object's mapit() method returns four Strings containing,
//    in turn:
//    - A representation of the original input string
//    - The words from the original that were not mapped 
//    - The words from the original that were mapped
//    - A new sentence with the tagged words replaced by their respective
//        mapped words.
//
// NOTES:
//    - Currently this is a single use object. Create a new one if you want
//        to map a different phrase.
//    - Public so that the struct can be accessed by the test module

pub struct MapSentence<'a> {
    input_str: &'a str,
}

impl<'a> MapSentence<'a> {

    // Initializes object with a clone of the input str ref
    // Returns:
    //    The new object

    fn new(new_sentence:&'a str) -> MapSentence {
        MapSentence{input_str:new_sentence.clone()}
    }

    // Map the words in the saved input string using the specified map
    // object
    // Args:
    //   map_obj - a ref to the WordMap instance that's pre-loaded with the
    //               word mapping information
    // Returns:
    //   Four Strings containing, in turn:
    //    - A representation of the original input string
    //    - A new sentence with the tagged words replaced by their respective
    //        mapped words.
    //    - The words from the original that were mapped
    //    - The words from the original that were not mapped 

    fn mapit(&self, map_obj:&'a WordMap) -> (String, String, String, String) {

        // Initialize lc here to ensure lifetime extends beyond the tagged
        // untagged collections
        let lc = self.input_str.to_ascii_lowercase();
        // Will recieve words that were/were not recognized, for return as
        // per the requirements. Using HashSet so that multiple occurrences
        // of a given word in the input string only get recorded a single
        // time in the returned report.
        let mut untagged = HashSet::new();
        let mut tagged = HashSet::new();

        // Tokenize the lowercase version of the input string, then
        // run through it attempting to map each word. Update the
        // tagged/untagged collections, as well as the sentence with
        // mapped words replaced.
        // Collects the values returned from the mapping iterator into a
        // new vector. We'll join() this Vec for return.
        let svec = lc.split(' ').collect::<Vec<_>>();
        let substr: Vec<_> = svec.iter().map(|w| {
            match map_obj.get(w) {
                Some(subst) => {
                    tagged.insert(w.clone());
                    subst
                },
                None => {
                    untagged.insert(w.clone());
                    *w
                },
            }
        }).collect();
        // Gather the keys from the HashSets into vectors to prepare for
        // the conversion to strings.
        let tagvec = tagged.into_iter().collect::<Vec<_>>();
        let untagvec = untagged.into_iter().collect::<Vec<_>>();

        ( self.input_str.to_string()
         ,substr.join(" ")
         ,tagvec.join(", ")
         ,untagvec.join(", ")
        )
    }
}

impl<'a> fmt::Display for MapSentence<'a> {
    // Prepare a printable version of the object that shows the value
    // of the input_str member
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", self.input_str)
    }
}

#[cfg(test)]
//
// Run the test functions
// Returns:
//    tuple containing the number of tests that passed in the first position
//       and the number than failed in the second position
mod tests {
    // NOTE: By default, you won't see the output of the println!s from the
    //      test functions.  In searching for an explanation, I came across
    //      this most helpful discussion:
    //          http://stackoverflow.com/questions/25106554/println-doesnt-work-in-rust-unit-tests
    //      "[the] Rust test program hides stdout of successful tests in order
    //      for [the] test output to be tidy. You can disable this behavior 
    //      [by] passing --nocapture option."
    //      However, in the same thread, we find out that, due to another issue,
    //      the actual command that works is:
    //
    //          cargo test -- --nocapture

    use super::*;

    #[test]
    fn test_wordmap() {
        // Set up some mapping values, each token in the first argument will
        // map to the second argument
        let wordmap = create_test_wordmap();
        // Run the test mapping function and check the results
        let mapped = wordmap.run_map("abc def ghi jkl mno pqr stu vwx yza bcd");
        
        let mapped_chk = "abc+802.11s+zigbee+jkl+zigbee+pqr+802.11s+\
                          802.11s+yza+bcd";
        print!( "\n   Mapped is: '{}'\n   Check is:  '{}'..."
               ,mapped
               ,mapped_chk
              );
        assert_eq!(mapped, mapped_chk.to_string());
    }

    #[test]
    fn test_wordmap_key_retrieval() {
        let tvec = vec!["vwx", "jkl", "mno", "xyz", "def"];
        let mut matches = Vec::new();
        let mut unmatched = Vec::new();
        let wordmap = create_test_wordmap();

        for k in &tvec {
            match wordmap.get(k){
                Some(matched) => {
                    let result = format!("{}:{}",k, matched);
                    matches.push(result);
                }
                None => {
                    unmatched.push(*k);
                }
            }
        }
        // Reference values
        let matched_chk = "vwx:802.11s, mno:zigbee, def:802.11s";
        let unmatched_chk = "jkl, xyz";
        assert_eq!(matches.join(", "), matched_chk.to_string());
        assert_eq!(unmatched.join(", "), unmatched_chk.to_string());
    }

    #[test]
    fn test_mapsentence_original_phrase() {
        let (orig_string, _, _, _) = get_mapsentence_results();
        let orig_phrase_chk = "Abc DEF Ghi Jkl MNO Pqr STU Vwx YZA bcd eFg";
        assert_eq!(orig_string, orig_phrase_chk.to_string())
    }


    #[test]
    fn test_mapsentence_mapped_string() {
        let (_, mapped_string, _, _) = get_mapsentence_results();
        let map_string_chk = "abc 802.11s zigbee jkl zigbee pqr 802.11s \
                           802.11s yza bcd efg";
        assert_eq!(mapped_string, map_string_chk.to_string())
    }


    #[test]
    fn test_mapsentence_tagged_words() {
        let (_, _, tagged, _) = 
                                                  get_mapsentence_results();
        let tagged_chk = "def, ghi, mno, stu, vwx";
        assert_eq!(sorted_toks(tagged), tagged_chk.to_string())
    }

    #[test]
    fn test_mapsentence_untagged_words() {
        let (_, _, _, untagged) = 
                                                  get_mapsentence_results();
        let untagged_chk = "abc, bcd, efg, jkl, pqr, yza";
        assert_eq!(sorted_toks(untagged), untagged_chk.to_string())
    }


    // Testing utility functions...

    // Returns:
    //  A set of (hopefully) predictable output from using both a known
    //  original phrase and a known mapping.
    fn get_mapsentence_results() -> 
                              (String, String, String, String) {
        let map_sentc = create_test_mapsentence();
        let wordmap = create_test_wordmap();
        map_sentc.mapit(&wordmap)
    }

    // Returns:
    //  A new WordMap instance with a known set of mapping data
    fn create_test_wordmap<'a>() -> WordMap<'a> {
        let mut wordmap = WordMap::new();
        // Set up some mapping values, each token in the first argument will
        // map to the second argument
        wordmap.add_map("ghi mno", "zigbee");
        wordmap.add_map("def stu vwx", "802.11s");
        return wordmap;
    }

    // Returns:
    //  A new MapSentence instance with a known phrase
    fn create_test_mapsentence<'a>() -> MapSentence<'a> {
        let orig_phrase = "Abc DEF Ghi Jkl MNO Pqr STU Vwx YZA bcd eFg";
        MapSentence::new(orig_phrase)
    }

    // Takes the given string of tokens, breaks them up, sorts them, and
    // reforms them into a string for return
    // Args:
    //   in_string - String containing comma+space separated tokens
    // Returns:
    //   String containing comma+space separated tokens in sorted order
    fn sorted_toks( in_string: String) -> String {
        let mut toks = in_string.split(", ").collect::<Vec<_>>();
        toks.sort();
        toks.join(", ")
    }
}


fn main() {
    // Use the command 'cargo test' or 'cargo test -- --nocapture' to run
    // the tests. The latter form displays some additional text during the
    // test.

    println!("\nRunning replace-words...\n");
    let mut word_map = WordMap::new();
    // Set up the word mapper the words in the first argument will map to
    // the word specified in the second argument.
    // Key / Value data from the original coding test
    word_map.add_map("jack jill", "NAME");
    word_map.add_map("one two three four five six seven eight nine", "NUM");

    // Set up the sentence object
    // Phrase from the original coding test
    let orig_phrase = "I'm Jack and I'm three years old";
    let map_phrase = MapSentence::new(orig_phrase);
    println!("\nmap_phrase contains: '{}'\n", map_phrase);

    // Run the mapping & display the results
    let (orig_string, mapped_string, tagged, untagged) = 
        map_phrase.mapit(&word_map);
    println!("\nResults:");
    println!("   Original String: \"{}\"", orig_string);
    println!("   Mapped Words:    \"{}\"", mapped_string);
    println!("   Unmapped Words:  \"{}\"", tagged);
    println!("   Mapped Phrase:   \"{}\"", untagged);
}

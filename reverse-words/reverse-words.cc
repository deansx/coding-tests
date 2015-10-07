/*****************************************************************************
*   DESCRIPTION:
*     Given a string, reverse the words, so that the last word becomes the 
*     first word, but each word still reads normally.
*     
*     INPUTS:
*       > A string containing words separated by a single space
*
*     OUTPUT:
*       > A string with the order of the words reversed, but each word is
*         still readable normally.
*
*     CONSTRAINTS:
*       > Do not us large amounts of extra storage.  Very limited local scope
*         variables are OK, but you can't do things like buffer up chunks
*         of the string or allocate a new list of the words for reversal.
*     
*     EXAMPLE:
*       > "The pen is red" becomes "red is pen The"
* 
*     DISCUSSION:
*       > Nothing very complex here, we have a function to do a pairwise
*         front-to-back swap of a given character vector.  We use this
*         function to reverse the input string, then we step through the
*         reversed string one token (word) at a time and reverse the
*         characters in each word.
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

#include <cstdlib>
#include <cstring>
#include <iostream>

// reverse() takes the specified vector of characters and performs
// pairwise swaps to reverse the characters.
// ARGS:
//   phrase - pointer to an array of characters. Note that we DO NOT assume
//            that phrase is a proper C string - that is, we don't assume
//            that it has the null terminating character, which is why
//            we need to have the length passed in
//   len - length of the string to be reversed, in characters.

void reverse(char *phrase, int len) {

  // "k" will start as the index of the final character of the buffer to
  // be reversed. we'll walk k in reverse order back towards the front of
  // the buffer.
  int k = len - 1;
  std::cout << "String is: '" << phrase << "'; len = " << len << std::endl;

  // i starts out as the index of the first character of the buffer and walks
  // towards the end of the buffer. We swap the character at [i] with the
  // character at [k] then move in 1 position from both ends, until we meet
  // in the middle.  If the buffer has an odd length, we can just leave the
  // middle character alone. If the buffer has an even length, the final swap
  // will be the two characters that straddle the middle of the buffer.
  for (int i = 0; i < k; i++) {
    char c = phrase[i];
    phrase[i] = phrase[k];
    phrase[k] = c;
    k--;
  }
}

int main(int argc, char *argv[]) {

  // initialize the input string and the buffer to reverse
  //char in_str[] = "The pen is red";
  char in_str[] = "The Quick Brown Fox Jumped Over The Fences";
  char phrase[4096];
  strcpy(phrase, in_str);
  // Reverse the whole buffer. This will put the words in the correct order
  // in the buffer, but the characters in each word will also be reversed -
  // you won't be able to read them normally
  reverse(phrase, strlen(phrase));
  std::cout << "Reversed:  '" << phrase << "'" << std::endl;

  int i = 0;
  int s = 0;
  while (i <= strlen(phrase)) {
    if (phrase[i]== ' ' || phrase[i] == '\0') {
      reverse(&phrase[s], i-s);
      s = i+1;
    }
    i++;
  }
  std::cout << "Original: " << in_str << std::endl;
  std::cout << "Reversed: " << phrase << std::endl;
  return EXIT_SUCCESS;
}

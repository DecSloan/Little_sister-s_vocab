# Little_sister-s_vocab

## A set of 4 challenges to test your coding for helping with little sister's vocabulary homework 

**Instructions**
You are helping your younger sister with her English vocabulary homework, which she is finding very tedious. Her class is learning to create new words by adding prefixes and suffixes. Given a set of words, the teacher is looking for correctly transformed words with correct spelling by adding the prefix to the beginning or the suffix to the ending.
There's four activities in the assignment, each with a set of text or words to work with.
1. Add a prefix to a word
One of the most common prefixes in English is un, meaning "not". In this activity, your sister needs to make negative, or "not" words by adding un to them.
Implement the add_prefix_un(<word>) function that takes word as a parameter and returns a new un prefixed word:

        word = " "

        def add_prefix_un(word):
            word = str(input("Please enter the the word you would like to " +
                             "add the prefix 'un' to: ")).strip()
            new_word = "un" + word
            print(new_word)

        add_prefix_test = add_prefix_un(word)

2. Add prefixes to word groups
There are four more common prefixes that your sister's class is studying: en (meaning to 'put into' or 'cover with'), pre (meaning 'before' or 'forward'), auto (meaning 'self' or 'same'), and inter (meaning 'between' or 'among').

    In this exercise, the class is creating groups of vocabulary words using these prefixes, so they can be studied together. Each prefix comes in a list with common words it's used 
    with. The students need to apply the prefix and produce a string that shows the prefix applied to all of the words.

    Implement the make_word_groups(<vocab_words>) function that takes a vocab_words as a parameter in the following form: [<prefix>, <word_1>, <word_2> .... <word_n>], and returns a 
    string with the prefix applied to each word that looks like: '<prefix> :: <prefix><word_1> :: <prefix><word_2> :: <prefix><word_n>'.


# Task 1 - Add a prefix to a word

word = " "

def add_prefix_un(word):
    word = str(input("Please enter the the word you would like to " +
                     "add the prefix 'un' to: ")).strip()
    new_word = "un" + word
    print(new_word)

add_prefix_test = add_prefix_un(word)


# Task 2 - Add prefixes to a word groups
# I made the code so you dont have to specify the amount of words in the list

vocab_words = []
new_list = []

def make_word_groups(*vocab_words):
    prefix = vocab_words[0]
    new_list. append(prefix)
    length = len(vocab_words)
    for i in range(1,length):
        new_list.append(prefix + vocab_words[i])

    print(*new_list, sep= " :: ")

make_word_test = make_word_groups("pre", "serve", "dispose", "disposition", "date")


# Task 3 - Remove a suffix from a word
# If the word ends in a i it is replaced to a y

diff_word = " "

def remove_suffix_ness(diff_word):
    diff_word = str(input("Please enter the the word you would like to " +
                     "remove the suffix 'ness' from: ")).strip()
    new_word = diff_word.rstrip(diff_word[-4:])
    if new_word[-1] == "i":
        final_word = new_word.rstrip(new_word[-1:])
        print(final_word + "y")
    else:
        print(new_word)

remove_suffix_test = remove_suffix_ness(diff_word)


# Task 4 - Extract and transfprm a word

split_list = []

def adjective_to_verb(sentence, index):
    split_list = sentence.split()
    adjective = split_list[index]
    verb = (adjective + "en")
    print(verb)

adjective_test = adjective_to_verb("I need to make that bright", -1)
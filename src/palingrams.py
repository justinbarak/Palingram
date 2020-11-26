"""Find all (up to 2 words) word pairs in a dictionary file"""

import load_dictionary

word_list = load_dictionary.load("src/dictionary.txt")


def minlen(n):
    """Returns true if length of the item > 1"""
    if len(n.strip()) > 1:
        return True
    return False


def purge_single_letter(full_list):
    """Remove single letters from the dictionary"""
    # in list comprehension syntax
    print(len(full_list))
    # filtered_list = list(i for i in full_list if (len(i) > 1))
    filtered_list = list(filter(minlen, full_list))
    print(len(filtered_list))
    return filtered_list


word_set = set(purge_single_letter(word_list))

# find word-pair palingrams
def find_palingrams():
    """Find dictionary palingrams"""
    pali_list = []
    for word in word_set:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if (word[i:] == rev_word[: end - i]) and (
                    rev_word[end - i :] in word_set
                ):
                    pali_list.append((word, rev_word[end - i :]))
                if (word[:i] == rev_word[end - i :]) and (
                    rev_word[: end - i] in word_set
                ):
                    pali_list.append((rev_word[: end - i], word))
    return pali_list


def somelen(item):
    """Returns true if length of the items > 14"""
    if len((item[0] + item[1])) > 14:
        return True
    return False


palingrams = find_palingrams()

# sort palingrams on first word
palingrams_sorted = sorted(palingrams)

# display list of palingrams
print("\nNumber of Palindromes found = {}\n".format(len(palingrams_sorted)))
# for first, second in palingrams_sorted:
for first, second in list(filter(somelen, palingrams_sorted)):
    print("{} {}".format(first, second))

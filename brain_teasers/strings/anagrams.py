from collections import Counter


def get_anagrams(word, word_array):
    if not word or not word_array:
        raise RuntimeError("Input parameters can't be empty!")

    if isinstance(word_array, list) or isinstance(word_array, tuple):
        char_occurrences = Counter(word)
        uniq_words = set(word_array)  # remove duplicates if any

        # use genexpr to save memory if many values are expected to return
        return [w for w in uniq_words if Counter(w) == char_occurrences]

    raise RuntimeError("'word_array' must be of type 'list' or 'tuple';"
                       " {} is given!\n".format(type(word_array)))

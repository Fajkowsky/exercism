def word_count(words):
    word_list = words.split()
    count = {k: word_list.count(k) for k in word_list}
    return count
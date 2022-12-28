def longest_word(text):

    def wl(w):
        return len(w)
        
    if text:
        
        splitted = text.split()
        # print(splitted)
        word_len = list(map(wl, splitted))
        # print(word_len)
        naj = max(word_len)
        ind = word_len.index(naj)
        
        return(splitted[ind])


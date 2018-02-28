class Input:
    def __init__(self):
        self.infile = open(input())

    def wordlist(self):
        return list(filter(lambda word: word != "", [word.strip(":;`_?!,.\'\"") for word in self.infile.read().split()]))

class Ngrams:
    def __init__(self):
        self._n = int(input())
        self._ngrams = {}

    def update(self, ngram):
        if ngram not in self._ngrams:
            self._ngrams[ngram] = 0
        self._ngrams[ngram] += 1

    def process_wordlist(self, wordlist):
        for i in range(len(wordlist) - (self._n)):
            ngram = _ngram(wordlist, i, self._n)
            self.update(" ".join(ngram).lower())

    def _get_max_ngrams(self):
        max_num = 0
        ret_list = []
        for key, val in self._ngrams.items():
            if val > max_num:
                ret_list.clear()
                ret_list.append((val, key))
                max_num = val
            elif val == max_num:
                ret_list.append((val, key))
        return ret_list

    def print_max_ngrams(self):
        out_list = self._get_max_ngrams()
        for elem in out_list:
            print("{:d} -- {}".format(elem[0], elem[1]))

def _ngram(arglist, startpos, length):
    """Computes the n-gram of the given list
    Parameters: arglist     list
                startpos    int
                length      int
    Returns:    list
    Pre-conditions: arglist is non-empty
    Post-conditions: returns a list."""
    ret_list = []
    l = arglist[startpos: startpos + length]
    if len(l) < length:
        return ret_list
    else:
        return l
def main():
    in_data = Input()
    ngrams = Ngrams()
    ngrams.process_wordlist(in_data.wordlist())
    ngrams.print_max_ngrams()


main()

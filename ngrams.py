class Input:
    """Input abstracts the basic input for the ngram processing.

    Attributes:
        infile  File Object that is the text file for processing.

    Methods:
        __init__ ()   constructor

        wordlist() None -> list
            cleans the infile and produced the list to be processed."""

    def __init__(self):
        """Constructor that opens an input file.
        Paramaters: None
        Returns: Input
        Pre-conditions: None
        Post-conditions: New Input object is returned."""
        self.infile = open(input())

    def wordlist(self):
        """Cleans the input file for processing.
        Parameters: None
        Returns: List for processing.
        Pre-conditions: infile is open
        Post-conditions: list is returned"""
        assert self.infile
        return list(filter(lambda x: x != "", [word.strip(":;`&$#@_?!,.\'\"") for word in self.infile.read().split()]))


class Ngrams:
    """Handles the input file and processes the n-grams.

    Attributes:
        _n          interger representing the length of the ngrams
        _ngrams     dictionary the holds the ngram as a key and a
                    count of its occurances in the text.

    Methods:
        __init__()
            constructor

        update(ngram) string -> None
            updates the count for ngram in _ngrams

        process_wordlist(wordlist) list -> None
            processes wordlist into the dictionary of ngrams.

        _get_max_ngrams() None -> list
            finds the max ngrams in _ngrams

        print_max_ngrams():
            prints the list of max ngrams."""
    def __init__(self):
        """Constructor
        Parameters: None
        Returns: Ngrams
        Pre-condtions: None
        Post-conditions: New Ngrams object."""
        self._n = int(input())
        self._ngrams = {}

    def update(self, ngram):
        """Updates the value of ngram in _ngrams.
        Parameters: ngram   string of the ngram to count.
        Returns:    None
        Pre-conditions: ngram is non-empty string
        Post-conditions: _ngrams[ngram] is incremented."""
        assert ngram != ""
        if ngram not in self._ngrams:
            self._ngrams[ngram] = 0
        self._ngrams[ngram] += 1

    def process_wordlist(self, wordlist):
        """Processes a given wordlist for ngrams of length _n.
        Parameters: wordlist    list of words to be processed.
        Returns:    None
        Preconditions: wordlist is a list
        Post-conditions: _ngrams is non-empty."""
        for i in range(len(wordlist) - (self._n) + 1):
            ngram = _ngram(wordlist, i, self._n)
            self.update(" ".join(ngram).lower())

    def _get_max_ngrams(self):
        """Constructs a list of the maximum ngrams in _ngrams
        Parameters: None
        Returns: List of the max ngrams
        Pre-conditions: None
        Post-conditions: a list is returned."""
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
        """Simply prints the max ngrams from _ngrams.
        Parameters: None
        Returns: None
        Pre-conditions: None
        Post-conditions: Side-effect."""
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
    assert len(arglist) > 0
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

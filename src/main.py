'''Category                No of letters unmatched
Pangram                     0
Lipogram                    >1
Pangrammatic Lipogram       1
'''
# function to check for Pangrammatic Lipogram
def panLipogramChecker(s):
 
    # dictionary to keep count of the
    # occurrence of each letter
    counter = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
               'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
               'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
               'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
               'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
               'z': 0}
 
    s = s.lower()
 
    # increment count of characters in dictionary
    for i in s:
        if (i.isalpha()):
            counter[i] += 1
 
    # returns a list containing the values of all
    # the keys in h=the dictionary
    b = list(counter.values())
 
    if (b.count(0) > 1):
        print("Not a pangram, but might be a lipogram.")
    elif (b.count(0) == 1):
        print("Pangrammatic Lipogram.")
    elif (b.count(0) < 1):
        print("Pangram.")
 # isalpha() is a string method that checks if 
 # a character is an alphabet
def main():
    panLipogramChecker("The quick brown fox \
                        jumped over the lazy dog")
    panLipogramChecker("The quick brown fox \
                        jumps over the lazy dog")
    panLipogramChecker("The quick brown fox \
                        jum over the lazy dog")
 
 
if __name__ == '__main__':
    main()
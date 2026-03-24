import os
import benczutils.common as common

def getCombinations(length, digits):
    places = [0] * length
    combinations = []
    goOn = True
    while goOn:
        combinations.append(places.copy())
        places[-1] += 1

        for i in range(length):
            if places[-(i + 1)] >= digits:
                if i == length - 1:
                    goOn = False
                else:
                    places[-(i + 1)] -= digits
                    places[-(i + 2)] += 1
    print(combinations)
    return combinations

def enumerate_lex(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        lexicon = f.readline().strip().split(' ')
        length = int(f.readline().strip())
        combinations = getCombinations(length, len(lexicon))

        for c in combinations:
            print("".join(map(lambda a:lexicon[a], c)))

enumerate_lex("sample.txt")
enumerate_lex("rosalind_lexf.txt")
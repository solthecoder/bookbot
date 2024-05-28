from collections import defaultdict

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
    f.close()
    unsorted = count_letters(words)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")
    print("\n")
    out = sorted(unsorted)
    for rank in out:
        print(f"The '{rank['abc']}' character was found {rank['num']} times")

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
result = defaultdict(int)
def count_letters(dawords):
    for word in dawords:
        #print(word)    
        for letter in alphabet:
            lower_case = word.lower()
            the_count = lower_case.count(letter)
            result[letter] += the_count
    return result

def sort_on(dict):
    return dict["num"]

def sorted(unsorted):
    list_abc = []
    holder_a = {}
    holder_b = {}
    for key in range(0,len(unsorted)):
        abc = alphabet[key]
        holder_a["abc"] = abc
        holder_b["num"] = unsorted[abc]
        list_abc.append(holder_a | holder_b)
        list_abc.sort(reverse=True,key=sort_on)
    return list_abc

main()
# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename) as doc:
        lines = doc.readlines()
    
    return lines


def count_words():
    count_dictionary = {}
    text = read_file_content("./story.txt")

    for line in text:
        for word in line.split():
            if word.lower() in count_dictionary:
                count_dictionary[word] += 1
            else:
                count_dictionary[word.lower()] = 1
    
    return count_dictionary
    
print(count_words())

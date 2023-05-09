
def char_check(word_list):
    # Make sure the list has at least 10 elements

    if len(word_list) < 10:
        print("Error: The list must have at least 10 elements")
    else:
        # Convert the input to all uppercase
        word_list = [word.upper() for word in word_list]
        return word_list

def count_words(word_list):
    # Return the length of the list
    return len(word_list)

def count_occurrence(word_list):
    # Create a dictionary to store the count of each word
    word_count = {}

    # Iterate over the list and count the occurrence of each word
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

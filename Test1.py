
import TextRead

from function import char_check,count_words,count_occurrence
# Call the char_check function to clean the data
clean_word_list = char_check(TextRead.word_list)

# Call the count_words function to get the number of words in the input
word_count = count_words(clean_word_list)
print("The number of words in the input is:", word_count)

# Call the count_occurrence function to get the word frequency count
word_frequency = count_occurrence(clean_word_list)
print("The word frequency count is:", word_frequency)

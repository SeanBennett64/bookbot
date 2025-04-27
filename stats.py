def word_counter(book_string):
  word_array = book_string.split()
  total_words = len(word_array)
  return total_words


def letter_counter(book_string):
  letter_count = {}
  for char in book_string.lower():
    if char in letter_count:
      letter_count[char] += 1
    else:
      letter_count[char] = 1
  return letter_count



def sorted_list(list_of_letters):
  true_letters = {}
  for key, value in list_of_letters.items():
    if key.isalpha() == True:
      true_letters[key] = value
      my_keys = list(true_letters.keys())
      my_keys.sort()
      sorted_letters = {k: v for k, v in sorted(true_letters.items(), key=lambda item: item[1], reverse=True)}
  for key, value in sorted_letters.items():
    print(f"{key}: {value}")



  

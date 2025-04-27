import sys
from stats import word_counter
from stats import letter_counter
from stats import sorted_list 

book = None

script_name = sys.argv[0]

if len(sys.argv) > 1:
  book = sys.argv[1]
else:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)




def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
  return file_contents

text = get_book_text(book)

def main():
  print(f"""============ BOOKBOT ============
Analyzing book found at {book}...
----------- Word Count ----------
Found {word_counter(text)} total words
--------- Character Count -------""")
  sorted_list(letter_counter(text))
  print("============= END ===============")



main()

  

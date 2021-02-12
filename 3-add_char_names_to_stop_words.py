#GenerateCharacterStopwords.py
import os
#Pull file names from character + dialogue file lists to create list
# of character names to add to stopwords
#Include option to add "s" to name to filter "'s" occurences

my_path = os.path.abspath(os.path.dirname(__file__))

def add_character_names_to_stopwords():
    charslist = []
    root = os.path.join(my_path, "data_char_lines")
    for path, subdirs, files in os.walk(root):
        for name in files:
            char = name.strip(".txt")
            charslist.append(char.lower())
            charlist.append("{}'s".format(char.lower())
            charlist.append("{}s".format(char.lower())
    charslist = set(charslist)
    return charslist



def dir_dir(dirname):
  if os.path.isdir(dirname):
    pass
  else:
    os.mkdir(dirname)



def generate_stopwords_file_from_character_names():

'''Call this function to create char_stopwords.txt file
populated with all the character names identified in preprocessing
to be used as supplementary stopwords list'''
  
  root = os.path.join(my_path, "resources")
  dir_dir(root)
  path = os.path.join(root, "char_stopwords.txt")
  with open(path, 'w') as fo:
    for ch in set(sorted(charslist)):
      fo.write(ch)
      fo.write("\n")

character_name_list = add_character_names_to_stopwords()
generate_stopwords_file_from_character_names(character_name_list)


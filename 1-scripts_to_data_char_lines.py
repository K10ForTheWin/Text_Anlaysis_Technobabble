import os
from collections import defaultdict
import re

##Change paths to relative paths

mychardict = defaultdict(list)


def process_file(fi):
    # Creates list of (character, line) tuples identifying the speaker of each line (in script character's
    # will have multi-line dialogue that is assigned the last character name found to link them to speaker
    
    newlines = []
    with open(fi, encoding="utf-8") as infile:
        lines = infile.readlines()
        inside_script = False
        previous_char = ""
        previous_lines = ""
        inside_parenthesis = False
        for line in lines:
            if line.startswith("<Back"):
                inside_script=False
                
            elif inside_script:
  
                if line.count(":")==1:  #some weird lines with timestamps in stage notes                                 
                    character, punct, current_line = line.partition(":")
                    character = clean(character)
                    line = clean(line)
                    line = clean_line(line)

                    if is_valid(character):
                        previous_char = character
                        previous_lines = current_line
                        newlines.append((character, current_line))          
                else:
                    line = clean(line)
                    line = clean_line(line)
                    current_line = line.strip()
                    character = previous_char
                    previous_lines += current_line
                    newlines.append((previous_char, current_line))

            elif "Original Airdate:" in line:
                inside_script = True
    
            else:
                pass
    return newlines

def clean(char):
  #  flags = ["{", "[", "("]
    char = re.sub("[\(\[].*?[\)\]]", "", char)
    char = char.upper()
##    if any(f in char for f in flags):
##        return re.sub("[\(\[].*?[\)\]]", "", char)
    return char

def clean_line(line):
    try:
        if "(" in line:
            line_keep, line_discard = line.split("(")
            line = line_keep
        elif ")" in line:
            line_discard, line_keep = line.split(")")
            line = line_keep
    except ValueError:
            line=""
    return line

def create_char_dict(newlines):
    mydict = defaultdict(list)
    for i in range(0, len(newlines) - 1):
        ch, line = newlines[i]
        ch = re.sub("[\(\[].*?[\)\]]", "", ch)   #remove parens and brackets from char name
        ch = ch.strip()
        ch = ch.upper() #standardise all name to uppercass
        line = re.sub("[\(\[].*?[\)\]]", "", line)  #remove text inside parens and brackets
        mydict[ch].append(line)
        mychardict[ch].append(line)

    return mydict


def dir_dir(dirname):
    if os.path.isdir(dirname):
        pass
        #print("directory already exists")
    else:
        os.mkdir(dirname)

        
def is_valid(charname):
    if charname=="":
        return False
    flags=["/", "\\", "?", "|", "<", ">", "(", "[", "+", ","]
    if any(flag in charname for flag in flags):
        return False
    return True

        

def create_dest(folder):
    _, series = folder.split("_")
    dirname = os.path.join(".\data_char_lines", series)
    dir_dir(dirname)
    return dirname


def write_lines(mydict, dest_folder):
    for char, lines in mydict.items():
        #if check_keys(k):
        fo = os.path.join(dest_folder, char + ".txt")
        with open(fo, "a", encoding="utf-8") as outfile:
            lines_clean = " ".join(i.strip() for i in lines)
            outfile.write(lines_clean)
            outfile.write("\n")


root = ".\data"
folders = os.listdir(root)

root_dest = ".\data_char_lines"
dir_dir(root_dest)

##if destination directory exists, it will be removed and replaced


def process_all_scripts():
    for folder in folders:  # folders in data/ are series folder with scripts within
        
        files = os.listdir(os.path.join(root, folder))

        for f in files:
            # give me the file locations
            file_loc = os.path.join(root, folder, f)
            # assign lines of dialogue to character they belong to, returns list
            character_lines = process_file(file_loc)
            # create dictionary of characters with lines as value, and normalize to reduce set
            char_dict = create_char_dict(character_lines)

            # create destination folders/files to save text
            dest_folder = create_dest(folder)

            # write character lines to files
            write_lines(char_dict, dest_folder)


process_all_scripts()


print(len(mychardict))

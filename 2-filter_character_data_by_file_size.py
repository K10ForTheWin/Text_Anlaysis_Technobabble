# Get files of a certain size threshold, top 100
# preview file lexicon
import string
from shutil import copyfile
import os
import operator
from nltk.corpus import stopwords

##  for m in more:
##  for mm in m:
##    statinfo = os.stat(mm)
##    size = statinfo.st_size
##    sz = file_size(mm)
##    print(file, sz)


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ["bytes", "KB", "MB", "GB", "TB"]:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)


def dir_dir(dirname):
    if os.path.isdir(dirname):
        os.rmdir(dirname)
    else:
        os.mkdir(dirname)


##root = "C:\Python3\data_char_lines"
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "data_char_lines")


start_dest = os.listdir(".\data_char_lines")
save_dest = ".\data_char_lines_top_100"
dir_dir(save_dest)

mydict = {}
keep_files = []
for folder in start_dest:
    file_sizes = []
    save_folder = os.path.join(".\data_char_lines", folder)
    for file in os.listdir(save_folder):
        f = os.path.join(save_folder, file)
        statinfo = os.stat(f)
        size = statinfo.st_size
        if size > 9228:
            keep_files.append(f)
            #  if os.path.join(save_dest, file)

            copyfile(
                f, os.path.join(save_dest, file)
            )  # copy file from data_char_lines to data_char_lines_top_100
        file_sizes.append(size)

    mydict[c] = file_sizes
    print(
        c,
        len(file_sizes),
        min(file_sizes),
        max(file_sizes),
        int(sum(file_sizes) / len(file_sizes)),
    )

print(len(keep_files))

##mydict2 = {}
##d={}
##for file in os.listdir(root_keep):
##  f = os.path.join(root_keep, file)
##  with open(f,encoding='utf-8') as infile:
##    lex = []
##    lines = infile.readlines()
##  ##      print(len(lines))
##    for l in lines:
##      words = l.split(" ")
##      words = [w.strip(string.punctuation) for w in words]
##      for w in words:
##        lex.append(w)
####      print(len(lex))
##      k=file.strip(".txt").title()
##      mydict2[file.strip(".txt")]=lex
##      d[file.strip(".txt")]=len(lex)


##for k, v in mydict2.items():
##  print("%s\t%d" % (k.title(), len(v)))

##sorted_x = sorted(d.items(), key=operator.itemgetter(1))
##for x in sorted_x:
##  print(x)
##
##
##root_keep = ".\data_char_lines_top_100"
##os.chdir(root_keep)
##picard_words = {}
##words = []
##with open("PICARD.txt") as infile:
##	w = infile.readlines()
##	for line in w:
##		lexs = line.split(" ")
##		words.extend(lexs)
##words = filter_words(words)
##
##def filter_words(wordlist):
##  filteredwords = []
##  for w in wordlist:
##    w = w.lower()
##    if w[-1:] in string.punctuation:
##      w = w[:-1]
##    elif w[0] in string.punctuation:
##      w = w[1:]
##    filteredwords.append(w)
##  return filteredwords
##
##
##for file in keepfiles:
##    pass
# 10 GB
##>>> os.stat("C:\Python3\data_char_lines\Voyager\GEGEN.txt")
##os.stat_result(st_mode=33206, st_ino=281474977348190, st_dev=606102944, st_nlink=1, st_uid=0, st_gid=0, st_size=9228, st_atime=1542864677, st_mtime=1542864677, st_ctime=1542864677)
##>>> x=_
##>>> x.st_size
##9228

##    print(f)
##    sz = file_size(f)
##    if not sz.endswith("bytes"):
##      print(file, sz)

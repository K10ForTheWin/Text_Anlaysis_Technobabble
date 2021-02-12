# Writes contents of webpage to text file
# saves to folder 'scripts_voyager_preprocessed'
import urllib.request
from bs4 import BeautifulSoup
import os

# initialize episode urls for download
a = ["http://www.chakoteya.net/Voyager/" + str(i) + ".htm" for i in range(101, 117)]
b = ["http://www.chakoteya.net/Voyager/" + str(i) + ".htm" for i in range(201, 226)]
c = ["http://www.chakoteya.net/Voyager/" + str(i) + ".htm" for i in range(301, 322)]
d = ["http://www.chakoteya.net/Voyager/" + str(i) + ".htm" for i in range(401, 427)]
e = ["http://www.chakoteya.net/Voyager/" + str(i) + ".htm" for i in range(501, 527)]
f = ["http://www.chakoteya.net/Voyager/" + str(i) + ".htm" for i in range(601, 627)]
g = ["http://www.chakoteya.net/Voyager/" + str(i) + ".htm" for i in range(701, 727)]
voyager_all = []
for x in [a, b, c, d, e, f, g]:
    voyager_all.extend(x)

tng_all = [
    "http://www.chakoteya.net/NextGen/" + str(i) + ".htm" for i in range(102, 278)
]

ent_1 = [
    "http://www.chakoteya.net/Enterprise/0" + str(i) + ".htm" for i in range(1, 10)
]  # add the 0 before 1-9
ent_2 = [
    "http://www.chakoteya.net/Enterprise/" + str(i) + ".htm" for i in range(10, 98)
]
enterprise_all = ent_1 + ent_2

dsnine_all = [
    "http://www.chakoteya.net/DS9/" + str(i) + ".htm" for i in range(401, 576)
]

tos_all = ["http://www.chakoteya.net/StarTrek/" + str(i) + ".htm" for i in range(1, 80)]


# set path to data/ for reset after each series downloads
my_path = os.path.abspath(os.path.dirname(__file__))


def is_dir(dirname):
    if os.path.isdir(dirname):
        pass
    else:
        os.mkdir(dirname)


def preprocess(series, prefix):

    os.chdir(os.path.join(my_path), "data")

    is_dir("data")

    fo_dir = "_".join(["scripts", prefix])
    is_dir(fo_dir)
    os.chdir(fo_dir)

    ep_count = 0

    for idx in series:
        htmlSource = ""

        try:
            with urllib.request.urlopen(idx) as response:
                htmlSource = response.read()
                soup = BeautifulSoup(htmlSource, "lxml")

            text = soup.get_text()
            lines = text.split("\n")
            lines = [l for l in lines if l != ""]

            fname = idx.rsplit("/")[-1]
            fname = fname.strip(".htm")
            fname = fname + ".txt"

            ##      outfile = os.path.join("_".join([scripts, prefix, "preprocessed"]), fname)
            ##
            ##      print(outfile)
            outfile = fname

            with open(outfile, "w", encoding="utf-8") as fo:
                for line in lines:
                    fo.write(line)
                    fo.write("\n")

            ep_count += 1

        except urllib.error.HTTPError:  # for episode numbers that do not exist
            print("idx ", idx, "raised urllib.error.HTTPError:")
            continue


def preprocess_all():
    """Call this function to download scripts from chakotay.net
    for each respective series"""
    preprocess(tng_all, "NextGen")
    preprocess(voyager_all, "Voyager")
    preprocess(dsnine_all, "DSNine")
    preprocess(enterprise_all, "Enterprise")
    preprocess(tos_all, "TOS")


def download_scripts(series="NextGen", episode_list=tng_all):
    """Alternate method of downloading scripts"""

    fo_dir = "_".join(["scripts", series, "preprocessed"])

    for idx in episode_list:
        htmlSource = ""

        try:
            with urllib.request.urlopen(idx) as response:
                htmlSource = response.read()
                soup = BeautifulSoup(htmlSource, "lxml")

            text = soup.get_text()
            lines = text.split("\n")
            lines = [l for l in lines if l != ""]

            outfile = get_fo_name(idx, fo_dir)

            print(outfile)

            with open(outfile, "w", encoding="utf-8") as fo:
                for line in lines:
                    fo.write(line)
                    fo.write("\n")

            ep_count += 1

        except urllib.error.HTTPError:
            print("idx ", "raised urllib.error.HTTPError:")
            continue


##download_scripts(series="NextGen", fo='scripts_tng_preprocessed')
##download_scripts(series="Voyager", fo='scripts_voyager_preprocessed')
##download_scripts(series="Enterprise", fo='scripts_enterprise_preprocessed')#01-98
##download_scripts(series="DS9", fo='scripts_deepspacenine_preprocessed')#401-576
##download_scripts(series="TOS", fo='scripts_startrek_preprocessed')#1-80

# -*- coding:utf-8 -*-
#! /usr/local/bin/python

import sys
import os
import re
import timeit
# from sets import Set

# default settings
connector = "_"
extension = ".txt"
split_size = 200
maxline = 60000

original_file = "coca60000.txt"
output_path = "output"

# remove duplicates while maintaining the order
def remove_duplicates(input_file):
    with open(input_file, "r") as fin:
        lines = fin.readlines()
        all_words = [x.strip() for x in lines]

        seen = {}
        pos = 0
        for word in all_words:
            if word not in seen:
                seen[word] = True
                all_words[pos] = word
                pos += 1
        del all_words[pos:]

        outfile = os.path.splitext(input_file)[0] + "_removed_duplicates" + extension
        with open(outfile, "w") as fout:
            for word in all_words:
                fout.write(word)
                fout.write("\n")

# strip spaces, symbols pre and post the words
def strip_spaces(input_file):
    outfile = os.path.splitext(input_file)[0] + "_removed_spaces" + extension

    with open(input_file, "r") as fin, open(outfile, "w") as fout:
        for line in fin:
            # line = re.sub(r'\(\)', '', line.strip())
            line = line.strip("()\n")
            fout.write(line)
            fout.write("\n")

# generate a file, with splits, that can be used for batch-importing of Eudic
def batch_import(input_file, num_of_words):
    if (len(sys.argv) < 3):
        print "split size is not specified, use default:%d" % split_size
    else:
        num_of_words = int(sys.argv[2])

    outfile = os.path.splitext(input_file)[0] + "_batch_import" + extension
    with open(input_file, "r") as fin, open(outfile, "w") as fout:
        base, cursor = 0, 0
        for line in fin:
            if base == 0:
                fout.write("#1_"+str(num_of_words))
                fout.write("\n")
                base = num_of_words

            if cursor > num_of_words - 1:
                start, end = str(base+1), str(base+cursor)
                title = '#'+start+connector+end
                fout.write(title)
                fout.write("\n")
                base = base + cursor
                cursor = 0

            fout.write(line.strip())
            fout.write("\n")
            cursor += 1

# strip chinese meanings, output only english words
def strip_meanings(input_file):
    outfile = os.path.splitext(input_file)[0] + "_no_meaning" + extension
    # print outfile
    with open(input_file, "r") as fin, open(outfile, "w") as fout:
        for line in fin:
            word = line.strip().split(" ")[0]
            fout.write(word)
            fout.write("\n")

        # remove last line, which is empty!
        fout.seek(-2, os.SEEK_CUR)
        fout.truncate()

# split words into groups with specified group size
def splitwords(input_file, num_of_words):
    if (len(sys.argv) < 3):
        print "split size is not specified, use default:%d" % split_size
    else:
        num_of_words = int(sys.argv[2])

    wordlist = []
    with open(input_file, "r") as fin:
        base, cursor = 0, 0
        for line in fin:
            # if base > maxline:
            #     sys.exit(0)

            if cursor > num_of_words - 1:
                #1. assemble filename
                start, end = str(base+1), str(base+cursor)
                outfile = os.path.join(output_path, start + connector + end + extension)

                #2. output to file
                with open(outfile, "w") as fout:
                    for word in wordlist:
                        fout.write(word)
                        fout.write("\n")

                    # delate last line
                    fout.seek(-2, os.SEEK_CUR)
                    fout.truncate()

                #3. update base, reset cursor and wordlist
                base = base + cursor
                cursor = 0
                wordlist = []


            # collects words and update cursor
            wordlist.append(line.strip())
            cursor+=1

        if cursor > 0:
            start, end = str(base+1), str(base+cursor)
            outfile = os.path.join(output_path, start + connector + end + extension)

            with open(outfile, "w") as fout:
                for word in wordlist:
                    fout.write(word)
                    fout.write("\n")
                fout.seek(-2, os.SEEK_CUR)
                fout.truncate()

###########################################################################

# usage:
# ./split.py filename 200

def main(argv):
    global output_path
    input_file = original_file

    if len(argv) < 2:
        print("must specify filename")
        sys.exit(1)
    else:
        input_file = argv[1]

    # create output directory if not exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    start = timeit.default_timer()
    # splitwords(input_file, split_size)
    batch_import(input_file, split_size)
    # remove_duplicates(input_file)
    # strip_spaces(input_file)
    # strip_meanings(input_file)

    stop = timeit.default_timer()
    print 'Time elapsed: {}'.format(stop - start)

if __name__ == "__main__":
    main(sys.argv)
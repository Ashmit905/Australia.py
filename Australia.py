#!/usr/bin/env python3
# Libraries
import os
import sys
import getopt
import csv
import pandas as pd




def main(argv):

  if len(argv) < 2:
    print("Usage: ./Australia.py -i <AustraliaInputFile>")
    sys.exit(2)
  try:
    (opts, args) = getopt.getopt(argv, "i:", ["input="])
  except getopt.GetoptError:
    print("Usage: ./Australia.py -i <AustraliaInputFile>")
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print("Usage: ./Australia.py -i <AustraliaInputFile>")
      sys.exit()
    elif opt in ("-i", "--AustraliaInputFile"):
      inputFileName = arg

    ranks = []
    names = []
    count = []
    gender = []
    year = []
    total = 0
    wordCount = 0

    with open(inputFileName) as my_file:
      for line in (my_file):
        wordCount = 0
        total += 1
        for word in line.split(','):
          if (total != 1):
            wordCount += 1
            if (wordCount == 1):
              ranks.append(word)
            elif (wordCount == 2):
              names.append(word)
            elif (wordCount == 3):
              count.append(word)
            elif (wordCount == 4):
              gender.append(word)
            elif (wordCount == 5):
              year.append(word.strip())

    if total > 0:
      people = {
        'NAME': names,
        'GENDER': gender,
        'YEAR': year,
        'COUNT': count,
        'RANK': ranks
      }
      people_df = pd.DataFrame(people)
      people_df.sort_values(["NAME", "GENDER", "YEAR", "COUNT", "RANK"],
                            axis=0,
                            ascending=[True, False, False, False, False],
                            inplace=True)

      male_df = people_df[people_df['GENDER'] == "Male"]
      female_df = people_df[people_df['GENDER'] == "Female"]

      people_df.to_csv("Australia-all-baby-names-frequency_1952_to_2021.csv",
                       sep=',',
                       index=False,
                       encoding='utf-8')
      male_df.to_csv("Australia-male-baby-names-frequency_1952_to_2021.csv",
                     index=False,
                     encoding='utf-8')
      female_df.to_csv(
        "Australia-female-baby-names-frequency_1952_to_2021.csv",
        sep=',',
        index=False,
        encoding='utf-8')



if __name__ == "__main__":
  main(sys.argv[1:])

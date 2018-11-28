
#CS10
#1003181
#Homework 3 set 3
#Due exam 3


# Program Set 4(10 points extra credit)
# Biologists use a sequence of letters A, C, T, and G to model a genome. A gene is a substring of a genome that
# starts after a triplet ATG and ends before a triplet TAG, TAA, or TGA. Furthermore, the length of a gene string is
# a multiple of 3 and the gene does not contain any of the triplets ATG, TAG, TAA, and TGA.
# Write a program that prompts the user to enter a genome and displays all genes in the genome. If no gene is
# found in the input sequence, the program displays no gene is found. Allow the user to repeat the process as
# many times as the user wants until the user decides to quit. Here are the sample runs:
# >>>
# ========== RESTART: E:/HW3/HW3_4_genes.py ==========
# Enter a genome string: TTATGTTTTAAGGATGGGGCGTTAGTT
# TTT
# GGGCGT
# Enter a genome string: TGTGTGTATAT
# no gene is found
# >>>
# Test with 4 more genome strings.
# TGATGCTCTAAGGATGCGCCGTTGATT
# TGATGCTCTAGAGATGCGCCGTTGAATAT
# TGATGCGTCTAAGAGACTGCTCGCCGGTTGAATAT
# TGATGGCTCCTATGAGAATGGCGCCCGTTTCGAAATAT

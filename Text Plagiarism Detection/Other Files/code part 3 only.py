print("Hello User, This is a Python Plagiarism Detection program")
print("This project detects plagiarized texts .\n\n") 

from difflib import SequenceMatcher
import difflib

first_file = "C:/Users/utkarsh/Desktop/g1.txt"
second_file = "C:/Users/utkarsh/Desktop/g2.txt"

first_file_lines = str(open(first_file).readlines())
second_file_lines = str(open(second_file).readlines())

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


val = similar(first_file_lines, second_file_lines)*100
percentage = round(val, 2)
print(" Similarity Percentage :", percentage, "%")

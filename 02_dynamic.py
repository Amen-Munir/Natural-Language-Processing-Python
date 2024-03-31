from itertools import product
from nltk.tokenize import word_tokenize
import pandas as pd

# Tokenization of the sentence
Input_text= input("Enter a sentence: ")
text=Input_text.lower()
tokens = word_tokenize(text)
print("Tokenized text:", tokens)

# Loading my data from xl file 
excel_file = 'data.xlsx'
df = pd.read_excel(excel_file)

# Creating a dictionary for each of the values of matched keys 
matched_values_dict = {}
for column_key in df.columns:
    if column_key in tokens:
        matched_values_dict[column_key] = df[column_key].dropna().tolist()

print("Matched values dictionary:", matched_values_dict)


values_lists = list(matched_values_dict.values())


combinations = [' '.join(comb) for comb in product(*values_lists)]

# Print allcombinations
for sentence in combinations:
    print(sentence)

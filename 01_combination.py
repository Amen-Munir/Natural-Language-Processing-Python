from itertools import product
filename = open('words.txt', 'r')
lines = filename.readlines()
lists = [[] for _ in range(len(lines))]  

for i, line in enumerate(lines):
    words = line.strip().split()  
    for word in words:
        lists[i].append(word)  

filename.close()  

print(lists)



sentences = []
count=0
for combination in product(*lists):
    sentence = ' '.join(combination)
    sentences.append(sentence)
    count+=1

print(type(combination))

print("All possible combinations of sentences:")
for sentence in sentences:
    print(sentence)

with open("output.txt",'a') as f :
 for item in sentences:
    f.write(item +'\n')


 


print(count)


import  os
print(os.getcwd())
with open("input.txt", 'r') as input_file:
    entries = input_file.readlines()
    
entries = [int(i) for i in entries]
for i, ent in enumerate(entries):
    for j in range(i+1, len(entries)):
        for k in range(j+1, len(entries)):
            if ent + entries[j] + entries[k] == 2020:
                print(ent*entries[j]*entries[k])
                break

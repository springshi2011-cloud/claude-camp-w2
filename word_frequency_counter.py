#get input from user 
text = input("Enter a sentence: ")

if not text.strip():
    print("[Error] Input cannot be empty")
    exit(1)
     

#convert to lowercase and split into words
text = text.lower()
text = text.replace(".", "")
text = text.replace(",", "")
text = text.replace("!", "")
text = text.replace("?", "")
words = text.split()

#count frequency of each word
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1    
sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

#print word frequency
print("\nWord Frequency:")
for word, count in sorted_counts.items():
    print(f"{word}: {count}")


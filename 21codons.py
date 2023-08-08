# 21codons.py

# Print out all the codons for the sequence below in reading frame 1

# Hint: use the slice operator

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'
sequence = 'ATAAGCGAATATCTCTCATGAGAGGGAA'

def FrequencyMap(text, k):
	freq= {}
	n = len(text)
	for i in range(n-k+1):
			pattern = text[i:i+k]
			freq[pattern]=0
			for i in range(n-k+1):
			if text[i:i+k] == pattern:
					freq[pattern] = freq[pattern]+1
	return freq
	
test input: 3
text = 'ATAAGCGAATATCTCTCATGAGAGGGAA'


n = len(text)
for i in range(n-k+1):
	pattern= text[i:i+k]
	freq[pattern]=0




text = "ATAAGCGAATATCTCTCATGAGAGGGAA"
k = 3
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern]=0
        for j in range(n-k+1):
            if Pattern == Text[j:j+k]:
                freq[Pattern] += 1
    return freq


"""
python3 21codons.py
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""

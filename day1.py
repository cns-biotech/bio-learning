dna = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
a = dna.count('A')
g = dna.count('G')
t = dna.count('T')
c = dna.count('C')
total=len(dna)
print('DNA lenght is',total,'base pairs.')
gc=(g+c)/total*100
print('GC pairs',round(gc, 1),'%')
rna=dna.replace('T','U')
print('RNA sequence is', rna)
ta=dna.find('TA')
print('First TA in sequence is on', ta,"position")
print(dna[10:20])


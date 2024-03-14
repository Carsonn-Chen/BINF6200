from urllib.request import urlopen
from Bio import SeqIO
import re
import os

IDS = []
with open('rosalind_mprt.txt') as f:
    for line in f:
        IDS.append(line.strip())
# print(IDS)

for ID in IDS:
    if '_' in ID:
        ID = ID.split('_')[0]
    URL = 'http://www.uniprot.org/uniprot/' + ID + '.fasta'
    # print(URL)
    data = urlopen(URL)
    fasta = data.read().decode('utf-8', 'ignore')
    with open('seq_file.fasta', 'a') as text_file:
        text_file.write(fasta)

handle = open('seq_file.fasta', 'r')
motifs = re.compile(r'(?=(N[^P][ST][^P]))')
count = 0
for record in SeqIO.parse(handle, 'fasta'):
    sequence = record.seq
    positions = []
    for m in re.finditer(motifs, str(sequence)):
        positions.append(m.start() + 1)
    if len(positions) > 0:
        print(IDS[count])
        print(' '.join(map(str, positions)))
    count += 1

os.remove('seq_file.fasta')
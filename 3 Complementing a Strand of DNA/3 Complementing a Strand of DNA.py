seq = input()

def reverse_complement(seq):
    seq = ''.join([{'A':'T','T':'A','C':'G','G':'C'}.get(base, base) for base in reversed(seq)])
    return seq

print(reverse_complement(seq))

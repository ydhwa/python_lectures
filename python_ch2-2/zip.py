seq1 = {'foo', 'bar', 'baz'}
seq2 = {'one', 'two', 'three'}

z = zip(seq1, seq2)
print(z, type(z))

for t in z:
    print(t, type(t))

# DB 등에서 필요할 수 있다.
tl = [('foo', 'one'), ('bar', 'two'), ('baz', 'three')]
seq, seq2 = zip(*tl)
print(seq1)
print(seq2)

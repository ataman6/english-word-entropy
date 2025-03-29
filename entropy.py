import sys, math

def is_all_eng(s):
	return all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in s)

# words = []
freqs = []
total = 0

file = sys.stdin
for line in file:
	l = line.split()
	if len(l) != 3:
		continue

	s = l[1]

	try:
		f = int(l[2])
	except Exception:
		continue

	if f == 0:
		continue

	if not is_all_eng(s):
		continue

	# words.append(s)
	freqs.append(f)
	total += f

def entropy():
	return -math.fsum([(f / total) * math.log2(f / total) for f in freqs])

# print([(f / total) * math.log2(f / total) for f in freqs])
print(entropy())


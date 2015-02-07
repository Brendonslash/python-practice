import sys
rack = sys.argv[1]
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,"f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,"l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,"r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
			"x": 8, "z": 10}
def calc_scores(line):
	sum=0
	for p in line.rstrip():
		sum+=scores[p.lower()]
	return sum
f=open('sowpods.txt','r')
final={}
for line in f:
	temp2=[p for p in line.rstrip()]
	temp=rack
	count=0
	for x in temp:
		if x in temp2:
			temp2.remove(x)
	if len(temp2)==0:
		final[line.rstrip().lower()]=calc_scores(line)
for c in sorted([(value,key) for (key,value) in final.items()],reverse=True):
	print c




import random
listlen = len
def rand(dataset):
	ls = []
	for v,n in dataset.items():
		ls += [v] * n
	return random.choice(ls)
def rchoice(dt):
	keys = list(dt.keys())
	return random.choice(keys)
def Marcov(len,S,data):
	if(S not in data):
		return S + Marcov(len - 1,rchoice(data),data)
	elif(len == 1):
		return rand(data[S])
	else:
		s = rand(data[S])
		return s + Marcov(len - 1,s,data)
def gen(data):
	dt = []
	for i in range(1,listlen(data)):
		it = [data[i - 1],data[i]]
		dt.append(it)
	m = {}
	for i,j in dt:
		if(i not in m):
			m[i] = {}
			m[i][j] = 1
		elif(j not in m[i]):
			m[i][j] = 1
		else:
			m[i][j] += 1
	return m
def dict_comb(d1,d2):
	res = dict(d1)
	for k,v in d2.items():
		if(k in res):
			res[k] += d2[k]
		else:
			res[k] = d2[k]
	return res
fnamer = input()
fnamew = input()
splitter = input()
len = int(input())
s = input()
print('generating marcov model')
marcov = {}
with open(fnamer,'r') as f:
	line = f.readline()[:-1]
	if(splitter):
		line = line.split(splitter)
	else:
		line = list(line)
	m = gen(line)
	marcov = dict_comb(marcov,m)
print('marcov model all set')
print('start generaing unreadable rubbish text')
with open(fnamew,'w') as f:
	marc = Marcov(len,s,marcov)
	f.write(splitter.join([str(i) for i in marc]))
print('unreadable rubbish text generated')

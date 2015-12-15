dataDic = {}
for name in df['Origin']:
    if name in dataDic:
        dataDic[name] += 1
    else:
        dataDic[name] = 1


def nbest(datadic, N = None):
    tups = datadic.items()
    tups = sorted(tups, key = lambda x: x[1], reverse = True)
    if N:
        return tups[:N]
    else:
        return tups

nbest(dataDic, 10)

n = 4
names, vals = zip(*nbest(dataDic, n))
names, vals = list(names), list(vals)
# print names
df2 = pd.DataFrame(vals, columns =['id'])
df2.plot(kind='bar')
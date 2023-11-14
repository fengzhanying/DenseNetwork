import numpy as np

f = open('/home/fengzhanying/data/Annotation/TranscriptFactor/Human-TF.csv')
allTF = f.readlines();f.close()
allTF = [allTF[i].strip('\n') for i in range(len(allTF))]

f = open('../CNCCNetwork_CleanMatrix.txt')
net = f.readlines();f.close()
for i in range(len(net)):
	net[i] = net[i].split('\t')
	for j in range(len(net[i])):
		net[i][j] = float(net[i][j])
net = np.array(net).T.tolist()
f = open('../CNCCNetwork_CleanTG.txt')
TG = f.readlines();f.close()
print(len(TG),len(net))
for i in range(len(TG)-1,-1,-1):
	if TG[i].strip('\n') not in allTF:
		del TG[i];del net[i]
net = np.array(net).T.tolist()
print(len(TG),len(net),len(net[0]))
g1 = open('CNCCNetwork_Clean_TFMatrix.txt','w')
g2 = open('CNCCNetwork_Clean_TG.txt','w')
for i in range(len(net)):
	for j in range(len(net[i])-1):
		g1.write(str(net[i][j])+'\t')
	g1.write(str(net[i][len(net[i])-1])+'\n')
for i in range(len(TG)):
	g2.write(TG[i])
g1.close();g2.close()

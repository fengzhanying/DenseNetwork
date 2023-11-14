f = open('CNCCNetwork_Clean_TFClass.txt')
TF = f.readlines();f.close()
TF = [TF[i].split('\t')[0] for i in range(len(TF))]

f = open('/home/fengzhanying/Project4/Model/Test2/CUT150/Val/CNCCNetwork_CleanExpMatrix.txt')
mat = f.readlines();f.close()
f = open('/home/fengzhanying/Project4/Model/Test2/CUT150/Val/CNCCNetwork_CleanExpTF.txt')
cleanTF = f.readlines();f.close()
cleanTF = [cleanTF[i].strip('\n') for i in range(len(cleanTF))]

g = open('DenseTFMatrix.txt','w')
for i in range(len(mat)):
	if cleanTF[i] in TF:
		g.write(cleanTF[i]+'\t'+mat[i])
g.close()

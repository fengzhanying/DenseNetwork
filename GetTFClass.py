f = open('/home/fengzhanying/data/Annotation/TranscriptFactor/Human-TF.csv')
alltf = f.readlines();f.close()
alltf = [alltf[ii].strip('\n') for ii in range(len(alltf))]

f = open('CNCCNetwork_Clean_TF.txt')
TF = f.readlines();f.close()
TF = [TF[i].strip('\n') for i in range(len(TF))]
f = open('CNCCNetwork_Clean_TFCoeffient.txt')
TFC = f.readlines();f.close()
del TFC[0]
TFC = [TFC[i].strip('\n').split('\t') for i in range(len(TFC))]

f = open('CNCCNetwork_Clean_TG.txt')
TG = f.readlines();f.close()
TG = [TG[i].strip('\n') for i in range(len(TG))]
f = open('CNCCNetwork_Clean_TGCoeffient.txt')
TGC = f.readlines();f.close()
del TGC[0]
TGC = [TGC[i].strip('\n').split('\t') for i in range(len(TGC))]

cutoff = 0.05
g = open('CNCCNetwork_Clean_TFClass.txt','w')
for i in range(len(alltf)):
	if alltf[i] in TF or alltf[i] in TG:
		if alltf[i] in TF and alltf[i] not in TG and float(TFC[TF.index(alltf[i])][1]) > 0.1:
			g.write(alltf[i]+'\tUpstream\n');
		if alltf[i] not in TF and alltf[i] in TG and float(TGC[TG.index(alltf[i])][1]) > 0.05:
			g.write(alltf[i]+'\tDownstream\n');
		if alltf[i] in TF and alltf[i] in TG:
			indel1 = TF.index(alltf[i]);indel2 = TG.index(alltf[i])
			if float(TFC[indel1][1]) > 0.1 and float(TGC[indel2][1]) > 0.05:
				g.write(alltf[i]+'\tCore\n');
			if float(TFC[indel1][1]) > 0.1 and float(TGC[indel2][1]) < 0.05:
				g.write(alltf[i]+'\tUpstream\n')
			if float(TFC[indel1][1]) < 0.1 and float(TGC[indel2][1]) > 0.05:
				g.write(alltf[i]+'\tDownstream\n');
g.close()
		
f = open('CNCCNetwork_Clean_TFClass.txt')
TFC = f.readlines();f.close()
TFC = [TFC[j].strip('\n').split('\t') for j in range(len(TFC))]

f = open('../CNCCNetwork_Clean.txt')
net = f.readlines();f.close()
for j in range(len(net)):
	net[j] = net[j].split('\t')
	del net[j][len(net[j])-1];del net[j][len(net[j])-1]
	net[j] = net[j][0]+'\t'+net[j][1]
pool = ['UpstreamCore','UpstreamDownstream','CoreDownstream']
g = open('CNCCNetwork_Clean_DenseTFNet.txt','w')
for j in range(len(TFC)):
	for k in range(len(TFC)):
		if TFC[j][1] + TFC[k][1] in pool and (TFC[j][0]+'\t'+TFC[k][0]) in net:
			g.write(TFC[j][0]+'\t'+TFC[k][0]+'\n')
g.close()

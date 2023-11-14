data = dlmread('CNCCNetwork_Clean_TFMatrix.txt','\t');
TF = importdata('CNCCNetwork_Clean_TF.txt');
TG = importdata('CNCCNetwork_Clean_TG.txt');

[TFC, TGC, Obj]= FindSubNetwork(2,data);
TFC = full(TFC);
TGC = full(TGC);
fid=fopen('CNCCNetwork_Clean_TFCoeffient.txt','wt');
	fprintf(fid, '%s\t','TF');
	fprintf(fid, '%s\n','Coefficient');
for i=1:size(TF,1)
	fprintf(fid, '%s\t',TF{i,1});
	fprintf(fid, '%g\n',TFC(i));
end
fclose(fid);

fid=fopen('CNCCNetwork_Clean_TGCoeffient.txt','wt');
fprintf(fid, '%s\t','TG');
fprintf(fid, '%s\n','Coefficient');
for i=1:size(TG,1)
	fprintf(fid, '%s\t',TG{i,1});
	fprintf(fid, '%g\n',TGC(i));
end
fclose(fid);

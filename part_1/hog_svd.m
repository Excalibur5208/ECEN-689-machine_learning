function hog_svd(name)
pathIn = ['figs\',name];
class = 0;
if strncmpi(name,'dog',3),
	class = 1;
end;

im = single(vl_imreadbw(pathIn));

cellSize = 8;
hog = vl_hog(im, cellSize);

XHog = zeros(size(hog,1)*size(hog,2),size(hog,3));
for i=1:size(hog,1),
	for j=1:size(hog,2),
		for k=1:size(hog,3),
			XHog((i-1)*size(hog,2)+j,k)= hog(i,j,k);
		end;
	end;
end;

X = [svd(XHog)' class];

fid=fopen('svd.txt', 'at');
for i=1:size(X,2),
	fprintf(fid,'%f',X(i));
	if i<size(X,2),
		fprintf(fid,'\t');
	end;
end;
fprintf(fid,'\n');
fclose(fid);
function python_matlab(image)

run('C:\Program Files\vlfeat-0.9.20\toolbox\vl_setup.m');
im = single(vl_imreadbw(image));
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
X_svd = svd(XHog)';

data = load ('svd.txt');
traningX = data(:,1:30);
traningY = data(:,32);
mdl = fitcknn(traningX,traningY,'NumNeighbors',6);
label = predict(mdl,X_svd(:,1:30));

fid=fopen('result.txt', 'wt');
fprintf(fid,'%d',int8(label(1)));
fclose(fid);
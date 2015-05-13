function python_matlab(image_dir, result_text)

run('C:\\Program Files\\vlfeat-0.9.20\\toolbox\\vl_setup.m');

di = dir([image_dir '\\*.jpg']);
X_svd = zeros(0,0);
for k=1:length(di),
	name = di(k).name;
	im = single(vl_imreadbw([image_dir name]));
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
	P = svd(XHog)';
	X_svd = [X_svd;P(1,:)];
end;

data = load ('D:\\mysite_2\\uploads\\svd.txt');
traningX = data(:,1:30);
traningY = data(:,32);
mdl = fitcknn(traningX,traningY,'NumNeighbors',6);
label = predict(mdl,X_svd(:,1:30));

fid=fopen(result_text, 'wt');
for k=1:length(di),
	fprintf(fid,'%d\n',int8(label(k)));
end;

fclose(fid);


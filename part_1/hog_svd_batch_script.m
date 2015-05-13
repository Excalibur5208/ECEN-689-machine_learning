di = dir('figs\*.jpg');
for k=1:length(di)
	name = di(k).name;
	hog_svd(name);
end;
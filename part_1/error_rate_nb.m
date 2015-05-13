function error_rate = error_rate_nb(data)

base = 0;
rate = 0.1;

for i=1:size(data,1),
	if data(i,32) == 1,
		base = i;
		break;
	end;
end;

traningX=data(floor(rate*base):base-1,1:30);
traningX=[traningX;data(base+floor(rate*(size(data,1)-base)):size(data,1),1:30)];
traningY=data(floor(rate*base):base-1,32);
traningY=[traningY;data(base+floor(rate*(size(data,1)-base)):size(data,1),32)];

testX=data(1:floor(rate*base)-1,1:30);
testX=[testX;data(base:base+floor(rate*(size(data,1)-base)),1:30)];
testY=data(1:floor(rate*base)-1,32);
testY=[testY;data(base:base+floor(rate*(size(data,1)-base)),32)];

mdl = fitcnb(traningX,traningY);
label = predict(mdl,testX);
error_rate = mean(label ~= testY);
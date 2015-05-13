data = load ('svd.txt');
error_rate_knn = error_rate_knn(data);
error_rate_svm = error_rate_svm(data);
error_rate_nb = error_rate_nb(data);
error_rate_dt = error_rate_dt(data);
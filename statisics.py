from statistics import mean,median,stdev,mode

list = [5, 6, 33, 4, 5, 6, 11, 17, 19, 100,]
print(max(list))
print(min(list))
print(mean(list))
print(max(set(list), key=list.count))

setwd('E:\\djVacs\\root\\temp')

data1 = read.table('grp_734357.csv', header=T, sep="")

newfnames = list(c("grp_1975463.csv", "grp_2235923.csv", "grp_252652.csv", 
"grp_2919822.csv", "grp_3178606.csv", "grp_3763699.csv", 
"grp_3772252.csv", "grp_3994181.csv", "grp_4866528.csv", 
"grp_4914699.csv", "grp_5384956.csv", "grp_5408395.csv", 
"grp_5482575.csv", "grp_6023023.csv", "grp_6236654.csv", 
"grp_6490457.csv", "grp_653721.csv", "grp_6895957.csv", 
"grp_7027412.csv", "grp_7084573.csv", "grp_723457.csv", 
"grp_734357.csv", "grp_7507794.csv", "grp_7525847.csv", 
"grp_7878133.csv", "grp_7902357.csv", "grp_8237798.csv", 
"grp_8398877.csv", "grp_8457399.csv", "grp_8752462.csv", 
"grp_8833737.csv", "grp_9017763.csv", "grp_916542.csv", 
"grp_9395583.csv", "grp_9731264.csv"))

files = c('grp_1097086.csv',
 'grp_1182815.csv',
 'grp_1237645.csv',
 'grp_1283141.csv',
 'grp_1288775.csv',
 'grp_1760946.csv',
 'grp_1990531.csv',
 'grp_2146950.csv',
 'grp_2408980.csv',
 'grp_2534288.csv',
 'grp_2995929.csv',
 'grp_3013926.csv',
 'grp_3064429.csv',
 'grp_3108597.csv',
 'grp_3192697.csv',
 'grp_3681326.csv',
 'grp_3935842.csv',
 'grp_4175680.csv',
 'grp_4219253.csv',
 'grp_4423050.csv',
 'grp_4578889.csv',
 'grp_4636490.csv',
 'grp_4836567.csv',
 'grp_5025021.csv',
 'grp_5090223.csv',
 'grp_5094880.csv',
 'grp_5142335.csv',
 'grp_5375396.csv',
 'grp_5533953.csv',
 'grp_6443306.csv',
 'grp_6474910.csv',
 'grp_6571594.csv',
 'grp_6808502.csv',
 'grp_6818168.csv',
 'grp_7061771.csv',
 'grp_7406816.csv',
 'grp_7425698.csv',
 'grp_7440652.csv',
 'grp_7663715.csv',
 'grp_8031106.csv',
 'grp_8044028.csv',
 'grp_8365300.csv',
 'grp_8478489.csv',
 'grp_8712114.csv',
 'grp_8795807.csv',
 'grp_8852354.csv',
 'grp_9232489.csv',
 'grp_9531261.csv',
 'grp_9594839.csv',
 'grp_9818543.csv')

fnames = strsplit(files, ",\n ")
fnames

#hist(data1[1:20,1], c(0,1,2,3))
#data1[1:20,1]

analyzeCSV <- function(x){
x20 = x[1:20,1]
x40 = x[21:40,1]
x60 = x[41:60,1]
x80 = x[61:80,1]
x100 = x[81:100,1]
par(mfrow=c(1,2))
hist(x20, col="#ff0000",density=15, ylim=c(0,15), angle=15, breaks=c(0,1,2,3), main = names(x))
#lines.histogramm(x40, col="#00ff00")
hist(x40, add=T , col="#00ff00", density=15, angle=35, breaks=c(0,1,2,3))
hist(x60, add=T , col="#0000ff", density=15, angle=55, breaks=c(0,1,2,3))
hist(x80, add=T , col="#880088", density=15, angle=75, breaks=c(0,1,2,3))
hist(x100, add=T , col="#888800", density=15, angle=95, breaks=c(0,1,2,3))
hist(x[1:100,1], col="#ff0000",density=15, ylim=c(0,55), angle=15, breaks=c(0,1,2,3))
hist(x[101:150,1], add=T , col="#888800", density=15, angle=135, breaks=c(0,1,2,3))
hist(x[151:200,1], add=T , col="#008888", density=15, angle=65, breaks=c(0,1,2,3))
savePlot(filename= paste("./",as.character(names(x)),".jpg"), type="jpeg")
}
analyzeCSV(data1)
analyzeCSV(data2)
analyzeCSV(data3)
analyzeCSV(data4)
analyzeCSV(data5)
#1-5 alle kacke

dim(fnames)[0]
ncol(fnames[])
length(newfnames[[1]])
for (i in 1:length(newfnames[[1]])){
	data = read.table(newfnames[[1]][i], header=T, sep="");
	analyzeCSV(data);
}

files[5]

for (i in 1:length(files)){
	data = read.table(files[i], header=T, sep="");
	analyzeCSV(data);
}

clean_fnames = sub("'","",fnames)
clean_fnames

plot(data1[20:35,1], type="h", add=T)
hist(data1[20:35,1], add=T , col="#00ff00", density=15)
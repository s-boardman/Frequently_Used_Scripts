> library(ggplot2) #load ggplot2
> data<-read.table("C:/Documents and Settings/BoardmanS/Desktop/normals.txt", header=TRUE) #open data file
> attach(data) #attach data file
> summary(data) #summary of data file
       x        normals     
 Min.   :1   Min.   :0.840  
 1st Qu.:1   1st Qu.:0.900  
 Median :1   Median :0.945  
 Mean   :1   Mean   :0.976  
 3rd Qu.:1   3rd Qu.:1.025  
 Max.   :1   Max.   :1.170  
> p <- ggplot(data,aes(factor(x),normals)) #specify starting plot structure
> p +geom_boxplot() #specify plot type (boxplot))
> p +geom_boxplot() +geom_jitter() #add individual data points, jittered
> p +geom_boxplot(aes(fill = "green80")) +geom_jitter() #specify colour of box plot
> p +geom_boxplot(aes(fill = "green80")) +geom_jitter() +scale_x_discrete(breaks=NULL)
> p +geom_boxplot(aes(fill = "green80")) +geom_jitter() +theme(axis.title.x = element_blank()) #remove x axis title and values
> p +geom_boxplot(aes(fill = "green80")) +geom_jitter() +theme(axis.title.x = element_blank()) +scale_x_discrete(breaks=NULL) #remove tick marks
> p +geom_boxplot(aes(fill = "green80")) +geom_jitter() +theme(axis.title.x = element_blank()) +scale_x_discrete(breaks=NULL) +ylab("Relative Quantitation (RQ)") +guides(fill=FALSE) #remove legend
> p +geom_boxplot(aes(fill = "green80")) +geom_jitter() +theme(axis.title.x = element_blank()) +scale_x_discrete(breaks=NULL) +ylab("Relative Quantitation (RQ)") +guides(fill=FALSE) + theme(panel.grid.minor=element_blank(), panel.grid.major=element_blank()) #remove gridlines

> p +geom_boxplot(aes(fill = "green80")) +
	#plot boxplot with a green fill
	geom_jitter() +
	#insert data points, jittered
	theme(axis.title.x = element_blank()) +
	#remove x axis label
	scale_x_discrete(breaks=NULL) +
	#remove x axis ticks
	ylab("Relative Quantitation (RQ)") +
	#rename y axis label
	guides(fill=FALSE) +
	#remove legend
	theme(panel.grid.minor=element_blank(), panel.grid.major=element_blank())
	#remove gridlines
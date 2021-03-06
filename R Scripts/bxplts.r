rqs<-read.delim("C:/Documents and Settings/BoardmanS/Desktop/qpcrrqs.txt")
attach(rqs)
library(ggplot2)
p <- ggplot(rqs, aes(factor(result), rq))
bxplt <- p + geom_boxplot(position = position_dodge(width = .9), outlier.colour = "red", outlier.size = 2) + geom_jitter()+ scale_y_continuous(breaks=seq(0, 2, 0.25)) + scale_x_discrete(limits=c("deletion","normal","duplication")) + ylab("Relative Quantitation") + xlab("Patient Copy Number")
bxplt2 <- p + geom_boxplot(position = position_dodge(width = .9), outlier.colour = "red", outlier.size = 2) + geom_jitter()+ scale_y_continuous(breaks=seq(0, 2, 0.25)) + facet_wrap(~type) + scale_x_discrete(limits=c("deletion","normal","duplication")) + ylab("Relative Quantitation") + xlab("Patient Copy Number")
pdf("bxplt.pdf")
plot(bxplt)
dev.off()
pdf("bxplt2.pdf")
plot(bxplt2)
dev.off()

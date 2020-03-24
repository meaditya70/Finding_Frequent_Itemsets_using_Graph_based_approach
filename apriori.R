mat<-read.table("F:/Research/Frequent Itemsets/data/mbd.txt",header=FALSE,sep=",")
mat=as.matrix(mat)
txn=as(mat,"transactions")

library(arules)

basket_rules <- apriori(txn,parameter = list(sup = 0.8,target="frequent itemsets"))

inspect(basket_rules)

df_basket <- as(basket_rules,"data.frame")

View(df_basket)

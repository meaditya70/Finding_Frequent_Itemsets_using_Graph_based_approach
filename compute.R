mat<-read.table("F:/Research/Frequent Itemsets/data/newdatabase.txt",header=FALSE,sep=",")
mat=as.matrix(mat)

library(igraph)
g=graph.adjacency(mat,mode="undirected",weighted=TRUE,diag=FALSE)

eigMat=eigen_centrality(g)
pageRank=page_rank(g)

write.table(eigMat$vector,file="F:/Research/Frequent Itemsets/data/eigenValues.txt",row.names=FALSE)
write.table(pageRank$vector,file="F:/Research/Frequent Itemsets/data/pageRank.txt",row.names=FALSE)
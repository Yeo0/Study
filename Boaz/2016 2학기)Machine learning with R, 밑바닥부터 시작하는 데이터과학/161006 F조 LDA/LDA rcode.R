#### 어느 공장에서 ring을 만든 후에 ring의 Curvature(곡률)과 Diameter(직경)을 검사 ####

QC_result<-factor(c(1,1,1,1,2,2,2),labels = c("Passed","Not Passed"))
levels(QC_result)

Curvature<-scan()
2.95
2.53
3.57
3.16
2.58
2.16
3.27

Diameter<-scan()
6.63
7.79
5.65
5.47
4.46
6.22
3.52


train_d<-as.data.frame(cbind(QC_result,Curvature,Diameter))
train_d


## train data plot
plot(Curvature,Diameter,xlim=c(2,4),ylim=c(2,9),col=as.numeric(QC_result),pch=as.numeric(QC_result))
legend("topright", levels(QC_result), col=c(1,2),pch =c(1,2) , bg="white")


## independent variables 
X<-cbind(Curvature,Diameter)
 
## 품질검사를 통과한 그룹에 속하는 data
X1<-subset(X,QC_result=="Passed")

## 품질검사를 통과하지 못한 그룹에 속하는 data 
X2<-subset(X,QC_result=="Not Passed")

## dependenet variable 
y<-as.matrix(as.numeric(QC_result))


#### mean vector ####

## 각 그룹의 mean vector
mu1<-round(t(as.matrix(apply(X1,2,mean))),3) # round 함수를 사용해서 소수점 셋째자리까지만 표현 
mu2<-round(t(as.matrix(apply(X2,2,mean))),3)

## 전체 data의 mean vector
mu<-round(t(as.matrix(apply(X,2,mean))),3)


#### variance-covariance matrix ####

## 각 그룹의 표본수 
n1<-nrow(X1)
n2<-nrow(X2)

## 각 그룹의 variance-covariance matrix

C1<-round(t(X1-matrix(rep(1,n1),n1,1)%*%mu)%*%(X1-matrix(rep(1,n1),n1,1)%*%mu)/(n1-1),3)
C2<-round(t(X2-matrix(rep(1,n2),n2,1)%*%mu)%*%(X2-matrix(rep(1,n2),n2,1)%*%mu)/(n2-1),3)

# round(t(X1-rep(mu,each=n1))%*%(X1-rep(mu,each=n1))/(n1-1),3)
# round(t(X2-rep(mu,each=n2))%*%(X2-rep(mu,each=n2))/(n2-1),3)


## pooled within group variance-covariance matrix

C<-round(((n1-1)*C1+(n2-1)*C2)/(n1+n2-2),3)


round(solve(C),3)


#### 결정 경계(Decision Boundary) 그리기 - Fisher's Discriminant function ####

W = round(solve(C)%*%(t(mu1-mu2)),3)
Z1=round(t(W)%*%t(mu1),3)
Z2=round(t(W)%*%t(mu2),3)
Z1;Z2
Z=round((n1*Z1+n2*Z2)/(n1+n2),3)
Z
W
# 2.493*X1+1.037*X2=13.089
# X2=-2.493/1.037*X1+13.089/1.037
round(-2.493/1.037,3)
round(13.089/1.037,3)

p<-seq(2,4,length.out=100) #X1
q<--2.404*p+12.622     #X2

plot(Curvature,Diameter,xlim=c(2,4),ylim=c(2,9),col=as.numeric(QC_result),pch=as.numeric(QC_result))
legend("topright", levels(QC_result), col=c(1,2),pch =c(1,2) , bg="white")
lines(p,q)
points(2.81,5.46,pch=3, col="blue")

x_p<-matrix(c(2.81,5.46),2,1)

round(abs(t(W)%*%(x_p-t(mu1))),3)
round(abs(t(W)%*%(x_p-t(mu2))),3) # Not passed 로 분류


#### Linear Disciminant function (ISLR 책에 나온 방법) ####

x_p<-matrix(c(2.81,5.46),1,2) # 예측하고자 하는 data point

f_p1<-round(mu1%*%solve(C)%*%t(x_p)-0.5*mu1%*%solve(C)%*%t(mu1)+log(n1/(n1+n2)),3)
f_p2<-round(mu2%*%solve(C)%*%t(x_p)-0.5*mu2%*%solve(C)%*%t(mu2)+log(n2/(n1+n2)),3)

f1<-c()
for (i in 1:nrow(X)){
  f1[i]<-round(mu1%*%solve(C)%*%as.matrix(X[i,])-0.5*mu1%*%solve(C)%*%t(mu1)+log(n1/(n1+n2)),3)
} 

f2<-c()
for (i in 1:nrow(X)){
  f2[i]<-round(mu2%*%solve(C)%*%as.matrix(X[i,])-0.5*mu2%*%solve(C)%*%t(mu2)+log(n2/(n1+n2)),3)
} 

f1;f2
f_p1;f_p2

a<-1:100
b<-1:100

plot(f1,f2,col=as.numeric(QC_result),pch=as.numeric(QC_result))
legend("topleft", levels(QC_result), col=c(1,2),pch =c(1,2) , bg="white")
lines(a,b) # f2=f1인 직선
points(31.166,31.11,pch=3,col="blue") # Passed로 분류. 위와 결과가 다르게 나옴 


(mu1-mu2)%*%solve(C)%*%t(x_p)-0.5*(mu1-mu2)%*%solve(C)%*%t(mu1-mu2)












## 공분산행렬 구할때 n-1 대신 n을 사용함 

x_p<-matrix(c(2.81,5.46),1,2) # 예측하고자 하는 data point

f_p1<-round(mu1%*%solve(C)%*%t(x_p)-0.5*mu1%*%solve(C)%*%t(mu1)+log(n1/(n1+n2)),3)
f_p2<-round(mu2%*%solve(C)%*%t(x_p)-0.5*mu2%*%solve(C)%*%t(mu2)+log(n2/(n1+n2)),3)

f1<-c()
for (i in 1:nrow(X)){
  f1[i]<-round(mu1%*%solve(C)%*%as.matrix(X[i,])-0.5*mu1%*%solve(C)%*%t(mu1)+log(n1/(n1+n2)),3)
} 

f2<-c()
for (i in 1:nrow(X)){
  f2[i]<-round(mu2%*%solve(C)%*%as.matrix(X[i,])-0.5*mu2%*%solve(C)%*%t(mu2)+log(n2/(n1+n2)),3)
} 

f1;f2
f_p1;f_p2

a<-1:100
b<-1:100

plot(f1,f2,col=as.numeric(QC_result),pch=as.numeric(QC_result))
legend("topleft", levels(QC_result), col=c(1,2),pch =c(1,2) , bg="white")
lines(a,b) # f2=f1인 직선
points(31.166,31.11,pch=3,col="blue")


(mu1-mu2)%*%solve(C)%*%t(x_p)-0.5*(mu1-mu2)%*%solve(C)%*%t(mu1-mu2)

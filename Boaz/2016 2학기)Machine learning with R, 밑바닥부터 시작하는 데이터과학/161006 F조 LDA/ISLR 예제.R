library(ISLR)

attach(Smarket)

names(Smarket)
str(Smarket)
unique(Year)

train<-(Year<2005)
trainset<-Smarket[train,]
Smarket.2005<-Smarket[!train,]
Direction.2005<-Direction[!train]

str(Direction)
head(Smarket)
levels(Direction)

plot(trainset$Lag1,trainset$Lag2,col=as.numeric(trainset$Direction),pch=as.numeric(trainset$Direction))
legend("topright",levels(trainset$Direction),col=c(1,2),pch=c(1,2))

plot(Smarket.2005$Lag1,Smarket.2005$Lag2,col=as.numeric(Smarket.2005$Direction),pch=as.numeric(Smarket.2005$Direction))
legend("topright",levels(trainset$Direction),col=c(1,2),pch=c(1,2))

X<-cbind(trainset$Lag1,trainset$Lag2)
y<-as.matrix(as.numeric(trainset$Direction))

X1<-subset(X,trainset$Direction=="Down")
X2<-subset(X,trainset$Direction=="Up")

#### mean vector ####

# 각 그룹의 mean vector
mu1<-t(as.matrix(round(apply(X1,2,mean),3)))
mu2<-t(as.matrix(round(apply(X2,2,mean),3)))

# 전체 data의 mean vector
mu<-t(as.matrix(round(apply(X,2,mean),3)))  # 소수점 셋째자리까지 표시 

#### variance-covariance matrix ####

# 각 그룹의 표본수 
n1<-nrow(X1)
n2<-nrow(X2)

# 각 그룹의 variance-covariance matrix
C1<-round(t(X1-rep(mu,each=n1))%*%(X1-rep(mu,each=n1))/(n1-1),3)
C2<-round(t(X2-rep(mu,each=n2))%*%(X2-rep(mu,each=n2))/(n2-1),3)

# pooled within group variance-covariance matrix

C<-round(((n1-1)*C1+(n2-1)*C2)/(n1+n2-2),3)

#### 결정 경계(Decision Boundary) 그리기 - Fisher's Discrimiant function ####
W = round(solve(C)%*%(t(mu1-mu2)),3)
Z1=round(t(W)%*%t(mu1),3)
Z2=round(t(W)%*%t(mu2),3)
Z1;Z2
Z=(n1*Z1+n2*Z2)/(n1+n2)
-6.412826e-05*100000
W

# 0.056*Lag1+0.044*Lag2=0.00006
# 0.44*Lag2=-0.056*Lag1+0.00006
# Lag2=-0.056/0.044*Lag1+0.00006/0.044

round(-0.056/0.044,3)
round(0.00006/0.044,3)

p<-seq(-6,6,length.out=100)
q=-1.273*p+0.001

plot(Smarket.2005$Lag1,Smarket.2005$Lag2,col=as.numeric(Smarket.2005$Direction),pch=as.numeric(Smarket.2005$Direction))
legend("topright",levels(Smarket.2005$Direction),col=c(1,2),pch=c(1,2))
lines(p,q)

points(-0.134 , 0.008, col="green", pch=20) # Up

# 직선 위쪽이 Down, 아래쪽이 Up


#### Linear Disciminant function (ISLR 책에 나온 방법) ####

x_p<-cbind(Smarket.2005$Lag1,Smarket.2005$Lag2) # 예측하고자 하는 data point

class(x_p[1,])
as.matrix(x_p[1,])

f_p1<-round(mu1%*%solve(C)%*%as.matrix(x_p[1,])-0.5*mu1%*%solve(C)%*%t(mu1)+log(n1/(n1+n2)),3)
f_p2<-round(mu2%*%solve(C)%*%as.matrix(x_p[1,])-0.5*mu2%*%solve(C)%*%t(mu2)+log(n2/(n1+n2)),3)

X[1,]

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

a<-seq(-1,1,length.out = 100)
b<-a

plot(f1,f2,col=as.numeric(Direction.2005),pch=as.numeric(Direction.2005))
legend("topright", levels(Direction.2005), col=c(1,2),pch =c(1,2) , bg="white")
lines(a,b) # f2=f1인 직선

plot(f_p1,f_p2,xlim=c(-1,1),ylim=c(-1,1))
lines(a,b)
points(f1,f2,col=as.numeric(Direction.2005),pch=as.numeric(Direction.2005)) # Up

# Down =1 Up =2

plot(f1,f2,col=as.numeric(Direction.2005),pch=as.numeric(Direction.2005))
points(f_p1,f_p2,xlim=c(-1,1),ylim=c(-1,1),col="blue",cex=5,pch=3)
lines(a,b)
 # Up




# lda ftn
library(MASS)
library(ISLR)
lda.fit<-lda(Direction~Lag1+Lag2,data=Smarket,subset=train)
lda.fit

# -0.642*Lag1-0.514*Lag2

plot(lda.fit)

lda.pred<-predict(lda.fit, Smarket.2005)
lda.pred$posterior
names(lda.pred)
lda.class<-lda.pred$class
table(lda.class,Direction.2005)

mean(lda.class==Direction.2005)

sum(lda.pred$posterior[,1]>=0.5)
sum(lda.pred$posterior[,1]<0.5)

lda.pred$posterior[1:20,1]
lda.class[1:20]

# -0.134  0.008
# $posterior
#         Down        Up
# 999  0.4901792 0.5098208

# Up



install.packages("klaR")
library(klaR)
partimat(Direction~Lag1+Lag2,data=Smarket,subset=train,method="lda")





#### MASS 라이브러리 사용 ####


library(MASS)

lda.fit2<-lda(QC_result~Curvature+Diameter,data=train_d)
lda.fit2
plot(lda.fit2)

??MASS

pred2<-as.data.frame(matrix(c(2.81,5.46,3,5,2,5,3,4,2,4,3,6,2,6),7,byrow=T))

names(pred2)<-c("Curvature","Diameter")

pred_d<-as.data.frame(matrix(c(2.81,5.46),1,2,byrow=T))
names(pred_d)<-c("Curvature","Diameter")

lda.pred2<-predict(lda.fit2,pred_d)
lda.pred2

table(lda.pred2$class,QC_result)

lda.pred2$posterior[,1]>0.5

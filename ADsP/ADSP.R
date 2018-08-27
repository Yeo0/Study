#####ADSP#####

#날짜
Sys.Date()
as.Date("2017-05-13")
as.Date(05/13/2026,format=%m/%d/%Y)
str(iris)
mfrow=c(1,2)

#산점도
plot(iris)
plot(iris[1:4]) = pairs(iris[1:4])

plot(iris[1:4], main="Iris", col=c("red","blue","green")[unclass(iris$Species)])
pairs(iris[1:4], main="Iris", pch=21, bg=c("red", "blue","green")[unclass(iris$Species)])#bg-서로다른 색상

?unclass
hist(iris[1])

#reshape
install.packages("reshape")
library(reshape)

data(airquality)
head(airquality)
names(airquality)=tolower(names(airquality))
names(airquality)

aqm=melt(airquality, id=c("month","day"), na.rm=T)
head(aqm)
a<-cast(aqm, day~month~variable)
a
b<-cast(aqm,month~variable,mean)
head(b)
c<-cast(aqm,month~.|variable, mean)
c
d<-cast(aqm,month~variable, mean, margins=c("grand_row","grand_col"))
d
e<-cast(aqm,day~month, mean, subset=variable=="ozone")
e
f<-cast(aqm,month~variable, range)
f


#sqldf
install.packages("sqldf")
library(sqldf)

head(sqldf("select Species from iris"))
sqldf("select * from iris limit 10")
sqldf("select count(*) from iris where Species like 'se%'")


#plyr
?set.seed
set.seed(1) #같은 난수 생성, 괄호 안에 숫자는 뭐가 들어가든 상관없음
d=data.frame(year=rep(2012:2014, each=6), count=round(runif(9,0,20)))
d
?rep

install.packages("plyr")
library(plyr)
ddply(d, )
?ddply
ddply(d,"year",function(x){
  mean.count=mean(x$count)
  sd.count=sd(x$count)
  cv=sd.count/mean.count
  data.frame(cv.count=cv)
})
  
  
ddply(d,"year",summarise,cv.count=sd(count)/mean(count)) #위랑 동일한 결과 (summarise함수이용)

ddply(d,"year",summarise, mean.count=mean(count))
ddply(d,"year",transform, total.count=sum(count))


#data.table
install.packages("data.table")
library(data.table)

dt<-data.table(x=c("b","b","b","a","a"),v=rnorm(5))
dt

CARS<-data.table(cars)
class(CARS)
sapply(CARS,class)

dt[2,]
dt[dt$x=="b",]
setkey(dt,x)
?setkey
dt #정렬순서 바뀜
dt["b"]
dt["b",mult="first"] #b의 first
dt["b",mult="last"]
?data.table
dim(dt)

grpsize<-ceiling(1e7/26^2)초 #천만개의 행과 676개 그
tt<-system.time(DF<-data.frame(
  x=rep(LETTERS, each=26*grpsize),
  y=rep(letters, each=grpsize),
  v=runif(grpsize*26^2),
  stringAsFactors=FALSE)
)
tt #생성하는데 3초

?system.time

head(DF,3)
tail(DF,3)
dim(DF)
tt<-system.time(ans1<-DF[DF$x=="R"&DF$y=="h",])
tt # data.frame은 하나하나 모든 자료를 비교해 찾는 벡터 검색 방식이라 매우 비효율적

DT<-data.table(DF)
setkey(DT,x,y)[
ss<-system.time(ans2<-DT[J("R","h")]) #binary search
?data.table
head(ans2)
?identical
identical(ans1$v, ans2$v)
ss
#bad case for using data.table
system.time(ans2<-DF[DF$x=="R"&DF$y=="h",])
mapply(identical,ans1,ans2)
?mapply

DT[,sum(v)]
DT[,sum(v), by=x] #x를 기준으로 summary  
ttt<-system.time(tt<-tapply(DT$v, DT$x, sum))
ttt
sss<-system.time(ss<-DT[,sum(v),by=x])
sss

identical(as.vector(tt),ss$V1)

sss<-system.time(ss<-DT[,sum(v),by="x,y"])
sss
ss

#데이터 탐색
cov(iris[,1:4])
cor(iris[,1:4])

#결측값 처리
y<-c(1,2,3,NA)
is.na(y)

mydata[mydata$v1=99,"v1"]=NA

x<-c(1,2,NA,3)
mean(x)
mean(x,na.rm=T)

mydata[!complete.cases(mydata),]

install.packages("Amelia")
library(Amelia)

data(freetrade)
head(freetrade)
str(freetrade)
freetrade
a.out<-amelia(freetrade, m=5, ts="year", cs="country") #m은 몇개의 imputation data set만들껀지, ts는 시계열에 대한 정보, cs는 cross-sectional 분석에 포함될 정보t
hist(a.out$imputations[[3]]$tariff, col="grey", border="white") #tariff에 imputations3을 썼을때의 plot
save(a.out, file="imputations.Rdata")
write.amelia(obj=a.out, file.stem="outdata")
a.out
?amelia

missmap(a.out) #결측값 처리전
?missmap
freetrade$tariff<-a.out$imputation[[5]]$tariff
missmap(freetrade)


#이상값 검색
x=rnorm(100)
boxplot(x)
x=c(x,19,28,30)
outwith=boxplot(x)
outwith$out

install.packages("outliers")
library(outliers)
set.seed(1234)
y=rnorm(100)
outlier(y) #평균과 가장 차이가 많이 나는 값 출력
outlier(y, opposite=T) #반대방향으로 가장 차이가 많이 나는 값 출력
?outlier
dim(y)=c(20,5)
outlier(y) #각 열의 평균과 가장 차이가 많은 값을 각 열별로 출력
outlier(y, opposite=T)
boxplot(y)


#회귀분석
set.seed(2)
x=runif(10,0,11) # 개수, 최대, 최소
?runif
y=2+3*x+rnorm(10,0,0.2)
dfrm=data.frame(x,y)
dfrm

lm(y~x, data=dfrm) #x가 b1, intercept가 오차

set.seed(2)
u=runif(10,0,11)
v=runif(10,11,20)
w=runif(10,1,30)
y=3+0.1*u+2*v-3*w+rnorm(10,0,0.1)
dfrm=data.frame(y,u,v,w)
dfrm
m=lm(y~u+v+w)
summary(m)

chick<-ChickWeight[ChickWeight$Diet==1,] #식이요법 방법1을 적용한 데이터만
chick<-ChickWeight[ChickWeight$Chick==1,] # 그 중에서 1번 닭만

data(cars)
head(cars)

speed2<-cars$speed^2
cars<-cbind(speed2,cars)
head(cars)

n<-lm(dist~speed+speed2, data=cars) #다항회귀분석
summary(n)



#예제1
x<-c(1,2,3,4,5,6,7,8,9)
y<-c(5,3,2,3,4,6,10,12,18)
df1<-data.frame(x,y)
df1
summary(lm(y~x, data=df1))
plot(lm(y~x)) #residual 이 이차형태띄므로 이차인 다항회귀를 적용하는것이 더 좋음



library(MASS)
head(hills)
step(lm(time~1,hills), scope=list(lower=~1, upper=~dist+climb), direction="forward")


#상관분석
install.packages("Hmisc")
library(Hmisc)

head(mtcars)
drat<-mtcars$drat
disp<-mtcars$disp
plot(disp~drat)
cor(drat,disp)
rcorr(as.matrix(mtcars),type="pearson")
cov(mtcars)

rcorr(as.matrix(mtcars), type="spearman")


#다차원 척도법
head(eurodist)
data(eurodist)
eurodist

loc<-cmdscale(eurodist)
loc
?cmdscale
x<-loc[,1]
y<-loc[,2]
plot(x,y,type="n", main="eurodist") # type =n 이름으로
text(x,y,rownames(loc),cex=0.8)
abline(v=0,h=0)


#주성분분석
summary(USArrests)
head(USArrests)
fit<-princomp(USArrests, cor=T)
fit
summary(fit,loadings=T) #첫번째 주성분 하나가 분산의 약 62% 설명, 
loadings(fit) #주성분의 로딩벡터 (앞에 계수)
plot(fit, type="line") #scree plot / 각 주성분의 분산의 크기/ 주성분의 분산 감소가 급격히 줄어들어 주성분의 개수를 늘릴 때 얻게되는 정보의 양이 상대적으로 미미한 지점에서 주성부느이 개수를 정하는 것 
fit$scores # 각 관측치를 주성분들로 표현한 값
biplot(fit)

round(predict(fit),2)
?predict


Price<-c(6,7,6,5,7,6,5,6,3,1,2,5,2,3,1,2)
Software<-c(5,3,4,7,7,4,7,5,5,3,6,7,4,5,6,3)
Aesthetics<-c(3,2,4,1,5,2,2,4,6,7,6,7,5,6,5,7)
Brand<-c(4,2,5,3,5,3,1,4,7,5,7,6,6,5,5,7)
data<-data.frame(Price,Software,Aesthetics,Brand)
pca<-princomp(data, cor=T)
summary(pca,loadings=T) #comp1로 60퍼 설명가능 , 2까지 합하면 84퍼, 로딩을 보면 comp1은 Aes, brand가 클수록, price가 낮을수록 높은값 가지고 software의 영향을 가장 적게받음
#comp2는 software영향만을 제일 크게 받음 나머지는 무시가능정도 -> comp1은 패션추구형 comp2는 기능추구
biplot(pca)

str(data)
summary(data)
head(data)


#시계열 분석
Nile
class(Nile) #데이터 타입이 time series임
ldeaths
plot(Nile) #평균이 변화하는 추세라 stationary X
plot(ldeaths) #계절성 띔

ldeaths.decompose<-decompose(ldeaths)
ldeaths.decompose$seasonal #분해해서 계절성부분만 
plot(ldeaths.decompose)
ldeaths.decompose.adj<-ldeaths-ldeaths.decompose$seasonal
plot(ldeaths.decompose.adj)

Nile.diff1<-diff(Nile, differences=1)
plot(Nile.diff1)
Nile.diff2<-diff(Nile, differences=2)
plot(Nile.diff2)
acf(Nile.diff2, lag.max = 20) #lag=1과 8일때를 제외하고 다 신뢰구간안에 들어와있음 
acf(Nile.diff2,lag.max=20, plot=F)
pacf(Nile.diff2, lag.max=20) #lag 가 1-8 은 신뢰구간을 넘어서 음의값, lag=9에서 절단된 모형
pacf(Nile.diff2, lag.max=20, plot=F)

install.packages("forecast")
library(forecast)
auto.arima(Nile) #적합한 모델 찾아줌.
Nile.arima<-arima(Nile,order=c(1,1,1))
Nile.forecasts<-forecast(Nile.arima,h=10)
plot(Nile.forecasts)


#exercise1
salary=c(3030,6050,3571,3300,0,9375,9525,5000,999,3300,3500,2493,1911,2130,1185,5236,1990,6000,6229,1523)
tenure=c(7,0,11,6,18,6,15,5,3,2,16,5,7,4,0,2,4,32,5,3)
age=c(61,51,63,60,63,57,60,61,57,60,63,61,58,59,56,60,60,74,63,56)
sales=c(161315,144416,139208,100697,100469,81667,76431,57813,56154,53588,50777,47678,47061,41322,37154,35853,33674,33296,32379,31707)
profits=c(2956,22071,4430,6370,9296,6328,5807,5372,1120,6398,5165,1704,2945,1048,3780,1259,568,3765,3782,578)
assets=c(257389,237545,49271,92630,355935,86100,668641,59920,36672,59550,617679,42754,33673,37675,30966,299804,14166,19166,194398,3665875)
length(tenure)
firm=data.frame(salary,tenure,age,sales,profits,assets)
head(firm)
summary(firm)
mean(firm$salary)
var(firm$salary)
sd(firm$salary)

plot(firm$salary~firm$profits)
cor(firm$salary,firm$profits)

rg=lm(firm$salary~firm$profits) #lm(salary~profits, data=firm)과 동일
summary(rg)#0.19>0.05 통계적으로 유의x
rg2=lm(salary~age+profits+sales, data=firm)
summary(rg2)#0.48>0.05 통계적으로 유의x
rg3=lm(salary~profits+age+sales+tenure+assets, data=firm)
summary(rg3) 

step(rg3, direction="backward")
step(rg3, direction="forward")
#?두개차이
#step(lm(salary~profits+age+sales+tenure+assets,data=firm),direction="forward")
#step(lm(salary~1, firm), scope=list(lower=~1, upper=~tenure+age+sales+profits+assets), direction="forward")
forward 에선 min model이 필요!!!! backward에서만 풀모델
step(rg3, direction="both")


#로지스틱 회귀
a<-subset(iris, Species=="setosa"|Species =="versicolor")
head(a)
a$Species<-factor(a$Species) #factor로 바꿈
str(a)
b<-glm(Species~Sepal.Length, data=a, family=binomial) #family: error들의 분포
?glm
summary(b) #sepal.length 는 매우 유의한 변수, 5.14가 beta1값이니까 오즈의 관점에서 해석하면 sepal.length가 한단위 증가함에 따라 오즈가 e^5140=170배 증가함을 알수있음
#null.deviance는 절편만 포함하는 모형(h0:beta=0)의 완전모형으로부터의 이탈도(deviance)를 나타냄
#residual deviance는 예측변수 sepal.length 가 추가된 적합 모형의 이탈도. null deviance에 비해 자유도 1 기준에 이탈도의 가모가 744정도의 큰 감소를 보임
#p값=p(x^2(98)>64.211) 카이제곱분포 = 0.997 이므로 귀무가설(적합모형) 기각못함 -> 자료를 잘 적합하고 있다고
#일반적인 회귀분석 유의도랑 조금 다르게 해석되는것같음

coef(b)#
exp(coef(b)["Sepal.Length"])
confint(b, parm="Sepal.Length")

?confint
fitted(b)[c(1:5, 96:100)] #
predict(b, newdata=a [c(1,50,51,100),], type="response")
?predict
cdplot(Species~Sepal.Length, data=a) #Sepal.Length가 커짐에 따라 versicolor의 확률이 증가함을 보여줌. 
plot(a$Sepal.Length, a$Species, xlab="Sepal.Length")
x=seq(min(a$Sepal.Length), max(a$Sepal.Length),0.1) #최소 최대 건너뛰면서 0.1 간격으로
lines(x, 1+(1/(1+(1/exp(-27.831+5.140*x)))), type="l", col="red")

#다중 로지스틱회귀
attach(mtcars)
str(mtcars)
glm.vs<-glm(vs~mpg+am, data=mtcars, family=binomial)
summary(glm.vs)

step.vs<-step(glm.vs, direction="backward")
ls(glm.vs)
str(glm.vs)
anova(glm.vs, test="Chisq")
?anova

#신경망구조
install.packages("nnet")
library(nnet)
nn.iris<-nnet(Species~., data=iris, size=2, rang=0.1, decay=5e-4, maxit=200) 
#size : hidden layer 개수, rang: w0의 weight, decay : weight 감소의 모수...? maxit: 반복의 maximum 횟수
#각 나오는 value값 :적합하는 목적식의 값
?nnet
summary(nn.iris) #input,hiddenlayer,output노드 수, 가중치수/ input->hiddenlayer로 가는 w값, hiddenlayer->output로 가는 w값/ b는 상수항(bias)의 w값

install.packages("devtools")
library(devtools)
#plot.nnet불러오는방법1
source_url("https://gist.githubusercontent.com/Peque/41a9e20d6687f2f3108d/raw/4008477e0aafa05a712d00dc4974011aa10e97a9/nnet_plot_update.r")
plot.nnet(nn.iris)
#plot.nnet불러오는방법2
library(clusterGeneration)
library(scales)
library(reshape)
plot(nn.iris)

table(iris$Species, predict(nn.iris, iris, type="class")) #predict(modeldata,testdata,type은 범주형이라 class)
?predict #setosa 50개 다 잘분류 , versicolor,virginica 는 50개 중 49개 잘 분류



head(infert)
str(infert)

install.packages("neuralnet")
library(neuralnet)
net.infert<-neuralnet(case~age+parity+induced+spontaneous, data=infert, hidden=2, err.fct="ce", linear.output=F, likelihood=T) 
#err.fct는 오차총합 (sse:오차총합, ce:교차엔트로피오차적용), 출력 노드에서 선형활성화 비적용
plot(net.infert)
net.infert$result.matrix #결과행렬에 대한 정보
net.infert$net.result

#원자료와 함께 적합값 출력
head(infert)
out<-cbind(net.infert$covariate, net.infert$net.result[[1]])
dimnames(out)<-list(NULL,c("age","parity","induced","spontaneous","nn-output"))
head(out)

head(net.infert$generalized.weights[[1]]) # 일반화가중치:각 공변량들의 효과, 로지스틱 회귀모형에서의 회귀계수와 유사하게 해석/모든 공변량에 의존하므로 각 자료점에서 국소적인 기여도를 나타냄 / 작은 분산은 선형효과를 제시, 큰 분산은 관측치 공간상에서 변화가 심하다는걸 나타냄=비선형적인 모형

?gwplot #neuralnet에서 범주형 자료들을 plot으로

par(mfrow=c(2,2))
gwplot(net.infert, selected.covariate="age", min=-2.5, max=5)
gwplot(net.infert, selected.covariate="parity", min=-2.5, max=5)
gwplot(net.infert, selected.covariate="induced", min=-2.5, max=5)
gwplot(net.infert, selected.covariate="spontaneous", min=-2.5, max=5)
#age는 모든값이 0근처 -영향없음, induced와 spontaneous는 전반적으로 1보다 큼->비선형효과, 모형단순화위해 age제거

par(mfrow=c(1,1))

new.output<-compute(net.infert, covariate=matrix(c(22,1,0,0,22,1,1,0,22,1,0,1,22,1,1,1), byrow=T, ncol=4)) #각 뉴런의 출력값 계산,새로운 공변량 조합에 대한 예측값, age=22, parity=1, induced<=1, spontaneous<=1,
new.output$net.result #사전 낙태수에 따라 예측확률 증가


#다층신경망구조
train.input<-as.data.frame(runif(50,0,100))
train.output<-sqrt(train.input)
train.data<-cbind(train.input, train.output)
colnames(train.data)<-c("Input","Output")
head(train.data)

net.sqrt<-neuralnet(Output~Input,train.data, hidden=10, threshold=0.01)
net.sqrt
plot(net.sqrt)

#testdata 적용
test.data<-as.data.frame((1:10)^2)
test.out<-compute(net.sqrt, test.data )
ls(test.out)
test.out$net.result
test.out

net2.sqrt<-neuralnet(Output~Input, train.data, hidden=c(10,8), threshold=0.01)
plot(net2.sqrt)
test2.out<-compute(net2.sqrt, test.data)
test2.out

cbind(test.out$net.result, test2.out$net.result)



#의사결정나무
install.packages("rpart")
library(rpart)
c<-rpart(Species~.,data=iris)
c
plot(c,compress=T, margin=0.3)
text(c, cex=1.5)
head(predict(c, newdata=iris, type="class")) # 새로운 자료에 대한 예측

install.packages("rpart.plot")
library(rpart.plot)
prp(c,type=4, extra=2)

c$cptable #트리의 크기에 따른 cost-complexity parameter을 제공하며, 교차타당성오차를 함께 제공
opt<-which.min(c$cptable[,"xerror"]) #최소값의 인뎃스
cp<-c$cptable[opt,"CP"]
prune.c<-prune(c,cp=cp) #이게 cp 최소인거 찾는건가
?prune
plot(prune.c)
text(prune.c, use.n=T)

plotcp(c) # cp값을 그림으로


install.packages("party")
library(party)
head(stagec)
str(stagec)
stagec1<-subset(stagec,!is.na(g2))
stagec1
stagec2<-subset(stagec1, !is.na(gleason))
stagec3<-subset(stagec2, !is.na(eet))
str(stagec3)


set.seed(1234)
ind<-sample(2,nrow(stagec3), replace=T, prob=c(0.7,0.3)) #1, 2를 총 134개만큼 training data 와 test data로 70% 30%로 구성
ind
trainData<-stagec3[ind==1,] #n=102개
testData<-stagec3[ind==2,] #n=32개
tree<-ctree(ploidy ~ ., data=trainData)
tree
plot(tree) #막대그래프는 반응변수의 각 범주별 비율을 나타냄

testPred=predict(tree, newdata=testData)
table(testPred, testData$ploidy) #predict 함수를 통해 검증용 자료에 적합모형 적용


airq<-subset(airquality, !is.na(Ozone))
head(airq)
airq
airct<-ctree(Ozone~., data=airq)
airct
plot(airct)
head(predict(airct, data=airq))
predict(airct, data=airq, type="node")
mean((airq$Ozone-predict(airct))^2)#예측값을 이용해서 구한 SSE


#배깅
install.packages("adabag")
library(adabag)
iris.bagging<-bagging(Species~., data=iris, mfinal=10)
iris.bagging$importance

plot(iris.bagging$trees[[10]])
text(iris.bagging$trees[[10]])

pred<-predict(iris.bagging, newdata=iris)
table(pred$class, iris[,5])

#부스팅
boo.adabag<-boosting(Species~.,data=iris, boos=T, mfinal=10)
boo.adabag$importance
plot(boo.adabag$trees[[10]])
text(boo.adabag$trees[[10]])

pred<-predict(boo.adabag, newdata=iris) 
tb<-table(pred$class, iris[,5])
tb

error.rpart<-1-(sum(diag(tb)/sum(tb)))
error.rpart

install.packages("ada")
library(ada)


#k-means
install.packages("NbClust")
library(NbClust)
wssplot<-function(data, nc=15, seed=1234){
  wss<-(nrow(data)-1)*sum(apply(data,2,var))
  for(i in 2:nc){
    set.seed(seed)
    wss[i]<-sum(kmeans(data,centers=i)$withinss)}
  plot(1:nc, wss, type="b")
  } #data는 수치형,nc=고려할 군집 최대수, seed난수 발생 초기값
wssplot(iris[,1:4]) #내가해본예시

521부

#혼합분포
install.packages("mixtools")
library(mixtools)
head(faithful)
hist(faithful$waiting)
wait1<-normalmixEM(faithful$waiting, lambda=.5, mu=c(55,80), sigma=5) #EM알고리즘이용
summary(wait1) #반복횟수 2회만에 로그-가능도 함수가 최대가됨. 
plot(wait1, density=T)

install.packages("mclust")
library(mclust)
mc<-Mclust(iris[,1:4], G=3)
summary(mc, parameters=T)
plot.Mclust(mc) #여러가지로 시각화 오오오
0
str(mc) #각 개체가 어느그룹으로 분류되었는지
mc$classification
predict(mc, data=) #새로운 자료에 대한 분류

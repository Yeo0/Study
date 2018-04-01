#########실습###########

#### 1. 자료탐색

install.packages("arules")
library(arules)
g1<-read.transactions("C:/groceries.csv", sep=",") #거래 데이터에 희소매트릭스를 생성
g1
#require(arules)
#data("Groceries")
#g1<-Groceries
inspect(g1[1:5])
summary(g1) # 9835개의 row(거래수)와 169개의 column(item), 이 데이터의 식료품이 169종류

itemFrequency(g1[,1:5]) #제품이 포함한 거래의 비율을 보여줌
itemFrequencyPlot(g1,support=0.1) # 지지도 0.1이상인 제품을 포함한 거래의 비율을 바차트로 보여줌
itemFrequencyPlot(g1,topN=20) # 상위 20개 데이터
itemFrequencyPlot(g1,topN=20,type="absolute") #상위 5개의 제품들이 다른제품들에 비해 빈도가 확실히 높다는 것을 시각적으로 알수 있음



#### 2. 연관성 분석

#support 0.05 일 때
rule1<-apriori(g1,parameter=list(supp=0.05, conf=0.3, minlen=2, maxlen=2)) # 최소 물품수와 최대 물품수를 2로 지정. 
summary(rule1) #영수증 9835개 데이터중 rules1에 대한 데이터는 3개 뿐. supp=0.05로 규칙을 엄격하게 주었기 때문에
inspect(rule1)


#support 0.01 일 때 (기준 낮춤)
rule2<-apriori(g1,parameter=list(supp=0.01, conf=0.3, minlen=2, maxlen=2))
summary(rule2) # 2개 관련된 연관규칙이 총 69개 규칙. lift의 max가 3.04로 높음
rule2<-sort(rule2, by="lift") # lift높은 순으로 정렬
inspect(rule2[1:10]) #beef와 root vegetables의 향상도가 높음. 고기 요리에 뿌리 채소가 같이 들어가기 때문으로 보임. 


#support 0.008 일 때 (기준 낮춤)
rule3<-apriori(g1,parameter=list(supp=0.008, conf=0.2, minlen=2, maxlen=2))
summary(rule3) #지지도를 좀 더 낮췄더니 265개 규칙. 
rule3<-sort(rule3, by="lift")
inspect(rule3[1:10]) # 베리와 휘핑샤워크림의 lift가 높은 것으로 보아 베리 옆에 휘핑샤워크림을 위치시켜 팔거나 베리를 구매한 고객에게 휘핑샤워크림의 할인쿠폰을 주는 식의 마케팅 전략을 쓴다면 매출이 증가할 것으로 보임. 


#berries를 구매했을 때의 다른 식료품과의 연관성
rules.sub<-subset(rule3, subset=lhs %pin% "berries")
rules.sub<-sort(rules.sub, by="lift")
inspect(rules.sub) # 베리를 구매했을 때 휘핑샤워크림과 요거트의 lift가 높음. 휘핑샤워크림과 요거트는 둘다 유제품이므로 위의 분석과 같이 유제품코너 옆에 베리를 위치시키는 것은 의미가 있다고 볼 수 있음.
 

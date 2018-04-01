##### 5장 : 결정 트리와 규칙(Decision tree and Rules)을 사용한 분류 -------------------

#### Part 1: 결정 트리 -------------------

## 결정 트리 이해 ----
# 두 부분 분류의 엔트로피 계산
-0.60 * log2(0.60) - 0.40 * log2(0.40)

curve(-x * log2(x) - (1 - x) * log2(1 - x),
      col="red", xlab = "x", ylab = "Entropy", lwd=4)

## 예제 : 위험 은행 대출 식별 ----
## 2 단계 : 데이터 준비와 살펴보기 ----
credit <- read.csv("C:/credit.csv")
str(credit)

# 지원자의 두 특성 확인
table(credit$checking_balance)
table(credit$savings_balance)

# 대출의 두 특성 확인
summary(credit$months_loan_duration)
summary(credit$amount)

# 분류 변수 확인
table(credit$default)

# 훈련과 테스트 데이터에 대한 무작위 샘플 생성
# 예제와 같은 무작위 수열을 사용하기 위해 set.seed 사용
set.seed(12345)
credit_rand <- credit[order(runif(1000)), ]

# credit과 credit_rand 데이터 프레임간 비교
summary(credit$amount)
summary(credit_rand$amount)
head(credit$amount)
head(credit_rand$amount)

# 데이터 프레임 나누기
credit_train <- credit_rand[1:900, ]
credit_test  <- credit_rand[901:1000, ]

# 분류 변수의 비율 확인
prop.table(table(credit_train$default))
prop.table(table(credit_test$default))

## 3 단계 : 데이터로 모델 훈련 ----
# 가장 단순한 결정 트리 생성
install.packages("C50")
library(C50)
credit_model <- C5.0(credit_train[-17], credit_train$default)

# 트리 정보 출력
credit_model

# 트리에 대한 상세 정보 출력
summary(credit_model)

## 4 단계 : 모델 성능 평가 ----
# 테스트 데이터에 대한 예측 팩터 벡터 생성
credit_pred <- predict(credit_model, credit_test)

# 예측과 실제 분류의 교차표
library(gmodels)
CrossTable(credit_test$default, credit_pred,
           prop.chisq = FALSE, prop.c = FALSE, prop.r = FALSE,
           dnn = c('actual default', 'predicted default'))

## 5 단계 : 모델 성능 향상 ----

## 결정 트리의 정확성 부스팅
# 10 trials과 부스트드 결정 트리
credit_boost10 <- C5.0(credit_train[-17], credit_train$default,
                       trials = 10)
credit_boost10
summary(credit_boost10)

credit_boost_pred10 <- predict(credit_boost10, credit_test)
CrossTable(credit_test$default, credit_boost_pred10,
           prop.chisq = FALSE, prop.c = FALSE, prop.r = FALSE,
           dnn = c('actual default', 'predicted default'))

# 100 trials과 부스트드 결정 트리
credit_boost100 <- C5.0(credit_train[-17], credit_train$default,
                        trials = 100)
credit_boost_pred100 <- predict(credit_boost100, credit_test)
CrossTable(credit_test$default, credit_boost_pred100,
           prop.chisq = FALSE, prop.c = FALSE, prop.r = FALSE,
           dnn = c('actual default', 'predicted default'))

## 가중치 매트릭스 생성
# 가중 비용 매트릭스
error_cost <- matrix(c(0, 1, 4, 0), nrow = 2)
error_cost

# 트리에 비용 매트릭스 적용
credit_cost <- C5.0(credit_train[-17], credit_train$default,
                    costs = error_cost)
credit_cost_pred <- predict(credit_cost, credit_test)

CrossTable(credit_test$default, credit_cost_pred,
           prop.chisq = FALSE, prop.c = FALSE, prop.r = FALSE,
           dnn = c('actual default', 'predicted default'))

#### Part 2: 규칙 학습기 -------------------

## 예제 : 독성 버섯 식별 ----
## 2 단게 : 데이터 준비와 살려보기 ---- 
mushrooms <- read.csv("C:/mushrooms.csv", stringsAsFactors = TRUE)

# 데이터 프레임 구조
str(mushrooms)

# veil_type 속성 제거
mushrooms$veil_type <- NULL

# 분류 분포 확인
table(mushrooms$type) #두그룹개수가 비슷할때 사용가능한 알고리즘


## 3 단계 : 데이터로 모델 훈련 ----
install.packages("RWeka")
library(RWeka)

# 데이터에 대한 OneR() 훈련
mushroom_1R <- OneR(type ~ ., data = mushrooms)

## 4 단계 : 모델 성능 평가 ----
mushroom_1R
summary(mushroom_1R)

## 5 단계 : 모델 성능 향상 ----
mushroom_JRip <- JRip(type ~ ., data = mushrooms)
mushroom_JRip
summary(mushroom_JRip)

# C5.0 결정 트리을 사용한 규칙 학습기 (책에서 다루지 않음)
library(C50)
mushroom_c5rules <- C5.0(type ~ odor + gill_size, data = mushrooms, rules = TRUE)
summary(mushroom_c5rules)

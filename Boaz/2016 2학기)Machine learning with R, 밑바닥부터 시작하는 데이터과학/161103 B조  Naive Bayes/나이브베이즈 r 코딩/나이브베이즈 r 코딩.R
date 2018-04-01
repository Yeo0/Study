##### 4장 : 나이브 베이즈(Naive Bayes)를 사용한 분류 

## 스팸 SMS 메시지 분류 

## 데이터 준비와 살펴보기  

# sms 데이터 데이터프레임으로 읽기
srms_raw <- read.csv("C:/sms_spam.csv", stringsAsFactors = FALSE, header = TRUE)

# sms 데이터 구조
str(sms_raw)
# 5558개의 SMS메시지와 두개의 속성 type과 text가 있음
# type에는 text의 유형(ham or spam)이 저장
# text에는 SMS 메시지 텍스트가 저장

# 팩터로 변환
sms_raw$type <- factor(sms_raw$type)
# 현재 문자 벡터인 type은 범주형 변수이기 때문에 팩터로 변경

# 변수형 확인
str(sms_raw$type)
# ham/spam 두 가지 범주로 이루어져 있음을 확인

table(sms_raw$type)
# 746개는 spam, 4812개는 ham임을 확인

# 텍스트 마이닝(tm) 패키지를 사용하여 말뭉치 생성
install.packages("tm")
library(tm)
getSources()
# tm패키지가 지원하는 문서 입력 소스들의 목록 
sms_corpus <- Corpus(VectorSource(sms_raw$text))
# Corpus() 함수는 텍스트 문서를 저장하기 위한 r 객체를 생성
# VectorSource() 메세지를 벡터로 저장

# sms 말뭉치 확인
print(sms_corpus)
# 5558개의 메시지에 대한 문서를 포함
as.character(sms_corpus[[1]])
# 첫 번째 메시지 "Hope you are having a good week. Just checking in"

# tm_map() 사용하여 말뭉치 정리
corpus_clean <- tm_map(sms_corpus, content_transformer(tolower))
# 메시지 전부를 소문자로 변경 
corpus_clean <- tm_map(corpus_clean, removeNumbers)
# 숫자 제거
corpus_clean <- tm_map(corpus_clean, removeWords, stopwords())
# to, and, but, or 같은 단어(stopword) 제거
corpus_clean <- tm_map(corpus_clean, removePunctuation)
# 마침표 제거 
corpus_clean <- tm_map(corpus_clean, stripWhitespace)
# 불필요한 공백 제거 

# 말뭉치 정리 확인
as.character(sms_corpus[[1]])
as.character(corpus_clean[[1]])

# 문서-용어 희소 매트릭스 생성
sms_dtm <- DocumentTermMatrix(corpus_clean)
sms_dtm
#행은 문서(SMS메시지), 열은 용어(단어)를 나타내는 매트릭스
#매트릭스 각 칸은 각 문서에서 나타나는 단어의 빈도수

# 훈련과 테스트 데이터셋 생성 
# 훈련데이터와 테스트데이터를 각각 75%, 25%로 나눔 
sms_raw_train <- sms_raw[1:4169, ]
sms_raw_test  <- sms_raw[4170:5558, ]

sms_dtm_train <- sms_dtm[1:4169, ]
sms_dtm_test  <- sms_dtm[4170:5558, ]

sms_corpus_train <- corpus_clean[1:4169]
sms_corpus_test  <- corpus_clean[4170:5558]

# 스팸 비율 확인
prop.table(table(sms_raw_train$type))
prop.table(table(sms_raw_test$type))
# 훈련 데이터와 테스트 데이터 모두 13% 스팸을 포함, 두 데이터에 스팸 메시지가 균등하게 나눠져 있음

# 빈번한 단어에 대한 속성 지시자
findFreqTerms(sms_dtm_train, 5)
#findFreqTerms는 특정 빈도수 이상 나타난 단어를 포함하는 문자 벡터 반환하는 함수
sms_dict <- findFreqTerms(sms_dtm_train, 5)
# 용어의 빈도수 목록을 저장
sms_train <- DocumentTermMatrix(sms_corpus_train, list(dictionary = sms_dict))
sms_test  <- DocumentTermMatrix(sms_corpus_test, list(dictionary = sms_dict))
# 훈련과 테스트 매트릭스를 빈도수 목록에 명시된 것으로 제한하기 위한 코드

# 개수를 팩터로 변환
convert_counts <- function(x) {
  x <- ifelse(x > 0, 1, 0)
  x <- factor(x, levels = c(0, 1), labels = c("No", "Yes"))
}
# 희소 매트릭스에 단어가 나타나는지를 판단하기위한 함수
# 이 함수는 단어가 나타나면 Yes, 나타나지 않으면 No로 표시

# apply() convert_counts()를 사용한 훈련/테스트 데이터 추출
sms_train <- apply(sms_train, MARGIN = 2, convert_counts)
sms_test  <- apply(sms_test, MARGIN = 2, convert_counts)
# 단어의 출연에 관심이 있기때문에 희소매트릭스의 열에 적용 (margin = 2) 

## 3 단계 : 데이터로 모델 훈련 ----
install.packages("e1071") #나이브베이즈 할 수 있는 거
library(e1071)
sms_classifier <- naiveBayes(sms_train, sms_raw_train$type)
# naiveBayes(train,class,laplace=c)
# train은 훈련 데이터를 포함한 데이터 프레임 또는 매트릭스 
# class은 훈련 데이터의 각 행에 대한 범주인 팩터
# laplace 라플라스 추정기를 제어하는 수 

sms_classifier

## 4 단계 : 모델 성능 평가 ----
sms_test_pred <- predict(sms_classifier, sms_test)
install.packages("gmodels")
library(gmodels)
CrossTable(sms_test_pred, sms_raw_test$type,
           prop.chisq = FALSE, prop.t = FALSE, prop.r = FALSE,
           dnn = c('predicted', 'actual'))
#1206개중 5개 메시지가 스팸으로 잘못 분류, 183개 중 31개가 햄으로 잘못 분류 

## 5 단계 : 모델 성능 향상 ----
sms_classifier2 <- naiveBayes(sms_train, sms_raw_train$type, laplace = 1)
sms_test_pred2 <- predict(sms_classifier2, sms_test)
CrossTable(sms_test_pred2, sms_raw_test$type,
           prop.chisq = FALSE, prop.t = FALSE, prop.r = FALSE,
           dnn = c('predicted', 'actual'))
# 라플라스 추정기 추가하여 성능 향상시키기  
# 스팸으로 잘못 분류하는 경우가 5개 -> 4개로 줄었음 
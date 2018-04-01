rm(list=ls())
gc() #컴퓨터 메모리리

install.packages("nnet")
library("nnet")
install.packages("neuralnet")
library("neuralnet")

suicide=read.csv("C:/Users/USER/Dropbox/보아즈/스터디/Panel_Suicide_data.csv",header=T)
sui_data=data.frame(suicide)
sui_data
str(sui_data)

# ?м??? ?ʿ??? ?????? ??��
  sui_data1=data.frame(sui_data$Sucide_Rate,sui_data$Past_Oriented, sui_data$GSP, sui_data$Gini_Coefficient, sui_data$populationgrowthrate, sui_data$unemploymentrate)
  sui_data1
  str(sui_data1)

#normalize

  normalize=function(x){
    return((x-min(x))/(max(x)-min(x)))
  }
  
  #사회과학적인 곳에서 많이씀
  
  sui_normalize=as.data.frame(lapply(sui_data1, normalize))
  sui_normalize
  summary(sui_normalize$sui_data.Sucide_Rate)

  
# training data, test data select..???? ???????ø?��?? ??��
  
  sui_train=sui_normalize[1:300, ]
  sui_test=sui_normalize[301:459, ]
  summary(sui_test)
  
  
# neural network model construction
  
  sui_model=neuralnet(sui_data.Sucide_Rate~sui_data.Past_Oriented+sui_data.GSP+
                        sui_data.Gini_Coefficient+sui_data.populationgrowthrate+
                        sui_data.unemploymentrate, data = sui_train, hidden=1)
  
  (
  # sui_model=neuralnet(sui_data.Sucide_Rate ~ . , #
    data=sui_train, hidden)  
  )

  sui_model

  plot(sui_model)
  sui_model$result.matrix  #?ֿ? ???? ?????Լ? result.matrix
  sui_rate_prediction=sui_model$net.result #????????
  sui_rate_prediction
  
  
# model accuracy
  model_result=compute(sui_model, sui_test[2:6])  #?��?????..??
  predict_suiciderate=model_result$net.result
  predict_suiciderate
  cor(predict_suiciderate, sui_test$sui_data.Sucide_Rate)

neuralnet


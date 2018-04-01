install.packages("devtools") 
library(devtools)

install.packages("Rcpp")#, dependencies = T)
library(Rcpp)

devtools::install_github("rstudio/reticulate")
devtools::install_github("rstudio/tensorflow")

# 
# install.packages("reticulate")
# install.packages("tensorflow")

library(tensorflow)


sess=tf$Session()
hello<-tf$constant('Hello, TensorFlow!')
sess$run(hello)



#몇 가지 데이터를 2 차원으로 작성한 다음 그 위에 한 줄을 맞추는 간단한 예제
# 
# Create 100 phony x, y data points, y = x * 0.1 + 0.3
x_data <- runif(100, min=0, max=1)
y_data <- x_data * 0.1 + 0.3

head(x_data)
head(y_data)

# Try to find values for W and b that compute y_data = W * x_data + b
# (We know that W should be 0.1 and b 0.3, but TensorFlow will
# figure that out for us.)
W <- tf$Variable(tf$random_uniform(shape(1L), -1.0, 1.0))
b <- tf$Variable(tf$zeros(shape(1L)))
y <- W * x_data + b

W
b
y


# Minimize the mean squared errors.는
loss <- tf$reduce_mean((y - y_data) ^ 2)  #최소제곱ㅂ
optimizer <- tf$train$GradientDescentOptimizer(learning_rate = 0.5)
train <- optimizer$minimize(loss) #loss최소로하느

loss
train

# Launch the graph and initialize the variables.
sess = tf$Session()
sess$run(tf$global_variables_initializer())

# Fit the line (Learns best fit is W: 0.1, b: 0.3)
for (step in 1:201) {
  sess$run(train)
  if (step %% 20 == 0)
    cat(step, "-", sess$run(W), sess$run(b), "\n")
}
#w b 를 반복될때마다 optimizer (gradient Descent 이용)

#MNIST data
library(tensorflow)
datasets <- tf$contrib$learn$datasets
mnist <- datasets$mnist$read_data_sets("MNIST-data", one_hot = TRUE)

# - MNIST 데이터는 세 가지 부분으로 나뉩니다 : 55,000 데이터 포인트의 교육 데이터 (train), 10,000 포인트의 테스트 데이터 (test) 및 5,000 포인트의 유효성 검사 데이터 (밸리데이션). 이 분할은 매우 중요합니다.
# 
# - 앞서 언급했듯이, 모든 MNIST 데이터 포인트는 두 부분으로되어 있습니다 : 손으로 쓴 숫자의 이미지와 해당 레이블. 우리는 이미지 "x"와 레이블 "y"를 부를 것입니다. 트레이닝 세트와 테스트 세트는 모두 이미지와 해당 레이블을 포함합니다. 예를 들어 트레이닝 이미지는 images이고 트레이닝 라벨은 labels입니다.
# 
# - 각 이미지는 28 x 28 픽셀입니다. 이것을 숫자의 큰 배열로 해석 할 수 있습니다.

# - 이 배열을 28x28 = 784 숫자의 벡터로 전개 할 수 있습니다. 우리가 이미지간에 일관성이 있는 한 배열을 어떻게 평평하게 만드는지는 중요하지 않습니다. 이 관점에서 볼 때, MNIST 이미지는 매우 풍부한 구조 (경고 : 계산 집약적 시각화)와 함께 784 차원의 벡터 공간에서 단지 한 묶음의 지점에 불과합니다.
# 
# - images는 쉐이프 (55000L, 784L)를 갖는 텐서 (n 차원 배열)입니다. 첫 번째 차원은 이미지 목록에 대한 인덱스이고 두 번째 차원은 각 이미지의 각 픽셀에 대한 인덱스입니다. 텐서의 각 엔트리는 특정 이미지의 특정 픽셀에 대해 0과 1 사이의 픽셀 강도입니다.

# - 3줄에 일어나는 

W <- tf$Variable(tf$zeros(shape(784L, 10L)))
b <- tf$Variable(tf$zeros(shape(10L)))

x <- tf$placeholder(tf$float32, shape(NULL, 784L))

x

y <- tf$nn$softmax(tf$matmul(x, W) + b) # xW+b의 regression form


y


#Inplementing the Regression_Training model

y_ <- tf$placeholder(tf$float32, shape(NULL, 10L))
cross_entropy <- tf$reduce_mean(-tf$reduce_sum(y_ * tf$log(y), reduction_indices=1L))
optimizer <- tf$train$GradientDescentOptimizer(0.5)
train_step <- optimizer$minimize(cross_entropy)
init <- tf$global_variables_initializer()

sess <- tf$Session()
sess$run(init)

for (i in 1:1000) {
  batches <- mnist$train$next_batch(100L)
  batch_xs <- batches[[1]]
  batch_ys <- batches[[2]]
  sess$run(train_step,
           feed_dict = dict(x = batch_xs, y_ = batch_ys)) #dictionary 에 넣어줌. minibatch?사용 / 각각하나하나 학습시킬
  
#Evaluating our model
correct_prediction <- tf$equal(tf$argmax(y, 1L), tf$argmax(y_, 1L))
accuracy <- tf$reduce_mean(tf$cast(correct_prediction, tf$float32))
sess$run(accuracy, feed_dict=dict(x = mnist$test$images, y_ = mnist$test$labels))



  
  
}









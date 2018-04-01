#alpha 유의수준 α

#m평균 n개수 b돌리는횟수

qqqq = function(n,m,b){
  num=rnorm(n,m,1)
  bbb=c()
  for(i in 1:b){
    k=ifelse(num>qnorm(0.025,m,1)&num<qnorm(0.975,m,1),0,1)
    bbb[i]=sum(k)/n
  }
  return(sum(bbb)/b)
}
  
qqqq(100000,10,10)


_________________________________________________________________________________________


rm(list = ls())
gc()

my_cl = function(n, m, mu){
  c_value = 0
  for(i in 1:1000){
    value = qnorm(0.025,mu,1) <= rnorm(n, mu, 1) & rnorm(n, mu, 1) <= qnorm(0.975,mu,1)
    c_value = c_value + sum(value)/n
  }
  return(c_value/m)
}

my_cl(1000,10000,5)


##system.time 오오오x오오오오오오오오오오오오
___________________________
#m 평균 n개수 sd 표편 k횟수
ppap=function(m,n,sd,k){
  rr=c()
  sde=qnorm(0.975)*sd/sqrt(n)
  for (i in 1:k){
    x=rnorm(n,m,sd)
    rr[i]=mean(x)-sde < mu & mean(x) + sde > mu
  }
  return(sum(rr)/k)
  
}
ppap()




























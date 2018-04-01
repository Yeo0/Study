x3=matrix(rnorm(1500,10,5)); y3=matrix(rpois(1500,5))

corr=function(k){
  x1=x-mean(x); y1=y-mean(y)
  xy=t(x1)%*%y1
  vx=(t(x1)%*%x1)
  vy=(t(y1)%*%y1)
  
  return(xy/(sqrt(vx)*sqrt(vy)))
}


corr(x3,y3)

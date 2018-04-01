x3=matrix(rnorm(1500,10,5)); y3=matrix(rpois(1500,5))

ex = data.frame(x1 = rnorm(1500, 3, 5), x2 = rpois(1500, 6), x3 = rgamma(1500, 2, 3), x4 = rexp(1500, 5))

my_corr=function(yeah){
  
 #i col j row
  result=matrix(0,nrow=ncol(yeah),ncol=ncol(yeah))
  
  
  for(i in 1:ncol(yeah)){
    for(j in i:ncol(yeah)){
      #대각행렬
      
      x=yeah[,i]
      y=yeah[,j]
      
      
      x1=x-mean(x); y1=y-mean(y)
      xy=t(x1)%*%y1
      vx=(t(x1)%*%x1)
      vy=(t(y1)%*%y1)
     
      result[i,j]=xy/(sqrt(vx)*sqrt(vy))
      

    }
  }
  return(round(result,2))
}


my_corr(ex)
______________


rm(list=ls())
gc()

ex = data.frame(x1 = rnorm(1500, 3, 5), x2 = rpois(1500, 6), x3 = rgamma(1500, 2, 3), x4 = rexp(1500, 5))

my_corr = function(exam){
  result = matrix(0,nrow = ncol(exam), ncol = ncol(exam))
  for(i in 1:ncol(exam)){
    for(j in i:ncol(exam)){
      m_ex = data.frame(m_x = exam[,i] - mean(exam[,i]), m_y = exam[,j] - mean(exam[,j]))
      result[i,j] = round(m_ex$m_x%*%m_ex$m_y/(sqrt(sum((m_ex$m_x)^2))*sqrt(sum((m_ex$m_y)^2))), 2)
    }
  }
  colnames(result)<- names(exam)
  rownames(result)<- names(exam)
  return(result)
}
my_corr(ex)


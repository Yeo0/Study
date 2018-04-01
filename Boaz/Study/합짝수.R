1과 사용자가 입력한 수 n 사이 (1과 n 포함하여)의 짝수의 합 출력
1부터 n까지의 짝수의 합
n=19
k=1
s=0
for(k in 1:n){  
 if(k%%2==0){
   s=s+k
 } 
  k=k+1
  }
print(sum(s))
print(s)
//[1] Input
var sum = 0; // 짝수의 합이 담길 그릇 선언/초기화
//[2] Process : 주어진 범위(for)에 주어진 조건(if)
for(var i = 1; i <= 100; i++) // 1부터 100까지
{
  if (i % 2 == 0) // 짝수
  {
    sum += i; // 합
  }
}
//[3] Output
document.write("1부터 100까지 짝수의 합 : " + sum + "<br />");

//Write your code here
private class Calculator implements AdvancedArithmetic{
 int divisorSum(int n){
     List<Integer> ls = new ArrayList<Integer>();
     ls.add(1);
     ls.add(n);
     for(i = 1; i < n; i++){
         if(n%i == 0){
             ls.add(i);
         }
     }
     Integer sum= 0; 
     for (Integer i:ls)
         sum = sum + i;
     return sum;
 }   
}

sum = 1 + n
for(i = 1; i < n; i++){
    if(n%i == 0){
        sum += i;
    }
}
function nthUglyNumber(n: number): number {
 let result = [1]
 let i =0 , j =0 ,k =0;
 while(result.length<n){
   let n2 = result[i]*2
   let n3 = result[j]*3
   let n5 = result[k]*5
   let nmin = Math.min(n2,n3,n5)
   result.push(nmin)
   if(nmin === n2) i++
   if(nmin === n3) j++
   if(nmin === n5) k++

 }
 console.log(result)
 return result[n-1]
};

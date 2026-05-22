function search(nums: number[], target: number): number {
    function bin(i:number,j:number){
        if(i > j) return -1
        let mid = Math.floor((i+j)/2)
        if(arr[mid] === target){
            return mid
        }
        if(arr[mid]<target){
           return  bin(mid+1,j)
        }
        else{
            return bin(i,mid-1)
        }
        // return -1
    }

let n = 0
for(let i=1;i<nums.length;i++){
    if(nums[i] < nums[i-1]){
        n = i
        break
    }
}
let arr = [...nums.slice(n),...nums.slice(0,n)]
console.log(arr)
let inx = bin(0,arr.length-1)
if(inx === -1) return -1
return (inx+n)%nums.length

};

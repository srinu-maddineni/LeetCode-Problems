function maxDistance(nums1: number[], nums2: number[]): number {
    let i =0
    let j = i
    let max = 0
    while( j<nums2.length && i<nums1.length){
        if(nums2[j]>=nums1[i] ){
            max = Math.max(max,j-i)
            j++
        }
        else{
            i++
        }
    }
    return max

};

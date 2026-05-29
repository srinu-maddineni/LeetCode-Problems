function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    let n = nums1.length
    let m = nums2.length
    let j = 0
    let i =0
    let nums = []
    while(i<n && j<m){
        if(nums1[i] < nums2[j]){
            nums.push(nums1[i])
            i++
        }
        else{
            nums.push(nums2[j])
            j++
        }
    }
    while(i<n){
        nums.push(nums1[i])
        i++
    }
    while(j<m){
        nums.push(nums2[j])
        j++
    }
    let k = nums.length
    console.log(k,nums)
    if(k%2 === 0){
        let mid  = k/2
        return (nums[mid]+nums[mid-1])/2
    }
    else{

        let mid  = Math.floor(k/2)

        return nums[mid]
    }
};

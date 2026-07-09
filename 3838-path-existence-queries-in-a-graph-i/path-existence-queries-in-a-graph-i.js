/**
 * @param {number} n
 * @param {number[]} nums
 * @param {number} maxDiff
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var pathExistenceQueries = function(n, nums, maxDiff, queries) {
    let group = new Array(n).fill(0);
    let groupId = 0;
    
    // Step 1: Pre-calculate connected components
    for (let i = 1; i < n; i++) {
        // If the gap between adjacent elements is too big, start a new group
        if (nums[i] - nums[i - 1] > maxDiff) {
            groupId++;
        }
        group[i] = groupId;
    }
    
    // Step 2: Answer each query in O(1) time
    let arr = [];
    for (let [u, v] of queries) {
        // If they belong to the same group, a valid path exists
        arr.push(group[u] === group[v]);
    }
    
    return arr;
 
};
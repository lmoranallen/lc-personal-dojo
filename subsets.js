/**
 * 76. Subsets
 * Given an integer array nums of unique elements, 
 * return all possible subsets (the power set).
 * The solution set must not contain duplicate subsets. 
 * Return the solution in any order.
 */


var subsets = function(nums) {
    const results = []
    const combo = []

    // use indexes - don't worry about the specific idx
    const iterate = (elemIndex) => {

        // at end of stream
        if (elemIndex >= nums.length) {
            const reference = [...combo] //deep copy of current state
            results.push(reference)
            return;
        }

        // recursive outcome with particular index
        combo.push(nums[elemIndex])
        iterate(elemIndex+1)


        // recursive outcome WITHOUT particular index
        combo.pop()
        iterate(elemIndex+1)
    }
    iterate(0)
    return results
};

console.log(subsets([1,2,3]))


const nums = [1,2,3,1,1,3]

const numIdenticalPairs = (nums) => {

    var counter = 0

    for (let i = 0; i < nums.length; i++) {
        for (let j = i+1; j < nums.length; j++) {
            nums[i] === nums[j] ? counter++ : null
        }
    }

    return counter
}
 
console.log(numIdenticalPairs(nums))
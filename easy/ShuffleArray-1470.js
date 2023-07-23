

const nums = [1,2,3,4,4,3,2,1]
const n = 4

const shuffle = (nums, n) => {

    let arr = []

    for (let i = 0; i < nums.length/2; i++) {
        
        arr.push(nums[i])
        arr.push(nums[n + i])

    }
    return arr
}


console.log(shuffle(nums, n))



const nums = [10,4,8,3]


var leftRightDifference = function(nums) {
    
    let newArr = []
    if (nums.length == 1){
        return [0]
    }

    for (let i = 0; i < nums.length; i++) {

        let leftsum = 0
        let rightsum = 0

        for (let j = 0; j < i; j++) {
            leftsum += nums[j]
        }
        for (let r = i+1; r < nums.length ;r++) {
            rightsum += nums[r]
        }

        console.log('leftsum:', leftsum)
        console.log('rightsum:', rightsum)

        let supersum = Math.abs(leftsum - rightsum)
        newArr.push(supersum)
    }
    return newArr
};

console.log(leftRightDifference(nums))





// loop through array
    // current number 
        // look left and sum
        // look right and sum
    
    // compare left sum and right sum
    // add to array

// loop through array
    // current number 
        // look left and sum and save into array
        // look right and sum and save into array
    
    // compare left sum and right sum
    // add to array
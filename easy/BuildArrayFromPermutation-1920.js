


// let nums = [0, 2, 1, 5, 3, 4]



var buildArray = function(nums) {
    
    let mutNums = []

    for (let i = 0; i < nums.length; i++) {
        var tempVar = nums[i]
        mutNums.push(nums[tempVar])
    }

    return mutNums
};



// console.log(buildArray(nums))

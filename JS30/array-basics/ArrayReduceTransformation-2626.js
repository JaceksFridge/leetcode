




// nums = []
// fn = function sum(accum, curr) { return 0; }
// init = 25




var reduce = function(nums, fn, init) {

    let val = init

    for (let i in nums) {
        val = fn(val, nums[Number(i)])   
    }
    return val
};

// reduce(nums, fn, init)
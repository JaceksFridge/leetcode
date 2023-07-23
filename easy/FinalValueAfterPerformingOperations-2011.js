


const operations = ["++X","++X","X++"]


var finalValueAfterOperations = function(operations) {
    
    let sum = 0

    for (i of operations) {

        if (i.includes('+')) {
            sum += 1
        } else if (i.includes('-')) {
            sum -= 1
        } else {
            null
        }
    }

    return sum
};

console.log(finalValueAfterOperations(operations))

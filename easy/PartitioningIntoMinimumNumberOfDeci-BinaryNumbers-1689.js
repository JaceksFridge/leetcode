


const n = "32"


var minPartitions = function(n) {

    let highestNumber = 0
    
    for (let i of n) {

        if (Number(i) > highestNumber) {
            highestNumber = Number(i)
        }
    }

    return highestNumber
};




console.log(minPartitions(n))
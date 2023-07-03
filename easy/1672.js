


// const accounts = [[2,8,7],[7,1,3],[1,9,5]]


var maximumWealth = function(accounts) {

    var richest = 0

    for (let acc of accounts) {

        let accountSum = 0

        for (let number of acc) {
            accountSum += number
        } 

        if (accountSum > richest) {
            richest = accountSum
        }

    }

    return richest
}


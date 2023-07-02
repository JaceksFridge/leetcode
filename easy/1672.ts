

const accounts = [[2,8,7],[7,1,3],[1,9,5]]

const maximumWealth = (accounts: number[][]): number => {
    
    let richest = 0

    for (let acc of accounts) {
        let accSum = 0

        for (let num of acc) {
            accSum += num
        }

        if (accSum > richest) {
            richest = accSum
        }
    }

    return richest
}


console.log(maximumWealth(accounts))
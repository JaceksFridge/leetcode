
const grid = [[1,2,4],[3,3,1]]

var deleteGreatestValue = function(grid) {   

    let loop = grid[0].length
    let allSum = 0
    for (let i = 0; i <= loop; i++) {

        let arrHigh = 0

        for (arr of grid) {
            arr.sort((a, b) => b - a)
            
            if (arr[0] > arrHigh) {
                arrHigh = arr[0]
            }
            arr.shift()
        }

        allSum += arrHigh
    }
    return allSum
};


console.log(deleteGreatestValue(grid))




// loop as many times as array.length
    // loop over grid
        // sort array
        // .pop arr



// const arr = [9, 81, 17]
// arr.sort((a, b) => a - b)
// console.log(arr)





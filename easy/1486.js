
let n = 5
let start = 0



var xorOperation = function(n, start) {
    
    let arr = [start]
    let xor = 0

    for (let i = 1; i < n; i++) {
        arr.push(start + 2 * i)
    }
    
    for (i in arr) {
        console.log(xor ^ arr[i])
        xor ^= arr[i]
    }

    return xor
};

console.log(xorOperation(n, start))

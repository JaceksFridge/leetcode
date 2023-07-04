

// arr = [10,20,30]
// fn = function constant() { return 42; }


const map = (arr, fn) => {

    temp = []

    for (let i = 0; i < arr.length; i++) {
        temp.push(fn(arr[i], i))
    }
    return temp
}


// console.log(map(arr, fn))
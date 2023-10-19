

arr = [1,2,3]
fn = function plusone(n) { return n + 1; }

var map = function(arr, fn) {

    const newArr = arr.map((item, i) => {
        return fn(item, i)
    })

    return newArr
};


console.log(map(arr, fn))
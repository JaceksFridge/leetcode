


const arr = [5, 4, 1, 2, 3]
const fn = (x) => x

var sortBy = function(arr, fn) {

    return arr.sort((a, b) => fn(a) + fn(b))
};


console.log(sortBy(arr, fn))






arr = [-2,-1,0,1,2]
fn = function plusOne(n) { return n + 1 }


var filter = function(arr, fn) {
    
    const filteredArr = []

    for (let i in arr) {

        fn(arr[i], Number(i)) ? filteredArr.push(arr[i]) : null
    }
    

    return filteredArr
};



console.log(filter(arr, fn))





var once = function(fn) {
     
    count = 0

    return function(...args){
        
        if (count === 0) {
            count += 1
            return fn(...args) 
        } else {
            return undefined
        } 
    }
};


// let fn = (a,b,c) => (a * b * c)
// let onceFn = once(fn)


// console.log(onceFn(5,7,4))
// console.log(onceFn(2,3,6))
// console.log(onceFn(4,6,8))


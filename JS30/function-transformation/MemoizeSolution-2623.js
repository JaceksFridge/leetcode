


function memoize(fn) {

    const cache = {}


    return function(...args) {
        let string = args.toString()

        if (string in cache) {

            return cache[string]
        }

        cache[string] = fn(...args)
        return cache[string]
    }
}




// let callCount = 0;
// const memoizedFn = memoize(function (a, b) {
//     callCount += 1;
//     return a + b;
// })
// console.log(
//     memoizedFn(2, 3),
//     memoizedFn(2, 3)
// )

// console.log(callCount)
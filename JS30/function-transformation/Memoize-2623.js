


function memoize(fn) {

    let correctCalls = {}

    const arrInside = (array, target) => {
        return array.find(mini => {

            return mini.every((value, index) => {
    
                return value === target[index]
            })
        })
    }


    let arr = []

    let memo = function(...args) {

        if (arrInside(arr, args)) {
            return correctCalls[`${args}`]
        } else {
            arr.push(args)
            let correct = fn(...args)
            correctCalls[`${args}`] = correct
            return correct
        }
    }

    memo.getCallCount = () => arr.length

    return memo
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














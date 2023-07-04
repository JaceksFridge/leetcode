


var createCounter = function(init) {

    let counter = init

    return {
        increment: () => {
            counter += 1
            return counter
        },
        decrement: () => {
            counter -= 1
            return counter
        },
        reset: () => {
            counter = init
            return counter
        }
    }
};


// const counter = createCounter(0)
// console.log(counter.increment(),counter.increment(),counter.decrement(),counter.reset(),counter.reset())




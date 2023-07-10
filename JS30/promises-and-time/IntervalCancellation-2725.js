









const result = []

const fn = (x) => x * 2
const args = [4], t = 20, cancelT = 110

const start = performance.now()




const cancellable = (fn, args, t) => {

    fn(...args)
    var id2cancel = setInterval(() => {
        fn(...args)
    }, t)


    const cancelFn = () => {
        clearInterval(id2cancel)
    }

    return cancelFn
}







const log = (...argsArr) => {
    const diff = Math.floor(performance.now() - start)
    result.push({"time": diff, "returned": fn(...argsArr)})
}       
const cancel = cancellable(log, args, t);

setTimeout(() => {
   cancel()
}, cancelT)

setTimeout(() => {
    console.log(result)
}, cancelT + t + 15)    

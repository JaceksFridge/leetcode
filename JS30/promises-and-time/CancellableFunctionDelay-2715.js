
const result = []

const fn = (x) => x * 5
const args = [2]
const t = 20

const cancelT = 50




var cancellable = function(fn, args, t) {

    const timeout = () => {
        
    }


    const cancelFn = () => {

    }


    return cancelFn
};







const log = (...argsArr) => {
       result.push(fn(...argsArr))
 }
      
const cancel = cancellable(fn, args, t);
          
setTimeout(() => {
   cancel()
   console.log(result) // [{"time":20,"returned":10}]
}, cancelT)




const t = 50
const calls = [
  {"t": 50, inputs: [1]},
  {"t": 75, inputs: [2]}
]




var debounce = function(fn, t) {

    let timeoutID

        return function (...args) {

            clearTimeout(timeoutID)


            timeoutID = setTimeout(() => {
                fn(...args)
            }, t)
        }
};


const log = debounce(calls, t);
log('Hello 1'); // cancelled
log('Hello 2'); // cancelled
log('Hello 3'); // Logged at t=100ms


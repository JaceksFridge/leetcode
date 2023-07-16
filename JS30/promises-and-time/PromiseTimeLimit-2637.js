




var timeLimit = function(fn, t) {

    
	return async function(...args) {

        return new Promise((resolve, reject) => {
            const id = setTimeout(() => reject("Time Limit Exceeded"), t)
            fn(...args)
                .then((res) => resolve(res))
                .catch((err) => reject(err))
                .finally(() => clearTimeout(id))
        })
    }
};


function fn(t) {
    return new Promise(
        res => setTimeout(res, t)
    )
}


const limited = timeLimit(fn, 100)
limited(150).catch(console.log)
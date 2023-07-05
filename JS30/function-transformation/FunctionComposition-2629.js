


const compose = (functions) => {
    return function (x) {
        //console.log('start', x)
        for (const f of functions.reverse()) {
            x = f(x)
            //console.log('fn:', f, 'x:', x)
        }
        //console.log('final:', x)
        return x
    }
}



const compose2 = (functions) => {

    const fn = (init, f) => f(init)

    return function (x) {

        return functions.reduceRight(fn, x)
    }
}


const fn = compose2([x => 10 * x, x => 10 * x, x => 10 * x])

console.log(fn(1))

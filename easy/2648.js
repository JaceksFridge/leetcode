


var fibGenerator = function*() {

    yield 0
    yield 1

    let start = [0, 1]

    while (true) {
        start.push(start[start.length -1] + start[start.length -2])
        yield start[start.length - 1]
    }
    
};

/*
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */


const gen = fibGenerator()
console.log(gen.next().value)




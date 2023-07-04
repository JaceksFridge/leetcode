

// let args = [{},null,42]


var createHelloWorld = function() {
    return function(...args) {
        return console.log("Hello World")
    }
};


// const f = createHelloWorld();
// f(args)
 
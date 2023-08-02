
const encoded = [6,2,7,3]
const first = 4

var decode = function(encoded, first) {
    
    let ogArray = [first]

    for (let i = 0; i < encoded.length; i ++) {
        ogArray.push(encoded[i] ^ ogArray[i])
    }
    return ogArray
};


console.log(decode(encoded, first))

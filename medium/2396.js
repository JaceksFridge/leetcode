
let n = 4

var isStrictlyPalindromic = function(n) {

    for (let i = 2; i < n; i++) {

        let string = n.toString(i)
        console.log(string)

        if (string === string.split('').reverse().join('')) {
            
        } else {
            return false
        }
    }

    return true
};

console.log(isStrictlyPalindromic(n))
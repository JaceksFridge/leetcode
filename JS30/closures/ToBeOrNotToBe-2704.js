
var expect = function(val) {
    return {
        toBe: (valToBe) => {
            if (val === valToBe) {
                return true
            } else {
                throw Error("Not Equal")
            }
        },
        notToBe: (valNotToBe) => {
            if (val !== valNotToBe) {
                return true
            } else {
                throw Error("Equal")
            }
        }
    }
};




// console.log(expect(5).notToBe(null))
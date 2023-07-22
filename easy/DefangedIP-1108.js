


let address = "1.1.1.1"
// "1[.]1[.]1[.]1"

var defangIPaddr = function(address) {
    return address.replace(/\./g, '[.]')
};


console.log(defangIPaddr(address))
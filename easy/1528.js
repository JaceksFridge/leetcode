

const s = "codeleet"
const indices = [4,5,6,7,0,2,1,3]



var restoreString = function(s, indices) {
    
    const order = {}

    for (let i = 0; i < s.length; i++) {
        order[indices[i]] = s[i]
    }

    return Object.values(order).join('')
};

console.log(restoreString(s, indices))



// create obj
    // add indices as strings
    // add s as values


// sort object
// convert to string
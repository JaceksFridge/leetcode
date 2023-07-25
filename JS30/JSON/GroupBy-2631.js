

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fn = function (n) { 
  return String(n > 5);
}


Array.prototype.groupBy = function(fn) {
    
    let tresor = {}

    for (val of this) {
       
        let key = fn(val)

        if (tresor[key]) {
            tresor[key].push(val)
        } else {
            tresor[key] = [val]
        }
    }

    return tresor
};


console.log(array.groupBy(fn))


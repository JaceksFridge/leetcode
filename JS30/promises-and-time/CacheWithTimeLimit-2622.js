


var TimeLimitedCache = function() {
    this.cache = new Map()
}




var obj = new TimeLimitedCache()
console.log(obj)



/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */
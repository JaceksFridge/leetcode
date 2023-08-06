


class ArrayWrapper {
    constructor(arr) {
        this.arr = arr
    }
    valueOf() {
        return this.arr.reduce((a,b) => a + b, 0)
    }
    toString() {
        return `[${String(this.arr)}]`
    }
}

 

const obj1 = new ArrayWrapper([1,2])
const obj2 = new ArrayWrapper([3,4])

console.log(String(obj1))
console.log(String(obj2))
console.log(obj1)
console.log(obj2 + obj1)


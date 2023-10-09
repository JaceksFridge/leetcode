
const nums = [null, {}, 3]

Array.prototype.last = function() {

    // if (this.length === 0) {
    //     return -1
    // } else {
    //     return this[this.length - 1]
    // }

    return this.length < 0 ? -1 : this[this.length -1]
};

console.log(nums.last())



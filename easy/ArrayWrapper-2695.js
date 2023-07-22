

var ArrayWrapper = function(nums) {
    
    class ArrayWrapper{
        constuctor(arr) {

        }
    }
};



ArrayWrapper.prototype.valueOf = function() {
    
}

ArrayWrapper.prototype.toString = function() {
    
}


const obj1 = new ArrayWrapper([1,2]);
const obj2 = new ArrayWrapper([3,4]);
obj1 + obj2; // 10
String(obj1); // "[1,2]"
String(obj2); // "[3,4]"

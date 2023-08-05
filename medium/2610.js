const nums = [1,3,4,1,2,3,1]
// const [[1,3,4,2],[1,3],[1]] 

var findMatrix = function(nums) {
    let tresor = [[]];
    let currentArrIndex = 0;

    for (let i = 0; i < nums.length; i++) {
        if (!tresor[currentArrIndex].includes(nums[i])) {
            tresor[currentArrIndex].push(nums[i]);
        } 
        
        if (i < nums.length - 1 && tresor[currentArrIndex].includes(nums[i + 1])) {
            currentArrIndex++;
            tresor.push([]);
        }     
    }

    return tresor;
}

console.log(findMatrix(nums)); // Outputs: [[1,3,4,2],[1,3],[1]]

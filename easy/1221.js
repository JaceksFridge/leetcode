
// loop thorugh string

    // r count
    // l count

    // if char = r -> r count ++

    // if char = l -> l count ++


    // ir count = il count
        // supercount + 1
        // clear count


const s = "RLRRLLRLRL"

var balancedStringSplit = function(s) {

    let superCount = 0
    let rCount = 0
    let lCount = 0
    
    for (i in s) {

        s[i] === "R" ? rCount++ : lCount++

        if (rCount === lCount) {
            superCount += 1
            rCount = 0; lCount = 0
        }
    }
    return superCount
}

console.log(balancedStringSplit(s))

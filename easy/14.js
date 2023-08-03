
const strs = ["flower","flow","flight"]


var longestCommonPrefix = function(strs) {

    let i = 0
    let compare
    let finishArr = []

    while (i < strs[0].length) {

        compare = strs[0][i]

        for (s of strs) {

            if (compare != s[i]) {
                return finishArr.join('')
            }
        }
        finishArr.push(compare)
        i++
    }
    return finishArr.join('')
}

console.log(longestCommonPrefix(strs))
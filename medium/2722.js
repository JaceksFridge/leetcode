
arr1 = [
    {"id": 1, "b": {"b": 94},"v": [4, 3], "y": 48}
]
arr2 = [
    {"id": 1, "b": {"c": 84}, "v": [1, 3]}
]


// const join = (arr1, arr2) => {

//     let endArray = arr1
  
//     for (i of arr2) {
        
//         let current = i.id

//         if (endArray.some(e => e.id === current)) {

//             let index = endArray.findIndex(e => e.id === current)
//             let overRide = Object.assign(endArray[index], i)

//         } else {
//             endArray.push(i)
//         }
//     }
//     endArray.sort((a, b) => a.id - b.id)
//     return endArray
// }

// create empty arr

// look at arr1

    // loop over it

        // check if same id already in empty arr
        // if yes

            // override this object with assing

        // if no

            // add object with that id to new arr

// return emtpy arr

const join = (arr1, arr2) => {
    
    const arrs = [...arr1, ...arr2]
    endObj = {}
    
    for (i in arrs) {
        endObj[arrs[i].id] = {...endObj[arrs[i].id], ...arrs[i]}
    }

    return Object.values(endObj)
}
console.log(join(arr1, arr2))


const arr = [1,9,6,3,4]
const size = 3


// var chunk = function(arr, size) {

//     let masterArr = []

//     while (arr.length > 0) {
//         console.log('array:', arr)

//         let slice = arr.slice(0, size)
//         arr.splice(0, size)
//         masterArr.push(slice)
//     }
//     return masterArr
// };




const chunk = (arr, size) => {

    let masterArr = []
    let i = 0

    while (i < arr.length) {

        masterArr.push(arr.slice(i, i+size))
        i += size
    }

    return masterArr
}



console.log(chunk(arr, size))

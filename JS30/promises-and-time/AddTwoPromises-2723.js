








var addTwoPromises = async function(promise1, promise2) {
    const pro1 = Number(promise1)
    const pro2 = Number(promise2)
    console.log('type:', pro1.value)
    const sum = pro1 + pro2
    return sum
};

addTwoPromises(Promise.resolve(2), Promise.resolve(5))
    .then(console.log);

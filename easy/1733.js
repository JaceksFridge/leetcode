

const items = [
    ["phone","blue","pixel"],
    ["computer","silver","phone"],
    ["phone","gold","iphone"]
]
const ruleKey = "type"
const ruleValue = "phone"


var countMatches = function(items, ruleKey, ruleValue) {

    let counter = 0
    let indexer

    switch (ruleKey) {
        case 'type':
            indexer = 0
            break;

        case 'color':
            indexer = 1
            break;
        case 'name':
            indexer = 2
    }

    for (i of items) {
        i[indexer] === ruleValue ? counter++ : null
    }
    return counter
};

console.log(countMatches(items, ruleKey, ruleValue))

export function getCategory(category, masterDeck) {
    return masterDeck[category];
}

export function pickKeyValue(categoryDeck) {
    const keys = Object.keys(categoryDeck); 
    const randomKey = keys[Math.floor(Math.random() * keys.length)]; // Math.random() picks a number between 0 and 1. 
    return {
        key: randomKey,
        value: categoryDeck[randomKey]
    }
}
export function generateRoles(playerCount, imposterplayernum, category, key, value) {
    const roles = [];
    for (let i = 0; i <= playerCount - 1; i++) {
        if (i !== imposterplayernum) {
            roles.push({ // push is the same as .append()
                playernum: i,
                isImposter: false, 
                category: category,
                word: key
            });
        } else {
            roles.push({
                playernum: i,
                isImposter: true, 
                category: category,
                hint: value
            });
        }
    }

    return roles;
}


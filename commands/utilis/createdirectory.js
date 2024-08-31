const fs = require('fs');
const path = require('path');

function createDirectory(dirName) {
    if (!fs.existsSync(dirName)) {
        fs.mkdirSync(dirName);
        console.log(`Director creat: ${dirName}`);
    } else {
        console.log(`Directorul ${dirName} există deja.`);
    }
}

// Se așteaptă un argument de tipul 'dirName'
const args = process.argv.slice(2);
createDirectory(args[0]);

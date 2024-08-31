const fs = require('fs');
const path = require('path');

function deleteDirectory(dirName) {
    if (fs.existsSync(dirName)) {
        fs.rmdirSync(dirName);
        console.log(`Director șters: ${dirName}`);
    } else {
        console.log(`Directorul ${dirName} nu există.`);
    }
}

// Se așteaptă un argument de tipul 'dirName'
const args = process.argv.slice(2);
deleteDirectory(args[0]);

const fs = require('fs');
const path = require('path');

function deleteFile(fileName) {
    if (fs.existsSync(fileName)) {
        fs.unlinkSync(fileName);
        console.log(`Fișier șters: ${fileName}`);
    } else {
        console.log(`Fișierul ${fileName} nu există.`);
    }
}

// Se așteaptă un argument de tipul 'fileName'
const args = process.argv.slice(2);
deleteFile(args[0]);

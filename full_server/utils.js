import fs from 'fs';

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    if (!filePath) {
      reject(new Error('Cannot load the database'));
      return;
    }
    fs.readFile(filePath, 'utf8', (err, content) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const rows = content.split('\n').filter((row) => row.trim() !== '').slice(1);
      const result = {};
      rows.forEach((row) => {
        const cols = row.split(',');
        const name = cols[0];
        const major = cols[cols.length - 1];
        if (!result[major]) result[major] = [];
        result[major].push(name);
      });
      resolve(result);
    });
  });
}

export default readDatabase;

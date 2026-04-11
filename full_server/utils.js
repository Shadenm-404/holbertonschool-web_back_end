import fs from 'fs';

const readDatabase = (filePath) => new Promise((resolve, reject) => {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
    } else {
      const lines = data.split('\n').slice(1).filter((line) => line);
      const result = {};

      lines.forEach((line) => {
        const [firstname, , , field] = line.split(',');

        if (!result[field]) {
          result[field] = [];
        }
        result[field].push(firstname);
      });

      resolve(result);
    }
  });
});

export default readDatabase;

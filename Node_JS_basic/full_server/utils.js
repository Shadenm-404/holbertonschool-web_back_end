import fs from 'fs';

const readDatabase = (filepath) => new Promise((resolve, reject) => {
  fs.readFile(filepath, 'utf-8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const lines = data.split('\n').slice(1);
    const filteredLines = lines.filter((line) => line.trim() !== '');

    const students = {};
    filteredLines.forEach((line) => {
      const [firstname, , , field] = line.split(',');
      if (!students[field]) students[field] = [];
      students[field].push(firstname);
    });

    resolve(students);
  });
});

export default readDatabase;

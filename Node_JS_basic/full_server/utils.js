const fs = require('fs');

const readDatabase = (filePath) => new Promise((resolve, reject) => {
  fs.readFile(filePath, 'utf-8', (error, data) => {
    if (error) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const rows = data.split('\n').filter((line) => line.trim() !== '');
    const students = rows.slice(1);
    const byField = {};

    students.forEach((student) => {
      const [firstname, , , field] = student.split(',');
      if (!byField[field]) {
        byField[field] = [];
      }
      byField[field].push(firstname);
    });

    resolve(byField);
  });
});

module.exports = readDatabase;

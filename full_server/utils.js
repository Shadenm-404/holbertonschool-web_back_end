import fs from 'fs';

export default function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(err);
        return;
      }

      const lines = data.split('\n').filter((l) => l.trim() !== '');
      const students = lines.slice(1);

      const fields = {};
      students.forEach((s) => {
        const [firstname, , , field] = s.split(',');
        if (!fields[field]) fields[field] = [];
        fields[field].push(firstname);
      });

      resolve(fields);
    });
  });
}

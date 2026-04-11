const { readDatabase } = require('../utils');

class StudentsController {
  static getAllStudents(req, res) {
    const filePath = process.argv[2];

    readDatabase(filePath)
      .then((students) => {
        const sortedFields = Object.keys(students).sort((a, b) =>
          a.toLowerCase().localeCompare(b.toLowerCase())
        );

        let response = 'This is the list of our students\n';

        sortedFields.forEach((field) => {
          response += `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}\n`;
        });

        res.status(200).send(response.trim());
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const filePath = process.argv[2];
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(filePath)
      .then((students) => {
        const list = students[major] || [];
        res.status(200).send(`List: ${list.join(', ')}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}

module.exports = StudentsController;

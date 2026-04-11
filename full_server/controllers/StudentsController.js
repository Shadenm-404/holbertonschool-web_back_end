import readDatabase from '../utils';

const database = process.argv[2];

class StudentsController {
  static getAllStudents(req, res) {
    readDatabase(database)
      .then((data) => {
        const fields = Object.keys(data).sort((a, b) => a.localeCompare(b));

        let response = 'This is the list of our students';

        fields.forEach((field) => {
          const list = data[field];
          response += `\nNumber of students in ${field}: ${list.length}. List: ${list.join(', ')}`;
        });

        res.status(200).send(response);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(database)
      .then((data) => {
        const list = data[major];
        res.status(200).send(`List: ${list.join(', ')}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;

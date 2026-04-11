import readDatabase from '../utils';

export default class StudentsController {
  static getAllStudents(req, res) {
    const db = process.argv[2];

    readDatabase(db)
      .then((fields) => {
        let out = 'This is the list of our students';
        const sorted = Object.keys(fields).sort((a, b) =>
          a.localeCompare(b, undefined, { sensitivity: 'base' })
        );

        sorted.forEach((f) => {
          out += `\nNumber of students in ${f}: ${fields[f].length}. List: ${fields[f].join(', ')}`;
        });

        res.status(200).send(out);
      })
      .catch((e) => {
        res.status(500).send(e.message);
      });
  }

  static getAllStudentsByMajor(req, res) {
    const db = process.argv[2];
    const major = req.params.major;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(db)
      .then((fields) => {
        res.status(200).send(`List: ${fields[major].join(', ')}`);
      })
      .catch((e) => {
        res.status(500).send(e.message);
      });
  }
}

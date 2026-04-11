import readDatabase from '../utils';

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const students = await readDatabase(process.argv[2]);
      let output = 'This is the list of our students\n';

      const sortedFields = Object.keys(students).sort();
      for (const field of sortedFields) {
        const studentList = students[field];
        output += `Number of students in ${field}: ${studentList.length}. List: ${studentList.join(', ')}\n`;
      }

      res.status(200).send(output.trim());
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    try {
      const students = await readDatabase(process.argv[2]);
      const studentList = students[major] || [];
      return res.status(200).send(`List: ${studentList.join(', ')}`);
    } catch (error) {
      return res.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;

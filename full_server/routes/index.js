import express from 'express';
import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';

const appRouter = express.Router();

appRouter.route('/').get(AppController.getHomepage);
appRouter.route('/students').get(StudentsController.getAllStudents);
appRouter.route('/students/:major').get(StudentsController.getAllStudentsByMajor);

export default appRouter;

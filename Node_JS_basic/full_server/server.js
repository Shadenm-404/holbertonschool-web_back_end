import express from 'express';
import router from './routes/index';

const app = express();


app.locals.database = process.argv[2];

app.use('/', router);

app.listen(1245);

export default app;

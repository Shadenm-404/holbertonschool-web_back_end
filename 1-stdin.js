process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.setEncoding('utf8');

process.stdin.on('readable', () => {
  let chunk;
  while ((chunk = process.stdin.read()) !== null) {
    const name = chunk.trim();
    process.stdout.write('Your name is: ' + name + '\n');
  }
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});

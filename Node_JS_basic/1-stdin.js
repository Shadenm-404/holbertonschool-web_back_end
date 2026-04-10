process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.setEncoding('utf8');

let input = '';

process.stdin.on('data', (chunk) => {
  input += chunk;
});

process.stdin.on('end', () => {
  input = input.trim();
  if (input) {
    console.log(`Your name is: ${input}`);
  }
  console.log('This important software is now closing');
});

if (process.stdin.isTTY) {
  process.stdin.on('data', (chunk) => {
    const name = chunk.trim();
    console.log(`Your name is: ${name}`);
  });
}

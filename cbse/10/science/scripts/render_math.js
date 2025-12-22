const katex = require('katex');
require('katex/dist/contrib/mhchem.js');

const input = process.argv[2];
const displayMode = process.argv[3] === 'true';

try {
    const output = katex.renderToString(input, {
        displayMode: displayMode,
        throwOnError: false
    });
    console.log(output);
} catch (e) {
    console.error(e);
    process.exit(1);
}

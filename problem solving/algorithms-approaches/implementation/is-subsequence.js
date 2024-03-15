// techgig code gladiators
process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});
// return true if patient string is subsequence of virus string
function isVirusPattern(virus, patient) {
    const lettersCount = {};
    virus.split('').forEach((letter, index) => {
        lettersCount[letter] ? (lettersCount[letter].push(index)) : (lettersCount[letter] = [index]);
    });
    let currentIndex = -1;
    let isInfected = true;
    for(let i=0;i<patient.length; ++i) {
        const letter = patient[i];
        if (!lettersCount[letter] || !lettersCount[letter].length) {
            isInfected = false;
            break;
        }
        let matchIndex = lettersCount[letter].findIndex((val) => val>currentIndex);
        if (matchIndex === -1) {
            isInfected = false;
            break;
        }
        currentIndex = lettersCount[letter][matchIndex];
        lettersCount[letter].splice(0, matchIndex + 1);
    }
    return isInfected;
}

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
	
	//Write code here
    const virusString = input_stdin_array[0];
    const patients = input_stdin_array.slice(2).filter(str => str);
    const output = patients
        .map(patient => isVirusPattern(virusString, patient) ? "POSITIVE" : "NEGATIVE")
        .join("\n");
    process.stdout.write(""+output+"\n");
});

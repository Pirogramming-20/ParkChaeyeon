let answer = generateRandomNumber();
let attempts = 0;

function generateRandomNumber() {
    let numbers = [];
    while (numbers.length < 3) {
        let num = Math.floor(Math.random() * 9) + 1;
        if (numbers.indexOf(num) === -1) numbers.push(num);
    }
    return numbers.join('');
}

function check_numbers() {
    let number1 = document.getElementById('number1').value;
    let number2 = document.getElementById('number2').value;
    let number3 = document.getElementById('number3').value;
    let guess = number1 + number2 + number3;
    attempts++;


    let strike = 0, ball = 0;
    for (let i = 0; i < 3; i++) {
        if (guess[i] === answer[i]) {
            strike++;
        } else if (answer.includes(guess[i])) {
            ball++;
        }

    }

    if (strike === 3) {
        displayResult('./success.png');
        return;
    } else {
        let resultDisplay = document.querySelector('.result-display');
        let result = document.createElement('div');
        result.className = 'check-result';
        let resultContent;

        if (strike === 0 && ball === 0) {

            resultContent = `<span>${number1}  ${number2}  ${number3}</span>` +
                `<span>:</span>` +
                `<span class="out num-result">0</span>`;
        } else {

            resultContent = `<span>${number1}  ${number2}  ${number3}</span>` +
                `<span>:</span>` +
                `<span>${strike}<span class="strike num-result">S</span> ${ball}<span class="ball num-result">B</span></span>`;
        }

        result.innerHTML = resultContent;
        resultDisplay.appendChild(result);
    }


    if (attempts >= 9) {
        displayResult("./fail.png");
        disableButton();
        return;
    }


}

function displayResult(imageFile) {
    let img = document.getElementById('game-result-img');
    img.src = imageFile;
}

function disableButton() {
    let button = document.querySelector('.submit-button');
    button.disabled = true;
}

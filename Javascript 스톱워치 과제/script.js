let startTime;
let savedTime;
let difference;
let tInterval;
let running = false;
const timeDisplay = document.getElementById('time');
const startButton = document.getElementById('start');
const stopButton = document.getElementById('stop');
const resetButton = document.getElementById('reset');
const recordDiv = document.getElementById('newrecord');

startButton.addEventListener('click', startTimer);
stopButton.addEventListener('click', stopTimer);
resetButton.addEventListener('click', resetTimer);

function startTimer() {
    if (!running) {
        startTime = new Date().getTime() - (savedTime || 0);
        tInterval = setInterval(getShowTime, 1);
        running = true;
    }
}

function stopTimer() {
    if (running) {
        clearInterval(tInterval);
        savedTime = difference;
        running = false;
        recordTime();
    }
}

function resetTimer() {
    clearInterval(tInterval);
    running = false;
    savedTime = 0;
    timeDisplay.innerHTML = '00:00';
}

function getShowTime() {
    updatedTime = new Date().getTime();
    difference = updatedTime - startTime;

    let seconds = Math.floor((difference % (1000 * 60)) / 1000);
    let milliseconds = Math.floor((difference % 1000) / 1);

    seconds = (seconds < 10) ? "0" + seconds : seconds;
    milliseconds = (milliseconds < 100) ? (milliseconds < 10 ? "00" + milliseconds : "0" + milliseconds) : milliseconds;

    timeDisplay.innerHTML = seconds + ':' + milliseconds;
}



function recordTime() {
    // 새로운 기록을 담을 div 요소
    const newRecord = document.createElement('div');
    newRecord.className = 'recordNew';

    // 시작 아이콘 생성 + 클릭시 바뀌게
    const startIcon = document.createElement('i');
    startIcon.className = 'fa-regular fa-circle reuse-record';
    startIcon.addEventListener('click', function () {
        startIcon.className = 'fa-regular fa-circle-check';
    });

    //빈 div 배치위함
    const emptydiv = document.createElement('div');
    emptydiv.className = 'recordNew';


    // 기록 시간 표시
    const timeDiv = document.createElement('div');
    timeDiv.innerHTML = timeDisplay.innerHTML;

    //구조화
    newRecord.appendChild(startIcon);
    newRecord.appendChild(timeDiv);
    newRecord.appendChild(emptydiv);
    recordDiv.appendChild(newRecord);
}

// 기록 선택 삭제 기능 수정
recordDiv.addEventListener('click', function (event) {
    if (event.target.classList.contains('fa-regular fa-circle-check')) {
        recordDiv.removeChild(event.target.parentNode);
    }
});

// 전체 기록 선택/해제
let selectAllIcon = document.querySelector('#recordHeader .fa-regular.fa-circle.reuse-record');
selectAllIcon.addEventListener('click', function () {
    const records = recordDiv.getElementsByClassName('recordNew');
    Array.from(records).forEach(record => {
        let icon = record.querySelector('.fa-regular.fa-circle.reuse-record, .fa-regular.fa-circle-check');
        icon.className = (icon.className === 'fa-regular fa-circle reuse-record') ? 'fa-regular fa-circle-check' : 'fa-regular fa-circle reuse-record';
    });
});

// 전체 기록 삭제
let trashAllIcon = document.querySelector('#recordHeader .fa-trash');
trashAllIcon.addEventListener('click', function () {
    while (recordDiv.firstChild) {
        recordDiv.removeChild(recordDiv.firstChild);
    }
});



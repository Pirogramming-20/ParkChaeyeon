// Fetch the items from the JSON file
function loadItems() {
  return fetch('data/data.json')
    .then(response => response.json())
    .then(json => json.items);
}

// Update the list with the given items
// data.json에서 받아온 인자인 items 를 html에 추가하자 
function displayItems(items) {
  const container = document.querySelector('.items');

  //items 안의 object를 html 속 li 태그로 변환 ->map 으로
  //문자열의 배열을 한가지의 문자열로 병합하기 위해 쓰는 것 ->join api
  container.innerHTML = items.map(item => createHTMLString(item)).join('');
}

// Create HTML list item from the given data item
// json 의 items 를 html의 li 태그로 바꾸는 함수
function createHTMLString(item) {
  return `
    <li class="item">
        <img src="${item.image}" alt="${item.type}" class="item__thumbnail" />
        <span class="item__description">${item.gender}, ${item.size}</span>
    </li>
    `;
}


function setEventListeners(items) {
  const logo = document.querySelector('.logo');
  const buttons = document.querySelector('.buttons');
  logo.addEventListener('click', () => displayItems(items));
  buttons.addEventListener('click', event => onButtonClick(event, items));
}

// 버튼 클릭시 처리할 함수
function onButtonClick(event, items) {
  const dataset = event.target.dataset;
  const key = dataset.key;
  const value = dataset.value;

  // 함수 끝내기 
  if (key == null || value == null) {
    return;
  }

  displayItems(items.filter(item => item[key] === value));
}


// main 에 loadItems 함수 정의
// data.json파일을 읽어오는데 시간이 걸려 그냥 item이 아니라 promise를 읽어온다 읽어오지 못했을 경우 catch이용
// data.json파일을 읽어오는데 시간이 걸림 :비동기 작업이라. 즉, 파일을 읽는 동안 JavaScript 코드의 다른 부분이 실행될 수 있도록 
//  Promise 객체는 .then() 메소드를 통해 이행 상태일 때의 처리를, .catch() 메소드를 통해 거부 상태일 때의 처리
loadItems()
  .then(items => {
    displayItems(items);
    setEventListeners(items);
  })
  .catch(console.log);

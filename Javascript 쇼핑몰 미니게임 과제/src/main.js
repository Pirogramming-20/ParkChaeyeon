// Fetch the items from the JSON file
function loadItems() {
  return fetch('data/data.json')
    .then(response => response.json())
    .then(json => json.items);
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

//추가 버튼시 POST
const addButton = document.querySelector('#addButton');
const detailInput = document.querySelector('#detailInput').value;

const timeblock = () => {
  fetch('/timeblock', {
    method: 'POST',
    body: JSON.stringify({timetable_pk:"{{timetable.pk}}",
                          timeblock_start: min,
                          timeblock_end: max,
                          timeblock_detail: detailInput}),
    headers: {
      "Content-Type": "application/json",
    },

  })
    .then((response) => response.json())
    
      
    };

addButton.addEventListener("click", timeblock)
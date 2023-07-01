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
    .then((data) => {
        const postResult = document.querySelector(".planCircleBox");
        postResult.innerHTML = "추가 완료!";
    //   var minSector;
    //   var maxSector;
    //   data.forEach(function(sector) {
    //     for (let i = 0; i < hour24.length; i++) {
    //       if (sector.endtime >= parseInt(hour24[i].display) && sector.starttime <= parseInt(hour24[i].display)) {
    //         ctx.beginPath();
    //         ctx.moveTo(centerX, centerY);
    //         ctx.arc(centerX, centerY, radius, (Math.PI / 180) * hour24[i].start, (Math.PI / 180) * hour24[i].end, false);
    //         ctx.fillStyle = selectedColor;
    //         ctx.fill();
    //         ctx.closePath();
    //       }
    //   }
      });
      
    };

addButton.addEventListener("click", timeblock)
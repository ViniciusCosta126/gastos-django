document.addEventListener('DOMContentLoaded',()=>{
    var data = document.querySelector(".date");
    var btnNext = document.querySelector(".next");
    var btnPrev = document.querySelector(".prev");
    
    var dataNova = data.textContent.split("/");
    
    btnNext.addEventListener("click", () => {
      if (parseInt(dataNova[0]) + 1 > 12) {
        dataNova[0] = 1;
        dataNova[1] = parseInt(dataNova[1]) + 1;
      } else {
        dataNova[0] = parseInt(dataNova[0]) + 1;
      }
      data.innerHTML = `${dataNova[0]}/${dataNova[1]}`;
      window.location.href = `http://localhost:8000/?data=${dataNova[0]}/${dataNova[1]}`;
    });
    btnPrev.addEventListener("click", () => {
      if (parseInt(dataNova[0]) - 1 < 1) {
        dataNova[1] = parseInt(dataNova[1]) - 1;
        dataNova[0] = 12;
      } else {
        dataNova[0] = parseInt(dataNova[0]) - 1;
      }
      data.innerHTML = `${dataNova[0]}/${dataNova[1]}`;
      window.location.href = `http://localhost:8000/?data=${dataNova[0]}/${dataNova[1]}`;
    
    });    
})


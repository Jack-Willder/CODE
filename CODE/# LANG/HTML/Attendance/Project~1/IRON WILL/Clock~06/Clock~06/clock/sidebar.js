let show = document.getElementById("toggleButton");
const querryVar = document.querySelector("#sideMenu");
const span = document.querySelectorAll('span');
localStorage.setItem("mode", null);
var mode = null;

const modeToggle = show.addEventListener("click", () => {
  if (mode != "enabled") {
    querryVar.classList.add("active-content");
    document.getElementById("toggleButton").style.left = "calc(1vw)";
    document.getElementById("toggleButton").style.backgroundColor = "transparent";
    document.getElementById("span1").style.backgroundColor = "whitesmoke";
    document.getElementById("span2").style.backgroundColor = "whitesmoke";
    document.getElementById("span3").style.backgroundColor = "whitesmoke";
    mode = "enabled";
    console.log(mode);
} else {
    querryVar.classList.remove("active-content");
    document.getElementById("toggleButton").style.left = "calc(300px + 1vw)";
    document.getElementById("toggleButton").style.backgroundColor = "whitesmoke";
    document.getElementById("span1").style.backgroundColor = "black";
    document.getElementById("span2").style.backgroundColor = "black";
    document.getElementById("span3").style.backgroundColor = "black";
    mode = null;
    console.log(mode);
  }
});

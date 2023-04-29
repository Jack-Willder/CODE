let show = document.getElementById("toggleButton");
const querryVar = document.querySelector("#sideMenu");
const span = document.querySelectorAll('span');
localStorage.setItem("mode", null);
var mode = null;

const modeToggle = show.addEventListener("click", () => {
  checker();
});


function call(prop)
{
  // console.log(prop)
  if(prop == 'clock')
  {
    document.getElementById('clock').style.visibility = 'visible';
    document.getElementById('counter').style.visibility = 'hidden';
    document.getElementById('counterclock').style.visibility = 'hidden';
    document.getElementById('settings').style.visibility = 'hidden';
    checker();
  }
  if(prop == 'counter')
  {
    document.getElementById('clock').style.visibility = 'hidden';
    document.getElementById('counter').style.visibility = 'visible';
    document.getElementById('counterclock').style.visibility = 'hidden'; 
    document.getElementById('settings').style.visibility = 'hidden';
    checker();
  }
  if(prop == 'counterclock')
  {
    document.getElementById('clock').style.visibility = 'hidden';
    document.getElementById('counter').style.visibility = 'hidden';
    document.getElementById('counterclock').style.visibility = 'visible';
    document.getElementById('settings').style.visibility = 'hidden';
    checker();
  }
  if(prop == 'settings')
  {
    document.getElementById('clock').style.visibility = 'hidden';
    document.getElementById('counter').style.visibility = 'hidden';
    document.getElementById('counterclock').style.visibility = 'hidden';
    document.getElementById('settings').style.visibility = 'visible';
    checker();
  }
}




function checker()
{
  if (mode != "enabled") 
  {
    querryVar.classList.add("active-content");
    document.getElementById("toggleButton").style.left = "calc(0.001vw + 10px)";
    document.getElementById("toggleButton").style.backgroundColor = "transparent";
    document.getElementById("span1").style.backgroundColor = "whitesmoke";
    document.getElementById("span2").style.backgroundColor = "whitesmoke";
    document.getElementById("span3").style.backgroundColor = "whitesmoke";
    mode = "enabled";
    // console.log(mode);
  } 
  else 
  {
    querryVar.classList.remove("active-content");
    document.getElementById("toggleButton").style.left = "calc(0.001vw + 300px + 50px)";
    document.getElementById("toggleButton").style.backgroundColor = "whitesmoke";
    document.getElementById("span1").style.backgroundColor = "black";
    document.getElementById("span2").style.backgroundColor = "black";
    document.getElementById("span3").style.backgroundColor = "black";
    mode = null;
    // console.log(mode);
  }
}

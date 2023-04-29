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

    var temp_width = document.getElementById("toggleButton").clientWidth;
    var temp_height = document.getElementById("toggleButton").clientHeight;

    if(temp_width==100 && temp_height==100) 
    {
      document.getElementById("span1").style.width = "90%";
      document.getElementById("span2").style.width = "90%";
      document.getElementById("span3").style.width = "90%";

      document.getElementById("span2").style.visibility = "hidden";
      document.getElementById("span1").style.rotate = "90deg"
      document.getElementById("span1").style.transform = "translateY(0px) translateX(16px)"
      document.getElementById("span3").style.transform = "translateY(-16.5px)"
      document.getElementById("chile").style.rotate = "45deg";
      mode = "enabled";
      // console.log(mode);
    }
    else
    {
      document.getElementById("span1").style.width = "31px";
      document.getElementById("span2").style.width = "31px";
      document.getElementById("span3").style.width = "31px";

      document.getElementById("span2").style.visibility = "hidden";
      document.getElementById("span1").style.rotate = "90deg"
      document.getElementById("span1").style.transform = "translateY(0px) translateX(1px)"
      document.getElementById("span3").style.transform = "translateY(-16.5px)"
      document.getElementById("chile").style.rotate = "45deg";
      mode = "enabled";
      // console.log(mode);
    }
  } 
  else 
  {
    querryVar.classList.remove("active-content");
    document.getElementById("toggleButton").style.left = "calc(0.001vw + 10px)";
    document.getElementById("toggleButton").style.backgroundColor = "whitesmoke";
    document.getElementById("span1").style.backgroundColor = "black";
    document.getElementById("span2").style.backgroundColor = "black";
    document.getElementById("span3").style.backgroundColor = "black";

    document.getElementById("span2").style.visibility = "visible";
    document.getElementById("span1").style.rotate = "0deg"
    document.getElementById("span1").style.transform = "translateY(0px)"
    document.getElementById("span3").style.transform = "translateY(0px)"
    document.getElementById("chile").style.rotate = "0deg";
    mode = null;
    // console.log(mode);
  }
}

secondInt = 0;
var x = setInterval(function() { ++secondInt;console.log('sring', secondInt);document.getElementById('secondsnum').innerText = secondInt;document.getElementById('minutesnum').innerText = secondInt;document.getElementById('hoursnum').innerText = secondInt;document.getElementById('daysnum').innerText = secondInt; }, 1000);
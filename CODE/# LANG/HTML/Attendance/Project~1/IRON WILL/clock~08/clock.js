var setTime = new Date("dec 03, 2022 00:00:00").getTime();

var x = setInterval(function() {
    var currentTime = new Date().getTime();
    var diff = setTime - currentTime;

    var Days = Math.floor(diff / (24*60*60*1000));
    // console.log("D", Days);
    var Hours = Math.floor((diff % (1000*60*60*24)) / (60*60*1000));
    // console.log("H", Hours);
    var Minutes = Math.floor((diff % (1000*60*60)) / (60*1000));
    // console.log("M", Minutes);
    var Seconds = Math.floor((diff % (1000*60)) / (1000));
    // console.log("S", Seconds);

    // Update elements
    document.getElementById('daysnum').innerText = Days;
    document.getElementById('hoursnum').innerText = Hours;
    document.getElementById('minutesnum').innerText = Minutes;
    document.getElementById('secondsnum').innerText = Seconds;
}, 1000);

// var y = setInterval(function() {
//     var current = new Date().getTime();
// var dif = setTime - current;
// document.getElementById('mil').innerText = Math.floor((dif % (1000)));
// console.log(milliseconds);
// }, 1);
var formateddate = localStorage.getItem('Formated-date')
datetime = String(formateddate);
console.log('Setting clock at : ' + datetime);
var setTime = new Date(formateddate).getTime();
console.log('Converted time : ' + setTime);
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

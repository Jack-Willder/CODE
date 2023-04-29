var button = document.getElementById("settings-button");

button.addEventListener("click", send);

// Year
var current_full_year = new Date().getFullYear();
// Month
var current_full_month = String(new Date().getMonth() + 1);
if (current_full_month.length < 2) {
  current_full_month = "0" + current_full_month;
}
// Date
var current_full_date = String(new Date().getDate());
if (current_full_date.length < 2) {
  current_full_date = "0" + current_full_date;
}
// Hour
var current_full_hours = String(new Date().getHours());
if (current_full_hours.length < 2) {
  current_full_hours = "0" + current_full_hours;
}
// Minute
var current_full_minutes = String(new Date().getMinutes());
if (current_full_minutes.length < 2) {
  current_full_minutes = "0" + current_full_minutes;
}

var current_full_time = current_full_year + "-" + current_full_month + "-" + current_full_date + "T" + current_full_hours + ":" + current_full_minutes;
console.log(current_full_time);

var timer_dial = document.getElementById("input-time");
timer_dial.setAttribute("value", current_full_time);

function send() {
  localStorage.setItem(
    "Formated-date",
    document.getElementById("input-time").value
  );
  location.reload();
}

// "dec 26, 2022 01:00:00"

// 2022-12-02T00:00

// 2023-02-04T

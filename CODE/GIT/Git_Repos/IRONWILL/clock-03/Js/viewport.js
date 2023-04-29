var y = setInterval(function viewportsize() {
    let viewportWidth = window.innerWidth;
    let viewportHeight  = window.innerHeight;

    // alert("ViewportHeight : " + viewportHeight);

    if(viewportHeight>640)
    {
        var coundownClock = document.getElementById("counter").style;
        coundownClock.height = "360px"
        var topgap = (viewportHeight - 360) / 2;
        coundownClock.top = topgap + "px"
    }
    else
    {
        var clockCounterHeight = document.getElementById("counter").clientHeight;
        var topgap = (viewportHeight - clockCounterHeight) / 2;
        document.getElementById("counter").style.top = topgap + "px";
    }
}, 1);
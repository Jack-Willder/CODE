function totalClick(click) 
{
    const totalClicks = document.getElementById('num');
    var sumvalue = parseInt(totalClicks.innerText) + click;
    if(sumvalue < 0) {sumvalue = 0;}
    totalClicks.innerText = sumvalue;
    
    // Avoid negatives and 90+
    if(sumvalue < 0) {totalClicks.innerText = 0}
    if(sumvalue > 90) {totalClicks.innerText = 90}
                
    // Saving to local storage
    localStorage.setItem('number', JSON.stringify(sumvalue));
    changecol(sumvalue);

}

// Reset Button
function resetButton() 
{
    const totalClicks = document.getElementById('num');
    totalClicks.innerText = 0;
    const sumvalue = 0;
    localStorage.setItem('number', JSON.stringify(sumvalue));
    changecol(sumvalue);
}

// Changing font color based on value
function changecol(sumvalue)
{
    var setcolorvar = 0;
    if(sumvalue >= 00 && sumvalue <= 10) {colorChanger('rgb(0, 225, 255)'); setcolorvar = 1;}
    if(sumvalue >= 11 && sumvalue <= 20) {colorChanger('yellow'); setcolorvar = 2;}
    if(sumvalue >= 21 && sumvalue <= 30) {colorChanger('orange'); setcolorvar = 3;}
    if(sumvalue >= 31) {colorChanger('red'); setcolorvar = 4;}
    colorChangertwo(setcolorvar);
}

// Recall value function
const recall = function() 
{
    const sumvalue = 0;
    const numvalue = document.getElementById('num');
    const getvalue = localStorage.getItem('number', sumvalue);
    if(getvalue >= 0 && getvalue <= 90) {numvalue.innerText = getvalue;}
    else {numvalue.innerText = 0;}

}

// Changing background
function colorChanger(value) {document.body.style.backgroundColor = value;}
function colorChangertwo(setcolorvar) {
    document.getElementById('num').style.textShadow = '8px 8px 10px red';
    if(setcolorvar == 1) {document.getElementById('num').style.textShadow = '8px 8px 10px rgb(0, 115, 255)';}
    if(setcolorvar == 2) {document.getElementById('num').style.textShadow = '8px 8px 10px yellow';}
    if(setcolorvar == 3) {document.getElementById('num').style.textShadow = '8px 8px 10px orange';}
    if(setcolorvar == 4) {document.getElementById('num').style.textShadow = '8px 8px 10px orangered';}

}

document.onload = recall();
document.onload = totalClick(0);

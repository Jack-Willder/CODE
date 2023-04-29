/*----------------------------------------------- This Part of the code belongs to the Flat Pge -----------------------------------------------*/
const list = document.querySelectorAll('.list');
function activeLink()
{
    list.forEach((item) => 
    item.classList.remove('active'));
    this.classList.add('active');
}
list.forEach((item) => 
item.addEventListener('click', activeLink))




function pageChanger(pagenumber)
{
    if(pagenumber == 'one') {document.getElementById('pg-one').style.display = 'flex'; document.getElementById('pg-two').style.display = 'none'; document.getElementById('pg-three').style.display = 'none'; document.getElementById('pg-four').style.display = 'none'; document.getElementById('pg-five').style.display = 'none'; document.getElementById('indicatorColor').style.backgroundColor = 'chocolate';}
    if(pagenumber == 'two') {document.getElementById('pg-one').style.display = 'none'; document.getElementById('pg-two').style.display = 'flex'; document.getElementById('pg-three').style.display = 'none'; document.getElementById('pg-four').style.display = 'none'; document.getElementById('pg-five').style.display = 'none'; document.getElementById('indicatorColor').style.backgroundColor = 'tomato';}
    if(pagenumber == 'three') {document.getElementById('pg-one').style.display = 'none'; document.getElementById('pg-two').style.display = 'none'; document.getElementById('pg-three').style.display = 'flex'; document.getElementById('pg-four').style.display = 'none'; document.getElementById('pg-five').style.display = 'none'; document.getElementById('indicatorColor').style.backgroundColor = 'springgreen';}
    if(pagenumber == 'four') {document.getElementById('pg-one').style.display = 'none'; document.getElementById('pg-two').style.display = 'none'; document.getElementById('pg-three').style.display = 'none'; document.getElementById('pg-four').style.display = 'flex'; document.getElementById('pg-five').style.display = 'none'; document.getElementById('indicatorColor').style.backgroundColor = 'turquoise';}
    if(pagenumber == 'five') {document.getElementById('pg-one').style.display = 'none'; document.getElementById('pg-two').style.display = 'none'; document.getElementById('pg-three').style.display = 'none'; document.getElementById('pg-four').style.display = 'none'; document.getElementById('pg-five').style.display = 'flex'; document.getElementById('indicatorColor').style.backgroundColor = 'yellow';}
    if(pagenumber == 'navbar') {document.getElementById('navbarvalue').style.backgroundColor = 'blue';}
}

// Pre-Loader Script
var loader = document.getElementById('pre-loader');
window.addEventListener('load', () => {setTimeout(() => {loader.style.display = 'none';},3000)});
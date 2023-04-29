const button = document.querySelector('button');
const layer = document.querySelector('div');
var layerpos = null;

layer.addEventListener('click', () => 
{
    visbilechanger();
})

function visbilechanger() 
{
    if(layerpos != "show") 
    {
        button.style.visibility = "hidden";
        layerpos = "show";
        console.log(layerpos);
    }
    else 
    {
        button.style.visibility = "visible";
        layerpos = null;
        console.log(layerpos);
    }
}
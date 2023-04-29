var button = document.getElementById('settings-button');

button.addEventListener('click', send);

function send() 
{
    localStorage.setItem('Formated-date', document.getElementById('input-time').value);
    location.reload();
}

// "dec 26, 2022 01:00:00"

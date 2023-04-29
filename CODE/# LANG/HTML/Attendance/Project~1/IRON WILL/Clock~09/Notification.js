const button = document.querySelector('#showNotification');
button.addEventListener('click', () => {
    if(perm === "granted") {
        Notification.requestPermission().then(prem => {
            // alert(prem)
            new Notification('Notification Alert', {
                body: 'hello World',
                data: {hello: "world"},
                tag: 'notify',
                silent: false,
            })
        })
    }
})
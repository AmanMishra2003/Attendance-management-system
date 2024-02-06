
let navlinks = document.querySelectorAll('.nav-link');

navlinks.forEach(element => {
    element.addEventListener('mouseover', (e)=>{
        element.classList.add('active')
    })
});

navlinks.forEach(element => {
    element.addEventListener('mouseout', (e)=>{
        element.classList.remove('active')
    })
});

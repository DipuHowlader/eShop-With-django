document.addEventListener('DOMContentLoaded',() =>{
    const paymentBtns = document.querySelectorAll('.payment-btn');

    paymentBtns.forEach(element =>{
        element.addEventListener('click',(e) =>{
            paymentBtns.forEach(element =>{
                element.classList.remove('active')
            });
            element.classList.add('active')
        });
    });

});

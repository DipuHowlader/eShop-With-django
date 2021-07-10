document.addEventListener('DOMContentLoaded',() =>{
    const paymentBtns = document.querySelectorAll('.payment-btn');
    const cardInfo = document.querySelectorAll('.info')

    paymentBtns.forEach(element =>{
        element.addEventListener('click',(e) =>{
            const btnId = element.dataset.reveal
            cardInfo.forEach(item =>{
               const infoId =  item.dataset.desc
               item.classList.add('none')
               if (btnId===infoId){
                   item.classList.remove('none')
                };
            });
            paymentBtns.forEach(element =>{
                element.classList.remove('active')
            });
            element.classList.add('active')
        });
    });

});

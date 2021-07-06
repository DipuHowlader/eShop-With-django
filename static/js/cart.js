const header = document.querySelector('.header-bottom')

increase.forEach(element =>{
    element.addEventListener('click', () =>{
        const quantity = element.parentElement.parentElement.querySelector('.quantity')
        const total = element.parentElement.parentElement.parentElement.querySelector('.total')
        const price = element.parentElement.parentElement.parentElement.querySelector('.price')
        quantity.innerText = Number(quantity.innerText) + 1
        total.innerText =Number(quantity.innerText) * price.innerText
    });
})


decrease.forEach(element =>{
    element.addEventListener('click', () =>{
        const quantity = element.parentElement.parentElement.querySelector('.quantity')
        const total = element.parentElement.parentElement.parentElement.querySelector('.total')
        const price = element.parentElement.parentElement.parentElement.querySelector('.price')
        if (Number(quantity.innerText) <=1) return
        quantity.innerText = Number(quantity.innerText) -1
        total.innerText =Number(quantity.innerText) * price.innerText
    });
})


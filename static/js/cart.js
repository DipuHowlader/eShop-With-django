const header = document.querySelector('.header-bottom')
const cart_total = document.querySelector('.simpleCart_total')
let = total_price = 0

increase.forEach(element =>{
    element.addEventListener('click', () =>{
        const quantity = element.parentElement.parentElement.querySelector('.quantity')
        const total = element.parentElement.parentElement.parentElement.querySelector('.total')
        const price = element.parentElement.parentElement.parentElement.querySelector('.price')
        total_price = Number(quantity.innerText) * price.innerText
        quantity.innerText = Number(quantity.innerText) + 1
        total.innerText = total_price
        cart_total.innerText = '$ ' + total_price
    });
})
    

decrease.forEach(element =>{
    element.addEventListener('click', () =>{
        const quantity = element.parentElement.parentElement.querySelector('.quantity')
        const total = element.parentElement.parentElement.parentElement.querySelector('.total')
        const price = element.parentElement.parentElement.parentElement.querySelector('.price')
        if (Number(quantity.innerText) <=1) return
        total_price = Number(quantity.innerText) * price.innerText
        quantity.innerText = Number(quantity.innerText) -1
        total.innerText = total_price
        cart_total.innerText = '$ ' + total_price
    });
})


const addToCart = document.getElementById('add-to-cart')
var removeFromCart = document.querySelectorAll('.close1')
const increase = document.querySelectorAll('.plus')
const decrease = document.querySelectorAll('.minus')


const UpdateData = (e) =>{
        const action = e.target.dataset.action
        const product = e.target.dataset.product
        const URL = '/update_data/'
    
        fetch(URL,
        {
            headers:{
                'Accept' :'application/json',
                'Content-Type':  'application/json',
                'X-CSRFTOKEN' : csrftoken,
            },
            method :'POST',
            body : JSON.stringify({'action': action, 'product' : product})
        })
    
        .then(res => res.json())
        .then(data =>console.log(data))

        //stop page refreshing for quantity update
        if (action != 'increase' && action != 'decrease') {
            location.reload(true)
        }
        
}

if (addToCart != null) {
    addToCart.addEventListener('click', UpdateData);
}


removeFromCart.forEach(element =>{
    element.addEventListener('click', UpdateData);
})

increase.forEach(element =>{
    element.addEventListener('click', UpdateData);
})

decrease.forEach(element =>{
    element.addEventListener('click', UpdateData);
})
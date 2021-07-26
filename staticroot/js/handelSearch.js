const form = document.querySelector('.search-bar')
const keyword = document.querySelector('#keyword')

const url = location.href
let value = 'Search'
if (url.includes('keyword')){
    value = url.split('keyword=').pop()
    value  = decodeURIComponent(value.replace('+', ' '))
}
keyword.value = value


keyword.addEventListener('blur', (event) =>{
    if(event.target.value == ''){
        event.target.value = value
    }
})

    
form.addEventListener('submit',(e)=>{
    if (keyword.value == 'Search' || keyword.value == ''){
        e.preventDefault()
    }
});

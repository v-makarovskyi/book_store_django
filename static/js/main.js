//register__window__wrapper
const open = document.querySelector('.register__open')
const wrapper = document.querySelector('.register')
const overlay = document.querySelector('.register__overlay')
const close = document.querySelector('.close')


open.addEventListener('click', () => {
    wrapper.classList.add('show__register')
    overlay.classList.add('active')
})

overlay.addEventListener('click', () => {
    wrapper.classList.remove('show__register')
    overlay.classList.remove('active')
})

close.addEventListener('click', () => {
    wrapper.classList.remove('show__register')
    overlay.classList.remove('active')
    console.log('close')
})


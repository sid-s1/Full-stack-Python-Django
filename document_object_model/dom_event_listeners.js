var headone=document.querySelector("#one")
var headtwo=document.querySelector("#two")
var headthree=document.querySelector("#three")
headone.addEventListener('mouseover',function(){
  headone.textContent='Mouse currently over'
  headone.style.color='Red'
})
headone.addEventListener('mouseout',function(){
  headone.textContent='HOVER OVER ME'
  headone.style.color='black'
})
headtwo.addEventListener('click',function(){
  headtwo.textContent='Clicked on'
  headtwo.style.color='blue'
})
headtwo.addEventListener('mouseout',function(){
  headtwo.textContent='CLICK ME'
  headtwo.style.color='black'
})
headthree.addEventListener('dblclick',function(){
  headthree.textContent='I was double clicked'
  headthree.style.color='green'
})
headthree.addEventListener('mouseout',function(){
  headthree.textContent='DOUBLE-CLICK ME'
  headthree.style.color='black'
})

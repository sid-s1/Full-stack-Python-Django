function getrandomcolor(){
  var base="0123456789ABCDEF"
  var i=0
  var color="#"
  for(i=0;i<6;i++){
    color+=base[Math.floor(Math.random()*16)]
  }
  return color
}
function changeheadercolor(){
var myhead=document.querySelector('h1')
myhead.style.color=getrandomcolor()
}
setInterval("changeheadercolor()",1000)

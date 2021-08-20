// $('h1').click(function(){
//   console.log("There was a click!")
// })
// $('li').click(function(){
//   console.log("Any li was clicked!")
// })
$('h1').click(function(){
  $(this).text('Yo! Someone clicked me!')
})
// $('input').eq(0).keypress(function(){
//   $('h3').toggleClass('turnBlue')
// })
// $('input').eq(0).keypress(function(event){
//   console.log(event)
// })
// $('input').eq(0).keypress(function(event){
//   if(event.which === 13){
//     $('h3').toggleClass('turnRed')
//   }
// })
$('h1').on('dblclick',function(){
  $(this).toggleClass('turnBlue')
})
$('input').eq(1).click(function(){
  $('.container').slideUp(3000)
})

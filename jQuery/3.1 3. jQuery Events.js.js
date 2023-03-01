// jQuery makes it easy to interact with the DOM!
//https://www.w3schools.com/jquery/jquery_events.asp

// List of all possible events!
// https://api.jquery.com/category/events/
//https://www.w3schools.com/jquery/jquery_ref_events.asp

// CLICKS

// On Click
$('h1').click(function(){
  console.log("h1 clicked");
})

// Click on multiple elements
$('li').click(function() {
  console.log("li(s) clicked");
})

// 'this' with jQuery
$('h3').click(function() {
  $(this).text("Text changed on h3");
})

// KEYPRESS

// Toggle class with jQuery
$('input').eq(0).keypress(function() {
  $('h3').toggleClass("Temp");
})

// The event object has a lot of information
$('input').eq(0).keypress(function(event) {
  console.log(event);
})

// Each Keyboard Key has a Keycode, e.g. Enter is 13
$('input').eq(0).keypress(function(event) {
  if(event.which === 13){
    $('h3').toggleClass("Temp");
  }
})

// ON()

// on() is like addEventListener()
$('h2').on("dblclick",function() {
  $('h2').addClass('hidden');
})

$('li').on('mouseenter',function() {
  $(this).toggleClass('NewClass');
})

// EFFECTS and ANIMATIONS

// http://api.jquery.com/category/effects/

$('input').eq(1).val("FADE OUT");

$('input').eq(1).on("click",function(){
  $(".container").fadeOut(2000) ;
})


$('input').eq(1).on("click",function(){
  $(".container").slideUp(2000) ;
})

//main.js - some simple javascript for the sancristocafe site

//when the page first opens
$(document).ready(function(){
 $('.header-of-site').height($(window).height());
});
//
////if the page gets resized change the height of the header to match that space
$(window).on('resize',function(){
	$('.header-of-site').height($(window).height())
});

/* When the user scrolls down, hide the navbar. When the user scrolls up, show the navbar */
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar").style.top = "0";
    document.getElementById('main').style.top = '0'
  } else {
    document.getElementById("navbar").style.top = "-60px";
    document.getElementById('main').style.margin-top = '-60px'
  }
  prevScrollpos = currentScrollPos;
}


// flipping the about us images
$('.flip').hover(function(){
        $(this).find('.card').toggleClass('flipped');
 });

$('.flip-card').hover(function(){$('.flip-card').toggleClass('applyflip');}.bind(this));

$('.header-of-site').delay(1000).fadeTo('slow', 0.3, function()
{
    $(this).css('background-image', "url(http://127.0.0.1:8000/media/images/Mount_Si.jpg)");
}).fadeTo('slow', 1);


////animate the home page
//$(".navbar a").click(function(){
//  $("body,html").animate({
//   scrollTop:$("#" + $(this).data('value')).offset().top
//  },1000)
// });
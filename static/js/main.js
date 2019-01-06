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

// flipping the about us images
$('.flip').hover(function(){
        $(this).find('.card').toggleClass('flipped');
 });

 $('.flip-card').hover(function(){$('.flip-card').toggleClass('applyflip');}.bind(this));
////animate the home page
//$(".navbar a").click(function(){
//  $("body,html").animate({
//   scrollTop:$("#" + $(this).data('value')).offset().top
//  },1000)
// });
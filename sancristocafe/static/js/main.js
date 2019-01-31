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

$(document).ready(function(){
  // Add smooth scrolling to all links
  $("a").on('click', function(event) {

    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){
   
        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });
});

/* When the user scrolls down, hide the navbar. When the user scrolls up, show the navbar */
$(function () {
  var lastScrollTop = 0;
  var $navbar = $('.navbar');

  $(window).scroll(function(event){
    var st = $(this).scrollTop();

    if (st > lastScrollTop) { // scroll down

      // use this is jQuery full is used
      $navbar.fadeOut()

      // use this to use CSS3 animation
      // $navbar.addClass("fade-out");
      // $navbar.removeClass("fade-in");

      // use this if no effect is required
      // $navbar.hide();
    } else { // scroll up

      // use this is jQuery full is used
      $navbar.fadeIn()

      // use this to use CSS3 animation
      // $navbar.addClass("fade-in");
      // $navbar.removeClass("fade-out");

      // use this if no effect is required
      // $navbar.show();
    }
    lastScrollTop = st;
  });
});

// transitioning between content
'use strict';

$('document').ready(function () {
  var transEffect = Barba.BaseTransition.extend({
    start: function start() {
      var _this2 = this;

      this.newContainerLoading.then(function (val) {
        return _this2.fadeInNewcontent(jQuery(_this2.newContainer));
      });
    },
    fadeInNewcontent: function fadeInNewcontent(nc) {
      nc.hide();
      var _this = this;
      $(this.oldContainer).fadeOut(300).promise().done(function () {
        nc.css('visibility', 'visible');
        nc.fadeIn(300, function () {
          _this.done();
        });
      });
    }
  });
  Barba.Pjax.getTransition = function () {
    return transEffect;
  };
  Barba.Pjax.start();
});
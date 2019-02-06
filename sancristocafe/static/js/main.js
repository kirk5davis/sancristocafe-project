//main.js - some simple javascript for the sancristocafe site

$('.header-of-site').height($(window).height());

var smoothScrolling = function(){
  $('a[href*="#"]').on('click', function (e) {
            console.log('clicked an a with href=#');
            if ( $(e.target.hash).length ) {
              e.preventDefault();
              console.log('got here');
            $('html, body').animate({
              scrollTop: $($(this).attr('href')).offset().top
            }, 500, 'linear');
          };
          });
        };
var kirk = new smoothScrolling();


$(document).ready(function(){
  // adjust the homepage splash photo to the window size
    // // Add smooth scrolling to all links
    // $("a").on('click', function(event) {
    //   // Make sure this.hash has a value before overriding default behavior
    //   if (this.hash !== "") {
    //     // Prevent default anchor click behavior
    //     event.preventDefault();
    //     // Store hash
    //     var hash = this.hash;
    //     // Using jQuery's animate() method to add smooth page scroll
    //     // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
    //     console.log('found a hash!')
    //     $('html, body').animate({
    //       scrollTop: $(hash).offset().top
    //     }, 800, function(){
    //       // Add hash (#) to URL when done scrolling (default click behavior)
    //       window.location.hash = hash;
    //     });
    //   } // End if
    // });
  var kirk = new smoothScrolling();

  // add smooth transitioning between pages
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
        $(window).scrollTop(0); 
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
  // don't forget to run <script> contents if it is available
Barba.Dispatcher.on('newPageReady', function (currentStatus, oldStatus, barbaContainer, newPageRawHTML) {
    var els = barbaContainer ? barbaContainer.querySelectorAll('script') : null;
    if (els !== null && els.length > 0) {
        for (var i = 0, l = els.length; i < l; i++) {
            var el = els[i];
            if (el) {
                var evalJsCode = new Function(el.innerHTML);
                evalJsCode();
            }
        }
    }
    var scrollEvent = new smoothScrolling();

});

Barba.Dispatcher.on('transitionCompleted', function(currentStatus, oldStatus, container){
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
      // $navbar.fadeOut()
      // use this to use CSS3 animation
      $navbar.addClass("fade-out");
      $navbar.removeClass("fade-in");
      // use this if no effect is required
      // $navbar.hide();
    } else { // scroll up
      // use this is jQuery full is used
      // $navbar.fadeIn()
      // use this to use CSS3 animation
      $navbar.addClass("fade-in");
      $navbar.removeClass("fade-out");
      // use this if no effect is required
      // $navbar.show();
    }
    lastScrollTop = st;
  });
});


//if the page gets resized change the height of the header to match that space
$(window).on('resize',function(){
	$('.header-of-site').height($(window).height())
});

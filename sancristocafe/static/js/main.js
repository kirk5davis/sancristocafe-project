//main.js - some simple javascript for the sancristocafe site


var resizeHeaderImg = function(){
  $('.header-of-site').height($(window).height());
};

var smoothScrolling = function(){
  $('a[href*="#"]').on('click', function (e) {
            if ( $(e.target.hash).length ) {
              e.preventDefault();
            $('html, body').animate({
              scrollTop: $($(this).attr('href')).offset().top
            }, 500, 'linear');
          };
          });
        };

var swipeCarousel = function(){
  var swiper = new Swiper('.swiper-container', {
    slidesPerView: 4,
    spaceBetween: 30,
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    breakpoints: {
      1024: {
        slidesPerView: 3,
        spaceBetween: 20,
      },
      768: {
        slidesPerView: 2,
        spaceBetween: 10,
      },
      640: {
        slidesPerView: 1,
        spaceBetween: 10,
      },
      320: {
        slidesPerView: 1,
        spaceBetween: 10,
      }
    }
  });
}
		

$(document).ready(function(){
  $('.header-of-site').height($(window).height());
  var resize = new resizeHeaderImg();
  var kirk = new smoothScrolling();
  var carousel = new swipeCarousel();
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
    var carousel = new swipeCarousel();
    var resize = new resizeHeaderImg();

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

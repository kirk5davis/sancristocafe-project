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

// var smoothImgBackgroundsIE = function(){
//   if(navigator.userAgent.match(/Trident\/7\./)) { // if IE
//     $('body').on("mousewheel", function (event) {
//         // remove default behavior
//         event.preventDefault(); 

//         //scroll without smoothing
//         var wheelDelta = event.wheelDelta;
//         var currentScrollPosition = window.pageYOffset;
//         window.scrollTo(0, currentScrollPosition - wheelDelta);
//     });
// }
// };

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
  // var ieFix = new smoothImgBackgroundsIE();
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
    //var ieFix = new smoothImgBackgroundsIE();

});

Barba.Dispatcher.on('transitionCompleted', function(currentStatus, oldStatus, container){
  AOS.init();
});

});


//if the page gets resized change the height of the header to match that space
$(window).on('resize',function(){
	$('.header-of-site').height($(window).height())
});

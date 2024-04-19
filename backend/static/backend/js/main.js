$('.carousel').slick({
  autoplay: true,
  autoplaySpeed: 5000,
  dots: true,
  infinite: true,
  speed: 500,
  fade: true,
  cssEase: 'linear'
});


$('.carousel-questions').slick({
  autoplay: true,
  autoplaySpeed: 5000,
  dots: true,
  arrows: true,
  infinite: true,
  speed: 500,
  slidesToShow: 3,
  slidesToScroll: 3,
  // centerPadding: '40px',
  centerMode: true,
  // variableWidth: true

});



$( ".news-card" ).hover(
  function() {
    $(this).find(".news-description").css( "opacity", "1" );
  }, function() {
    $(this).find(".news-description").css( "opacity", "0" );
  }
);


$( ".questions-card" ).hover(
  function() {
    $(this).find(".questions-description").css( "opacity", "1" );
    $(this).find(".question").css( "opacity", "0" );
  }, function() {
    $(this).find(".questions-description").css( "opacity", "0" );
    $(this).find(".question").css( "opacity", "1" );
  }
);

$(document).ready( function() {
  // init Masonry
  var $grid = $('.grid').masonry({
    columnWidth: '.grid-item',
    itemSelector: '.grid-item',
    gutter: 13,
    percentPosition: true
  });


  // layout Isotope after each image loads
  $grid.imagesLoaded().progress( function() {
    $grid.masonry();
  });
});

function highlightLast30(periods) {
  if ($.countdown.periodsToSeconds(periods) === 30 * 60) { 
    $(this).addClass('highlight'); 
  }
}

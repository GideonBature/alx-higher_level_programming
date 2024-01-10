/* global $ */

$(function () {
  $('DIV#toggle_header').bind('click', function () {
    if ($(this).hasClass('green')) {
      $(this).removeClass('green');
      $(this).addClass('red');
    } else {
      $(this).removeClass('red');
      $(this).addClass('green');
    }
  });
});

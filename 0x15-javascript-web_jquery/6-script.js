/* global $ */

$(function()
{
    $('DIV#update_header').bind('click', function()
    {
        $('header').text('New Header!!!');
    })
})
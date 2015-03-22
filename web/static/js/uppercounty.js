/*
 * Copyright © 2014 Upper County Dolphins
 *
 * Permission is hereby granted, free of charge, to any person obtaining
 * a copy of this software and associated documentation files (the "Software"),
 * to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense,
 * and/or sell copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included
 * in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 * OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
 * IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
 * DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
 * TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
 * OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */

!function ($) {
  $(function() {
    var $window = $(window);
    var $body = $(document.body);

    $('.theme-toggler').click(function() {
      $('.theme-toggle').hide();
      $($(this).attr('data-image-id')).show();
    });

    $body.scrollspy({
      target: '.uc-sidebar'
    });

    $window.on('load', function() {
      $body.scrollspy('refresh')
    });

    $('.uc-container [href=#]').click(function(event) {
      event.preventDefault()
    });

    $('.uc-navbar').tooltip({
      selector: 'a[data-toggle="tooltip"]',
      container: '.uc-navbar .nav'
    });

    var url = window.location;
    $('ul.nav a[href="' + url + '"]').parent().addClass('active');
    $('ul.nav a').filter(function() {
      return this.href == url;
    }).parent().addClass('active');

    if ($('.sidebar').offset()) {
      $('.sidebar').affix({
        offset: {
          top: $('.sidebar').offset().top - 40
        }
      });
    }
    var affixElement = $('.sidebar');
    affixElement.css('width', affixElement.parent().width());

    $('#scroll').click(function() {
      $('html,body').animate({
        scrollTop: window.scrollY + window.innerHeight + navHeight
      }, 1000);
    });
  })
}(jQuery)

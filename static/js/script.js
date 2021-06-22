$(".header__closer").click(function (e) {
  e.preventDefault();
  $(".menu-btn").removeClass('menu-btn_active');
  $(".header").removeClass('header--active');
  $(".header__closer").removeClass('header__closer--active');
});
$(window).scroll(function () {
  var height = $(window).scrollTop();
  /*Если сделали скролл на 100px задаём новый класс для header*/

  if (height > 125) {
    $('.header').addClass('header--fixed');
  } else {
    /*Если меньше 100px удаляем класс для header*/
    $('.header').removeClass('header--fixed');
  }
});
$(".menu-btn").click(function (e) {
  e.preventDefault();
  $(this).toggleClass('menu-btn_active');
  $(".header__nav").toggleClass('header__nav--active');
});
jQuery(document).ready(function ($) {
  var url = document.location.href;
  $.each($(".header__link"), function () {
    if (this.href == url) {
      $(this).addClass('header__link--active');
    }
  });
});
$('.spec__slider').slick({
  dots: false,
  arrows: true,
  infinite: true,
  speed: 300,
  slidesToShow: 3,
  adaptiveHeight: true,
  prevArrow: "<div class='arrow-wrap prev'><i class='fas fa-long-arrow-alt-left '></i></div>",
  nextArrow: "<div class='arrow-wrap next'><i class='fas fa-long-arrow-alt-right '></i></div>",
  responsive: [{
    breakpoint: 1400,
    settings: {
      slidesToShow: 2,
      slidesToScroll: 2,
      infinite: true,
      dots: true
    }
  }, {
    breakpoint: 993,
    settings: {
      slidesToShow: 1,
      slidesToScroll: 1
    }
  } // You can unslick at a given breakpoint now by adding:
  // settings: "unslick"
  // instead of a settings object
  ]
});
$('.slider-for').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: false,
  fade: true,
  asNavFor: '.slider-nav'
});
$('.branch__slider').slick({
  slidesToShow: 2,
  slidesToScroll: 1,
  arrows: true,
  asNavFor: '.branch__nav, .branch__text-nav',
  prevArrow: "<div class='arrow-wrap prev'><i class='fas fa-long-arrow-alt-left '></i></div>",
  nextArrow: "<div class='arrow-wrap next'><i class='fas fa-long-arrow-alt-right '></i></div>",
  responsive: [{
    breakpoint: 1401,
    settings: {
      slidesToShow: 1,
      slidesToScroll: 1,
      infinite: true,
      dots: true
    }
  } // You can unslick at a given breakpoint now by adding:
  // settings: "unslick"
  // instead of a settings object
  ]
});
$('.branch__nav').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  asNavFor: '.branch__slider, .branch__text-nav',
  infinite: true
});
$('.branch__text-nav').slick({
  slidesToShow: 3,
  slidesToScroll: 1,
  asNavFor: '.branch__slider, .branch__nav',
  infinite: true
});
$(document).ready(function () {
  $('#output').val($('#range').val());
  $('#range').mousemove(function () {
    $('#output').val($('#range').val());
  });
  $('#output').change(function () {
    $('#range').val($('#output').val());
  });
});
$(window).keyup(function (e) {
  var target = $('label input[type=checkbox]:focus');

  if (e.keyCode == 9 && $(target).length) {
    $(target).parent().addClass('focused');
  }
});
$(".range-form__clear").click(function () {
  $('input[type=checkbox]').each(function () {
    this.checked = false;
  });
  $('.range-form__clear').removeClass('range-form__clear--active');
});
$(".checkbox").click(function () {
  $('.range-form__clear').addClass('range-form__clear--active');
});
$('.range-form__btn').click(function (e) {
  e.preventDefault();
  var checkboxes = [];
  $('input:checkbox:checked').each(function () {
    checkboxes.push(this.value);
  }); // $('#output').val(checkboxes.join(', '));
  // $('.range').val($('#range').val());
});
var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function () {
    /* Toggle between adding and removing the "active" class,
    to highlight the button that controls the panel */
    this.classList.toggle("active");
    /* Toggle between hiding and showing the active panel */

    var panel = this.nextElementSibling;

    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}

$(".rewiew__open").click(function (e) {
  e.preventDefault();
  $(this).prev().find('.rewiew__text').parent().toggleClass('rewiew__wrap--active');
  $.fn.extend({
    toggleText: function (a, b) {
      return this.text(this.text() == b ? a : b);
    }
  });
  $(this).toggleText('подробнее', 'скрыть');
});
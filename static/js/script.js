$(".header__link-decor, .header__online-link, .header__tel").click(function () {
  $(".menu-btn").removeClass('menu-btn_active');
  $(".header").removeClass('header--active');
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
  $(".header").toggleClass('header--active');
});
jQuery(document).ready(function ($) {
  var url = document.location.href;
  $.each($(".header__link"), function () {
    if (this.href == url) {
      $(this).addClass('header__link--active');
    }
  });
});
jQuery(document).ready(function ($) {
  var url = document.location.href;
  $.each($(".header__dropdown-link"), function () {
    if (this.href == url) {
      $(this).addClass('header__dropdown-link--active');
      $('.header__item-drop').addClass('header__link--active');
    }
  });
});
$(".header__item-drop").click(function (e) {
  e.preventDefault();
  $(".header__dropdown").toggleClass('header__dropdown--active');
});
$(".header__dropdown").mouseleave(function () {
  $(".header__dropdown").removeClass('header__dropdown--active');
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
      infinite: true
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
      infinite: true
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
  infinite: true,
  centerMode: true,
  focusOnSelect: true
});
$('.our-command__wrap').slick({
  infinite: true,
  speed: 300,
  arrows: true,
  slidesToShow: 4,
  slidesToScroll: 1,
  infinite: true,
  dots: false,
  adaptiveHeight: true,
  prevArrow: "<div class='arrow-wrap prev'><i class='fas fa-long-arrow-alt-left '></i></div>",
  nextArrow: "<div class='arrow-wrap next'><i class='fas fa-long-arrow-alt-right '></i></div>",
  responsive: [{
    breakpoint: 992,
    settings: {
      slidesToShow: 3,
      slidesToScroll: 1,
      infinite: true
    }
  }, {
    breakpoint: 768,
    settings: {
      slidesToShow: 2,
      slidesToScroll: 1,
      infinite: true
    }
  }, {
    breakpoint: 481,
    settings: {
      slidesToShow: 1,
      slidesToScroll: 1,
      infinite: true
    }
  } // You can unslick at a given breakpoint now by adding:
  // settings: "unslick"
  // instead of a settings object
  ]
});
$('.rewiew__inner').slick({
  infinite: true,
  speed: 300,
  arrows: true,
  slidesToShow: 4,
  slidesToScroll: 1,
  infinite: true,
  dots: false,
  adaptiveHeight: true,
  prevArrow: "<div class='arrow-wrap prev'><i class='fas fa-long-arrow-alt-left '></i></div>",
  nextArrow: "<div class='arrow-wrap next'><i class='fas fa-long-arrow-alt-right '></i></div>",
  responsive: [{
    breakpoint: 1667,
    settings: {
      slidesToShow: 2,
      slidesToScroll: 1,
      infinite: true
    }
  }, {
    breakpoint: 993,
    settings: {
      slidesToShow: 2,
      slidesToScroll: 1,
      infinite: true
    }
  }, {
    breakpoint: 481,
    settings: {
      slidesToShow: 1,
      slidesToScroll: 1,
      infinite: true
    }
  } // You can unslick at a given breakpoint now by adding:
  // settings: "unslick"
  // instead of a settings object
  ]
});
$('.blog-home__inner').slick({
  infinite: true,
  speed: 300,
  arrows: true,
  slidesToShow: 4,
  slidesToScroll: 1,
  infinite: true,
  dots: false,
  adaptiveHeight: true,
  prevArrow: "<div class='arrow-wrap prev'><i class='fas fa-long-arrow-alt-left '></i></div>",
  nextArrow: "<div class='arrow-wrap next'><i class='fas fa-long-arrow-alt-right '></i></div>",
  responsive: [{
    breakpoint: 1367,
    settings: {
      slidesToShow: 3,
      slidesToScroll: 1,
      infinite: true
    }
  }, {
    breakpoint: 993,
    settings: {
      slidesToShow: 2,
      slidesToScroll: 1,
      infinite: true
    }
  }, {
    breakpoint: 568,
    settings: {
      slidesToShow: 1,
      slidesToScroll: 1,
      infinite: true
    }
  } // You can unslick at a given breakpoint now by adding:
  // settings: "unslick"
  // instead of a settings object
  ]
}); // $(document).ready(function(){
// 	$('#output').val($('#range').val());
// 	$('#range').mousemove(function() {
// 		$('#output').val($('#range').val());
// 	});
// 	$('#output').change(function() {
// 		$('#range').val($('#output').val());
// 	});
// })

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

let onChange = function () {
  let range = document.getElementById('range');

  if (range.value >= 55) {
    document.getElementById('output').innerHTML = range.value + '+';
  } else {
    document.getElementById('output').innerHTML = range.value;
  }
};

document.getElementById('range').addEventListener('input', function () {
  onChange();
});
onChange();
$('.range-form__btn').click(function (e) {
  e.preventDefault();
  var checkboxes = [];
  $('input:checkbox:checked').each(function () {
    checkboxes.push(this.value);
  });
  $('.popup').addClass('popup--active');
  $('#value').val(checkboxes.join(', '));

  if ($('#range').val() >= 55) {
    $('#old').val($('#range').val() + ' +');
  } else {
    $('#old').val($('#range').val());
  } // $('#old').val($('#range').val());

});
$('.popup__closer, .popup__cancel').click(function () {
  $('.popup').removeClass('popup--active');
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
  $(this).parent().toggleClass('rewiew__item--active');
  $.fn.extend({
    toggleText: function (a, b) {
      return this.text(this.text() == b ? a : b);
    }
  });
  $(this).toggleText('подробнее', 'скрыть');
});
$('.our-command__profile-text-cancel').click(function (e) {
  e.preventDefault();
  $('.our-command__profile-text').removeClass('our-command__profile-text--active');
});
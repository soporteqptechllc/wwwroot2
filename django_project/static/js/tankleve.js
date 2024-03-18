$(document).ready(function() {
  /*TANQUE 1*/
  $(".tk1").each(function() {
    var amount = $('.lq1').attr('data-amount')
    var quantity = amount;
    $(this).find('.lq1').animate({
      'height': parseInt(amount) + '%'
    }, 1000);
    $('.ring1').css({
      height: 100 - amount + 10 + '%'
    });
    $('.text1').text(quantity + '%');
  });
  $('.text1').each(function() {
    var $this1 = $(this);
    jQuery({
      Counter: 0
    }).animate({
      Counter: $this1.text()
    }, {
      duration: 1000,
      easing: 'swing',
      step: function() {
        $this1.text(Math.ceil(this.Counter) + "%");
      }
    });
  });
  /*TANQUE 2*/
  $(".tk2").each(function() {
    var amount = $('.lq2').attr('data-amount')
    var quantity = amount;
    $(this).find('.lq2').animate({
      'height': parseInt(amount) + '%'
    }, 1000);
    $('.ring2').css({
      height: 100 - amount + 10 + '%'
    });
    $('.text2').text(quantity + '%');
  });
  $('.text2').each(function() {
    var $this2 = $(this);
    jQuery({
      Counter: 0
    }).animate({
      Counter: $this2.text()
    }, {
      duration: 1000,
      easing: 'swing',
      step: function() {
        $this2.text(Math.ceil(this.Counter) + "%");
      }
    });
  }); 
  /*TANQUE 3*/
  $(".tk3").each(function() {
    var amount = $('.lq3').attr('data-amount')
    var quantity = amount;
    $(this).find('.lq3').animate({
      'height': parseInt(amount) + '%'
    }, 1000);
    $('.ring3').css({
      height: 100 - amount + 10 + '%'
    });
    $('.text3').text(quantity + '%');
  });
  $('.text3').each(function() {
    var $this3 = $(this);
    jQuery({
      Counter: 0
    }).animate({
      Counter: $this3.text()
    }, {
      duration: 1000,
      easing: 'swing',
      step: function() {
        $this3.text(Math.ceil(this.Counter) + "%");
      }
    });
  });
  /*TANQUE 4*/
  $(".tk4").each(function () {
    var amount = $('.lq4').attr('data-amount')
    var quantity = amount;
    $(this).find('.lq4').animate({
      'height': parseInt(amount) + '%'
    }, 1000);
    $('.ring4').css({
      height: 100 - amount + 10 + '%'
    });
    $('.text4').text(quantity + '%');
  });
  $('.text4').each(function () {
    var $this4 = $(this);
    jQuery({
      Counter: 0
    }).animate({
      Counter: $this4.text()
    }, {
      duration: 1000,
      easing: 'swing',
      step: function () {
        $this4.text(Math.ceil(this.Counter) + "%");
      }
    });
  });
  /*TANQUE 5*/
  $(".tk5").each(function () {
    var amount = $('.lq5').attr('data-amount')
    var quantity = amount;
    $(this).find('.lq5').animate({
      'height': parseInt(amount) + '%'
    }, 1000);
    $('.ring5').css({
      height: 100 - amount + 10 + '%'
    });
    $('.text5').text(quantity + '%');
  });
  $('.text5').each(function () {
    var $this5 = $(this);
    jQuery({
      Counter: 0
    }).animate({
      Counter: $this5.text()
    }, {
      duration: 1000,
      easing: 'swing',
      step: function () {
        $this5.text(Math.ceil(this.Counter) + "%");
      }
    });
  });
  /*TANQUE 6*/
  $(".tk6").each(function () {
    var amount = $('.lq6').attr('data-amount')
    var quantity = amount;
    $(this).find('.lq6').animate({
      'height': parseInt(amount) + '%'
    }, 1000);
    $('.ring6').css({
      height: 100 - amount + 10 + '%'
    });
    $('.text6').text(quantity + '%');
  });
  $('.text6').each(function () {
    var $this6 = $(this);
    jQuery({
      Counter: 0
    }).animate({
      Counter: $this6.text()
    }, {
      duration: 1000,
      easing: 'swing',
      step: function () {
        $this6.text(Math.ceil(this.Counter) + "%");
      }
    });
  });
  /*TANQUE 7*/
  $(".tk7").each(function () {
    var amount = $('.lq7').attr('data-amount')
    var quantity = amount;
    $(this).find('.lq7').animate({
      'height': parseInt(amount) + '%'
    }, 1000);
    $('.ring7').css({
      height: 100 - amount + 10 + '%'
    });
    $('.text7').text(quantity + '%');
  });
  $('.text7').each(function () {
    var $this7 = $(this);
    jQuery({
      Counter: 0
    }).animate({
      Counter: $this7.text()
    }, {
      duration: 1000,
      easing: 'swing',
      step: function () {
        $this7.text(Math.ceil(this.Counter) + "%");
      }
    });
  });
  /*TANQUE 8*/
  $(".tk8").each(function () {
    var amount = $('.lq8').attr('data-amount')
    var quantity = amount;
    $(this).find('.lq8').animate({
      'height': parseInt(amount) + '%'
    }, 1000);
    $('.ring8').css({
      height: 100 - amount + 10 + '%'
    });
    $('.text8').text(quantity + '%');
  });
  $('.text8').each(function () {
    var $this8 = $(this);
    jQuery({
      Counter: 0
    }).animate({
      Counter: $this8.text()
    }, {
      duration: 1000,
      easing: 'swing',
      step: function () {
        $this8.text(Math.ceil(this.Counter) + "%");
      }
    });
  });
  /*TANQUE 9*/
  $(".tk9").each(function () {
    var amount = $('.lq9').attr('data-amount')
    var quantity = amount;
    $(this).find('.lq9').animate({
      'height': parseInt(amount) + '%'
    }, 1000);
    $('.ring9').css({
      height: 100 - amount + 10 + '%'
    });
    $('.text9').text(quantity + '%');
  });
  $('.text9').each(function () {
    var $this9 = $(this);
    jQuery({
      Counter: 0
    }).animate({
      Counter: $this9.text()
    }, {
      duration: 1000,
      easing: 'swing',
      step: function () {
        $this9.text(Math.ceil(this.Counter) + "%");
      }
    });
  });
  /*TANQUE 10*/
  $(".tk10").each(function () {
    var amount = $('.lq10').attr('data-amount')
    var quantity = amount;
    $(this).find('.lq10').animate({
      'height': parseInt(amount) + '%'
    }, 1000);
    $('.ring10').css({
      height: 100 - amount + 10 + '%'
    });
    $('.text10').text(quantity + '%');
  });
  $('.text10').each(function () {
    var $this10 = $(this);
    jQuery({
      Counter: 0
    }).animate({
      Counter: $this10.text()
    }, {
      duration: 1000,
      easing: 'swing',
      step: function () {
        $this10.text(Math.ceil(this.Counter) + "%");
      }
    });
  });
  /*TANQUE 11*/
  $(".tk11").each(function () {
    var amount = $('.lq11').attr('data-amount')
    var quantity = amount;
    $(this).find('.lq11').animate({
      'height': parseInt(amount) + '%'
    }, 1000);
    $('.ring11').css({
      height: 100 - amount + 10 + '%'
    });
    $('.text11').text(quantity + '%');
  });
  $('.text11').each(function () {
    var $this11 = $(this);
    jQuery({
      Counter: 0
    }).animate({
      Counter: $this11.text()
    }, {
      duration: 1000,
      easing: 'swing',
      step: function () {
        $this11.text(Math.ceil(this.Counter) + "%");
      }
    });
  });
  /*TANQUE 12*/
  $(".tk12").each(function () {
    var amount = $('.lq12').attr('data-amount')
    var quantity = amount;
    $(this).find('.lq12').animate({
      'height': parseInt(amount) + '%'
    }, 1000);
    $('.ring12').css({
      height: 100 - amount + 10 + '%'
    });
    $('.text12').text(quantity + '%');
  });
  $('.text12').each(function () {
    var $this12 = $(this);
    jQuery({
      Counter: 0
    }).animate({
      Counter: $this12.text()
    }, {
      duration: 1000,
      easing: 'swing',
      step: function () {
        $this12.text(Math.ceil(this.Counter) + "%");
      }
    });
  });
  /*TANQUE 13*/
  $(".tk13").each(function () {
    var amount = $('.lq13').attr('data-amount')
    var quantity = amount;
    $(this).find('.lq13').animate({
      'height': parseInt(amount) + '%'
    }, 1000);
    $('.ring13').css({
      height: 100 - amount + 10 + '%'
    });
    $('.text13').text(quantity + '%');
  });
  $('.text13').each(function () {
    var $this13 = $(this);
    jQuery({
      Counter: 0
    }).animate({
      Counter: $this13.text()
    }, {
      duration: 1000,
      easing: 'swing',
      step: function () {
        $this13.text(Math.ceil(this.Counter) + "%");
      }
    });
  });
  /*TANQUE 14*/
  $(".tk14").each(function () {
    var amount = $('.lq14').attr('data-amount')
    var quantity = amount;
    $(this).find('.lq14').animate({
      'height': parseInt(amount) + '%'
    }, 1000);
    $('.ring14').css({
      height: 100 - amount + 10 + '%'
    });
    $('.text14').text(quantity + '%');
  });
  $('.text14').each(function () {
    var $this14 = $(this);
    jQuery({
      Counter: 0
    }).animate({
      Counter: $this14.text()
    }, {
      duration: 1000,
      easing: 'swing',
      step: function () {
        $this14.text(Math.ceil(this.Counter) + "%");
      }
    });
  });
  /*TANQUE 15*/
  $(".tk15").each(function () {
    var amount = $('.lq15').attr('data-amount')
    var quantity = amount;
    $(this).find('.lq15').animate({
      'height': parseInt(amount) + '%'
    }, 1000);
    $('.ring15').css({
      height: 100 - amount + 10 + '%'
    });
    $('.text15').text(quantity + '%');
  });
  $('.text15').each(function () {
    var $this15 = $(this);
    jQuery({
      Counter: 0
    }).animate({
      Counter: $this15.text()
    }, {
      duration: 1000,
      easing: 'swing',
      step: function () {
        $this15.text(Math.ceil(this.Counter) + "%");
      }
    });
  });
  
});
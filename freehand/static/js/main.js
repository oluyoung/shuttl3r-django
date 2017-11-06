(function($){
  /**
  NAV BAR
  **/

  /* TOGGLE MOBILE NAV
  */
  $('#nav-mob-toggle').on('click', function(e){
    e.preventDefault();
    $('body').toggleClass('is-showNavMob');
  });
  
  /* SHOW SOCIAL ICONS
  */
  $('#icon-more-btn').on('click', function(e){
    e.preventDefault();
    $('body').toggleClass('is-showNavFollow');
    $(this).toggleClass('icon-more-open');
  });
  
  /* MAKE NAV STICKY
  */    
  $(window).on('scroll', function(e){
    /*
    if ($(document).scrollTop() > ($('.nav').outerHeight()-5)) {
      $('.nav').css('position', 'fixed'); 
    } else {
      $('.nav').css('position', 'absolute');
    }*/
    $('.nav').css('position', 'fixed');
    $('body').addClass('is-navSticky');
    if( $(document).scrollTop() === 0 ){
      $('body').removeClass('is-navSticky');
      $('.nav').css('position', 'absolute');
    }
  });

  /** OPEN DRIVER ORDER MODAL
  */
  $('.license .view-btn, .route-outline .apply-btn').each(function(){
    $(this).on('click', function(e){
      e.preventDefault();
      $(this).magnificPopup({
        type: 'inline',
        callbacks: {
          close: function(){
            $('.order-form form').find('input[type=reset]').trigger('click');
          }  
        }
      });
    });
  });

  /* CHANGE CHOOSE BUTTON TO CHECK CHECKBOX
  */
  $('.order-form').each(function(){
    var btn = $(this).find('.choose-btn'),
      $checkbox = $(this).find('.within');

    btn.on('click', function(e){
      e.preventDefault();
      if($(this).hasClass('yes')){
        $checkbox.prop('checked', true);
      } else {
        $checkbox.prop('checked', false);
      }
      // console.log($checkbox.prop('checked'));
      btn.removeClass('selected');
      $(this).addClass('selected');
    });
  });


  $('.order-form form').each(function(){
    form = $(this);
    form.find('.start-date').on('change', function(){
      console.log(console.log('changed'));
      console.log("start:", $(this).val());
      console.log("end:", form.find('.end-date'));
      form.find('.end-date').attr('disabled', false);
      form.find('.end-date').attr('min', $(this).val());
      console.log("end:", form.find('.end-date').attr('min'));
    });
  });

  // ORDER FORM AJAX REQUEST
  $('.order-form form').submit(function(e){
    e.preventDefault();
    let form = $(this),
     action = form.attr('action');

    let data = {
        // hires
        start_date: form.find('.start-date').val(),
        end_date: form.find('.end-date').val(),
        is_within_lagos: form.find('.within').prop('checked'),
        pickup_address: form.find('.pickup-addr').val(),
        // shuttle
        subscription: form.find('.subscription-choice').val(),
        morning_stop: form.find('.morning-pickup-stop').val(),
        morning_time: form.find('.morning-pickup-time').val(),
        evening_stop: form.find('.evening-pickup-stop').val(),
        evening_time: form.find('.evening-pickup-time').val(),

        item_id: form.find('.item_id').val(),
        user: form.find('.user_id').val(),
    };

    $.ajax({
      url: action,
      type: 'POST',
      data: {
        // hires
        start_date: form.find('.start-date').val(),
        end_date: form.find('.end-date').val(),
        is_within_lagos: form.find('.within').prop('checked'),
        pickup_address: form.find('.pickup-addr').val(),
        // shuttle
        subscription: form.find('.subscription-choice').val(),
        morning_stop: form.find('.morning-pickup-stop').val(),
        morning_time: form.find('.morning-pickup-time').val(),
        evening_stop: form.find('.evening-pickup-stop').val(),
        evening_time: form.find('.evening-pickup-time').val(),

        item_id: form.find('.item_id').val(),
        user: form.find('.user_id').val(),
        csrfmiddlewaretoken: form.find('input[name=csrfmiddlewaretoken]').val()
      },
      error: function(xhr){
        console.log('error');
        console.log(data);
      },
      success: function(){
        console.log('successful');
        console.log(data);
        // reset form
        form.find('input[type=reset]').trigger('click');
        $('.order-form .choose-btn').removeClass('selected');
        // close mag pop
        $.magnificPopup.close();
      },

    });

  });

})(jQuery);
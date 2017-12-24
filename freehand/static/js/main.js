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


  /* SHOW TOP MOST NAV ON MOBILE RESPONSIVE UPWARD SCROLL
  */

  var lastScrollTop=0, delta=5;
  $(window).scroll(function(){
    var wScroll = $(this).scrollTop();

    if(Math.abs(lastScrollTop - wScroll) <= delta)
      return;

    if (wScroll > lastScrollTop){
      // downscroll code
      if(!($(window).width()>768)) $('body.is-navSticky nav').css('top', '-50px');
    } else {
      // upscroll code
      $('body.is-navSticky nav').css('top', '-10px');
    }

    // reset lastscrolltop distance
    lastScrollTop = wScroll;
  });


  /* DISPLAY USER MENU
  */

  $('.nav-icons .user-nav-icon').on('click', function(e){
    e.preventDefault();
    $('.nav-icons .user-nav-menu').toggle('300');
  });
  $('.nav-icons .user-nav-menu').on('mouseleave', function(event) {
    $(this).hide(300);
  });



  /** OPEN DRIVER ORDER MODAL
  */

  $('.open-request').each(function(){
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


  /* ORDER FORM END DATE RENDER AFTER START DATE
  */
  
  $('.order-form form').each(function(){
    form = $(this);
    var enddate = form.find('.end-date');
    form.find('.start-date').on('change', function(){
      var startdate = $(this);

      enddate.attr('disabled', false);
      enddate.attr('min', startdate.val());
      enddate.val(startdate.val());

    });
  });


  /**/

  new LazyLoad({
    elements_selector: ".lazy"
  });
  

  /* SHOW SUBSCRIPTION DAILY START DATE
  */

  $('.route-sheet').each(function(){
    var sheet = $(this);
    sheet.find('.order-form #subscription-choice').on('change', function(){
      if($(this).val().toLowerCase() == 'daily'){
        $('.date-hidden').find('input').attr('required','required');
        $('.date-hidden').show('1000');
      } else {
        $('.date-hidden').hide('1000');
        $('.date-hidden .start-date').val('');
        $('.date-hidden').find('input').removeAttr('required');
      }
      sheet.find('.price').css('color', '#111');
      if($(this).val().toLowerCase() == 'daily') {
        sheet.find('.price_daily').css('color', '#009688');
        sheet.find('.selected_price').val(sheet.find('.price_daily').attr('data-price'));
      }
      if($(this).val().toLowerCase() == 'weekly'){
        sheet.find('.price_weekly').css('color', '#009688');
        sheet.find('.selected_price').val(sheet.find('.price_weekly').attr('data-price'));
      }
      if($(this).val().toLowerCase() == 'monthly'){
        sheet.find('.price_monthly').css('color', '#009688');
        sheet.find('.selected_price').val(sheet.find('.price_monthly').attr('data-price'));
      }
    });
  });


  /* ORDER FORM AJAX REQUEST
  */
  $('.driver-form form, .car-form form').submit(function(e){
    e.preventDefault();
    var form = $(this);
    var action = form.attr('action');
    var data = {
      // hires
      start_date: form.find('.start-date').val(),
      end_date: form.find('.end-date').val(),
      is_within_lagos: form.find('.within').prop('checked'),
      order_class: form.find('.order_class').val(),
      pickup_address: form.find('.pickup-addr').val(),
      user: form.find('.user_id').val(),
      csrfmiddlewaretoken: form.find('input[name=csrfmiddlewaretoken]').val()
    };

    $.ajax({
      url: action,
      type: 'POST',
      data: data,
      error: function(xhr){
        console.log('error');
        $('#order-alert').html('Oops! There was an error in ordering, kindly try again or refresh.');
      },
      success: function(){
        console.log('successful');
        // reset form
        form.find('input[type=reset]').trigger('click');
        $('.order-form .choose-btn').removeClass('selected');        
        // show order alert
        $('#order-alert').html('The order was successful. <a href="/users/user/dashboard" class="order-alert-view-orders">VIEW ORDERS</a>');
      },
      complete: function(){
        console.log(data);
        $('#order-alert').append('<a href="#" id="close-order-alert">x</a>');
        // show order alert
        $('#order-alert').css({'display':'block','transform':'translateY(0%)'});
        // close mag pop
        $.magnificPopup.close();
      }
    });

  });

  $('.shuttle-form form').submit(function(e){
    e.preventDefault();
    var form = $(this),
      action = form.attr('action');
    order_obj = {
      // 
      amount: (form.find('.selected_price').val()*100),
      email: form.find('.user_id').attr('data-identifier'),
      // shuttle
      daily_pickup_date: form.find('.daily-pickup-date').val(),
      subscription: form.find('.subscription-choice').val(),
      morning_stop: form.find('.morning-pickup-stop').val(),
      morning_time: form.find('.morning-pickup-time').val(),
      evening_stop: form.find('.evening-pickup-stop').val(),
      evening_time: form.find('.evening-pickup-time').val(),
      item_id: form.find('.item_id').val(),
      user: form.find('.user_id').val(),
      csrfmiddlewaretoken: form.find('input[name=csrfmiddlewaretoken]').val()
    };

    pay_with_paystack(order_obj, action);

  });  // end Shuttle Order Submit function

  /* Paytsack Paynment Function */
  function pay_with_paystack(orderObj, action){
    var handler = PaystackPop.setup({
      key: 'pk_test_663e2f645c09ff2b3008ea4133c4ab5060e7f934',
      email: orderObj.email,
      amount: orderObj.amount,
      callback: function(response){
        $('.order-form form').find('input[type=reset]').trigger('click');
        // $('.order-form .choose-btn').removeClass('selected');        
        // close mag pop
        $.magnificPopup.close();
        var posting = $.post(action, order_obj);
        posting.done(function(data){
          console.log('success');
          // success order alert
          $('#order-alert').html('The order was successful. <a href="/users/user/dashboard" class="order-alert-view-orders">VIEW ORDERS</a>');
          // show order alert
          $('#order-alert').append('<a href="#" id="close-order-alert">x</a>');
          $('#order-alert').css({'display':'block','transform':'translateY(0%)'});
        });
        posting.fail(function(data){
          console.log('error');
          console.log(data);
        })
      },
      onClose: function(){
        $('#order-alert').html('Oops! There was an error in your payment, kindly try again or refresh.');
        // show order alert
        $('#order-alert').append('<a href="#" id="close-order-alert">x</a>');
        $('#order-alert').css({'display':'block','transform':'translateY(0%)'});
      }
    });
    handler.openIframe();
  }

  /* Show Ordder Alert */
  $('#del-acct').on('click', function(e){
    e.preventDefault();
    $('#order-alert').html('Are you sure you want to delete your account? <a href="/users/user/delete" id="del-yes">YES</a> <a href="#" id="del-no">NO</a><a href="#" id="close-order-alert">x</a>');
    $('#order-alert').show('1000');
  });

  /* Delete user */
  $('#del-yes').on('click', function(e){
    e.preventDefault();
    $('#del-form').submit();
  });

  /* Close Order Alert */
  $('#order-alert').on('click', '#del-no, #close-order-alert', function(e){
    e.preventDefault();
    console.log('clicked');
    $('#order-alert').hide('1000');
  });

  /* Google Maps Render for Directions In Shuttle Routes */
  $('.route-outline').each(function(){
    var route = $(this);
    var btn = $(this).find('.apply-btn');

    function setCenter(geocoder, address){
      var directionsDisplay = new google.maps.DirectionsRenderer();
      var directionsService = new google.maps.DirectionsService();
      geocoder.geocode({'address':address}, function(results, status){
        if(status===google.maps.GeocoderStatus.OK){
          console.log(results[0].geometry.location);
          var map = new google.maps.Map(document.getElementById(btn.attr('data-map-id')), {
            center: results[0].geometry.location,
          });
          directionsDisplay.setMap(map);

          // calculates route from point A to B showing stopovers
          var start = btn.attr('data-map-start'),
          end = btn.attr('data-map-end'),
          waypts = [],
          checkboxArr = route.find('.stop-list').eq(0).find('option');
          
          for(var i=0;i<checkboxArr.length;i++){
            waypts.push({
              location:checkboxArr.eq(i).attr('data-location'),
              stopover:true });
          }

          var request = {
            origin: start,
            destination: end,
            waypoints: waypts,
            optimizeWaypoints: true,
            travelMode: google.maps.TravelMode.DRIVING
          };

          console.log(request);

          directionsService.route(request, function(response, status){
            if(status === 'OK'){
              directionsDisplay.setDirections(response);
              var route = response.routes[0];
              console.log(route);
            } else {
              console.log('Failed to get Directions' + status);
            }
          });

        } else {
          console.log('Geocode was not successful due to: ' + status);
        }
      });
    }
    
    function initialize(){
      var geocoder = new google.maps.Geocoder();
      setCenter(geocoder, btn.attr('data-map-start'));
    }

    var applybtnid = $(this).find('.apply-btn').attr('data-id');
    var applybtn = document.getElementById(applybtnid);
    google.maps.event.addDomListener(applybtn, 'click', initialize);
    
  }); // route outline


  /* Parallax */
  
    var wScroll = $(window).scrollTop();
    $('html.no-touchevents .flyers').each(function(){
      var $flyer = $(this);
      if(wScroll > $flyer.offset().top-$(window).height()/1.2){
        $flyer.find('li').each(function(i){
          setTimeout(function(){
            $flyer.find('li').eq(i).addClass('is-showing');
          }, 150*(i+1));
        });
      }
    });

  $(window).scroll(function(){
    var wScroll = $(this).scrollTop();
    $('html.no-touchevents .flyers').each(function(){
      var $flyer = $(this);
      if(wScroll > $flyer.offset().top-$(window).height()/1.2){
        $flyer.find('li').each(function(i){
          setTimeout(function(){
            $flyer.find('li').eq(i).addClass('is-showing');
          }, 150 * (i+1));
        })
      }  
    });
  });


  /* Unsliders */
  $('html.touchevents .flyers').unslider({
    autoplay: true,
    infinte: true,
    delay: 3000,
    keys: false,
    arrows: false
  });

  $('html.touchevents .shuttle-how-wrap').unslider({
    autoplay: true,
    infinte: true,
    delay: 2000,
    keys: false,
    arrows: false
  });

})(jQuery);


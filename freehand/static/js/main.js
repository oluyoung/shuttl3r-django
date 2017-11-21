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


  /* DISPLAY USER MENU
  */
  $('.nav-icons .user-nav-icon').on('click', function(e){
    e.preventDefault();
    $('.nav-icons .user-nav-menu').toggle();
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
/*  $('.order-form form').each(function(){
    form = $(this);
    form.find('.start-date').on('change', function(){
      console.log(console.log('changed'));
      console.log("start:", $(this).val());
      console.log("end:", form.find('.end-date'));
      form.find('.end-date').attr('disabled', false);
      form.find('.end-date').attr('min', $(this).val());
      console.log("end:", form.find('.end-date').attr('min'));
    });
  });*/


  /* ORDER FORM AJAX REQUEST
  */
  $('.order-form form').submit(function(e){
    e.preventDefault();
    let form = $(this),
     action = form.attr('action');

   /* let data = {
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
    };*/

    $.ajax({
      url: action,
      type: 'POST',
      data: {
        // hires
        start_date: form.find('.start-date').val(),
        end_date: form.find('.end-date').val(),
        is_within_lagos: form.find('.within').prop('checked'),
        order_class: form.find('.order_class').val(),
        pickup_address: form.find('.pickup-addr').val(),
        // shuttle
        subscription: form.find('.subscription-choice').val(),
        morning_stop: form.find('.morning-pickup-stop').val(),
        morning_time: form.find('.morning-pickup-time').val(),
        evening_stop: form.find('.evening-pickup-stop').val(),
        evening_time: form.find('.evening-pickup-time').val(),

        user: form.find('.user_id').val(),
        csrfmiddlewaretoken: form.find('input[name=csrfmiddlewaretoken]').val()
      },
      error: function(xhr){
        console.log('error');
        // console.log(data);
        $('#order-alert').text('Oops! There was an error in ordering, kindly try again or refresh.');
      },
      success: function(){
        console.log('successful');
        // console.log(data);
        // reset form
        form.find('input[type=reset]').trigger('click');
        $('.order-form .choose-btn').removeClass('selected');        
        // show order alert
        $('#order-alert').html('The order was successful. <a href="/users/user/dashboard" class="order-alert-view-orders">VIEW ORDERS</a>');
      },
      complete: function(){
        // show order alert
        $('#order-alert').show();
        // close mag pop
        $.magnificPopup.close();
      }

    });

  });  // end Order Submit function

  $('#close-order-alert').on('click', function(e){
    e.preventDefault();
    $('#order-alert').hide();
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

  /* Unsliders */
  $('html.touchevents .flyers').unslider({
    autoplay: true,
    infinte: true,
    delay: 3000,
    keys: false,
    arrows: false
  });

})(jQuery);


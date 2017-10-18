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
    $('.license .view-btn').each(function(){
  		$(this).on('click', function(e){
        e.preventDefault();
  		  $(this).magnificPopup({
          type: 'inline',
        });
  		});
  	});


    /* CHANGE CHOOSE BUTTON TO CHECK CHECKBOX
    */
  	$('.order-form .choose-btn').each(function(){
      var btn = $(this),
        $checkbox = $('.driver-order-form #within');
      btn.on('click', function(e){
        e.preventDefault();
        if(btn.hasClass('yes')){
           $checkbox.prop('checked', true);
           $checkbox.attr('checked', true);
        } else {
          $checkbox.prop('checked', false);
          $checkbox.attr('checked', false);
        }
        $('.driver-order-form .choose-btn').removeClass('selected');
        btn.addClass('selected');
      });
  	});



})(jQuery);
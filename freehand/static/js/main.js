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
		/*if ($(document).scrollTop() > ($('.nav').outerHeight()-5)) {
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

  	/** OPEN DRIVER INFO MODAL
  	*/
/*  	$('.driver-license').each(function(){
  		$(this).on('click', function(){
  			$(this).find('.driver-portfolio').trigger('click');
  		});
  	});*/

})(jQuery);
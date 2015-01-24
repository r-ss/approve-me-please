$(document).ready(function() {

	var debug = $('#debug_field');

	

	// alert('ok');

	

	function ajust_height(){
		var window_height = $(window).height();
		var content_height = $('#content').height();
	    // debug.text('window:' + window_height + ' content:' + content_height);
	    $('#title').height((window_height - content_height) / 2 - 12);
		$('#info').height((window_height - content_height) / 2 - 13);
	}

	$(window).resize(function(){
        ajust_height()
    });

    ajust_height();

});


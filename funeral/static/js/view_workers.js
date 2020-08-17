$(function() {
	if (!$('#workers-wrapper, #view-workers').length) {
		return;
	}	
		// Add logic for search filter
	var searchVal, comparator, hasMatch, regex, showAll;
	$('#search-worker').on('keyup', function() {
		searchVal = $(this).val();
		showAll = false;
		// not searching for anything
		if (searchVal === '') {
			showAll = true;	}

		$.each($('.worker-nodule'), function() {
			comparator = $(this).find('.first_name, .last_name, .Main_job_description,\
			 .date_joined, .City_or_Town, .likes').text();
			//comparator += $(this).find('.stars').attr('data-star-count');
			hasMatch = comparator.match( new RegExp(searchVal, "ig") );
			if (hasMatch || showAll) {
				if ($(this).is(':hidden')) {
					$(this).fadeIn();
				}
			}
			else {
				$(this).fadeOut();
			}
		});
	});
});
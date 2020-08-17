$(function() {
	if (!$('#reviews-wrapper, #view-review').length) {
		return;
	}

	// Add star glyphs to each review
	var numStars, $stars, i;
	$.each($('.review-nodule'), function() {
		numStars = $(this).find('.stars').attr('data-star-count');
		$stars = $('<span>');
		for (i = 0; i < 5; i++) {
			if (i < numStars) {
				glyphClass = 'glyphicon-star';
			}
			else {
				glyphClass = 'glyphicon-star-empty';
			}

			$stars.append($('<span>').addClass('glyphicon ' + glyphClass));
		}
		$(this).find('.stars').html($stars);
	});


	// Add logic for search filter
	var searchVal, comparator, hasMatch, regex, showAll;
	$('#search-filter').on('keyup', function() {
		searchVal = $(this).val();

		showAll = false;
		// not searching for anything
		if (searchVal === '') {
			showAll = true;
		}

		$.each($('.review-nodule'), function() {
			comparator = $(this).find('.name, .review, .date').text();
			comparator += $(this).find('.stars').attr('data-star-count');

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
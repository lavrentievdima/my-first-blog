window.onload = function() {

	var scrollUp = document.getElementById('scrollup');
	scrollUp.style.display = 'none';

	scrollUp.onmouseover = function() {
		scrollUp.style.opacity=0.5;
		scrollUp.style.filter  = 'alpha(opacity=50)';
	};

	scrollUp.onmouseout = function() {
		scrollUp.style.opacity = 0.7;
		scrollUp.style.filter  = 'alpha(opacity=70)';
	};

	scrollUp.onclick = function() {
		window.scrollTo(0,0);
	};

	window.onscroll = function () {
		if ( window.pageYOffset > 0 ) {
			scrollUp.style.display = 'block';
		} else {
			scrollUp.style.display = 'none';
		}
	};
};
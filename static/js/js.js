function getCookie(name) {
	let cookieValue = null;
	if (document.cookie && document.cookie !== "") {
		const cookies = document.cookie.split(";");
		for (let i = 0; i < cookies.length; i++) {
			const cookie = cookies[i].trim();
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + "=")) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}

$(document).ready(function () {
	const darkModeSwitch = document.getElementById('darkModeSwitch');
	const htmlElement = document.documentElement;
	darkModeSwitch.addEventListener('change', function () {
		if (darkModeSwitch.checked) {
			htmlElement.setAttribute('data-bs-theme', 'dark');
			dark_mode = 'on'
		} else {
			htmlElement.removeAttribute('data-bs-theme');
			dark_mode = 'off'
		}
		$.ajax({
			url: '/api/change_dark_mode/',
			type: "POST",
			dataType: "json",
			data: JSON.stringify({dark_mode: dark_mode}),
			headers: {
			  "X-Requested-With": "XMLHttpRequest",
			  "X-CSRFToken": getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
			},
			success: (data) => {				
				//console.log(data);
			},
			error: (error) => {
			  console.log(error);
			}
		});
	});

});
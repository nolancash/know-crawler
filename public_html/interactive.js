window.onload = function() {
	$("selectAllUrls").onclick = function() { allUrls(true); };
	$("deselectAllUrls").onclick = function() { allUrls(false); };
	$("schedule").onsubmit = function() {
		return validateCheckboxes("daysOfWeek[]", "day in a week");
	};
	$("sources").onsubmit = function() {
		return validateCheckboxes("urls[]", "news source");
	};
};

function allUrls(val) {
	var urls = document.getElementsByName("urls[]");
	for (i = 0; i < urls.length; i++) {
		urls[i].checked = val;
	}
}

function validateCheckboxes(checkboxName, message) {
	var boxes = document.getElementsByName(checkboxName);
	for (i = 0; i < boxes.length; i++) {
		if (boxes[i].checked) {
			return true;
		}
	}
	alert("Please select at least one " + message + ".");
	return false;
}
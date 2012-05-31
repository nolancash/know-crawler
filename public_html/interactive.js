window.onload = function() {
	$("crawlerOn").onclick = turnCrawler;
	$("crawlerOff").onclick = turnCrawler;
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

function turnCrawler() {
	var xmlhttp;
	if (window.XMLHttpRequest) {
		// code for IE7+, Firefox, Chrome, Opera, Safari
	  xmlhttp = new XMLHttpRequest();
	} else {
		// code for IE6, IE5
	  xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
	}
	
	xmlhttp.open("POST","index.php",true);
	xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	xmlhttp.send("state=" + this.value);
}
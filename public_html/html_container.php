<?php
function html_doc_top() {
	?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
		<title>KNOW-Crawler Settings</title>
		
		<!-- CSS stylesheet -->
		<link href="index.css" type="text/css" rel="stylesheet" />

		
		<!-- Linked JavaScript files -->
		<!-- some JS libraries I used before, we can use them if we want later -->
		<script src="http://ajax.googleapis.com/ajax/libs/prototype/1.6.1.0/prototype.js" type="text/javascript"></script>
		<script src="http://ajax.googleapis.com/ajax/libs/scriptaculous/1.8.3/scriptaculous.js" type="text/javascript"></script>
		<script src="interact.js" type="text/javascript"></script>

	</head>
	<body>
	<?php
}

function crawler_switch() {
	?>
	
	<?php
}

function time_setting_top() {
	?>
	<fieldset>
		<legend>Time Schedule:</legend>
		<div>
			<strong>Crawler:</strong>
			<label><input type="radio" id="crawlerOn" name="state" value="on" checked="true" />On</label>
			<label><input type="radio" id="crawlerOff" name="state" value="off" />Off</label>
		</div>
		<form id="schedule" action="index.php" method="post"> 
			<!-- Get time setting from database -->
	<?php
}

function time_setting_bottom() {
	?>
			<div>
				<input type="submit" value="Submit" />
			</div>
		</form>
	</fieldset>
	<?php
}

function url_setting_top() {
	?>
	<fieldset>
		<legend>Articles to Crawl:</legend>
		<div>
			<strong>Article List:</strong>
		<div>
		<div>
			<button id="selectAllUrls">Select All</button>
			<button id="deselectAllUrls">Deselect All</button>
		</div>
		<form id="sources" action="index.php" method="post"> 
			<div>
				<!-- Get news sources from database -->
	<?php
}

function url_setting_bottom() {
	?>
			</div>
			<div>
				<input type="submit" value="Submit" />
			</div>
		</form>
	</fieldset>
	<?php
}

function html_doc_bottom() {
	?>
	</body>
</html>
<?php
}
?>
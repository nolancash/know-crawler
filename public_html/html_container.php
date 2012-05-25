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

	</head>
	<body>
	<?php
}

function time_setting_top() {
	?>
		<form action="index.php" method="post"> 
			<fieldset>
				<legend>Time Schedule:</legend>
				<!-- Get time setting from database -->
	<?php
}

function time_setting_bottom() {
	?>
				<div>
					<input type="submit" value="Submit" />
				</div>
			</fieldset>
		</form>
	<?php
}

function url_setting_top() {
	?>
	<form action="index.php" method="post"> 
		<fieldset>
			<legend>Articles to Crawl:</legend>
			<div>
				<strong>Article List:</strong>
			<div>
			<div>
				<!-- Get articles from database -->
	<?php
}

function url_setting_bottom() {
	?>
			</div>
			<div>
				<input type="submit" value="Submit" />
			</div>
		</fieldset>
	</form>
	<?php
}

function html_doc_bottom() {
	?>
	</body>
</html>
<?php
}
?>
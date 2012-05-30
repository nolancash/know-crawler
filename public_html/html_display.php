<!--
html_display.php populates KNOW-Crawler website with the current 
crawler's configuration.
-->

<?php
include("db_manager.php");

# Queries and displays crawler switch ("On" or "Off"), schedule 
# and news sources settings.
function display_settings() {
	display_crawler_switch();
	
	time_setting_top();
	// query schedule table
	display_time_setting();
	time_setting_bottom();
	
	url_setting_top();
	// query user_list and white_list tables
	$user_urls = get_rows(USER_TABLE, URL_COLUMN, URL_COLUMN);
	$white_urls = get_rows(WHITE_TABLE, URL_COLUMN, URL_COLUMN);
	display_url_setting($user_urls, $white_urls);
	url_setting_bottom();
}

# Creates HTML elements to display the crawler on/off switch.
function display_crawler_switch() {
	?>
	<fieldset>
		<legend>Crawler:</legend>
	<?php
	$rows = get_rows(SWITCH_TABLE, STATE_COLUMN, STATE_COLUMN);
			
	if (empty($rows)) {
		die("The " . SWITCH_TABLE . " table is empty.");
	}
	
	$state = $rows[0];
	
	if ($state) {
		?>
		<label><input type="radio" name="state" id="crawlerOn" value="1" checked="true" />On</label>
		<label><input type="radio" name="state" id="crawlerOff" value="0" />Off</label>
		<?php
	} else {
		?>
		<label><input type="radio" name="state" id="crawlerOn" value="1" />On</label>
		<label><input type="radio" name="state" id="crawlerOff" value="0" checked="true" />Off</label>
		<?php
	}
	?>
	</fieldset>
	<?php
}

# Creates HTML elements to display the schedule setting.
function display_time_setting() {
	$rows = get_rows(SCHEDULE_TABLE, DAY_COLUMN);
			
	if (empty($rows)) {
		die("The " . SCHEDULE_TABLE . " table is empty.");
	}
	
	$hour = $rows[0][HOUR_COLUMN];
		
	if ($hour < MAX_HOUR) {
		$period = "am";
		
		if ($hour == 0) {
			# midnight
			$hour = 12;
		}
	} else {
		$period = "pm";
		
		if ($hour > MAX_HOUR) {
			$hour = $hour - MAX_HOUR;
		}
	}
	?>
	<div>
		<strong>Time:</strong>
		<select name="hour">
	<?php
	for ($i = 1; $i <= MAX_HOUR; $i++) {
		if ($i == $hour) {
			?>
			<option value=<?= "\"" . $i . "\"" ?> selected="selected" /> <?= $i . ":00" ?> </option>
			<?php
		} else {
			?>
			<option value=<?= "\"" . $i . "\"" ?> /> <?= $i . ":00" ?> </option>
			<?php
		}
	}
	?>
		</select>
		<select name="period">
	<?php
	
	if ($period == "am") {
		?>
			<option value="am" selected="selected">am</option>
			<option value="pm">pm</option>
		<?php
	} else {
		?>
			<option value="am">am</option>
			<option value="pm" selected="selected">pm</option>
		<?php
	}
	?>
		</select>
	</div>
	<div>
		<strong>Days:</strong>
	<?php
	$days = array();
	
	foreach ($rows as $row) {
		array_push($days, $row[DAY_COLUMN]);
	}
	
	$DAYS_OF_WEEK = array("Sunday", "Monday", "Tuesday", "Wednesday",
											"Thursday", "Friday", "Saturday" );
											
	for ($i = 0; $i < count($DAYS_OF_WEEK); $i++) {
		if (in_array($i, $days)) {
			?>
			<input type="checkbox" name="daysOfWeek[]" value=<?= "\"" . $i . "\"" ?> checked="checked" /> <?= $DAYS_OF_WEEK[$i] ?>
			<?php
		} else {
			?>
			<input type="checkbox" name="daysOfWeek[]" value=<?= "\"" . $i . "\"" ?> /> <?= $DAYS_OF_WEEK[$i] ?>
			<?php
		}
	}
	?>
	</div>
	<?php
}

# Creates HTML elements to display the news sources setting.
function display_url_setting($user_urls, $white_urls) {
	foreach ($white_urls as $white_url) {		
		if (in_array($white_url, $user_urls)) {
			?>
			<input type="checkbox" name="urls[]" value=<?= "\"" . $white_url . "\"" ?> checked="checked" /> <?= $white_url ?> <br/>
			<?php
		} else {
			?>
			<input type="checkbox" name="urls[]" value=<?= "\"" . $white_url . "\"" ?> /> <?= $white_url ?> <br/>
			<?php
		}
	}
}

function time_setting_top() {
	?>
	<fieldset>
		<legend>Time Schedule:</legend>
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
?>
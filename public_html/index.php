<?php

include("html_container.php");

# Prints HTML header.
html_doc_top();

const SERVER = "ovid01.u.washington.edu";
const PORT_NUM = "32002";
const USER_NAME = "root";
const PASSWORD = "purple pony disco";
const DB_NAME = "know_db";

const SCHEDULE_TABLE = "schedule";
const DAY_COLUMN = "day";
const HOUR_COLUMN = "hour";

const USER_TABLE = "user_list";
const WHITE_TABLE = "white_list";
const URL_COLUMN = "url";

const MAX_HOUR = 12;

ini_set('mysql.default_socket', '/rc12/d04/knowcse2/mysql.sock');
$connection = mysql_connect(SERVER . ":" . PORT_NUM, USER_NAME, PASSWORD);
check_result_successful($connection, "mysql_connect");

$select = mysql_select_db(DB_NAME);
check_result_successful($select, "mysql_select_db");

// handle HTTP requests
if ($_SERVER["REQUEST_METHOD"] == "GET") {
	display_settings();
	
} else if ($_SERVER["REQUEST_METHOD"] == "POST") {
	if (isset($_POST["hour"]) and isset($_POST["period"])) {
		// time setting
		$hour = $_POST["hour"];
		$period = $_POST["period"];
		
		if ($period != "am" and $hour != 12) {
			$hour += 12;
		} else if ($period == "am" and $hour == 12) {
			$hour = 0;
		}
		
		// delete old time setting
		$remove_all_query = "DELETE FROM " . SCHEDULE_TABLE . ";";
		do_query($remove_all_query);
		
		if (isset($_POST["daysOfWeek"])) {
			$daysOfWeek = $_POST["daysOfWeek"];
			
			foreach ($daysOfWeek as $day) {
				$set_time_query = "INSERT INTO schedule VALUES ('$day', '$hour');";
				do_query($set_time_query);
			}
		} else {
			// no day selected
			$set_time_query = "INSERT INTO schedule VALUES (0, '$hour');";
			do_query($set_time_query);
		}
	} else if (isset($_POST["urls"])) {
		// url setting: at least 1 url is selected
		$new_user_urls = $_POST["urls"];
		$user_urls = get_rows(USER_TABLE, URL_COLUMN, URL_COLUMN);
		
		for ($i = 0; $i < count($new_user_urls); $i++) {
			$url = $new_user_urls[$i];
			
			if (!in_array($url, $user_urls)) {
				// newly selected url
				$add_url_query = "INSERT INTO " . USER_TABLE . " (" . URL_COLUMN . ") " . 
												"VALUES ('$url');";
				do_query($add_url_query);
			}
		}
					
		for ($i = 0; $i < count($user_urls); $i++) {
			$old_url = $user_urls[$i];
			
			if (!in_array($old_url, $new_user_urls)) {
				// deselected url
				$remove_url_query = "DELETE FROM " . USER_TABLE . 
														" WHERE " . URL_COLUMN . " = '$old_url';";
				do_query($remove_url_query);
			}
		}
		
	} else {
		// url setting: no url selected
		$remove_all_query = "DELETE FROM " . USER_TABLE . ";";
		do_query($remove_all_query);
	}
	
	display_settings();
}

mysql_close($connection);

html_doc_bottom();

# Calls mysql_query on the query, checks if the call 
# is successful, and return the query result.
function do_query($query) {
	$result = mysql_query($query);
	check_result_successful($result, "mysql_query of " . $query);
	
	return $result;
}

# Checks whether the query result was successful.
# If not, prints an error and exits.
function check_result_successful($result, $info) {
	if (!$result) {
		die("SQL error during '$info': " . mysql_error());
	}
}

# Queries and displays time and url settings.
function display_settings() {
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

# Returns a list of all rows from a table, sorted by 
# a specified column in ascending order.
function get_rows($table, $order_by, $target_column = NULL) {
	$query = "SELECT * FROM $table " . 
					"ORDER BY $order_by ASC;";
	$result = do_query($query);
	
	$rows = array();
	
	while ($row = mysql_fetch_array($result)) {
		if (isset($target_column)) {
			array_push($rows, $row[$target_column]);
		} else {
			array_push($rows, $row);
		}
	}
	
	return $rows;
}

# Creates HTML elements to display the time setting.
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

# Creates HTML elements to display the url setting.
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
?>
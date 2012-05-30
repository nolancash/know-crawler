<?php
include("html_display.php");

$connection = mysql_connect(SERVER . ":" . PORT_NUM, USER_NAME, PASSWORD);
check_result_successful($connection, "mysql_connect");

$select = mysql_select_db(DB_NAME);
check_result_successful($select, "mysql_select_db");

// handle HTTP requests
if ($_SERVER["REQUEST_METHOD"] == "GET") {
	display_settings();
	
} else if ($_SERVER["REQUEST_METHOD"] == "POST") {
	if (isset($_POST["state"])) {
		// crawler on/off
		$state = $_POST["state"];
		
		do_query("DELETE FROM " . SWITCH_TABLE . ";");
		do_query("INSERT INTO " . SWITCH_TABLE . " VALUES ('$state');");
		
	} else if (isset($_POST["hour"]) and isset($_POST["period"])) {
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
				$set_time_query = "INSERT INTO " . SCHEDULE_TABLE . " VALUES ('$day', '$hour');";
				do_query($set_time_query);
			}
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
?>
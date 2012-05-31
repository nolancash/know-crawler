<!--
db_manager.php handles interaction with MySQL database.
-->

<?php

const SERVER = "ovid01.u.washington.edu";
const PORT_NUM = "32002";
const USER_NAME = "root";
const PASSWORD = "purple pony disco";
const DB_NAME = "know_db";

const SWITCH_TABLE = "crawler_switch";
const STATE_COLUMN = "state";

const SCHEDULE_TABLE = "schedule";
const DAY_COLUMN = "day";
const HOUR_COLUMN = "hour";

const NEWS_SOURCES_TABLE = "news_sources";
const NSOURCE_URL_COLUMN = "nsource_url";
const NSOURCE_NAME_COLUMN = "nsource_name";
const USER_TABLE = "user_list";
const WHITE_TABLE = "white_list";
const URL_COLUMN = "url";

const MAX_HOUR = 12;

ini_set('mysql.default_socket', '/rc12/d04/knowcse2/mysql.sock');


# Calls mysql_query on the query, checks if the call 
# is successful, and returns the query result.
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

# Returns a list of rows, where each row contains 
# a news source name and its url.
function get_nsource_rows($url_table) {
	$query = "SELECT a." . NSOURCE_NAME_COLUMN . ", a." . NSOURCE_URL_COLUMN .
					" FROM " . NEWS_SOURCES_TABLE . " a, $url_table b " . 
					"where a." . NSOURCE_URL_COLUMN . " = b." . URL_COLUMN . 
					" ORDER BY a." . NSOURCE_NAME_COLUMN . " ASC;";
	$result = do_query($query);
	
	$nsource_rows = array();
	
	while ($row = mysql_fetch_array($result)) {
		array_push($nsource_rows, $row);
	}
	
	return $nsource_rows;
}
?>
<?php
const SERVER = "localhost";
const USER_NAME = "root";
const PASSWORD = "purple pony disco";
const DB_NAME = "know_db";
const USER_TABLE = "user_list";
const WHITE_TABLE = "white_list";
const URL_COLUMN = "url";

$connection = mysql_connect(SERVER, USER_NAME, PASSWORD);
checkResultSuccessful($connection, "mysql_connect");

$connection = mysql_select_db(DB_NAME);
checkResultSuccessful($connection, "mysql_select_db");

$user_list = get_url_list(USER_TABLE);
$white_list = get_url_list(WHITE_TABLE);
	
if ($_SERVER["REQUEST_METHOD"] == "GET") {
	display_urls($user_list, $white_list);
	
} else if ($_SERVER["REQUEST_METHOD"] == "POST") {
	$new_user_list = $_POST["userList"];
	
	if (!empty($new_user_list)) {
		$new_size = count($new_user_list);
	
		for ($i = 0; i < $new_size; $i++) {
			$url = $new_user_list[$i];
			
			if (!in_array($url, $user_list)) {
				// new selected url
				$add_url_query = "INSERT INTO " . USER_TABLE . " (" . URL_COLUMN . ") " . 
								"VALUES ('$url');";
				mysql_query($add_url_query);
			}
		}
		
		$old_size = count($user_list);
		
		for ($i = 0; i < $old_size; $i++) {
			$old_url = $user_list[$i];
			
			if (!in_array($old_url, $new_user_list)) {
				// deselected url
				$remove_url_query = "DELETE FROM " . USER_TABLE . 
									" WHERE " . URL_COLUMN . " = '$old_url';";
				mysql_query($remove_url_query);
			}
		}
	} else {
		// no url selected
	}
}

mysql_close($connection);
?>

<?php

# Checks whether the query result was successful.
# If not, prints an error and exits.
function checkResultSuccessful($result, $info) {
	if (!$result) {
		die("SQL error during '$info': " . mysql_error());
	}
}

# Queries the url list of the given type (user or white list).
# Returns the result array of the query.
function get_url_list($list_type) {
	$list_query = "SELECT " . URL_COLUMN . " FROM '$list_type' " . 
				"ORDER BY " . URL_COLUMN . " ASC;";
	$list_result = mysql_query($list_query);
	
	checkResultSuccessful($list_result, $list_query);
	
	$url_list = array();
	
	while ($row = mysql_fetch_array($list_result)) {
		array_push($url_list, $row[URL_COLUMN]);
	}
	
	return $url_list;
}

# Creates HTML elements to display the urls.
function display_urls($user_list, $white_list) {
	foreach ($white_list as $white_url) {
		if (in_array($white_url, $user_list)) {
			?>
			<input type="checkbox" name="userList[]" value=<?= "\"" . $white_url . "\"" ?> checked="checked" /> <?= $white_url ?> <br/>
			<?php
		} else {
			?>
			<input type="checkbox" name="userList[]" value=<?= "\"" . $white_url . "\"" ?> /> <?= $white_url ?> <br/>
			<?php
		}
	}
}
?>
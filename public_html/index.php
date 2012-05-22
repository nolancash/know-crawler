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
		<form action="scheduler" method="post"> 
			<fieldset>
				<legend>Time Schedule:</legend>
				<div>
					<strong>Time:</strong>
					<input type="text" name="hour" size="8" maxlength="5" />
					<input type="text" name="minute" size="8" maxlength="5" />
					<select name="period">
						<option value="am" selected="selected">am</option>
						<option value="pm">pm</option>
					</select>
				</div>
				<div>
					<strong>Days:</strong>
					<!-- We should do this part in php, querying the database
						 to figure out if they are checked or not -->
					<input type="checkbox" name="daysofweek" value="Sunday" /> Sunday 
					<input type="checkbox" name="daysofweek" value="Monday" /> Monday 
					<input type="checkbox" name="daysofweek" value="Tuesday" /> Tuesday 
					<input type="checkbox" name="daysofweek" value="Wednesday" /> Wednesday
					<input type="checkbox" name="daysofweek" value="Thursday" /> Thursday 
					<input type="checkbox" name="daysofweek" value="Friday" /> Friday 
					<input type="checkbox" name="daysofweek" value="Saturday" /> Saturday 
				</div>
				<div>
					<input type="submit" value="Submit" />
				</div>
			</fieldset>
		</form>
		
		<form action="index.php" method="post"> 
			<fieldset>
				<legend>Articles to Crawl:</legend>
				<div>
					<strong>Article List:</strong>
				<div>
				<div>
					<!-- Get articles from database -->
					
<?php
const SERVER = "ovid.u.washington.edu";
const PORT_NUM = "32001";
const USER_NAME = "root";
const PASSWORD = "purple pony disco";
const DB_NAME = "know_db";
const USER_TABLE = "user_list";
const WHITE_TABLE = "white_list";
const URL_COLUMN = "url";

ini_set('mysql.default_socket', '/rc12/d04/knowcse2/mysql.sock');
$connection = mysql_connect(SERVER . ":" . PORT_NUM, USER_NAME, PASSWORD);
checkResultSuccessful($connection, "mysql_connect");

$select = mysql_select_db(DB_NAME);
checkResultSuccessful($select, "mysql_select_db");

$user_list = get_url_list(USER_TABLE);
	
if ($_SERVER["REQUEST_METHOD"] == "GET") {
	$white_list = get_url_list(WHITE_TABLE);
	display_urls($user_list, $white_list);
	
} else if ($_SERVER["REQUEST_METHOD"] == "POST") {
	$new_user_list = $_POST["userList"];
		
	if (!empty($new_user_list)) {
		$new_size = count($new_user_list);
				
		for ($i = 0; $i < $new_size; $i++) {
			$url = $new_user_list[$i];
			
			if (!in_array($url, $user_list)) {
				// new selected url
				$add_url_query = "INSERT INTO " . USER_TABLE . " (" . URL_COLUMN . ") " . 
								"VALUES ('$url');";
				mysql_query($add_url_query);
			}
		}
		
		$old_size = count($user_list);
		
		for ($i = 0; $i < $old_size; $i++) {
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
	
	$user_list = get_url_list(USER_TABLE);
	$white_list = get_url_list(WHITE_TABLE);
	display_urls($user_list, $white_list);
}

mysql_close($connection);
?>

				</div>
				<div>
					<input type="submit" value="Submit" />
				</div>
			</fieldset>
		</form>
	</body>
</html>

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
	$list_query = "SELECT " . URL_COLUMN . " FROM $list_type " . 
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
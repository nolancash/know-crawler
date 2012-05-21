<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<title>Welcome!</title>
		<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
	</head>

	<body>
<form action="schedule.php" method="post"> 
	<fieldset>
		<legend>New Crawler Schedule:</legend>
                <div>
			<strong>Hour:</strong>
			<select name="hour">
		                <option>1</option> 
				<option>2</option>
                                <option>3</option>
				<option>4</option>
				<option>5</option>
                                <option>6</option> 
				<option>7</option>
				<option>8</option>
                                <option>9</option>
				<option>10</option>
				<option>11</option> 
                                <option>12</option> 
			 </select> <br />
		</div>
                    <div>
			<strong>Minute:</strong>
			<select name="minute">
                                <option>0</option>
		                <option>5</option>
				<option>10</option>
                                <option>15</option>
				<option>20</option>
				<option>25</option>
                                <option selected="selected">30</option>
				<option>35</option>
				<option>40</option>
                                <option>45</option>
				<option>50</option>
				<option>55</option> 
			 </select> <br />
		</div>
		 <div>
			<strong>AMorPM:</strong>
			<input type="radio" name="amorpm" value="AM" /> am 
			<input type="radio" name="amorpm" value="PM" checked="checked" /> pm <br />
		</div>
		<div>
			<strong>DaysToRun:</strong>
			<input type="radio" id = "next" name="daytorun" value="Daily" onclick = "if (this.checked) {document.getElementById('next1').disabled = true;
document.getElementById('next1').checked = true;
document.getElementById('next2').disabled = true;
document.getElementById('next2').checked = true;
document.getElementById('next3').disabled = true;
document.getElementById('next3').checked = true;
document.getElementById('next4').disabled = true;
document.getElementById('next4').checked = true;
document.getElementById('next5').disabled = true;
document.getElementById('next5').checked = true;
document.getElementById('next6').disabled = true;
document.getElementById('next6').checked = true;
document.getElementById('next7').disabled = true;
document.getElementById('next7').checked = true;}"/> Each day 
			<input type="radio" name="daytorun"  value="Weekly" checked="checked" onclick = "if (this.checked) {document.getElementById('next1').disabled = false;
document.getElementById('next1').checked = true;
document.getElementById('next2').disabled = false;
document.getElementById('next2').checked = false;
document.getElementById('next3').disabled = false;
document.getElementById('next3').checked = false;
document.getElementById('next4').disabled = false;
document.getElementById('next4').checked = false;
document.getElementById('next5').disabled = false;
document.getElementById('next5').checked = false;
document.getElementById('next6').disabled = false;
document.getElementById('next6').checked = false;
document.getElementById('next7').disabled = false;
document.getElementById('next7').checked = false;}"/> Some days <br />
		</div>
       	 <div>
           <input type="checkbox" id="next1" name="day" checked value="M"/> Monday
           <input type="checkbox" id="next2" name="day" value="T" /> Tuesday
           <input type="checkbox" id="next3" name="day" value="W" /> Wednesday
           <input type="checkbox" id="next4" name="day" value="Th"/> Thursday
           <input type="checkbox" id="next5" name="day" value="F" 	 /> Friday				
           <input type="checkbox" id="next6" name="day" value="S"  /> Saturday			
           <input type="checkbox" id="next7" name="day" value="Sun" /> Sunday   
          </div>
		<div>
			<a href="lastpage.php">
				Save
			</a>
		
		</div>
	</fieldset>
</form>

	</body>
</html>

<?php
require_once "db.php";
$id = $_POST["id"];
$result = mysqli_query($conn,"SELECT * FROM test where application_id = $id");
?>
<option value="">Select Test</option>
<?php
while($row = mysqli_fetch_array($result)) {
?>
<option value="<?php echo $row["id"];?>"><?php echo $row["test_name"];?></option>
<?php
}
?>
<?php
require_once "db.php";
$id = $_POST["test_id"];
$result = mysqli_query($conn,"SELECT * FROM version where test_id = $id");
?>
<option value="">Select Version</option>
<?php
while($row = mysqli_fetch_array($result)) {
?>
<option value="<?php echo $row["id"];?>"><?php echo $row["name"];?></option>
<?php
}
?>
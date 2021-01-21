<?php
 $path = $_SERVER['DOCUMENT_ROOT'];
 $path .= "/testing/db.php";
 include_once($path);
 $path .= "/testing/db.php";

 include_once($path);

//getting id of the data from url
$id = $_GET['id'];

// echo $id;exit;
 
$result = mysqli_query($conn, "DELETE FROM application WHERE id=$id");
if(!$result){
    echo "Error while deleting data";
}else{
    echo "Record Deleted Sucessfully";
}
 
header("Location:add_application.php");
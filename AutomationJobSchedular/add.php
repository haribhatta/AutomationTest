<?php
//including the database connection file
$path = $_SERVER['DOCUMENT_ROOT'];
$path .= "/testing/db.php";
include_once($path);
 
if(isset($_POST['Submit'])) {    
    $name = $_POST['name'];
    // checking empty fields
    if(empty($name)) {                
        if(empty($name)) {
            echo "<font color='red'>Name field is empty.</font><br/>";
        }
        
       
    } else {
        // if all the fields are filled (not empty)             
        //insert data to database
        $result = mysqli_query($conn, "INSERT INTO application(name) VALUES('$name')");
        
        //display success message
        header("Location: add_application.php");
        
      
    }
}
?>
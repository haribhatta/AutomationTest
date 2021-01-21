<?php
// including the database connection file
include_once("db.php");
 
if(isset($_POST['update']))
{    
    $id = $_POST['id'];
    
    $name=$_POST['name'];
  
    // checking empty fields
    if(empty($name)) {            
        if(empty($name)) {
            echo "<font color='red'>Name field is empty.</font><br/>";
        }
        
             
    } else {    
        //updating the table
        $result = mysqli_query($conn, "UPDATE application SET name='$name' WHERE id=$id");

        // echo $name;exit;
        
        header("Location: add_application.php");
    }
}
?>
<?php
//getting id from url
$id = $_GET['id'];
 
$result = mysqli_query($conn, "SELECT * FROM application WHERE id=$id");
 
while($res = mysqli_fetch_array($result))
{
    $name = $res['name'];
    
}
?>
<html>
<head>    
    <title>Edit Data</title>
</head>
 <?php include "header.php"; ?>
<body>
    
    <form name="form1" method="post" action="">
        <label for="name">Name</label>
        <input type="text" name="name" class="form-control" value="<?php echo $name;?>"></td>
            
                <td><input type="hidden" name="id" value=<?php echo $_GET['id'];?>></td>
                <button class="btn"  name="update" value=""  >Update</button>
                <button class="btn"><a href="add_application.php">Cancle</a></button>

    </form>
</body>
</html>

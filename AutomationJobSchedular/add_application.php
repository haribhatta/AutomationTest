<?php 
 include "header.php";
?>
<style>
    .m-4{
        margin-left:15px;
    }
</style>
<button class="btn btn-warning" name="application" > <a href="index.php" class="text-decoration-none" >Home</a> </button>

<button class="btn btn-info" name="application" > <a href="add_test_type.php" class="text-decoration-none" >Add Test Type</a> </button>
<button class="btn btn-info" name="application" > <a href="add_version.php" class="text-decoration-none" >Add Version</a> </button>



<?php 
 include "db.php";

 
if(isset($_POST['add']))
{    
  
    $name=$_POST['name'];
    echo $name;exit;
  
    // checking empty fields
    if(empty($name)) {            
        if(empty($name)) {
            echo "<font color='red'>Name field is empty.</font><br/>";
        }
    } else {    
        $result = mysqli_query($conn, "INSERT INTO application(name) VALUES ('$name) ");
        header("Location: add_application.php");
    }
}
?>
<hr>
<section style="margin-bottom: 25px; margin-top: 20px;">
<form action="add.php" method="post">
    <label for="label"> Name Of Application</label>
    <input type="text" class="form-control" name="name">
    <button class="btn" type="submit" name="Submit">Add</button>
</form>
</section>

<hr>





<section>
<table class="table table-responsive table-bordered table-striped">
<tr>
          <th>SN</th>
            <th>Name of Application</th>
            <th>Action</th>
          </tr>
<?php 
$count = 1;
// $path = $_SERVER['DOCUMENT_ROOT'];
// $path .= "/testing/db.php";
// include_once($path);
  $result = mysqli_query($conn,"SELECT * FROM application");

  while($row = mysqli_fetch_array($result)) {
  ?>
          <tr>
            <td><?php echo $count;?></td>
            <td><?php echo $row['name'];?></td>
            <td>
             <?php   echo "<a href='edit_application.php?id=". $row['id'] ."' title='Update Record' data-toggle='tooltip'><span class='glyphicon glyphicon-pencil m-4'></span></a>";
                     echo "<a href='delete_application.php?id=". $row['id'] ."' title='Delete Record' data-toggle='tooltip'><span class='glyphicon glyphicon-trash m-4'></span></a>";
             ?>
            </td>
  <?php
  $count++;
  }?>
  </tr>
  </table>
  <?php
?>
</section>
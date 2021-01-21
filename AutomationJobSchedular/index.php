<?php 
    include "header.php";
    ?>


            <button class="btn btn-info" name="job"> <a href="job.php">New Job</a></button>
            <button class="btn btn-info" name="reschedule" > <a href="reschedule.php" class="text-decoration-none" >Reschedule Job</a> </button>
            <button class="btn btn-info" name="application" > <a href="add_application.php" class="text-decoration-none" >Add Application</a> </button>
            
           <h3> Scehedule a job Now </h3>
           <form  method="post">

            <label for="" class="form-main">Select Appliction</label>
            
                <select name="apps[ ]" class="form-control" id="app-dropdown">
                <option value="">Select Application</option>
                <?php
                require_once "db.php";
                $result = mysqli_query($conn,"SELECT * FROM application");

                while($row = mysqli_fetch_array($result)) {
                ?>
                <option value="<?php echo $row['id'];?>"><?php echo $row["name"];?></option>
                <?php
                }
                ?>
                </select>
            <label for=""class="form-main"> Select Type</label>
          
            <select class="form-control" name="tests[ ]" id="test-type-dropdown">
            </select>

            <label for="" class="form-main">Select Version</label>
            <select class="form-control" id="version-dropdown">
            </select>
            
            <button class="btn btn-success m-3" type="submit" name="button1">Schedule</button>
            <button class="btn btn-danger m-3" name="button2" onclick="reset()">Cancel</button>
            </form>

            <script>
                $(document).ready(function() {
                $('#app-dropdown').on('change', function() {
                var id = this.value;
                $.ajax({
                url: "test-type.php",
                type: "POST",
                data: {
                id: id
                },
                cache: false,
                success: function(result){
                $("#test-type-dropdown").html(result);
                $('#version-dropdown').html('<option value="">Select Test Type First</option>'); 
                }
                });
                });    
                $('#test-type-dropdown').on('change', function() {  
                var test_id = this.value;
                $.ajax({
                url: "version.php",
                type: "POST",
                data: {
                test_id: test_id
                },
                cache: false,
                success: function(result){
                $("#version-dropdown").html(result);
                }
                });
                });
                });
                </script>





            <?php
      
      if(isset($_POST['button1'])) { 
         
        
        $tests = $_POST['tests'];
        $ver = $_POST['versions'];
        $app = $_POST['apps'];
        $test;
        $version;
        $appname;


        foreach ($tests as $a){
            $test= $a;
        }
        foreach ($ver as $a){
            $version =  $a;
        }
        foreach ($app as $a){
            $appname =  $a;
        }
        //    echo $appname;
        //     echo $version;
        //     echo $test;

            //  shell_exec('start cmd.exe @cmd /k"cd\ & cd D:\svn\DanpheEMR\SystemTest & d: & python SmokeSanityRun.py"');
        shell_exec('start cmd.exe @cmd /k"cd\ & cd D:\svn\"'.$appname.'"\SystemTest & d: & python "'.$test.'".py"');

      } 
   
  ?> 
    </div>
</body>
</html>

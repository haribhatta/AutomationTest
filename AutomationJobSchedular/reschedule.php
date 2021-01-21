<?php include "header.php"; ?>
<?php

  include "SimpleXLSX.php";
  echo '<h3 class="text-center"> Reschedule Jobs</h3><pre>';

  if ( $xlsx = SimpleXLSX::parse('SmokeSanityExecutionResultV1.47.3.xlsx') ) {
    echo '<table class="table table table-striped table-responsive"><tbody>';
    $i = 0;

    foreach ($xlsx->rows() as $elt) {
      if ($i == 0) {
        ?>
        <tr> 
            <th>  <?php echo $elt[0]; ?> </th>
            <th>  <?php echo $elt[1]; ?> </th>
            <th>  <?php echo $elt[2]; ?> </th>
            <th>  <?php echo $elt[3]; ?> </th>
            <th>  <?php echo $elt[4]; ?> </th>
            <th>  <?php echo $elt[5]; ?> </th>
            <th>  <?php echo $elt[6]; ?> </th>
            <th>Action</th>
        </tr>
        <?php
      } else {
        ?>
        <tr> 
            <td>  <?php echo $elt[0]; ?> </td>
            <td>  <?php echo $elt[1]; ?> </td>
            <td>  <?php echo $elt[2]; ?> </td>
            <td>  <?php echo $elt[3]; ?> </td>
            <td>  <?php echo $elt[4]; ?> </td>
            <td>  <?php echo $elt[5]; ?> </td>
            <td>  <?php echo $elt[6]; ?> </td>

        </tr>
        <?php
      }      

      $i++;
    }

    echo "</tbody></table>";

  } else {
    echo SimpleXLSX::parseError();
  }

?>

<hr>
<a href="index.php" class="ml-3"> Back to Home</a>
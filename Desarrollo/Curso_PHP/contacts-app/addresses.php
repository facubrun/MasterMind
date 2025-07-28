<?php

require "database.php";

session_start();

if (!isset($_SESSION["user"])) {
  header("Location: login.php");
  return;
}

$addresses = $conn->query("SELECT * FROM address WHERE user_id = {$_SESSION['user']['id']}");

?>

<?php require "partials/header.php" ?>

<div class="container pt-4 p-3">
  <div class="row">
    
    <?php if ($addresses->rowCount() == 0): ?>
      <div class="col-md-4 mx-auto">
        <div class="card card-body text-center">
          <p>No addresses saved yet</p>
          <a href="addAddress.php">Add One!</a>
        </div>
      </div>
    <?php endif ?>
    <?php foreach ($addresses as $address): ?>
      <div class="col-md-4 mb-3">
        <div class="card text-center">
          <div class="card-body">
            <h3 class="card-title text-capitalize"><?= $address["address"] ?></h3>
            <p class="m-2"><?= $address["phone_number"] ?></p>
            <a href="editAddress.php?id=<?= $address["id"] ?>" class="btn btn-secondary mb-2">Edit Address</a>
            <a href="deleteAddress.php?id=<?= $address["id"] ?>" class="btn btn-danger mb-2">Delete Address</a>
          </div>
        </div>
      </div>
    <?php endforeach ?>

  </div>
</div>

<?php require "partials/footer.php" ?>

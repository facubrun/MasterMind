<?php

  require "database.php";

  session_start();

  if (!isset($_SESSION["user"])) {
    header("Location: login.php");
    return;
  }

  $error = null;

  if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (empty($_POST["address"])) {
      $error = "Please fill the address field.";
    } else if (strlen($_POST["address"]) < 10) {
      $error = "Address must be at least 10 characters.";
    } else {
      $address = $_POST["address"];

      $statement = $conn->prepare("INSERT INTO address (address, user_id) VALUES (:address,{$_SESSION['user']['id']})");
      $statement->bindParam(":address", $_POST["address"]);
      $statement->execute();

      $_SESSION["flash"] = ["message" => "Address {$_POST['address']} added."];

      header("Location: addresses.php");
      return;
    }
  }
?>

<?php require "partials/header.php" ?>

<div class="container pt-5">
  <div class="row justify-content-center">
    <div class="col-md-8">
      <div class="card">
        <div class="card-header">Add Address</div>
        <div class="card-body">
          <?php if ($error): ?>
            <p class="text-danger">
              <?= $error ?>
            </p>
          <?php endif ?>
          <form method="POST" action="newAddress.php">
            <div class="mb-3 row">
              <label for="address" class="col-md-4 col-form-label text-md-end">Address</label>

              <div class="col-md-6">
                <input id="address" type="text" class="form-control" name="address" autocomplete="address" autofocus>
              </div>
            </div>

            <div class="mb-3 row">
              <div class="col-md-6 offset-md-4">
                <button type="submit" class="btn btn-primary">Submit</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</div>

<?php require "partials/footer.php" ?>

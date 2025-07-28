<?php

  require "database.php";

  session_start();

  if (!isset($_SESSION["user"])) {
    header("Location: login.php");
    return;
  }

  $id = $_GET["id"];

  $statement = $conn->prepare("SELECT * FROM address WHERE id = :id LIMIT 1");
  $statement->execute([":id" => $id]);

  if ($statement->rowCount() == 0) {
    http_response_code(404);
    echo("HTTP 404 NOT FOUND");
    return;
  }

  $address = $statement->fetch(PDO::FETCH_ASSOC);

  if ($address["user_id"] !== $_SESSION["user"]["id"]) {
    http_response_code(403);
    echo("HTTP 403 UNAUTHORIZED");
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

      $statement = $conn->prepare("UPDATE address SET address = :address WHERE id = :id");
      $statement->execute([
        ":id" => $id,
        ":address" => $address,
      ]);

      $_SESSION["flash"] = ["message" => "Address {$_POST['address']} updated."];

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
        <div class="card-header">Edit Address</div>
        <div class="card-body">
          <?php if ($error): ?>
            <p class="text-danger">
              <?= $error ?>
            </p>
          <?php endif ?>
          <form method="POST" action="editAddress.php?id=<?= $address['id'] ?>">
            <div class="mb-3 row">
              <label for="address" class="col-md-4 col-form-label text-md-end">Address</label>

              <div class="col-md-6">
                <input value="<?= $address['address'] ?>" id="address" type="text" class="form-control" name="address" autocomplete="address" autofocus>
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

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

$conn->prepare("DELETE FROM address WHERE id = :id")->execute([":id" => $id]);

$_SESSION["flash"] = ["message" => "Address {$address['address']} deleted."];

header("Location: addresses.php");

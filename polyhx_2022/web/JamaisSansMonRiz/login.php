<?php

// FLAG{2_je_me_sens_tellement_inclu}

include_once("lib/crypto.php");
session_start();

if(isset($_SESSION["admin"]) && $_SESSION["admin"]) {
    header("Location: /admin/index.php");
    exit();
}

// Validate Remember Me
if(isset($_COOKIE["remember_me"])) {
    if ($remember_me = validate_remember_me_cookie($_COOKIE["remember_me"])) {
        $_SESSION["admin"] = true;
        $_SESSION["username"] = "admin";
        header("Location: /admin/index.php");
        exit();
    }
}

// Validate login

if(isset($_POST["email"]) && isset($_POST["password"])) {
    // TODO: Ajouter une base de donnees, comme ca on ne riz plus
    if($_POST["email"] === "admin@jamaissansmonriz.com" && $_POST["password"] === getenv("FLAG4")) {
        
        $_SESSION["admin"] = true;
        $_SESSION["username"] = "admin";

        if(isset($_POST["remember_me"]) && $_POST["remember_me"] === "on") {
            setcookie("remember_me", generate_remember_me_cookie($_SESSION["username"], "1"), time()+3600*24*30, "/", "", 0);
        }   
        header("Location: /admin/index.php");
        exit();
    }
}



?

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style/styles.css">
    <title>Connexion</title>
</head>
<body background="blue">
<main>
    <center><h1>Bonjour, veuillez vous connectez</h1></center>
</br>
    <form action="verification.php" method="post">
        <div>
            <label for="user">Nom d'utilisateur:</label>
            <input type="text" name="utilisateur" id="user">
        </div>
        <div>
            <label for="password">Mot de passe :</label>
            <input type="password" name="password" id="password">
        </div>
        <section>
            <button  type="submit">Se connecter</button>
        </section>
    </form>
    </main>
</body>
</html>
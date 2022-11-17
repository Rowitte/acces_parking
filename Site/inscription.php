<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style/styles.css">
    <title>Pré-inscription</title>
</head>
<body background="blue">
<main>
<form action="add.php" method="post">
        <h1>Inscription</h1>
        <div>
            <label for="nom">Nom :</label>
            <input type="text" name="nom" id="nom">
        </div>
        <div>
            <label for="prenom">Prénom :</label>
            <input type="text" name="prenom" id="prenom">
        </div>
        <div>
            <label for="age">Age :</label>
            <input type="text" name="age" id="age">
        </div>
        <di  v>
            <label for="email">Email :</label>
            <input type="email" name="mail" id="email">
        </div>
        <div>
            <label for="adresse">Adresse :</label>
            <input type="text" name="adresse" id="adresse">
        </div>
        <div>
            <label for="num">Mobile :</label>
            <input type="text" name="tel" id="num">
        </div>
        </br>
        <section>
        <button type="submit" name="Ajouter">Enregistrer</button>
        </section>
        <footer>pour retourner à l'acceuil <a href="select.php">cliquez ici</a></footer>
    </form>

    </main>
</body>
</html>
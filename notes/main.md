# Ok tātad...
Jauna rinda
Sākumā vajag izveidot repo

Githubā to var caur UI vai CMD

Ir komanda:

    gh repo create

**gh** ir githuba cmd

Tālāk vajag noklonēt izveidoto repo

Kaut *gh piedāvā to izdarīt automātiski*

    git clone https://github.com/v-ir-mans/git_learning_notes.git

Lai pievienotu failu ir

    git add [faila/mapes nosaukums]

bet var arī

    git .

kas pievieno visus failus

Ja ir faili, ko negrib pievienot, var izveidot *.gitignore* failu (vai nepievienot to ar git add)

Tad ir

```
git commit
```

bet vajag ziņu

```
git commit -m "mana jaukā ziņa"
```

var bez *-m*, bet Windows tad atver *laikam vim*. Es nesaprotu vimu. 

```
git commit -F commit_message.txt
```

Tas ir no faila^



Tad ir

```
git push [kur] [zars]
```

Beeet

```
git push
```

arī strādās



---

### Komandas, kuras atklāju

```
git status
```

Uzraksta statusu

```
git clean -fd
```

Noņem visus failus, kas nav pēdējā comit

```
git commit --amend -m "New commit message" 
```

izmaina pēdējo commit ziņu



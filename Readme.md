# Manipulation de documents HTML

## Donnée

La branche `master` du dépôt contient les fichiers nécessaires à la réalisation du projet.

## Corrigé

Le corrigé du TP est disponible dans la branche `corrige`. Pour visiter cette branche, 
on peut se rendre directement sur GitHub et changer la branche avec le 
contrôle de sélection en haut. 

Lien du corrigé : https://github.com/oci1315/tp-html-manip/tree/corrige

Il est également possible de visiter cette branche `corrige` en clonant le dépôt
en local et en faisant un `git checkout corrige` comme suit :

```{bash}
$ git clone https://github.com/oci1315/tp-html-manip.git
$ git checkout corrige
```

## Tests

Les tests sont effectués dans le fichier `test.py`
(https://github.com/oci1315/tp-html-manip/blob/master/tests.py) 
à l'aide du module Python
`unittest`. Les tests utilisent des assertions et sont assez intéressants 
puisqu'ils n'impriment pas les arbres sur la sortie standard mais teste 
leur équivalence à un certain code HTML de test.
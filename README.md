TP Dataviz – Lisibilité et accidents de la route en Île-de-France

Partie 1 – Étude des règles de lisibilité (7 à 16)

Introduction

La lisibilité est un élément essentiel dans la création de visualisations de données. Un graphique doit permettre de comprendre rapidement une information sans demander trop d'efforts au lecteur. Les règles 7 à 16 de GoldenViz présentent plusieurs erreurs fréquentes et proposent des solutions pour améliorer la présentation des graphiques.

Règle 7 – Rendre les axes et les étiquettes faciles à lire

Problème : lorsque les graduations sont trop rapprochées ou que les intitulés sont trop petits, la lecture des axes devient compliquée. Les étiquettes trop longues peuvent également se chevaucher.

Correction : adapter la taille des textes, limiter les graduations et choisir une représentation adaptée. Les barres horizontales peuvent notamment faciliter la lecture des libellés.

Application : pour comparer les départements franciliens, nous privilégierons des barres horizontales afin que les noms restent facilement identifiables.

Règle 8 – Choisir des couleurs accessibles

Problème : une palette composée de trop nombreuses couleurs ou de nuances similaires rend les catégories difficiles à distinguer, notamment pour les personnes daltoniennes.

Correction : utiliser une palette limitée avec des contrastes suffisants et éviter les associations de couleurs difficiles à différencier.

Application : notre carte utilise plusieurs nuances de bleu pour représenter les concentrations d'accidents. Les accidents mortels sont identifiés en orange afin de les distinguer rapidement.

Règle 9 – Placer les étiquettes directement sur les données

Problème : une légende séparée oblige le lecteur à faire des allers-retours pour identifier les différentes informations représentées.

Correction : afficher directement les noms et les valeurs à proximité des éléments concernés lorsque cela est possible.

Application : les valeurs sont indiquées directement sur les barres du graphique comparatif. Les informations complémentaires sont également accessibles sur la carte.

Règle 10 – Éviter les éléments graphiques inutiles

Problème : les effets 3D, les ombres et les grilles trop visibles peuvent surcharger une visualisation et détourner l'attention des données.

Correction : supprimer les décorations qui n'apportent aucune information et conserver une présentation simple.

Application : nous avons privilégié une carte épurée et des graphiques sans effets décoratifs superflus afin de mettre les données au premier plan.

Règle 11 – Limiter le nombre de catégories

Problème : lorsqu'un graphique présente trop de catégories, il devient difficile de comparer les informations et de repérer les différences importantes.

Correction : regrouper les catégories similaires, utiliser des filtres ou répartir les informations sur plusieurs graphiques.

Application : les cinq modalités initiales de luminosité ont été regroupées en quatre catégories. Les territoires ont également été répartis en trois ensembles géographiques.

Règle 12 – Organiser les barres selon leurs valeurs

Problème : lorsque les barres sont présentées sans ordre précis, il est moins évident de repérer les valeurs les plus importantes.

Correction : classer les catégories par ordre croissant ou décroissant, sauf lorsqu'un ordre chronologique ou logique doit être conservé.

Application : les catégories du graphique comparatif sont organisées selon leur proportion d'accidents graves afin de faciliter l'identification des écarts.

Règle 13 – Éviter le chevauchement des points

Problème : un grand nombre de points concentrés dans une même zone peut provoquer des superpositions. Certaines observations deviennent alors invisibles.

Correction : utiliser de la transparence, réduire la taille des marqueurs ou regrouper les observations grâce à des représentations par densité.

Application : plutôt que d'afficher individuellement les 14 688 accidents, nous avons utilisé des hexagones pour représenter leur concentration géographique. Les accidents mortels restent affichés sous forme de points orange.

Règle 14 – Adapter le nombre de décimales

Problème : une précision excessive rend les valeurs plus difficiles à lire et n'apporte pas nécessairement d'information supplémentaire.

Correction : conserver les nombres entiers pour les effectifs et limiter les décimales pour les taux et les pourcentages.

Application : les nombres d'accidents sont affichés sous forme d'entiers et les pourcentages sont arrondis à une décimale.

Règle 15 – Simplifier l'affichage des dates

Problème : un axe contenant trop de dates peut devenir surchargé et rendre les évolutions temporelles difficiles à suivre.

Correction : réduire le nombre de graduations et utiliser des formats plus courts, par exemple en affichant uniquement les mois.

Application : cette règle n'a pas été directement utilisée dans nos visualisations, car l'analyse porte sur une seule année et se concentre sur les conditions de luminosité plutôt que sur une évolution temporelle.

Règle 16 – Privilégier la simplicité visuelle

Problème : vouloir représenter trop d'informations dans un même graphique peut rendre le message principal difficile à identifier.

Correction : sélectionner les informations pertinentes et attribuer un objectif précis à chaque visualisation.

Application : nous avons séparé l'analyse géographique de l'étude de la gravité selon la luminosité. Chaque graphique possède ainsi un objectif distinct.

Bilan de la première partie

L'étude des règles de lisibilité montre qu'une visualisation efficace doit avant tout faciliter la compréhension des données. Les choix de couleurs, de formes, de légendes et de catégories ont donc une réelle importance. Ces principes ont été pris en compte dans la réalisation de notre carte et de nos graphiques comparatifs.

Partie 2 – Analyse des accidents corporels en Île-de-France (2025)

1. Présentation de l'étude

Cette deuxième partie porte sur la répartition géographique des accidents corporels de la circulation en Île-de-France pour l'année 2025.

L'objectif est d'identifier les zones qui concentrent le plus d'accidents et d'étudier les différences de gravité selon les conditions de luminosité.

Deux axes d'analyse ont été retenus :

La localisation géographique des accidents.

La comparaison de leur gravité selon les conditions de luminosité et les zones géographiques.

2. Préparation et nettoyage des données

L'analyse a été réalisée à partir des fichiers BAAC 2025, notamment les fichiers caract-2025.csv et usagers-2025.csv.

La base initiale contient 55 093 accidents sur l'ensemble du territoire français, dont 14 760 en Île-de-France.

Plusieurs opérations ont été nécessaires avant de réaliser les visualisations :

Conversion des coordonnées géographiques lat et long en valeurs numériques, en remplaçant les virgules par des points.

Transformation des coordonnées dans le système de projection Lambert 93 afin de faciliter leur représentation cartographique.

Vérification de la cohérence géographique des accidents et suppression de 72 observations dont les coordonnées ne correspondaient pas à leur département.

Rattachement des informations concernant les victimes aux accidents correspondants.

Regroupement des cinq modalités initiales de luminosité en quatre catégories. Les deux modalités correspondant à une nuit sans éclairage ont notamment été rassemblées.

La gravité d'un accident est déterminée à partir de la victime présentant les conséquences les plus importantes. Un accident est considéré comme grave lorsqu'il comporte au moins une personne décédée ou hospitalisée.

Après nettoyage, l'étude porte sur 14 688 accidents, parmi lesquels 252 sont mortels et 1 929 sont considérés comme graves.

3. Cartographie des accidents



La première visualisation représente la répartition des accidents sur l'ensemble de l'Île-de-France. Elle permet d'observer la région dans son ensemble et de distinguer les secteurs où les accidents sont les plus concentrés.

Les nuances de bleu représentent le nombre d'accidents par zone, tandis que les points orange permettent de localiser les accidents mortels.

Cette représentation met en évidence une concentration importante des accidents à Paris et dans les départements de la petite couronne. Le niveau de détail permet également d'observer plus précisément les différences de répartition entre les territoires.

4. Comparaison selon les conditions de luminosité



La deuxième visualisation étudie la proportion d'accidents graves selon les conditions de luminosité.

Les résultats obtenus à l'échelle régionale sont les suivants :

Conditions de luminosité

Part d'accidents graves

Nuit sans éclairage

17,7 %

Nuit avec éclairage

13,8 %

Aube ou crépuscule

13,7 %

Plein jour

12,3 %

La nuit sans éclairage présente la proportion d'accidents graves la plus élevée, avec 17,7 %. À l'inverse, le plein jour présente la proportion la plus faible, avec 12,3 %.

Cette première comparaison permet d'observer des différences selon les conditions de luminosité, mais elle ne prend pas encore en compte les spécificités géographiques.

5. Comparaison selon les zones géographiques



La comparaison est ensuite approfondie en distinguant Paris, la petite couronne et la grande couronne.

Cette représentation permet de constater que les proportions d'accidents graves sont globalement plus importantes en grande couronne, quelles que soient les conditions de luminosité.

Elle apporte donc une nuance importante à la première visualisation, puisque les différences observées à l'échelle régionale peuvent également être liées à la localisation des accidents.

6. Interprétation des résultats

Répartition géographique

Zone géographique

Nombre d'accidents

Accidents mortels

Part d'accidents graves

Paris

3 656 (24,9 %)

32 (12,7 %)

10,0 %

Petite couronne

6 625 (45,1 %)

63 (25,0 %)

9,6 %

Grande couronne

4 407 (30,0 %)

157 (62,3 %)

21,0 %

Les résultats montrent que Paris et la petite couronne concentrent environ 70 % des accidents étudiés.

Cependant, la répartition des accidents mortels est différente. La grande couronne représente 62,3 % des accidents mortels alors qu'elle concentre seulement 30 % de l'ensemble des accidents.

La proportion d'accidents graves y atteint 21 %, contre 10 % à Paris et 9,6 % en petite couronne.

La Seine-et-Marne présente notamment 1 213 accidents, mais compte 62 accidents mortels, soit le nombre le plus élevé parmi les départements étudiés.

Une explication possible pourrait être liée aux différences de circulation et aux vitesses pratiquées selon les environnements. Les routes situées en dehors des zones urbaines peuvent notamment présenter des conditions de circulation différentes. Cette hypothèse reste toutefois à vérifier, car les données étudiées ne permettent pas d'établir directement un lien avec la vitesse des véhicules.

Influence des conditions de luminosité

À l'échelle régionale, les accidents survenant la nuit sans éclairage présentent la proportion d'accidents graves la plus élevée, avec 17,7 %, contre 12,3 % en plein jour.

Cette différence pourrait laisser penser que l'absence d'éclairage augmente les risques de gravité. Toutefois, l'analyse par zone apporte une nuance importante.

En grande couronne, la proportion d'accidents graves atteint notamment 24 % la nuit sans éclairage, contre 20 % en plein jour.

Par ailleurs, 59 % des accidents survenant la nuit sans éclairage sont localisés en grande couronne.

Ces observations suggèrent que le territoire joue un rôle important dans l'interprétation des résultats. Il faut donc éviter de conclure que la luminosité explique à elle seule les différences de gravité.

7. Règles de lisibilité mises en œuvre

Les principes étudiés dans la première partie ont été appliqués aux différentes visualisations.

Règle

Mise en pratique

7 – Lisibilité des axes

Utilisation de libellés courts et de représentations faciles à parcourir

8 – Couleurs accessibles

Dégradé de bleus et points orange pour les accidents mortels

9 – Étiquetage direct

Valeurs affichées sur les graphiques et informations accessibles sur la carte

10 – Chartjunk

Suppression des éléments décoratifs inutiles

11 – Nombre de catégories

Regroupement de la luminosité en quatre catégories et des territoires en trois zones

12 – Tri des barres

Organisation selon la proportion d'accidents graves

13 – Surimpression

Regroupement des accidents par hexagones

14 – Décimales

Effectifs entiers et pourcentages arrondis à une décimale

16 – Économie visuelle

Séparation de l'analyse géographique et des comparaisons sur la luminosité

La règle 15 n'a pas été directement mobilisée, car les visualisations ne comportent pas d'axe temporel.

8. Conclusion générale

Cette étude a permis de mettre en évidence des différences importantes dans la répartition des accidents corporels en Île-de-France en 2025.

La carte montre une concentration importante des accidents à Paris et en petite couronne. Cependant, la grande couronne présente une proportion d'accidents graves nettement supérieure et concentre la majorité des accidents mortels.

L'analyse selon les conditions de luminosité montre également une proportion plus élevée d'accidents graves durant la nuit sans éclairage. Néanmoins, la comparaison entre les territoires indique que ces résultats doivent être interprétés en tenant compte de leur localisation.

Enfin, ce travail a permis de mettre en pratique plusieurs principes de lisibilité afin de produire des visualisations compréhensibles, cohérentes et adaptées à la quantité de données étudiées.

Sources

GoldenViz, règles de lisibilité, règles 7 à 16.

Base BAAC 2025, fichiers de données utilisés pour le TP.

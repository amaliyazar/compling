# [ Compling ]

## Создание графа друзей при помощи Gephi


![Graph](https://github.com/amaliyazar/compling/blob/master/Graph.pdf)
### Операции, которые я провела после загрузки графа:
* Распределение цветов вершин и ребер в зависимости от города проживания человека
* Изменение размера вершин по критерию relation
* Разные цвета у имен в зависимости от пола человека
* Размер текста имени по критерию degree
* Укладка - Fruchterman Reingold

[Файл с таблицей](https://github.com/amaliyazar/compling/blob/master/Graph.xlsx)

В итоге, граф разделился на три сообщества, что в принципе довольно-таки верно. Два из этих сообществ разделились по двум городам, где люди в целом взаимосвязаны друг с другом. Но иногда бывает, что укладка графа не совсем удачна, и разделение на сообщество нечетко выражено. Также есть соврешнно отдельные люди, что тоже верно. Я не совсем поняла, что значит фильтр relation, так как количество общих друзей не совпадает с результатами, и частота общения тоже. 
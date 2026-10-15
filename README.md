# Corporate Performance Management

## Projekt 14 Vorhersage numerischer Werte (Regressionsbaum)

Erstellen Sie einen Regressionsbaum zur Verkaufsprognose. Der Baum sollte bezüglich der Hierarchiestufen minimiert werden und die Vorhersagefunktion sollte linear sein. Wenden Sie Ihre Lösung auf folgende Fragestellungen an: Welche Subkategorien erzielen die größten Stückzahlen? Wie wird sich ein neues Produkt „Road-Racer" verkaufen, wenn es zur Produktlinie = „Road", zum Modell = „Road-150" sowie zur Kategorie = „Bikes" und zur Subkategorie = „Road Bikes" gehört?** **

Anleitung: Die Ausarbeitung soll eine Darstellung der Theorie der Entscheidungsbäume für numerische Vorhersagen enthalten. Illustrieren Sie an der gestellten Aufgabe die Wahl der optimalen Klassifizierer (hier Produkteigenschaften). Stellen Sie dar, wo und wie das Abschneiden (pruning) von Zweigen der Hierarchie erfolgt und wie Sie die Vorhersagemodelle ermitteln.** **

Datenquelle: Adventure WorksDW (MS SQL Server)** **




## 1. Einleitung

1.1 Problemstellung und Zielsetzung
1.2 Aufgabenstellung und Forschungsfragen
1.3 Aufbau der Ausarbeitung

## 2. Theoretische Grundlagen der Entscheidungsbäume

2.1 Grundlagen und Funktionsweise von Entscheidungsbäumen
2.2 Klassifikationsbäume und Regressionsbäume im Vergleich
2.3 Entscheidungsbäume für numerische Vorhersagen
2.4 Auswahl geeigneter Produkteigenschaften als Prädiktoren
2.5 Hierarchische Strukturierung der Produkteigenschaften

## 3. Methodik zur Erstellung des Regressionsbaums

3.1 Beschreibung der Datenbasis und Zielvariable (Verkaufsmenge)
3.2 Definition der Prädiktoren: Produktlinie, Modell, Kategorie und Subkategorie
3.3 Auswahl des optimalen Aufteilungskriteriums
3.4 Aufbau des Regressionsbaums und Ermittlung der Vorhersagewerte
3.5 Minimierung der Hierarchiestufen durch Pruning
3.6 Bewertung der Modellgüte und Vermeidung von Overfitting

## 4. Anwendung auf die Verkaufsprognose

4.1 Datenanalyse und Identifikation relevanter Produkteigenschaften
4.2 Konstruktion und Visualisierung des hierarchischen Regressionsbaums
4.3 Bestimmung der optimalen Baumtiefe und Beschneidung der Zweige
4.4 Vergleich der Verkaufszahlen nach Subkategorien
4.5 Identifikation der Subkategorien mit den höchsten Stückzahlen
4.6 Verkaufsprognose für das neue Produkt „Road-Racer“
4.6.1 Zuordnung zu Produktlinie, Modell, Kategorie und Subkategorie
4.6.2 Anwendung des reduzierten Regressionsbaums
4.6.3 Berechnung und Interpretation der prognostizierten Verkaufsmenge

## 5. Ergebnisse und Diskussion

5.1 Darstellung und Interpretation des optimalen Regressionsbaums
5.2 Beantwortung der Forschungsfragen
5.3 Aussagekraft und Grenzen der Verkaufsprognose
5.4 Kritische Würdigung des Pruning-Verfahrens

## 6. Fazit und Ausblick

6.1 Zusammenfassung der wesentlichen Ergebnisse
6.2 Beurteilung der Eignung des Regressionsbaums
6.3 Weiterführende Ansätze zur Verbesserung der Verkaufsprognose

## 7. Literaturverzeichnis

## 8. Anhang

8.1 Verwendete Datengrundlage
8.2 Berechnungen und Modellparameter
8.3 Vollständiger und beschnittener Regressionsbaum

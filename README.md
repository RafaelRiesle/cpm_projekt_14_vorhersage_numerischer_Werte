# Corporate Performance Management

## Projekt 14 Vorhersage numerischer Werte (Regressionsbaum)

Erstellen Sie einen Regressionsbaum zur Verkaufsprognose. Der Baum sollte bezüglich der Hierarchiestufen minimiert werden und die Vorhersagefunktion sollte linear sein. Wenden Sie Ihre Lösung auf folgende Fragestellungen an: Welche Subkategorien erzielen die größten Stückzahlen? Wie wird sich ein neues Produkt „Road-Racer" verkaufen, wenn es zur Produktlinie = „Road", zum Modell = „Road-150" sowie zur Kategorie = „Bikes" und zur Subkategorie = „Road Bikes" gehört?** **

Anleitung: Die Ausarbeitung soll eine Darstellung der Theorie der Entscheidungsbäume für numerische Vorhersagen enthalten. Illustrieren Sie an der gestellten Aufgabe die Wahl der optimalen Klassifizierer (hier Produkteigenschaften). Stellen Sie dar, wo und wie das Abschneiden (pruning) von Zweigen der Hierarchie erfolgt und wie Sie die Vorhersagemodelle ermitteln.** **

Datenquelle: Adventure WorksDW (MS SQL Server)** **


**Inhaltsverzeichnis**

1. **Einleitung**
   1.1 Problemstellung und Relevanz
   1.2 Zielsetzung und Forschungsfragen
   1.3 Aufbau der Arbeit
2. **Theoretische Grundlagen**
   2.1 Grundlagen des Data Mining und maschinellen Lernens
   2.2 Entscheidungsbäume zur Vorhersage numerischer Werte
   2.3 Aufbau und Funktionsweise von Regressionsbäumen
   2.4 Auswahl geeigneter Prädiktoren
   2.5 Lineare Vorhersagefunktionen
3. **Datenbasis und Datenaufbereitung**
   3.1 Vorstellung der Datenquelle Adventure WorksDW
   3.2 Auswahl und Verknüpfung der relevanten Datenbanktabellen
   3.3 Definition der Zielvariable und der Eingangsvariablen
   3.4 Aufbereitung und Aggregation der Verkaufsdaten
4. **Entwicklung und Optimierung des Regressionsbaums**
   4.1 Methodisches Vorgehen und Modellerstellung
   4.2 Auswahl der optimalen Produkteigenschaften
   4.3 Aufbau und Bewertung des Entscheidungsbaums
   4.4 Pruning zur Reduktion der Baumkomplexität
   4.5 Ermittlung der linearen Vorhersagefunktion
   4.6 Bewertung der Prognosequalität
5. **Ergebnisse und Anwendung des Modells**
   5.1 Analyse der Verkaufsstückzahlen nach Subkategorien
   5.2 Identifikation der absatzstärksten Subkategorien
   5.3 Prognose der Verkaufsstückzahl für das Produkt „Road-Racer“
   5.4 Interpretation der Ergebnisse
6. **Diskussion und kritische Würdigung**
   6.1 Aussagekraft und Grenzen des Regressionsbaums
   6.2 Bewertung der Modellkomplexität und Prognosequalität
   6.3 Wirtschaftliche Bedeutung der Ergebnisse
7. **Fazit und Ausblick**

**Literaturverzeichnis**

**Anhang**

- SQL-Abfragen
- Zusätzliche Tabellen und Abbildungen
- Modellparameter und weitere Ergebnisse

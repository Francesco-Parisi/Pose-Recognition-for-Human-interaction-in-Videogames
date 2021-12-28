# Human-Pose-Recognition-in-Videogames

## Descrizione
Questo progetto consiste, sulla base di un sistema per il rilevamento facciale già sviluppato da terzi, nella stima della direzione del volto e la sua applicazione in ambientazioni 3D e videogames.
L'obiettivo è stato quello di creare un sistema in grado di acquisire ed elaborare una sequenza di immagini allo scopo di estrarre le informazioni relative al volto rilevato per inviarle ad un server tcp, incaricato di decodificarle per creare una mappatura 3D e infine determinare il suo orientamento.

![Descrizione ](images/image.png)

Il progetto si articola in tre fasi essenziali: 

• Acquisizione delle immagini per il rilevamento del volto

• Estrazione delle informazioni del volto rilevato e mappatura in 3D

• Identificazione dell’orientamento del volto

La prima fase comprende l’acquisizione di una sequenza di immagini da webcam e il rilevamento del volto. L’acquisizione delle immagini è ottenuta grazie a un algoritmo sviluppato in python che sfrutta la libreria OpenCV e Scikit-image. Il sistema impiega una rete neurale in grado di localizzare 68 punti di riferimento del viso (landmarks). I landmarks vengono organizzati in 9 aree specifiche del viso: contorno facciale, sopracciglio sinistro e destro, naso, narici, occhio sinistro e destro, labbra e denti. La seconda fase comprende l’estrazione delle informazioni, la codifica in un formato specifico, il loro invio a un server tcp in Unity e la mappatura 3D. Le informazioni ottenute riguardano le coordinate di ciascun landmark nelle posizioni x, y e z. Tali informazioni vengono manipolate e inviate al server tcp, permettendo la creazione di una mesh 3D del viso. La terza fase comprende la stima della direzione del volto, ottenuta sfruttando 3 landmarks specifici dai quali è possibile calcolare il punto esatto in cui l’utente sta guardando, grazie alla creazione di un raggio luminoso. Infine tale lavoro è stato integrato in diversi ambienti di gioco, mettendone in evidenza il suo scopo finale.

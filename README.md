# Hvor grønt snakker politikerne _egentlig_?
## Beskrivelse
Dette er den medfølgende information til artiklen udgivet på 
Den Grønne Studenterbevægelses (DGSB) blog. Her kan man finde
koden brugt til analysen, klimaord og figurer fra analysen. 

Den rå data er ikke tilgængelig her, da det ligger under Twitters
betingelser og vi dermed ikke må dele det.

## Filer
- [klimaord.md](klimaord.md) indeholder ordene brugt i analysen
- [/figurer](/figurer) indeholder alle output-figurerne fra analysen
- [analysis.Rmd](analysis.Rmd) indeholder hele analysen ud over...
- [analysis.py](analysis.py), der indeholder kode til at vurdere positivitet

## Figurer
Emner fundet gennem maskinlæring (3 = klimaemne)

![topics](figurer/topics.png)

Hvor meget de forskellige politikere snakker om klimaemnet (3, herover)

![members topic](figurer/member_topic.png)

Samme som ovenstående men for partier

![parties topic](figurer/party_topic.png)

Frekvensen af klimaord i politikernes ordforbrug

![members climate word frequency](figurer/member_frequency.png)

Endelig score for partierne

![final party score](figurer/party_final.png)

Endelig score for politikerne

![final member score](figurer/member_final.png)
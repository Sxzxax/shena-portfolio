"""Generates index.html, competenties/*.html and projects/*.html for the portfolio.

Edit COMPETENTIES, TAGS and PROJECTS below, then run:  python3 build.py
Generated pages are overwritten, so don't edit them by hand.
"""
import os
import re
from html import escape

ROOT = os.path.dirname(os.path.abspath(__file__))

# General site text, hero photo and contact details.
# In hero_title, the words between *asterisks* are shown in the accent colour,
# and \n starts a new line.
# Leave a contact field empty ("") to hide it.
SITE = {
    "hero_greeting": "Hoi, ik ben Shena",
    "hero_title": "Minor Portfolio\n*Digital skills in de gebouwde omgeving*",
    "hero_text": "Ik studeer bouwkunde en werk op het snijvlak van architectuur en techniek: van parametrisch ontwerpen en ruimtelijke analyses tot digitale fabricage en programmeren.",
    "hero_image": None,  # e.g. "shena.jpg" in images/; None shows a stand-in photo
    "hero_image_alt": "Voorbeeldfoto (placeholder)",
    "email": "shenaalexander2005@gmail.com",
    "phone": "+31 6 87473973",
    "linkedin": "https://www.linkedin.com/in/shena-alexander-077860359/",
    "linkedin_label": "linkedin.com/in/shena",  # shown text; leave out to show the full link
    "github": "https://github.com/Sxzxax",
}

# Each competentie has numbered leerdoelen. Their codes ("1.1", "1.2", ...) are what projects refer to.
# Optional: "diagram" (image in images/ with alt and caption) shown below the leerdoelen.
COMPETENTIES = [
    {
        "number": "1",
        "slug": "digitale-expert",
        "name": "De digitale expert: onderzoeker & uitvoerder",
        "leerdoelen": [
            "Formuleert relevante digitale onderzoek- of ontwerpvragen binnen de gebouwde omgeving en kiest hiervoor passende methoden.",
            "Verzamelt, analyseert en interpreteert data kritisch om onderbouwde oplossingen te ontwikkelen.",
            "Integreert en prototypeert digitale tools/technieken in innovatieve oplossingen voor opgaven in de gebouwde omgeving.",
            "Reflecteert kritisch op het onderzoek en/of ontwerpproces en valideert de impact van “oplossingen” met stakeholders (opdrachtgever, adviseurs, medestudenten etc.).",
        ],
    },
    {
        "number": "2",
        "slug": "teamspeler",
        "name": "De teamspeler in digitale context",
        "leerdoelen": [
            "Werkt effectief samen in multidisciplinaire teams met behulp van digitale middelen & processen.",
            "Communiceert bevindingen en ontwerpkeuzes helder, visueel en doelgroepgericht om besluitvorming en overdracht te ondersteunen.",
            "Bouwt en onderhoudt een professioneel (online) netwerk en draagt actief bij aan kennisdeling binnen de vak-gemeenschap.",
        ],
    },
    {
        "number": "3",
        "slug": "zelfsturende-professional",
        "name": "De zelfsturende digitale professional",
        "leerdoelen": [
            "Stelt meetbare persoonlijke leerdoelen op en stuurt bij op basis van voortdurende kritisch reflectie.",
            "Toont een zelflerende houding in het eigen maken van zowel digitale vakbekwaamheid als softskills.",
            "Signaleert technologische innovaties en eigent zich zelfstandig nieuwe tools en werkwijzen toe om de professionele praktijk te versterken.",
        ],
    },
    {
        "number": "4",
        "slug": "professioneel-handelen",
        "name": "Professioneel handelen HBO",
        "leerdoelen": [
            "De student handelt professioneel. Zie onderstaand diagram, professioneel handelen HBO.",
        ],
        "diagram": {
            "image": None,  # e.g. "professioneel-handelen-hbo.png" in images/
            "alt": "Diagram professioneel handelen HBO",
            "caption": "Professioneel handelen HBO.",
        },
    },
]

# Tags shown on project cards and pages (the former themes). Projects refer to them by key.
TAGS = {
    "parametrisch": "Parametrisch ontwerpen",
    "arcgis": "ArcGIS",
    "fabricage": "Digitale fabricage",
    "python": "Python",
}

# The home-page timeline covers these months ("YYYY-MM", inclusive).
# Projects dated outside this range are left out of the timeline.
TIMELINE = {"start": "2026-09", "end": "2027-01"}

# Required per project: slug, title, leerdoelen (codes; the first one's competentie is the primary one),
#   tags (keys from TAGS, or [] for none), lead, role, date ("YYYY-MM", e.g. "2026-10"), tools.
# Optional: challenge, process, result (text, or a list of paragraphs), steps (list), image (file in images/ or URL),
#   image_alt, caption, details (the "Werk in detail" steps, see below), feedback (keys from FEEDBACK).
# Each step in "details": title, and optionally date, text (list of paragraphs), points (list of [label, text])
#   and media: pictures {"image", "alt", "caption"}, videos {"video" (file in videos/), "poster", "alt", "caption"}
#   or links {"url", "label"}.
# Optional fields that are left out get placeholder text (see CONTENT_DEFAULTS).
PROJECTS = [
    {
        "slug": "hittestress-parkhaven",
        "title": "Hittestress-analyse Parkhaven",
        "leerdoelen": ["1.1", "2.2", "3.3"],
        "tags": ["arcgis"],
        "lead": "Kaarten en een hittestressanalyse in ArcGIS Pro voor het masterplan Parkhaven, waarin ik het effect van bomen, groene daken en een groene kade op de gevoelstemperatuur vergelijk.",
        "role": "Groepsproject (project 1): kaarten, ontwerpkansen en hittestressanalyse",
        "date": "2026-10",
        "tools": "ArcGIS Pro, Claude, Gemini",
        "challenge": [
            "Voor het project Parkhaven moesten we als groep in fase 1 de omgeving onderzoeken en ontwerpkansen vinden. In fase 2 maakten we een simulatie voor klimaatadaptatie.",
            "Mijn deel was onder andere de vraag hoeveel koeler het gebied wordt met meer groen. ArcGIS Pro was nieuw voor mij.",
        ],
        "process": "In fase 1 voegde ik bestaande kaarten samen in ArcGIS Pro en haalde ik daar data uit. In fase 2 bracht ik het landgebruik in kaart, tekende ik zelf de maatregelen in en berekende ik met de analysetools de heat index per maatregel. Hieronder staat elke stap, met de kaarten en video's.",
        "steps": [
            "Bestaande kaarten samenvoegen in ArcGIS Pro (fase 1, september 2026)",
            "Landgebruik in kaart brengen en maatregelen tekenen (fase 2, oktober 2026)",
            "Heat index berekenen voor bomen, groene daken, een groene kade en alle maatregelen samen",
            "Resultaten presenteren aan de bedrijven achter het masterplan",
        ],
        "result": [
            "Met alle maatregelen samen wordt de omgeving ongeveer 2 graden koeler.",
            "In dit project heb ik geleerd om zelfstandig met digitale tools te werken. Ik begon met weinig ervaring in ArcGIS Pro en kan nu zelf kaarten samenvoegen, data analyseren en een heat-indexanalyse maken.",
            "Nieuwe software of tools kunnen veel tijd kosten en je weet vooraf niet of je ze echt nodig hebt. Een volgende keer controleer ik eerder of software en data kloppen voordat ik er veel tijd in stop.",
        ],
        "image": "hittestress-parkhaven.jpg",
        "image_alt": "Vier heat-indexkaarten van Parkhaven naast elkaar: A. bomen, B. groene daken, C. groene kade en D. alle maatregelen samen, in tinten van lichtgeel (koeler) tot donkerbruin (warmer).",
        "caption": "Heat index met vier varianten: bomen, groene daken, een groene kade en alle maatregelen samen (15 oktober 2026).",
        "details": [
            {
                "title": "Taakverdeling",
                "text": [
                    "In fase 1 zocht ik de regelgeving, maakte ik de kaarten en bedacht ik ontwerpkansen; in fase 2 deed ik de gebouwen in Forma, Tygron en de hittestressanalyse. Groepsleden deden de AI-visualisatie en de analyses van water en groen.",
                ],
            },
            {
                "title": "Fase 1: kaarten",
                "date": "17 september 2026",
                "media": [
                    {"image": "parkhaven-kaarten-fase1.png", "alt": "Vier kaarten van het studiegebied naast elkaar, elk met een legenda: bebouwing (hoogtes), ondergrond (kabels), wateroverlast en hittestress.", "caption": "Bestaande kaarten op elkaar: bebouwing, ondergrond, wateroverlast en hittestress."},
                ],
                "text": [
                    "Ik voegde in ArcGIS Pro vier bestaande kaarten samen: hoogte, ondergrondse kabels, wateroverlast en hittestress. Het was mijn eerste keer met ArcGIS Pro, maar ik had in korte tijd vier bruikbare kaarten.",
                ],
            },
            {
                "title": "Niet gebruikte kaarten",
                "media": [
                    {"image": "parkhaven-kaart-dichtheid.png", "alt": "Kaart van het studiegebied met de bebouwingsdichtheid in rood en oranje, met legenda en schaalbalk.", "caption": "Kaart over dichtheid."},
                    {"image": "parkhaven-kaart-schaduw.png", "alt": "Kaart van het studiegebied met schaduw in tinten blauw en groen, met legenda en schaalbalk.", "caption": "Kaart over schaduw."},
                ],
                "text": [
                    "Twee extra kaarten over dichtheid en schaduw voegden niets toe en kwamen niet in de eindpresentatie. Geleerd: bepaal eerst welke data je echt nodig hebt.",
                ],
            },
            {
                "title": "Video fase 1",
                "text": [
                    "Een nagemaakte schermopname van fase 1: data inladen in ArcGIS Pro en bestaande kaarten zoeken. Dat ik dit nu zonder hulp kan nadoen, laat zien hoeveel ik heb geleerd.",
                ],
                "media": [
                    {"video": "parkhaven-fase1-arcgis.mp4", "poster": "poster-parkhaven-fase1-arcgis.jpg", "alt": "Schermopname van ArcGIS Pro: data inladen en bestaande kaarten zoeken", "caption": "Schermopname van fase 1 in ArcGIS Pro (33 seconden, zonder geluid)."},
                ],
            },
            {
                "title": "Fase 2: landgebruik",
                "date": "14 oktober 2026",
                "media": [
                    {"image": "parkhaven-landgebruik-alle-data.png", "alt": "Kaart van het landgebruik in Parkhaven met alle data in één kaart: daken, verharding, groen en water.", "caption": "Afbeelding 1: alle data in één kaart."},
                    {"image": "parkhaven-landgebruik-overzichtelijk.png", "alt": "Overzichtelijke kaart van het landgebruik: daken in donkerrood, bestrating in roze, gras en bomen in groen, water in lichtblauw.", "caption": "Afbeelding 2: de kaart overzichtelijk gemaakt."},
                    {"image": "parkhaven-landgebruik-maatregelen.png", "alt": "Dezelfde kaart met de nieuwe maatregelen ingetekend: extra bomen, groene daken en groen op de plek van een parkeerplaats langs de kade.", "caption": "Afbeelding 3: de nieuwe maatregelen ingetekend."},
                ],
                "text": [
                    "Ik laadde alle data in één kaart, maakte die overzichtelijk en tekende de maatregelen in: bomen, groene daken en groen in plaats van een parkeerplaats. Dit ging sneller en zelfstandiger dan in fase 1.",
                ],
            },
            {
                "title": "Fase 2: heat index (gevoelstemperatuur)",
                "date": "15 oktober 2026",
                "media": [
                    {"image": "hittestress-parkhaven.jpg", "alt": "Vier heat-indexkaarten: A. bomen, B. groene daken, C. groene kade en D. alle maatregelen.", "caption": "A: bomen, B: groene daken, C: groene kade, D: alle maatregelen."},
                    {"image": "parkhaven-heat-index-legenda.png", "alt": "Legenda: een kleurverloop van lichtgeel bij 31 °C naar donkerbruin bij 40 °C.", "caption": "Legenda van de heat index: van 31 °C (lichtgeel) tot 40 °C (donkerbruin)."},
                ],
                "text": [
                    "Met de analysetools van ArcGIS berekende ik de gevoelstemperatuur voor elke maatregel. Zo werd duidelijk welke variant het meest koelt en hoeveel graden dat scheelt.",
                ],
            },
            {
                "title": "Video fase 2",
                "text": [
                    "Een nagemaakte schermopname van de heat index in ArcGIS Pro. Je ziet vooral het einde van het proces, want de data was al ingeladen.",
                ],
                "media": [
                    {"video": "parkhaven-fase2-heat-index.mp4", "poster": "poster-parkhaven-fase2-heat-index.jpg", "alt": "Schermopname van ArcGIS Pro: de heat index maken met de analysetools", "caption": "Schermopname van de heat index in ArcGIS Pro (53 seconden, zonder geluid)."},
                    {"url": "https://youtu.be/tAAOGNIfaxA", "label": "Bekijk de video op YouTube"},
                ],
            },
            {
                "title": "Gebruikte tools en hulpmiddelen",
                "text": [
                    "Revit en Gemini kende ik al; ArcGIS Pro, Claude, Forma en Tygron waren nieuw voor mij. Met Forma kan ik nu zelfstandig een gebouw ontwerpen, maar in ArcGIS Pro en Tygron valt nog veel te ontdekken.",
                ],
            },
        ],
        "feedback": ["docenten-parkhaven"],
    },
    {
        "slug": "forma-masterplan-parkhaven",
        "title": "Masterplan Parkhaven in Forma",
        "leerdoelen": ["2.1", "4.1"],
        "tags": [],
        "lead": "De gebouwen van het masterplan Parkhaven, samen met een groepsgenoot nagebouwd in Forma als basis voor de hittestressanalyse, en een eerste simulatie in Tygron.",
        "role": "Modelleur, samen met N. Morales (project 1)",
        "date": "2026-10",
        "tools": "Forma, Revit, Tygron",
        "challenge": "Voor de simulaties in fase 2 hadden we zo snel mogelijk de gebouwen van het masterplan nodig. Forma en Tygron had ik nog nooit gebruikt.",
        "process": "N. Morales en ik verdeelden de gebouwen en bouwden ze na in Forma, met de situatietekening als onderlegger. Omdat mijn deel eerst klaar was, legde ik uit hoe ik het in Forma had gedaan, zodat de gebouwen op elkaar aansloten. Daarna probeerden we de hittestress te simuleren in Tygron.",
        "steps": [
            "Gebouwen verdelen en de situatietekening op schaal als onderlegger gebruiken",
            "Eigen gebouwen modelleren in Forma en de werkwijze uitleggen aan N. Morales",
            "Terrein in Revit verwijderen en opnieuw exporteren als IFC voor ArcGIS en Tygron",
            "Hittestress simuleren in Tygron",
        ],
        "result": "Alle gebouwen staan in één model, klaar voor de analyses. Forma was best eenvoudig om mee te werken, dus het was de snelste manier om de gebouwen te ontwerpen. Ik wil me verder verdiepen in de omgevingsanalyses die Forma zelf kan maken. Tygron lukte tijdens het project niet, maar na de presentatie hebben N. Morales en ik verder geëxperimenteerd en is het alsnog gelukt.",
        "image": "forma-masterplan-parkhaven.jpg",
        "image_alt": "3D-model in Forma van een rij woontorens langs de kade van Parkhaven, met een groen kader om de gebouwen die ik zelf heb gemodelleerd en het label Eigen bijdrage.",
        "caption": "Mijn eigen bijdrage aan het Forma-model van het masterplan (6 oktober 2026).",
        "details": [
            {
                "title": "Masterplan",
                "date": "6 oktober 2026",
                "text": ["Uit het masterplan haalden we de maten en hoogtes van de bouwblokken."],
                "media": [
                    {"image": "parkhaven-masterplan.jpg", "alt": "Tekeningen uit het masterplan Parkhaven: bovenaan de bouwblokken in aanzicht met hun breedte en hoogte, onderaan een 3D-overzicht van de oranje bouwblokken langs de Euromast.", "caption": "Masterplan: verscheidenheid in maten van de bouwblokken."},
                ],
            },
            {
                "title": "Gebouwen in Forma",
                "media": [
                    {"image": "forma-taakverdeling.png", "alt": "Forma-model van Parkhaven met een paars kader om de gebouwen van groepsgenoot N. Morales en een groen kader om mijn eigen bijdrage.", "caption": "Verdeling van de gebouwen: N. Morales (paars) en mijn eigen bijdrage (groen)."},
                    {"image": "forma-gebouwen-terrein.png", "alt": "Grijs terreinvlak met daarop de witte gebouwen van het masterplan, zoals Forma ze exporteert.", "caption": "De gebouwen met het terrein, zoals Forma ze exporteert."},
                ],
                "text": [
                    "N. Morales en ik bouwden de gebouwen na in Forma, met de situatietekening als onderlegger; de hoogtes waren een puzzel, omdat alleen het toppunt bekend was. Forma exporteert het terrein altijd mee, dus dat haalde ik in Revit weg.",
                ],
            },
            {
                "title": "Tygron",
                "media": [
                    {"image": "tygron-import.jpg", "alt": "3D-weergave in Tygron van Parkhaven met de witte gebouwen uit Forma langs de Maas.", "caption": "Afbeelding 1: het Forma-ontwerp in Tygron."},
                    {"image": "tygron-data-2013.jpg", "alt": "Tygron-weergave van Parkhaven met een blauwe laag over het hele gebied.", "caption": "Afbeelding 2: Tygron rekende met data van 2013."},
                    {"image": "tygron-gelukt.jpg", "alt": "Tygron-weergave van Parkhaven met een hittestresskaart in kleuren en een grafiek van de temperatuur eronder.", "caption": "Afbeelding 3: na de presentatie lukte de simulatie alsnog."},
                    {"video": "parkhaven-tygron.mp4", "poster": "poster-parkhaven-tygron.jpg", "alt": "Schermopname van de hittestresssimulatie in Tygron", "caption": "De hittestresssimulatie in Tygron (13 seconden, zonder geluid)."},
                ],
                "text": [
                    "Tijdens het project lukte de simulatie in Tygron niet: het importeren kostte veel tijd en Tygron rekende met data van 2013. Na de presentatie hebben N. Morales en ik verder geëxperimenteerd en lukte het alsnog.",
                ],
            },
        ],
        "feedback": ["docenten-parkhaven", "natasha"],
    },
    {
        "slug": "vakwerk-grasshopper",
        "title": "Vakwerk in Grasshopper",
        "leerdoelen": ["1.3", "3.2", "3.3"],
        "tags": ["parametrisch"],
        "lead": "Een parametrisch script met vier soorten vakwerken, doorgerekend met Karamba3D en geëxporteerd naar Technosoft Raamwerken, gemaakt op mijn leerplek bij ABT.",
        "role": "Leerplek bij ABT, Oosterhoff Digital team",
        "date": "2026-10",
        "tools": "Rhino, Grasshopper, Karamba3D, Technosoft Raamwerken",
        "challenge": "Ik wilde zonder template een vakwerk bouwen dat meebeweegt met parameters en dat ik kan doorrekenen. Toen ik op 1 oktober begon bij ABT, kon ik alleen de parameters van een bestaand script aanpassen.",
        "process": "Via de ThinkParametric-cursus leerde ik Grasshopper en Karamba3D beter begrijpen. Daarna bouwde ik zelfstandig een Pratt-vakwerk en koppelde ik dat aan Karamba3D. Ik maakte drie andere vakwerktypes en een keuzecomponent, zodat je de varianten één voor één kunt doorlopen en vergelijken.",
        "steps": [
            "Grasshopper en Karamba3D leren via ThinkParametric",
            "Een Pratt-vakwerk bouwen met invoerparameters en koppelen aan Karamba3D",
            "Drie andere diagonaalpatronen toevoegen, met een keuzecomponent om te wisselen",
            "Een vakwerk als XML exporteren en importeren in Technosoft Raamwerken",
        ],
        "result": "Een script met meerdere invoerparameters en diagonale patronen, gekoppeld aan Karamba3D en Technosoft Raamwerken. Mijn begeleider noemde dit een belangrijke stap vooruit. Zijn verbeterpunt: meer parametrisch denken, zodat de geometrie als één geheel meebeweegt en het script makkelijk uitbreidbaar is.",
        "image": "vakwerk-grasshopper.jpg",
        "image_alt": "Vier rode vakwerkliggers in Grasshopper met belastingpijlen erboven: een vakwerk met schuine diagonalen, een met verticalen en diagonalen, een met kruisende diagonalen en een driehoeksvakwerk.",
        "caption": "Vier vakwerktypes uit hetzelfde script, belast en doorgerekend met Karamba3D.",
        "details": [
            {
                "title": "Grasshopper-script",
                "text": [
                    "Links staan de vier vakwerken (Vakwerk 1 tot en met 4), elk in een eigen groep. Ze komen samen in de keuzecomponent en gaan daarna naar het oranje deel, waar Karamba3D het gekozen vakwerk doorrekent.",
                ],
                "media": [
                    {"image": "vakwerk-grasshopper-script.jpg", "alt": "Grasshopper-script met vier grijze groepen componenten (Vakwerk 1 tot en met 4) die via een keuzecomponent verbonden zijn met een oranje groep voor de berekening in Karamba3D.", "caption": "Het Grasshopper-script met de vier vakwerken en de berekening in Karamba3D."},
                ],
            },
            {
                "title": "Video",
                "media": [
                    {"url": "https://youtu.be/tAAOGNIfaxA", "label": "Bekijk de video van het vakwerk op YouTube"},
                ],
            },
        ],
        "feedback": ["begeleider-abt"],
    },
    {
        "slug": "parametrische-overspanning",
        "title": "Parametrische overspanning",
        "leerdoelen": ["1.3", "1.4", "2.1"],
        "tags": ["parametrisch", "fabricage"],
        "lead": "Mijn eigen ontwerp voor een overspanning van kleiblokken, parametrisch gemaakt in Grasshopper voor project 2 (digitale fabricage).",
        "role": "Ontwerper in de printergroep (project 2)",
        "date": "2026-11",
        "tools": "Rhino, Grasshopper",
        "challenge": [
            "Onze opdracht was om een overspanning te ontwerpen met blokken van klei. Deze blokken worden geprint met kleiprinters en daarna samengesteld door de cobot. Onze groep van zes was opgesplitst: drie mensen werkten aan de cobot en drie aan de printer. Ik zat in de printergroep.",
            "Iedereen maakte eerst een eigen concept. Ik bouwde een eigen model na op basis van een referentie, met mijn Grasshopper-vaardigheden van de leerplek. Ik wilde mezelf uitdagen: de vorm is simpel, maar heeft toch zijn uitdagingen.",
        ],
        "process": "Pas na veel pogingen kwam ik in de buurt van de referentie. Ik wist niet welke components het handigst waren, dus ik heb getest en uitgeprobeerd met verschillende components, want dit kan op meerdere manieren. Hieronder staan de pogingen, het eindmodel en de feedback.",
        "steps": [
            "Plan van aanpak maken (met groepsleden)",
            "Eigen concept ontwerpen in Grasshopper",
            "Drie pogingen: loft, extrude en amplitude",
            "Eindmodel bakken en renderen",
        ],
        "result": [
            "Vergeleken met waar ik begon is dit een grote vooruitgang. Ik heb geleerd vormen te maken in Grasshopper en curves te roteren.",
            "Er was twijfel tussen mijn model en dat van een groepslid. We kozen het model van het groepslid, omdat het mijne ingewikkeld was om te printen en voor de cobot. Ik heb geleerd om bij het ontwerpen rekening te houden met printen en de cobot.",
        ],
        "image": "parametrische-overspanning.jpg",
        "image_alt": "Twee renders van een witte boog die is opgebouwd uit veelhoekige blokken: links een schuin aanzicht, rechts een vooraanzicht met zwarte lijnen langs de randen.",
        "caption": "Rendering van het ontwerp (4 november 2026).",
        "details": [
            {
                "title": "Samenwerking",
                "text": [
                    "Drie groepsleden verdiepten zich in de cobot en drie in de klei, met vaste momenten om samen te zitten. Toen we niet konden kiezen tussen de concepten, hebben we samen ideeën geschetst.",
                ],
                "media": [
                    {"image": "overspanning-schets-groep.jpg", "alt": "Schetsen in blauwe pen op gelinieerd papier: een boog van blokken, losse blokken en verbindingen tussen de blokken.", "caption": "Samen ideeën geschetst om tussen de concepten te kiezen."},
                ],
            },
            {
                "title": "Referentie",
                "text": [
                    "Ik bouwde mijn model na op basis van deze referentie: een boog van veelhoekige blokken. De vorm is simpel, maar heeft toch zijn uitdagingen.",
                ],
                "media": [
                    {"image": "overspanning-referentie.jpg", "alt": "Foto van een papieren model: een boog opgebouwd uit wit en bruin gevouwen veelhoekige blokken.", "caption": "Referentie."},
                ],
            },
            {
                "title": "Pogingen",
                "media": [
                    {"image": "overspanning-poging-1-loft.png", "alt": "Rode boog in Grasshopper die uit één doorlopend vlak bestaat.", "caption": "Poging 1: loft."},
                    {"image": "overspanning-poging-2-extrude.png", "alt": "Rode boog van losse blokken waarvan de blokken aan de uiteinden rechtop staan.", "caption": "Poging 2: extrude."},
                    {"image": "overspanning-poging-3-amplitude.png", "alt": "Rode boog van grote veelhoekige blokken die allemaal horizontaal liggen.", "caption": "Poging 3: amplitude."},
                    {"image": "overspanning-eindmodel.png", "alt": "Rode boog van veelhoekige blokken die bovenaan smaller zijn, het eindmodel.", "caption": "Eindmodel."},
                ],
                "text": [
                    "Een loft gaf één doorlopend vlak, dus ik stapte over op extrude en daarna op een amplitude-component om de uiteinden goed te richten. Met feedback van K. Afshar (de onderkant is kleiner dan de bovenkant) en twee stralen kwam ik tot het eindmodel.",
                ],
            },
            {
                "title": "Eindmodel en Grasshopper-script",
                "date": "4 november 2026",
                "text": [
                    "Dit is mijn uiteindelijke model, gebakt en gerenderd. Hierbij zie je ook het Grasshopper-script dat ik heb gebruikt, met sliders voor onder andere de overspanning, de boogfactor, het aantal blokken, de dikte en de stralen.",
                ],
                "media": [
                    {"image": "overspanning-render-1.png", "alt": "Render van de witte boog van veelhoekige blokken, schuin van voren.", "caption": "Render, schuin aanzicht."},
                    {"image": "overspanning-render-2.png", "alt": "Render van de witte boog van voren, met zwarte lijnen langs de randen van de blokken.", "caption": "Render, vooraanzicht."},
                    {"image": "overspanning-grasshopper-script.png", "alt": "Grasshopper-script met links sliders voor de parameters en rechts een reeks verbonden componenten.", "caption": "Het Grasshopper-script."},
                ],
            },
            {
                "title": "Feedback en keuze",
                "media": [
                    {"video": "overspanning-parameters.mp4", "poster": "poster-overspanning-parameters.jpg", "alt": "Schermopname van Grasshopper en Rhino waarin de sliders worden verschoven en de rode boog meeverandert", "caption": "De parameters van het model aanpassen (17 seconden, zonder geluid)."},
                ],
                "text": [
                    "Een groepslid en mijn begeleider vonden mijn ontwerp niet helemaal parametrisch; de sliders van de twee stralen koppelen zou helpen. De groep koos een ander ontwerp, omdat het mijne lastig te printen was en voor de cobot.",
                ],
            },
        ],
        "feedback": ["kebriya", "natasha"],
    },
    {
        "slug": "kleiprinter-blokken-printen",
        "title": "Blokken printen met de kleiprinter",
        "leerdoelen": ["1.2", "1.4", "3.3", "4.1"],
        "tags": ["fabricage", "parametrisch"],
        "lead": "Uitzoeken hoe de kleiprinter werkt, de printbestanden voorbereiden met de Termite-template en de kleiblokken van het gekozen ontwerp printen, voor project 2 (digitale fabricage).",
        "role": "Printergroep, samen met N. Morales en K. Afshar (project 2)",
        "date": "2026-11",
        "tools": "WASP 2040 kleiprinter, Rhino, Grasshopper, Termite",
        "challenge": "Na de keuze voor het ontwerp moesten wij als printergroep de blokken printen. In het begin hadden we geen idee hoe de kleiprinter werkte en de informatie was beperkt.",
        "process": "Samen met N. Morales en K. Afshar zocht ik uit hoe de kleiprinter werkt. Ik onderzocht de Termite-template, bereidde de bestanden voor en printte met hen de blokken. Hieronder staat elke stap, met de testprints en video's.",
        "steps": [
            "Informatie zoeken over de kleiprinter (met twee anderen)",
            "De Termite-template onderzoeken en uitleggen",
            "Bestanden voorbereiden en de G-code exporteren",
            "Testprints maken en de instellingen aanpassen",
            "Blokken printen (met twee anderen)",
        ],
        "result": [
            "Na veel pogingen is het gelukt: alle blokken zijn geprint en zo komen ze bij elkaar.",
            "In dit project heb ik vooral gewerkt aan mijn vaardigheden met Grasshopper en met de kleiprinter. Bij Grasshopper heb ik geleerd om meer parametrisch na te denken over mijn ontwerpen en om te werken met extrude en planes. Bij de kleiprinter heb ik geleerd hoe het werkt, hoe je de printer schoonmaakt, hoe je print en hoe je de klei voorbereidt. We kunnen dit nu ook aan anderen uitleggen.",
            "Wat ik anders zou doen: minder afwachtend zijn. We begonnen later met printen, omdat we eerst alles goed wilden weten. Toen we wilden beginnen, bleek wat we hadden geleerd niet genoeg. Veel hebben we toen geleerd van de andere groep, die eerder met printen was begonnen.",
        ],
        "image": "kleiprinter-overspanning-resultaat.jpg",
        "image_alt": "De geprinte kleiblokken samengesteld tot een boog op een tafel.",
        "caption": "Het resultaat: de geprinte blokken samen als overspanning.",
        "details": [
            {
                "title": "Onderzoek kleiprinter",
                "text": [
                    "Met N. Morales en K. Afshar zocht ik uit hoe de kleiprinter werkt, via video's van WASP 2040 en uitleg van de andere groep. Een groepslid vond de plug-in Termite en ik vond een template die laat zien hoe die werkt.",
                ],
            },
            {
                "title": "De template",
                "media": [
                    {"image": "kleiprinter-template-script.png", "alt": "De Termite-template in Grasshopper: kolommen met componenten en een paars gemarkeerde groep.", "caption": "De Termite-template in Grasshopper."},
                    {"video": "kleiprinter-template.mp4", "poster": "poster-kleiprinter-template.jpg", "alt": "Schermopname van Rhino en Grasshopper waarin de template twee testblokken in lagen opdeelt", "caption": "De template testen (25 seconden, zonder geluid)."},
                ],
                "text": [
                    "Ik testte de template en legde hem uit aan de groep. In een test vervormde het tweede blok, dus sorteerden we het printpad zodat de printer laag voor laag per blok print.",
                ],
            },
            {
                "title": "Bestanden voorbereiden",
                "media": [
                    {"image": "kleiprinter-verdeling-blokken.png", "alt": "Bovenaanzicht van de boog van blokken in Rhino, verdeeld in drie gekleurde kaders: Shena links, N. Morales in het midden en K. Afshar rechts.", "caption": "Verdeling van het overtekenen: Shena, N. Morales en K. Afshar."},
                    {"image": "kleiprinter-polylines.png", "alt": "De omtrekken van alle blokken als losse polylines op het printbed in Rhino.", "caption": "Alle blokken als polylines op het printbed."},
                    {"video": "kleiprinter-printpad.mp4", "poster": "poster-kleiprinter-printpad.jpg", "alt": "Simulatie van het printpad in de rode printer in Rhino, waarin de blokken laag voor laag ontstaan", "caption": "Simulatie van het printpad (48 seconden, zonder geluid)."},
                ],
                "text": [
                    "We tekenden het gekozen ontwerp in Rhino over met polylines; ik voegde alles samen, maakte een extrude en exporteerde de G-code. Na een testprint maakten we de blokken 2 cm en de opening van de pen-gatverbinding 4 mm groter.",
                ],
            },
            {
                "title": "Testprints",
                "media": [
                    {"image": "kleiprinter-print-1-en-2.jpg", "alt": "Twee geprinte testblokken van klei op een draaischijf naast een handleiding.", "caption": "Print 1 (rechts) en print 2 (links)."},
                    {"image": "kleiprinter-testprint.jpg", "alt": "Een geprint kleiblok met een uitsparing op een witte plaat.", "caption": "Testprint."},
                    {"image": "kleiprinter-beste-testprint.jpg", "alt": "Een geprint kleiblok met gelijkmatige lagen.", "caption": "Beste testprint: de lagen kwamen mooi op elkaar."},
                    {"image": "kleiprinter-blokken-geprint.jpg", "alt": "Alle geprinte kleiblokken van het gekozen ontwerp dicht naast elkaar op het printbed.", "caption": "De blokken van het gekozen ontwerp."},
                ],
                "text": [
                    "De eerste prints mislukten door de instellingen; na aanpassingen aan onder andere de nozzle en de printsnelheid kwamen de lagen mooi op elkaar. Daarna printten we de blokken van het gekozen ontwerp.",
                ],
            },
            {
                "title": "Trial-and-error",
                "media": [
                    {"image": "kleiprinter-gebroken-blokken.jpg", "alt": "Gebroken en hele kleiblokken en testprints op een stuk karton.", "caption": "Gebroken blokken en testen."},
                ],
                "text": [
                    "Sommige blokken braken en elke nieuwe klei printte anders, ook met dezelfde instellingen. Daarom printten we alle blokken op één dag.",
                ],
            },
            {
                "title": "Blokken printen",
                "text": [
                    "Het voorbereiden van de printer duurde ongeveer 3 uur, onder andere door een harde slang en rommelige eerste prints; het printen zelf 24 minuten. Na veel pogingen is het gelukt en komen de blokken samen.",
                ],
                "media": [
                    {"video": "kleiprinter-printen.mp4", "poster": "poster-kleiprinter-printen.jpg", "alt": "De kleiprinter print de blokken laag voor laag", "caption": "De kleiprinter aan het werk (4 seconden, zonder geluid)."},
                    {"video": "kleiprinter-printen-kort.mp4", "poster": "poster-kleiprinter-printen-kort.jpg", "alt": "Close-up van de nozzle van de kleiprinter tijdens het printen", "caption": "Close-up van de nozzle (4 seconden, zonder geluid)."},
                    {"image": "kleiprinter-printer.jpg", "alt": "De bovenkant van de kleiprinter met de container en de slang.", "caption": "De printer voorbereiden."},
                    {"image": "kleiprinter-shena-bij-printer.jpg", "alt": "Shena steekt lachend haar duimen op naast de kleiprinter.", "caption": "Gelukt!"},
                    {"image": "kleiprinter-blokken-op-rij.jpg", "alt": "De geprinte kleiblokken in een boog naast elkaar op een tafel.", "caption": "Zo komen de blokken bij elkaar."},
                    {"image": "klei-geprinte-blokken.jpg", "alt": "Alle geprinte kleiblokken los op een witte plaat, met metalen pennen ernaast.", "caption": "De geprinte blokken met de pennen voor de verbindingen."},
                ],
            },
        ],
        "feedback": ["kebriya", "natasha"],
    },
    {
        "slug": "vakwerk-python",
        "title": "Vakwerk met Python in Grasshopper",
        "leerdoelen": ["1.3", "3.1", "3.3"],
        "tags": ["python", "parametrisch"],
        "lead": "Hetzelfde vakwerk als in mijn Grasshopper-script, opnieuw opgebouwd met alleen Python-code in de ingebouwde Python van Grasshopper.",
        "role": "Leerplek bij ABT, Oosterhoff Digital team",
        "date": "2026-11",
        "tools": "Rhino, Grasshopper, Python",
        "challenge": "Een van mijn leerdoelen was een basis Python-script schrijven, maar ik merkte dat ik er nog niets mee had gedaan. Dat besprak ik met mijn begeleider. Hij gaf mij de opdracht om mijn vakwerk opnieuw te maken, nu met Python.",
        "process": "Het lastigste was hoe de Grasshopper-componenten als code werken. Ik testte verschillende manieren en vroeg Copilot om uitleg, maar niet om het script te schrijven. Het script maakt punten onder en boven op basis van de lengte, hoogte en het aantal vakken, en verbindt die met verticalen en diagonalen.",
        "steps": [
            "Video's van mijn begeleider bekijken",
            "Onder- en bovenpunten berekenen uit lengte, hoogte en aantal",
            "Verticalen en diagonalen tekenen met lijnen in een lus",
            "Het resultaat in Rhino vergelijken met het Grasshopper-vakwerk",
        ],
        "result": "Het vakwerk in Python werkt en mijn begeleider vond dat ik het snel had gemaakt. Zijn advies: let op de structuur van de code, vooral op variabelenamen en opmerkingen. Mijn volgende stap is een klein script dat een terugkerende handeling automatiseert.",
        "image": "vakwerk-python.jpg",
        "image_alt": "Links de Python-code in de scripteditor van Grasshopper, met lussen voor punten, verticalen en diagonalen. Rechts het groene vakwerk dat de code in Rhino tekent.",
        "caption": "De Python-code en het vakwerk dat die code in Rhino maakt.",
        "feedback": ["begeleider-abt"],
    },
    {
        "slug": "van-brienenoordbrug",
        "title": "Van Brienenoordbrug",
        "leerdoelen": ["1.3", "3.2"],
        "tags": ["parametrisch"],
        "lead": "Een parametrisch model van de Van Brienenoordbrug in Grasshopper: in september lukte alleen de boog, in november bouwde ik zelfstandig de hele brug.",
        "role": "Eigen opdracht",
        "date": "2026-11",
        "tools": "Rhino, Grasshopper",
        "challenge": "Bij de workshop over items, lists en trees modelleerde ik de Van Brienenoordbrug. Met hulp van anderen kwam ik toen niet verder dan de boog. Na de ThinkParametric-cursus wilde ik zien of ik de brug zelfstandig kon maken.",
        "process": "Bij de eerste poging (21 september 2026) maakte ik met hulp de curves van de boog. Na de cursus begon ik opnieuw en bouwde ik zonder hulp de bogen met vakwerk ertussen, het brugdek, de pijlers en de aanbruggen (23 november 2026).",
        "steps": [
            "Eerste poging met hulp: alleen de curves van de boog",
            "Grasshopper leren via de ThinkParametric-cursus",
            "Tweede poging zonder hulp: bogen, vakwerk, brugdek en pijlers",
        ],
        "result": "Het verschil tussen de twee pogingen laat zien hoeveel ik in twee maanden heb geleerd: van een paar curves met hulp naar een complete brug die ik zelf heb opgebouwd.",
        "image": "van-brienenoordbrug.jpg",
        "image_alt": "Rood, half doorzichtig 3D-model van de Van Brienenoordbrug in Rhino: twee bogen met vakwerk ertussen boven het brugdek, op twee ronde pijlers.",
        "caption": "Tweede poging, zonder hulp gemaakt (23 november 2026).",
        "details": [
            {
                "title": "Referentie",
                "media": [
                    {"image": "van-brienenoordbrug-referentie.jpg", "alt": "Luchtfoto van de Van Brienenoordbrug over de Nieuwe Maas: een witte boogbrug met vakwerk tussen de twee bogen.", "caption": "Referentiefoto van de Van Brienenoordbrug."},
                ],
            },
            {
                "title": "Eerste poging met hulp van anderen",
                "date": "21 september 2026",
                "media": [
                    {"image": "van-brienenoordbrug-eerste-poging.jpg", "alt": "Twee rode boogcurves met controlepunten boven een grijs raster in Rhino.", "caption": "Eerste poging: alleen de curves van de boog."},
                ],
            },
            {
                "title": "Tweede poging zonder hulp (na de cursus)",
                "date": "23 november 2026",
                "media": [
                    {"image": "van-brienenoordbrug.jpg", "alt": "Rood 3D-model van de complete brug met bogen, vakwerk, brugdek en pijlers.", "caption": "Tweede poging: de complete brug."},
                ],
            },
        ],
    },
]

# Feedback that projects link to with their "feedback" list. Text as received (plain text, one string per paragraph).
FEEDBACK = {
    "begeleider-abt": {
        "title": "Feedback begeleider leerplek",
        "from": "E. Estrado, begeleider bij ABT (Samen Oosterhoff)",
        "date": "17 november 2026",
        "paragraphs": [
            "Sinds 1 oktober ben je bij ABT gestart met je leerplek als deel van de Oosterhoff Digital team. Tijdens de speeddate sessie gaf je aan dat je doel was om je digitale skills te ontwikkelen vooral met Grasshopper en Python in het kader van constructief ontwerp. Wat mij betreft gaat je ontwikkeling tot nu toe de goede kant op.",
            "Je bent bijna vanuit het niets begonnen en hebt je nu zo ver ontwikkeld dat je in Grasshopper kleine parametrische scripts kunt maken voor eenvoudige constructies. Het vakwerk-script dat je hebt gebouwd met meerdere invoerparameters en diagonale patronen plus koppeling met Karamba en Technosoft Raamwerken is een belangrijke stap vooruit. Nu begin je ook meer te doen met Python en ik vind deze ontwikkeling eveneens veelbelovend. Je hebt de basis vrij snel onder de knie gekregen.",
            "Naarmate je verdergaat, zou ik het parametrisch denken meer in gedachten houden. Dat betekent dat je bij het ontwikkelen van Grasshopper-scripts niet alleen moet nadenken over wat werkt met de huidige parameters, maar ook over hoe het zich gedraagt wanneer je parameters wijzigt. Zorg ervoor dat de geometrie als één geheel meebeweegt, dat invoerwaarden worden hergebruikt en niet gedupliceerd, en dat je script zo is opgezet dat het gemakkelijk uitbreidbaar is, d.w.z. dat je er gemakkelijk dingen aan kunt toevoegen zonder grote wijzigingen in de bestaande workflow. Let bij Python op de structuur en overzichtelijkheid van de code, met name wat betreft variabelenamen en opmerkingen. Dit helpt je later bij het terugkijken op en leren van wat je hebt gedaan.",
            "Tot nu toe heb je tijdens de leerplek een positieve houding getoond ten opzichte van leren en het uitproberen van nieuwe dingen. Je lijkt oprecht geïnteresseerd in digitale vaardigheden en bereid om dingen uit te proberen om jezelf verder te ontwikkelen. Je luistert aandachtig en volgt advies op. Je werkt best zelfstandig. Mijn feedback op dit gebied zou zijn om meer vragen te stellen en ook aan te geven of je iets nieuws of anders wilt zien, doen of uitproberen, zodat we kunnen bekijken hoe we dat kunnen regelen. Het doel van deze periode is gewoon te leren, niet alleen direct techniek maar ook van jouw collega's.",
            "Over het algemeen vind ik je een prettige collega die goed in het team past. Je maakt in een goed tempo je ontwikkeling door. Ik kijk uit naar de rest van de leerplekperiode en ben ervan overtuigd dat je aan het einde een resultaat zult behalen waar je trots op kunt zijn.",
        ],
    },
    "docenten-parkhaven": {
        "title": "Feedback docenten (eindpresentatie)",
        "from": "Docenten, eindpresentatie project Parkhaven",
        "date": "",
        "paragraphs": [
            "Algemene feedback: Jullie hebben als groep vooral gefocust op het maken van analyses ==> er is veel informatie. Maar wat ga je er nu mee doen? Of wat hebben jullie hier precies mee gedaan? Dat ontbreekt nog in de presentatie. Mogelijk veel laten leiden door AI-ondersteuning, maar daardoor mogelijk cruciale vragen vergeten. Bijvoorbeeld: waarom een wadi in buitendijks gebied? Wat is het nut hier dan van als de rivier de grondwaterstand bepaalt.",
            "Notitie: start 09:48. Eindtijd: 10:02. 40% overtijd.",
            "Presentatiebeelden zijn soms klein, daardoor moeilijk te zien.",
            "De presentatie heeft wel een eenduidig ontwerp.",
            "Jullie zijn echt in GIS verdiept, dat is een nieuwe tool geweest en daar hebben jullie goede eerste analyses mee gemaakt. Dank daarvoor.",
            "Gevoelstemperatuur neemt af door (schaduw van) gebouwen?",
            "Presentatie werkt niet op de laptop, zorg dat je dit van tevoren test.",
            "M. begint om 09:55, 7 minuten in de presentatie.",
            "Presentatie overtijd.",
            "\"het was heel kut\", let graag op taalgebruik.",
            "N. geeft de vraag: hoe heeft deze analyse invloed gehad op de keuzes die jullie hebben gemaakt.",
            "Hoe heeft de afweging van soorten bomen invloed gehad op de digitale tools die je hebt gebruikt.",
            "Euromast is buitendijks gebied... dus gaat een wadi dan wel effect hebben als de rivier de grond aanvult. Let op dat er tijdens hittestress ook minder water is.. dus als daar je verkoelingsstrategie op is gebaseerd.... Oftewel, ondanks alle slimme digitale technieken is het nog belangrijker de systemen zelf ook goed te begrijpen.",
            "5 losse analyses en daarmee wat minder 1 verhaal. Er lijken daardoor dubbelingen of overlappen te zijn tussen de 5 verhalen, maar het blijven losse stukjes.",
        ],
    },
    "natasha": {
        "title": "Feedback groepsgenoot",
        "from": "N. Morales, groepsgenoot bij project 1 en project 2",
        "date": "18 november 2026",
        "paragraphs": [
            "Ik vond de samenwerking bij project 1 en project 2 erg prettig. Hieronder geef ik je mijn feedback. Je communiceert duidelijk en legt je bevindingen helder uit, zodat anderen, zoals ik, je goed kunnen volgen. Als je een taak krijgt, voer je die altijd zo zorgvuldig mogelijk uit. Je onderzoek is ook echt grondig, zoals bij de Termite-template, waarbij je precies uitzocht hoe je ermee moest werken. Als ik iets niet begrijp, kan ik altijd bij je terecht en help je me graag. Daardoor weet ik dat ik in een groepsopdracht op je kan rekenen. Ik vind het ook echt top dat je het wilt bespreken met de groep als de samenwerking niet goed gaat.",
            "Ik heb nog twee tips. De eerste is dat je het meteen moet zeggen als je het ergens niet mee eens bent, in plaats van het naar een later moment te schuiven. Dan kan de groep er direct rekening mee houden. De tweede is dat je niet het initiatief durft te nemen bij presentaties. Zeg gerust: \"Ik wil graag presenteren.\" Je presenteert duidelijk en goed, dus ga gerust wat vaker uit je comfortzone.",
        ],
    },
    "kebriya": {
        "title": "Feedback groepsgenoot",
        "from": "K. Afshar, groepsgenoot bij project 2 (Klei Master)",
        "date": "24 november 2026",
        "paragraphs": [
            "Tijdens het project Klei Master heb ik de samenwerking met jou als erg prettig ervaren. Je communiceerde duidelijk en goed met de groep en zorgde ervoor dat iedereen op de hoogte bleef van de voortgang en de gemaakte afspraken.",
            "Wat ik ook sterk vond, is dat je niet alleen problemen signaleerde, maar ook zelf actief nadacht over mogelijke oplossingen. Je nam initiatief om problemen aan te pakken en probeerde altijd mee te denken over hoe we als groep verder konden komen.",
            "Daarnaast kwam je je afspraken altijd na en voerde je de afgesproken taken op tijd uit. Je toonde veel verantwoordelijkheidsgevoel en was betrokken bij het gezamenlijke proces.",
            "Een mogelijk ontwikkelpunt is om soms iets minder perfectionistisch te zijn. Je wilt graag dat het werk zo goed mogelijk wordt uitgevoerd, wat natuurlijk een sterke eigenschap is. Toch kan het soms helpen om te accepteren dat iets goed genoeg is, zodat je je tijd en energie efficiënter kunt verdelen.",
            "Ik vond het fijn om met je samen te werken. Je goede communicatie, oplossingsgerichte houding en verantwoordelijkheidsgevoel hebben een positieve bijdrage geleverd aan onze samenwerking en het eindresultaat van het project.",
        ],
    },
}

# Content of the standalone reflectie page (reflectie.html), written as a STAR-reflectie.
# Each step has a letter, a heading and a list of paragraphs (plain text, one string per paragraph).
REFLECTIE = {
    "title": "STAR-reflectie",
    "lead": "Een reflectie op mijn ontwikkeling als bouwkundige in een digitale context, over alle competenties en projecten heen, volgens de STAR-methode.",
    "sections": [
        {
            "letter": "S",
            "heading": "Situatie",
            "paragraphs": [
                "Beschrijf de context: in welke periode, opleiding of omgeving speelde dit zich af, en met wie werkte je samen?",
            ],
        },
        {
            "letter": "T",
            "heading": "Taak",
            "paragraphs": [
                "Wat was jouw taak of rol, en wat werd er van je verwacht? Welke leerdoelen wilde je in deze periode aantonen?",
            ],
        },
        {
            "letter": "A",
            "heading": "Actie",
            "paragraphs": [
                "Wat heb je concreet gedaan? Beschrijf je aanpak, de keuzes die je maakte en waarom, met verwijzingen naar je projecten.",
            ],
        },
        {
            "letter": "R",
            "heading": "Resultaat",
            "paragraphs": [
                "Wat was het resultaat van je acties? Welke leerdoelen heb je aangetoond, wat ging goed en wat zou je een volgende keer anders doen?",
            ],
        },
    ],
}

# STARR-reflectie per competentie, shown on its competentie page between the leerdoelen and the projects.
# Keyed by competentie number. "leerdoelen" is the line above the reflectie.
# Each part (situatie, taak, actie, resultaat, reflectie) is a list of paragraphs (plain text, one string per paragraph).
# A competentie without an entry here shows no reflectie.
STARR = {
    "1": {
        "leerdoelen": "Leerdoelen gebruikt: 1.1, 1.2, 1.3 en 1.4 (persoonlijk leerdoel PD1)",
        "situatie": [
            "Mijn persoonlijke leerdoel was om zelfstandig een parametrisch model op te zetten in Rhino/Grasshopper voor een draagconstructie. Ik begon klein: ik had één keer met een template van A. gewerkt en alleen parameters aangepast. In de eerste weken lukte het me niet om de pergola af te maken, en bij de workshop over item, list en tree maakte ik alleen de boog van de brug. Daarna begon ik bij ABT, in het Oosterhoff Digital team.",
        ],
        "taak": [
            "Ik wilde zonder template een vakwerk bouwen dat meebeweegt met parameters en dat ik kan doorrekenen. Mijn vraag was of ik dat zelf kon, en mijn methode was: eerst de basis leren, dan zelf bouwen en daarna koppelen aan Karamba3D om varianten te vergelijken.",
        ],
        "actie": [
            "Een video en de workshop legden bijna dezelfde dingen uit en ik snapte het nog niet. Daarom volgde ik via mijn leerplek de ThinkParametric-cursus, om Grasshopper beter te begrijpen. Daar viel het ineens op zijn plek. Waarschijnlijk doordat ik het een aantal keer had gehoord, al weet ik dat niet zeker.",
            "Daarna bouwde ik helemaal zelfstandig een Pratt-vakwerk. Ik koppelde het aan Karamba en voerde berekeningen uit. Ik maakte drie andere vakwerktypes, koppelde elk aan een Karamba-component en bouwde een keuzecomponent, zodat je de varianten één voor één kunt doorlopen. Daarna exporteerde ik een vakwerk als XML-bestand vanuit Grasshopper en importeerde ik het in Technosoft Raamwerken.",
        ],
        "resultaat": [
            "Ik heb een script met meerdere invoerparameters en diagonale patronen, gekoppeld aan Karamba3D en Technosoft Raamwerken. Door de varianten naast elkaar door te rekenen kan ik een ontwerpkeuze onderbouwen met data. Mijn begeleider noemt dit een belangrijke stap vooruit en zag dat ik de basis snel onder de knie heb gekregen.",
        ],
        "reflectie": [
            "In het begin kon ik alleen de parameters van een ander aanpassen en nu bouw ik zelf scripts. Mijn begeleider gaf ook een verbeterpunt: parametrisch denken. Ik moet niet alleen kijken wat werkt met de huidige parameters, maar ook hoe het script reageert als ze wijzigen. De geometrie moet als één geheel meebewegen, invoerwaarden moeten hergebruikt worden in plaats van gedupliceerd en het script moet makkelijk uitbreidbaar zijn. Dat herken ik: bij project 2 merkte een groepsgenoot al op dat mijn parameters niet helemaal correct waren. Dat ik dit van twee kanten hoor, laat zien dat ik hier echt mee moet oefenen. Daarom bepaal ik bij elk nieuw script eerst welke parameters ik wil kunnen wijzigen, test ik het door ze aan te passen en kijk ik bij uitbreidingen of dat kan zonder opnieuw te beginnen.",
            "Het lastigst vond ik in het begin dat ik de componenten niet kende en niet wist wat ik kon gebruiken. Daardoor duurde het even voordat mijn script werkte, maar na een aantal scripts ging het sneller. Het leukst vind ik het moment waarop het script werkt en ik mijn doel bereik. Als vervolgstap ga ik op mijn leerplek een echte draagconstructie maken, zoals een gebouw of brug, met Karamba, Python en Technosoft.",
        ],
    },
    "2": {
        "leerdoelen": "Leerdoelen gebruikt: 2.1, 2.2 en 2.3 (persoonlijk leerdoel PD3)",
        "situatie": [
            "Bij project 1 (Parkhaven) onderzochten we met een groep welke klimaatadaptatiemaatregelen bij de gebouwen van het masterplan konden. Mijn taak was de hittestressanalyse in ArcGIS Pro. Mijn persoonlijke leerdoel was goed samenwerken met digitale tools, zodat we tot één samenhangende oplossing komen. Mijn startsituatie was dat iedereen aan zijn eigen onderdeel werkt en we pas op het laatst samenvoegen.",
        ],
        "taak": [
            "Voor de analyse hadden we de gebouwen van het masterplan nodig. Daarom ontwierpen N. Morales en ik die in Forma. Als groep spraken we meteen af om steeds af te stemmen.",
        ],
        "actie": [
            "Eerst maakte ik in ArcGIS Pro kaarten van het studiegebied, waaronder hittestress. Later paste ik de analysetools zelf toe, tekende ik maatregelen met groen en berekende ik de heat index. Zo zette ik de effecten van bomen, groene daken, een groene kade en alle maatregelen naast elkaar. Met legenda's en een duidelijke afkadering maakte ik de kaarten begrijpelijk voor anderen.",
            "Voor de gebouwen gebruikten N. Morales en ik Forma, dat nieuw voor mij was. Omdat ik mijn deel eerst klaar had, legde ik haar uit hoe ik het had gedaan, zodat de gebouwen op elkaar aansloten. Ik gebruikte de overzichtstekening van het masterplan op schaal als onderlegger. Omdat Forma het terrein meeneemt in de IFC, haalde ik dat eerst in Revit weg.",
        ],
        "resultaat": [
            "Het Forma-model lukte: alle gebouwen in één model, klaar voor de analyse. De belangrijkste uitkomst was dat de omgeving met alle maatregelen samen 2 graden koeler wordt.",
            "Bij de eindpresentatie aan de bedrijven presenteerde ik de analyse ten opzichte van groen, maar de presentatie verliep minder goed. De gastbezoeker vroeg waar we naartoe wilden met al deze informatie. De docenten vroegen wat een deel over soorten bomen met digitale tools te maken had; een groepslid had dat zelf besloten, zonder afspraak met de groep. Een ander groepslid wilde haar Grasshopper-script laten zien, maar had het niet in de PowerPoint gezet. Haar laptop aansluiten lukte niet. We hadden dit vooraf moeten testen, maar dat was niet afgesproken.",
        ],
        "reflectie": [
            "Samenwerken met één persoon, met een concrete afspraak en uitleg, ging goed. In de hele groep lukte dat niet: afspraken helpen alleen als iedereen zich eraan houdt. We spraken de personen aan die niet werkten, maar dat hielp niet. Voortaan meld ik het direct bij de docent als iemand niets doet of zelf dingen besluit zonder afspraak. Ik had mijn eigen onderdeel ook kunnen afsluiten met een conclusie en een vervolgstap, zodat de vraag waar we naartoe willen beantwoord was.",
            "Los hiervan bouwde ik mijn netwerk op (2.3). Tijdens de speeddatesessie sprak ik met vier professionals en op de Prefab Beurs met meer dan 15 mensen en bedrijven. Ik liet mijn QR-code scannen en vertelde dat ik de minor Digitaliseren volg. Zo leerde ik wat anderen in de praktijk met digitaliseren doen en dat het een hot topic bij bedrijven is.",
        ],
    },
    "3": {
        "leerdoelen": "Leerdoelen gebruikt: 3.1, 3.2 en 3.3 (persoonlijke leerdoelen PD2, PD4 en PD5)",
        "situatie": [
            "Ik moest in korte tijd nieuwe tools leren: ArcGIS Pro en Tygron voor de hittestressanalyse in het project, en Python op mijn leerplek. Mijn persoonlijke leerdoelen waren tijdig bijsturen als ik vastloop, in mijn eigen tijd nieuwe tools leren en een basis Python-script schrijven. Mijn startsituatie was dat ik vaak afwachtend was en dat ik nog geen programmeerervaring had.",
        ],
        "taak": [
            "Ik moest deze tools zelf onder de knie krijgen om bij te dragen aan het project en aan mijn werk op de leerplek.",
        ],
        "actie": [
            "In ArcGIS Pro liep ik vast op een foutmelding bij het clippen van een laag. Ik zocht met AI uit wat de oorzaak was en maakte aantekeningen met wat ik leerde en shortcuts. Daarna probeerde ik Tygron voor de hittestressanalyse, maar dat kreeg ik niet onder de knie. Ik stapte over op ArcGIS Pro en experimenteerde later opnieuw met Tygron, wat een beetje lukte. Ook maakte ik via een Esri-cursus mijn eigen 3D-scene in ArcGIS Online.",
            "Op mijn eerste dag bij mijn leerplek zag ik projecten met Grasshopper en Python en begon ik aan een Python-cursus. Na een tijdje merkte ik dat ik er verder niets mee had gedaan. Ik besprak dat met mijn begeleider. Hij stuurde video's en gaf mij de opdracht om hetzelfde vakwerk dat ik in Grasshopper had gemaakt opnieuw te bouwen met de ingebouwde Python in Grasshopper. Lastig was hoe de componenten als code werken, dus hoe je die in een script zet. Ik loste dat zelf op door verschillende manieren te testen en Copilot om uitleg te vragen, maar niet om het script zelf te schrijven. Daarna ging het best makkelijk.",
        ],
        "resultaat": [
            "In ArcGIS Pro maakte ik vier kaarten waarin bomen, groene daken, een groene kade en alle maatregelen naast elkaar staan. Tygron lukte deels. Het vakwerk in Python heb ik gebouwd en mijn begeleider merkte op dat ik dat heel snel deed. Hij noemt mijn ontwikkeling veelbelovend.",
        ],
        "reflectie": [
            "Vroeger stopte ik als ik vastliep. Nu stuur ik bij: bij Tygron veranderde ik van aanpak in plaats van op te geven en bij Python bracht ik het zelf ter sprake. AI hielp me uitzoeken, maar ik leerde pas echt door aantekeningen te maken en het zelf opnieuw toe te passen.",
            "Mijn Python-scripts zijn nog niet netjes gecodeerd, maar ze werken wel. Mijn begeleider adviseert te letten op structuur en overzichtelijkheid, vooral variabelenamen en opmerkingen, zodat ik later makkelijk kan terugkijken. Hij ziet ook een positieve houding en dat ik zelfstandig werk, maar adviseert meer vragen te stellen en aan te geven wat ik nog wil zien of proberen. Daarom schrijf ik mijn vragen op en stel ik ze gewoon, in plaats van ze direct zelf op te zoeken.",
            "Mijn Python-leerdoel is nog niet helemaal behaald: ik heb een vakwerk gebouwd, maar nog geen tool die mij efficiënter laat werken. Mijn volgende stap is een klein script dat een terugkerende handeling automatiseert. Verder maak ik voor januari een kleine Rhino-opdracht om mijn Rhino-skills aan te scherpen.",
        ],
    },
    "4": {
        "leerdoelen": "Leerdoelen gebruikt: 4.1 (persoonlijk leerdoel PD4)",
        "situatie": [
            "Volgens het model van professioneel handelen werk je aan een complex vraagstuk, is de oplossing nog onbekend en is samenwerken noodzakelijk. Dat herken ik in mijn projecten en op mijn leerplek. Mijn persoonlijke leerdoel was mijn leerproces kritisch te monitoren en tijdig bij te sturen. Mijn startsituatie was dat ik bij vastlopen neig te stoppen en af te wachten.",
        ],
        "taak": [
            "Ik wilde actief feedback vragen, die verwerken en kennis delen met mijn team.",
        ],
        "actie": [
            "Vroeg in de minor kreeg ik handgeschreven feedback van een medestudent op mijn leerdoelen. Een paar weken later leverde ik een reflectie in over de speeddatesessie en kreeg ik feedback van de docent: ik ben goed op weg met reflecteren, maar moet meer nadenken over waar ik wil eindigen en hoe ik kan groeien. Op mijn leerplek kreeg ik feedback van mijn begeleider. Toen Python bleef liggen, bracht ik dat zelf ter sprake. Bij Parkhaven legde ik N. Morales uit hoe ik in Forma werkte, zodat onze gebouwen op elkaar aansloten.",
        ],
        "resultaat": [
            "Mijn begeleider noemt mij een prettige collega die goed in het team past, in een goed tempo ontwikkelt, een positieve houding heeft ten opzichte van leren en adviezen opvolgt.",
        ],
        "reflectie": [
            "Binnen het model past dit bij interactief leervermogen (leerdoelen stellen, reflecteren, open staan voor feedback en die verwerken) en bij effectief samenwerken (kennis delen). Ik zie een verschil met mijn begin: ik wacht minder af, dat bleek bij Tygron en bij Python.",
            "Er komen ook twee verbeterpunten terug. Mijn begeleider adviseert meer vragen te stellen en mijn docent wil dat ik meer nadenk over de toekomst. Ik schrijf mijn vragen op en stel ze gewoon. Waar ik nu sta: ik heb veel meer kennis over digitale tools, ik begrijp veel meer begrippen uit de digitale wereld en ik heb een nieuwe interesse gevonden.",
        ],
    },
}

# STARR-reflectie per leerdoel, shown inside that leerdoel's accordion on the competentie page.
# Keyed by leerdoel code ("1.1", "1.2", ...). "titel" is a short name shown at the top of the reflectie.
# The parts work like in STARR above: lists of paragraphs; leave a part out to hide it.
# A leerdoel without an entry here shows its "toelichting" (or a placeholder) instead.
LEERDOEL_STARR = {
    "1.1": {
        "titel": "Digitale onderzoeks- of ontwerpvraag formuleren",
        "situatie": [
            "Voor project 1 (Parkhaven) moesten we onderzoeken welke klimaatadaptatiemaatregelen bij de gebouwen van het masterplan konden.",
        ],
        "taak": [
            "Ik moest een onderzoeksvraag formuleren en een passende methode kiezen.",
        ],
        "actie": [
            "Ik koos voor een hittestressanalyse in ArcGIS Pro. Hiervoor hadden we eerst de gebouwen nodig. N. Morales en ik modelleerden ze in Forma, ik haalde het terrein weg in Revit en exporteerde het opnieuw als IFC. Daarna vergeleek ik de effecten van bomen, groene daken, een groene kade en alle maatregelen samen.",
        ],
        "resultaat": [
            "De omgeving wordt met alle maatregelen samen 2 graden koeler.",
        ],
        "reflectie": [
            "Ik heb geleerd dat je vraag bepaalt welke data en tool je nodig hebt.",
        ],
    },
    "1.2": {
        "titel": "Data verzamelen en interpreteren",
        "situatie": [
            "Voor project 2 (digitale fabricage) moest ik met twee groepsgenoten onderzoeken hoe de kleiprinter werkt. Dat was uitdagend. De informatie was beperkt en je weet vooraf niet precies wat je moet weten. Dat leer je pas tijdens het proces, en dat kost veel tijd.",
        ],
        "taak": [
            "Ik moest informatie verzamelen zodat onze groep kon gaan printen.",
        ],
        "actie": [
            "Ik vroeg eerst aan AI wat belangrijk is om te weten voordat je gaat printen en welke websites handig zijn. Die informatie heb ik kritisch gecontroleerd door de video's van het bedrijf achter de WASP 2040 te bekijken en door testprints te maken.",
            "Na kennisuitwisseling stelde een groepslid voor om Termite te gebruiken, een Grasshopper-plug-in waarmee je de printer kunt aansturen. Ik dook in de informatie over Termite, vond de template, keek een video en paste toe wat ik leerde. De eerste print ging niet goed door de instellingen. J. van de andere groep gaf mij hier feedback op. Ik keek de video opnieuw en de tweede print ging beter. Zo bestond het proces uit testen, bespreken wat er misging, oplossingen bedenken, toepassen en opnieuw testen.",
        ],
        "resultaat": [
            "In het begin hadden we geen idee hoe de printer werkte. Nu hebben we genoeg basiskennis om het aan een ander uit te kunnen leggen.",
        ],
        "reflectie": [
            "Ik heb geleerd dat je geduld nodig hebt en dat je door met anderen te overleggen meer ziet dan alleen. Zonder de kennisuitwisseling had ik Termite waarschijnlijk niet gevonden.",
        ],
    },
    "1.3": {
        "titel": "Digitale tools integreren en prototypen",
        "situatie": [
            "Sinds 1 oktober loop ik leerplek bij ABT, in het Oosterhoff Digital team. Mijn doel was mijn digitale skills te ontwikkelen, vooral Grasshopper en Python voor constructief ontwerp. Ik begon bijna vanuit het niets.",
        ],
        "taak": [
            "Ik moest parametrische vakwerken ontwerpen en deze koppelen aan Karamba3D en Technosoft Raamwerken.",
        ],
        "actie": [
            "Ik keek eerst een video over Grasshopper, maar die legde bijna dezelfde dingen uit als A. over lists, items en trees. Ik snapte er nog niks van. Daarom volgde ik de cursus op ThinkParametric. Die vertelde ook dezelfde dingen, maar opeens kon ik wel begrijpen wat er bedoeld werd. Daarna maakte ik een vakwerk en koppelde dat aan Karamba3D. Vervolgens maakte ik meerdere vakwerken en koppelde die aan Revit.",
        ],
        "resultaat": [
            "Ik heb een vakwerk-script gebouwd met meerdere invoerparameters en diagonale patronen, gekoppeld aan Karamba3D en Technosoft Raamwerken. Mijn begeleider noemt dit een belangrijke stap vooruit en ziet dat ik de basis vrij snel onder de knie heb gekregen.",
        ],
        "reflectie": [
            "Waar ik nu sta met Grasshopper is een groot verschil met mijn beginpunt. Ik heb veel geleerd over de verschillende componenten. Mijn begeleider adviseert om het parametrisch denken meer in gedachten te houden. Ik moet dus niet alleen nadenken over wat werkt met de huidige parameters, maar ook over hoe het script zich gedraagt als parameters wijzigen. De geometrie moet als één geheel meebewegen, invoerwaarden moeten hergebruikt worden in plaats van gedupliceerd, en het script moet makkelijk uitbreidbaar zijn.",
            "Dat wil ik verder ontwikkelen. Ik ga dat doen door bij elk nieuw script eerst te bepalen welke parameters ik wil kunnen wijzigen, het script te testen door die parameters aan te passen en bij uitbreidingen te kijken of ik het kan aanpassen zonder opnieuw te beginnen.",
        ],
    },
    "1.4": {
        "titel": "Reflecteren en valideren met stakeholders",
        "situatie": [
            "Bij het project digitale fabricage twijfelden we in de groep tussen twee ontwerpen, dat van mij en dat van R. Beide waren gebogen en de printer kan niet schuin printen.",
        ],
        "taak": [
            "We moesten een ontwerp kiezen dat we daadwerkelijk konden printen.",
        ],
        "actie": [
            "We kozen voor het ontwerp van R. Mijn ontwerp was ingewikkelder om te printen en voor de cobot. Daarnaast merkte een groepslid op dat mijn parameters niet helemaal correct waren.",
            "Toch hadden we nog steeds het probleem hoe we het gingen printen. Iemand kwam met het idee om de blokken hol te laten, zodat je de vorm van boven kunt printen. Daarna kwam iemand met het idee om pennen als verbinding te gebruiken. Ik vroeg hoe dat zou werken als de klei krimpt, want de blokken moeten precies in elkaar passen zodat ze niet vallen. Daarop kwam het idee om schuurpapier te gebruiken: passen de verbindingen niet, dan kunnen we ze zo passend maken.",
        ],
        "resultaat": [
            "Door elkaars ideeën kritisch te bekijken, kwamen we tot een oplossing die printbaar was.",
        ],
        "reflectie": [
            "Ik heb geleerd dat een ontwerp niet alleen mooi moet zijn, maar ook uitvoerbaar. Wat het groepslid zei over mijn parameters sluit aan bij het advies van mijn begeleider op mijn leerplek over parametrisch denken. Dat dezelfde feedback twee keer komt, laat zien dat ik hier echt mee moet oefenen.",
        ],
    },
    "2.1": {
        "titel": "Samenwerken in teams met digitale middelen",
        "situatie": [
            "Voor project 1 (Parkhaven) hadden we zo snel mogelijk de gebouwen van het masterplan nodig om simulaties te kunnen maken.",
        ],
        "taak": [
            "N. Morales en ik moesten de gebouwen modelleren.",
        ],
        "actie": [
            "We besloten Forma te gebruiken. Voor de efficiëntie deed ik een aantal gebouwen en zij een aantal, zodat het samen één geheel werd. Omdat ik mijn deel eerst klaar had, legde ik N. Morales uit hoe ik het precies in Forma had gedaan, zodat de gebouwen met elkaar overeen zouden komen.",
            "Ik gebruikte de overzichtstekening van het masterplan op schaal als onderlegger en speelde met de afmetingen van de hoogtes. Dat was een gepuzzel, omdat in de gegevens alleen het hoogste punt stond en niet de verdiepingen ertussen. Daarnaast exporteert Forma altijd een IFC-bestand inclusief terrein, en dat hadden we niet nodig. Daarom zette ik het eerst in Revit om het terrein weg te halen en exporteerde het daarna opnieuw als IFC voor Tygron of ArcGIS.",
        ],
        "resultaat": [
            "We hadden alle gebouwen in één model, klaar voor de simulaties.",
        ],
        "reflectie": [
            "Forma is best eenvoudig en je leert snel hoe het werkt. De samenwerking ging prima zolang we maar niet op dezelfde plek werkten. Ik heb vooral geleerd om met Forma te werken, want ik had het eerder niet gebruikt. Ik wil mij verder ontwikkelen in de omgevingstools en de analyses die Forma zelf maakt.",
        ],
    },
    "2.2": {
        "titel": "Helder communiceren van bevindingen",
        "situatie": [
            "Voor project Parkhaven moesten we aan de bedrijven achter het masterplan onze resultaten presenteren, om te kijken welke klimaatadaptatiemaatregelen bij de gebouwen konden.",
        ],
        "taak": [
            "Ik presenteerde de hittestressanalyse ten opzichte van groen. We moesten onze bevindingen helder en doelgroepgericht overbrengen.",
        ],
        "actie": [
            "De presentatie is niet goed verlopen. Een feedbackpunt dat mij bijbleef, kwam van de gastbezoeker: waar willen we naartoe met al deze informatie? Dat ontstond door de samenwerking. We wilden met de resultaten meer doen, maar niet iedereen werkte effectief en dus kregen we tijdstekort. Zo ging een deel van de presentatie over soorten bomen. Ik vroeg mij af wat dat met digitale tools te maken had, want dat was niet wat we hadden afgesproken. Ook werkte de presentatie niet op de laptop, en wisselen van laptop was niet gepland.",
        ],
        "resultaat": [
            "Doordat minder mensen werkten, konden we geen mooi geheel maken van onze bevindingen. Dat had invloed op hoe we ze communiceerden.",
        ],
        "reflectie": [
            "We hadden gesproken met de personen die niet werkten, maar dat hielp niet. Als ik nu zie dat iemand niets doet, meld ik dat direct bij de docenten. Ik had mijn eigen onderdeel ook kunnen afsluiten met een conclusie en een vervolgstap, zodat de vraag waar we naartoe willen beantwoord was.",
        ],
    },
    "2.3": {
        "titel": "Netwerken en kennisdeling",
        "situatie": [
            "Ik ben naar de Prefab Beurs gegaan, waar veel bedrijven hun producten kwamen uitleggen. Ook heb ik meegedaan aan het inspiratie-event voor afstuderen.",
        ],
        "taak": [
            "Ik wilde mijn professionele netwerk opbouwen.",
        ],
        "actie": [
            "Op de Prefab Beurs vroeg ik bedrijven mijn QR-code te scannen, zodat ze hun contactgegevens of productinformatie konden sturen. Ik vertelde ook dat ik de minor Digitaliseren volg en dat ik daar erg in geïnteresseerd ben. Bij het inspiratie-event sprak ik met een aantal bedrijven en vertelde ik wat ik in mijn minor heb geleerd.",
        ],
        "resultaat": [
            "Ik kreeg contactgegevens en volgde de bedrijven op Instagram of LinkedIn. Het netwerk leverde vooral inzicht in wat anderen in de praktijk met digitaliseren doen. Ik kreeg veel kennis en nieuwe interesses in het bouwen van digitale tools.",
        ],
        "reflectie": [
            "Digitaliseren in de gebouwde omgeving is heel anders dan wat ik gewend ben, en juist dat vind ik inspirerend. Het is echt een hot topic bij bedrijven. Dat heeft mij geïnspireerd om dieper in digitaliseren te duiken.",
        ],
    },
    "3.1": {
        "titel": "Persoonlijke leerdoelen en bijsturen",
        "situatie": [
            "Een van mijn persoonlijke leerdoelen was: “Ik kan een basis Python-script schrijven dat een handige tool is voor een bouwopdracht en mij efficiënter laat werken.” Recent merkte ik dat ik hier niets mee had gedaan. Het was het enige leerdoel waar ik niet aan werkte.",
        ],
        "taak": [
            "Ik moest mijn leerdoel weer oppakken. Dat sluit aan bij een ander leerdoel van mij: tijdig bijsturen als ik vastloop, in plaats van te stoppen en af te wachten.",
        ],
        "actie": [
            "Ik ging in gesprek met mijn begeleider en vertelde dat ik Python opzij had gelaten. Hij stuurde mij een aantal video's. Daarna gaf hij mij de opdracht om hetzelfde vakwerk dat ik in Grasshopper had gemaakt opnieuw te maken, nu met de ingebouwde Python in Grasshopper.",
        ],
        "resultaat": [
            "Ik heb het vakwerk in Python gebouwd. Mijn begeleider merkte op dat ik dit heel snel heb gedaan en noemt mijn ontwikkeling veelbelovend.",
        ],
        "reflectie": [
            "Ik heb geleerd dat ik een leerdoel dat blijft liggen sneller moet bespreken. Mijn begeleider adviseert bij Python te letten op structuur en overzichtelijkheid van de code, vooral variabelenamen en opmerkingen. Dat helpt mij later bij het terugkijken.",
            "Mijn leerdoel is nog niet helemaal behaald, want ik heb een vakwerk gebouwd, maar nog geen tool die mij efficiënter laat werken. Mijn volgende stap is een klein script dat een terugkerende handeling in mijn werk automatiseert.",
        ],
    },
    "3.2": {
        "titel": "Zelflerende houding",
        "situatie": [
            "Voor mijn leerplek had ik als doel Grasshopper en Python te leren.",
        ],
        "taak": [
            "Ik wilde beide zelf eigen maken.",
        ],
        "actie": [
            "Voor Grasshopper begon ik met cursussen op ThinkParametric. Daarna maakte ik een opdracht van mijn begeleider, waarin ik vakwerken maakte en deze koppelde aan Karamba en Technosoft. Voor Python gebruikte ik de ingebouwde Python in Grasshopper om een vakwerk te maken. Bij beide zocht ik eerst zelf uit en stelde ik vragen als ik vastliep.",
        ],
        "resultaat": [
            "Mijn begeleider ziet een positieve houding ten opzichte van leren en uitproberen. Hij zegt dat ik oprecht geïnteresseerd lijk in digitale vaardigheden, advies opvolg en best zelfstandig werk.",
        ],
        "reflectie": [
            "Ik heb echt een zelfstandige houding. Ik hou van zelf uitzoeken en oplossen. Mijn begeleider adviseert om meer vragen te stellen en aan te geven of ik iets nieuws of anders wil zien of uitproberen. Dat ben ik met hem eens. Daarom ga ik mijn vragen opschrijven en ze niet meer direct zelf opzoeken, maar gewoon stellen.",
        ],
    },
    "3.3": {
        "titel": "Zelfstandig nieuwe tools eigen maken",
        "situatie": [
            "Voor project 2 ontdekte ik een template die gekoppeld is aan de kleiprinter. Op mijn leerplek leerde ik daarnaast zelfstandig nieuwe tools.",
        ],
        "taak": [
            "Ik wilde deze tools toepassen in mijn projecten en op mijn leerplek.",
        ],
        "actie": [
            "Dankzij mijn Grasshopper-kennis kon ik de printer-template makkelijk gebruiken. Voor de template heb je een vorm nodig die je koppelt, en het maken en aanpassen van die vorm in Rhino duurde mij langer. Karamba leerde ik via een cursus op ThinkParametric. Daarna bouwde ik zelfstandig mijn vakwerken op en paste toe wat ik van Karamba had geleerd. Ook Python leerde ik en paste ik toe in de ingebouwde Python in Grasshopper, waardoor ik een vakwerk met alleen Python kon bouwen.",
        ],
        "resultaat": [
            "Ik kan nu zelfstandig tools oppakken en toepassen. Mijn begeleider noemt mij bereid om dingen zelf verder te ontwikkelen.",
        ],
        "reflectie": [
            "Ik heb Grasshopper geleerd maar Rhino niet echt, waardoor ik soms niet weet hoe ik iets in Rhino moet doen. Ook al kun je veel met Grasshopper, soms moet je Rhino volledig gebruiken. Daarom wil ik mijn Rhino-skills aanscherpen door YouTube-video's te kijken en een oefenopdracht te doen. Voor januari maak ik een kleine Rhino-opdracht.",
        ],
    },
    "4.1": {
        "titel": "Professioneel handelen",
        "situatie": [
            "Volgens de minor betekent professioneel handelen dat je werkt aan een complex vraagstuk waarvan de oplossing nog onbekend is en waarbij samenwerken noodzakelijk is. Dat herken ik in project 2 (digitale fabricage): we wisten niet hoe de kleiprinter werkte en moesten dat samen uitzoeken. Daarnaast loop ik sinds 1 oktober leerplek bij ABT, in het Oosterhoff Digital team.",
        ],
        "taak": [
            "Ik wilde in deze situaties professioneel handelen. Ik licht drie kenmerken uit het model uit: interactief leervermogen, effectief samenwerken en verbeter- of vernieuwingsgericht werken.",
        ],
        "actie": [
            "Interactief leervermogen: toen ik merkte dat ik niets met Python had gedaan, besprak ik dit met mijn begeleider en stelde ik mijn leerdoel bij. Ik volg zijn adviezen op.",
            "Effectief samenwerken: bij Parkhaven legde ik N. Morales uit hoe ik in Forma had gewerkt, zodat onze gebouwen met elkaar overeen zouden komen. Ik bouwde ook mijn netwerk op bij de Prefab Beurs en het inspiratie-event.",
            "Verbeter- of vernieuwingsgericht: bij de kleiprinter experimenteerde ik met de Termite-template en testprints en paste ik mijn aanpak aan na feedback.",
        ],
        "resultaat": [
            "Mijn begeleider noemt mij een prettige collega die goed in het team past en in een goed tempo ontwikkelt. Hij ziet een positieve houding en dat ik adviezen opvolg en best zelfstandig werk.",
        ],
        "reflectie": [
            "Ik heb geleerd dat professioneel handelen niet alleen techniek is, maar ook feedback vragen, kennis delen en samenwerken. Mijn begeleider adviseert om meer vragen te stellen, dus ik ga mijn vragen opschrijven en ze gewoon stellen.",
            "Waar ik nu sta: ik heb veel meer kennis over digitale tools, ik begrijp veel meer begrippen uit de digitale wereld en ik heb een nieuwe interesse gevonden.",
        ],
    },
}

# The five STARR parts, in the order shown: key in STARR, letter on the badge, heading.
STARR_PARTS = [
    ("situatie", "S", "Situatie"),
    ("taak", "T", "Taak"),
    ("actie", "A", "Actie"),
    ("resultaat", "R", "Resultaat"),
    ("reflectie", "R", "Reflectie"),
]

# Placeholder case-study text, used for any of these fields a project leaves out.
CONTENT_DEFAULTS = {
    "challenge": "Beschrijf de ontwerp- of onderzoeksvraag. Wat moest er worden opgelost, voor wie en binnen welke randvoorwaarden?",
    "process": "Licht je aanpak toe: analyse, ontwerpvarianten, berekeningen, prototypes en de keuzes die je onderweg maakte.",
    "steps": ["Analyse en onderzoek", "Ontwerp en modellering", "Uitwerking, testen en evaluatie"],
    "result": "Laat het eindresultaat zien, wat je hebt geleerd en wat je een volgende keer anders zou doen.",
    "caption": "Bijschrift bij de afbeelding.",
}

# ---------------------------------------------------------------------------
# Lookups and validation

COMP_BY_NUMBER = {c["number"]: c for c in COMPETENTIES}
def leerdoel_parts(entry):
    """A leerdoel is plain text, or {"text": ..., "toelichting": ...} with an explanation."""
    if isinstance(entry, dict):
        return entry["text"], entry.get("toelichting", "")
    return entry, ""


LEERDOELEN = {  # "1.2" -> (competentie, text, toelichting)
    f"{c['number']}.{i}": (c, *leerdoel_parts(entry))
    for c in COMPETENTIES
    for i, entry in enumerate(c["leerdoelen"], start=1)
}

for _p in PROJECTS:
    for _code in _p["leerdoelen"]:
        if _code not in LEERDOELEN:
            raise SystemExit(f"error: project '{_p['slug']}' refers to unknown leerdoel {_code}")
    for _tag in _p["tags"]:
        if _tag not in TAGS:
            raise SystemExit(f"error: project '{_p['slug']}' refers to unknown tag '{_tag}'")
    for _key in _p.get("feedback", []):
        if _key not in FEEDBACK:
            raise SystemExit(f"error: project '{_p['slug']}' refers to unknown feedback '{_key}'")
    for _step in _p.get("details", []):
        for _m in _step.get("media", []):
            for _field, _folder in (("image", "images"), ("video", "videos"), ("poster", "images")):
                if _m.get(_field) and not os.path.exists(os.path.join(ROOT, _folder, _m[_field])):
                    raise SystemExit(f"error: project '{_p['slug']}' uses {_folder}/{_m[_field]}, which does not exist")
            if (_m.get("image") or _m.get("video")) and not _m.get("alt") and not _m.get("caption"):
                raise SystemExit(f"error: project '{_p['slug']}' has a picture or video without alt text or caption in '{_step['title']}'")
for _number in STARR:
    if _number not in COMP_BY_NUMBER:
        raise SystemExit(f"error: STARR has a reflectie for competentie '{_number}', which does not exist")
for _code in LEERDOEL_STARR:
    if _code not in LEERDOELEN:
        raise SystemExit(f"error: LEERDOEL_STARR has a reflectie for leerdoel '{_code}', which does not exist")

MONTHS = ["januari", "februari", "maart", "april", "mei", "juni",
          "juli", "augustus", "september", "oktober", "november", "december"]


def parse_month(value, where):
    try:
        year, month = (int(n) for n in value.split("-"))
        if not 1 <= month <= 12:
            raise ValueError
    except ValueError:
        raise SystemExit(f"error: {where} has date '{value}'; use \"YYYY-MM\", e.g. \"2026-10\"")
    return year, month


def format_month(value):
    """ "2026-10" -> "oktober 2026" """
    year, month = parse_month(value, "a date")
    return f"{MONTHS[month - 1]} {year}"


for _p in PROJECTS:
    parse_month(_p["date"], f"project '{_p['slug']}'")
parse_month(TIMELINE["start"], "TIMELINE start")
parse_month(TIMELINE["end"], "TIMELINE end")


def comp_of(code):
    return LEERDOELEN[code][0]


def projects_for(comp):
    return [p for p in PROJECTS if any(comp_of(code) is comp for code in p["leerdoelen"])]


def codes_for(p, comp):
    return [code for code in p["leerdoelen"] if comp_of(code) is comp]


def comps_of(p):
    result = []
    for code in p["leerdoelen"]:
        if comp_of(code) not in result:
            result.append(comp_of(code))
    return result


def plural(n, one, many):
    return f"{n} {one if n == 1 else many}"


# ---------------------------------------------------------------------------
# Shared markup


def page(*, title, description, prefix, body, current=None):
    def link(href, label, key):
        aria = ' aria-current="page"' if current == key else ""
        return f'<li><a class="nav__link" href="{prefix}{href}"{aria}>{label}</a></li>'

    def disabled_link(label, key, tooltip="Binnenkort beschikbaar"):
        """A menu item that looks disabled: not a link, with a tooltip on hover, focus or tap."""
        tip = f"nav-tooltip-{key}"
        return (f'<li class="nav__item nav__item--disabled">'
                f'<span class="nav__link nav__link--disabled" role="link" aria-disabled="true" tabindex="0" aria-describedby="{tip}">{label}</span>'
                f'<span class="nav__tooltip" id="{tip}" role="tooltip">{tooltip}</span></li>')

    return f"""<!DOCTYPE html>
<html lang="nl" class="no-js">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description)}">

  <link rel="stylesheet" href="{prefix}css/variables.css">
  <link rel="stylesheet" href="{prefix}css/base.css">
  <link rel="stylesheet" href="{prefix}css/style.css">
  <script src="{prefix}js/main.js" defer></script>
  <script>
    /* Apply a saved light/dark choice before the page is drawn, to avoid a flash */
    try {{
      var savedTheme = localStorage.getItem("theme");
      if (savedTheme === "light" || savedTheme === "dark") document.documentElement.dataset.theme = savedTheme;
    }} catch (e) {{}}
  </script>
</head>
<body>
  <a class="skip-link" href="#main">Direct naar de inhoud</a>

  <header class="site-header">
    <div class="container site-header__inner">
      <a class="site-header__logo" href="{prefix}index.html" aria-label="Shena, terug naar home">Shena</a>

      <nav class="nav" aria-label="Hoofdmenu">
        <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="nav-list">
          <span class="nav__toggle-icon" aria-hidden="true"></span>
          Menu
        </button>
        <ul class="nav__list" id="nav-list">
          {link("index.html#home", "Home", "home")}
          {link("index.html#competenties", "Competenties", "competenties")}
          {disabled_link("Reflectie", "reflectie")}
          {link("index.html#contact", "Contact", "contact")}
        </ul>
      </nav>

      <button class="theme-toggle" type="button" aria-pressed="false" data-theme-toggle hidden>
        <svg class="theme-toggle__icon theme-toggle__icon--sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
          <circle cx="12" cy="12" r="4.5"/>
          <path d="M12 1.5v3M12 19.5v3M1.5 12h3M19.5 12h3M4.6 4.6l2.1 2.1M17.3 17.3l2.1 2.1M4.6 19.4l2.1-2.1M17.3 6.7l2.1-2.1"/>
        </svg>
        <svg class="theme-toggle__icon theme-toggle__icon--moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
          <path d="M20.5 14.5A8.5 8.5 0 0 1 9.5 3.5a8.5 8.5 0 1 0 11 11z"/>
        </svg>
        <span class="visually-hidden">Lichte modus</span>
      </button>
    </div>
  </header>

  <main id="main">
{body}
  </main>

  <footer class="site-footer">
    <div class="container site-footer__inner">
      <p>&copy; <span data-year>2026</span> Shena. Alle rechten voorbehouden.</p>
      <p><a href="{prefix}index.html">Terug naar home</a></p>
    </div>
  </footer>
</body>
</html>
"""


def tag_list(p):
    if not p["tags"]:
        return ""
    tags = "\n".join(f'                  <li class="tag">{escape(TAGS[t])}</li>' for t in p["tags"])
    return f"""                <ul class="tag-list" aria-label="Tags">
{tags}
                </ul>"""


def picsum(seed, width, height):
    """Stand-in photo from picsum.photos; the seed keeps the same photo on every load."""
    return f"https://picsum.photos/seed/{seed}/{width}/{height}"


def image_src(p, prefix, width, height):
    """A project's own image (file in images/ or a full URL), or a Picsum stand-in."""
    image = p.get("image")
    if not image:
        return picsum(f"shena-{p['slug']}", width, height)
    if image.startswith(("http://", "https://")):
        return image
    return f"{prefix}images/{image}"


def card_image(p, prefix):
    # Decorative here: the card title already names the project
    src = image_src(p, prefix, 800, 500)
    return f'<img src="{escape(src)}" alt="" width="800" height="500" loading="lazy">'


def project_card(p, prefix, comp):
    codes = ", ".join(codes_for(p, comp))
    label = "Leerdoel" if len(codes_for(p, comp)) == 1 else "Leerdoelen"
    return f"""          <li class="reveal">
            <article class="project-card">
              <div class="project-card__media">
                {card_image(p, prefix)}
              </div>
              <div class="project-card__body">
                <h3 class="project-card__title">
                  <a class="project-card__link" href="{prefix}projects/{p['slug']}.html">{escape(p['title'])}</a>
                </h3>
{tag_list(p)}
                <p class="project-card__description">{escape(p['lead'])}</p>
                <p class="project-card__leerdoelen">{label} {codes}</p>
                <p class="project-card__cta" aria-hidden="true">Bekijk project &rarr;</p>
              </div>
            </article>
          </li>"""


def competentie_card(c):
    counts = f"{plural(len(c['leerdoelen']), 'leerdoel', 'leerdoelen')} · {plural(len(projects_for(c)), 'project', 'projecten')}"
    return f"""          <li class="reveal">
            <article class="project-card theme-card">
              <div class="project-card__body">
                <p class="theme-card__number" aria-hidden="true">{c['number']}</p>
                <p class="theme-card__label">Competentie {c['number']}</p>
                <h3 class="project-card__title">
                  <a class="project-card__link" href="competenties/{c['slug']}.html">{escape(c['name'])}</a>
                </h3>
                <p class="theme-card__count">{counts}</p>
                <p class="project-card__cta" aria-hidden="true">Bekijk competentie &rarr;</p>
              </div>
            </article>
          </li>"""


def write(rel, content):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", rel)


# ---------------------------------------------------------------------------
# Pages


def hero_title():
    """Escapes the title, turns *words* into the accent-coloured span and \\n into a line break."""
    parts = escape(SITE["hero_title"]).split("*")
    html = "".join(
        f'<span class="hero__title-accent">{part}</span>' if i % 2 else part
        for i, part in enumerate(parts)
    )
    return html.replace("\n", "<br>")


def hero_image_src():
    image = SITE.get("hero_image")
    if not image:
        return picsum("shena-hero", 800, 1000)
    if image.startswith(("http://", "https://")):
        return image
    return f"images/{image}"


def contact_items():
    def item(label, href, text, external=False):
        new_tab = ' rel="noopener noreferrer" target="_blank"' if external else ""
        hint = '<span class="visually-hidden"> (opent in een nieuw tabblad)</span>' if external else ""
        return f"""            <li class="contact__item reveal">
              <span class="contact__label">{label}</span>
              <a class="contact__value" href="{escape(href)}"{new_tab}>{escape(text)}{hint}</a>
            </li>"""

    def short(url):
        for prefix in ("https://", "http://", "www."):
            url = url.removeprefix(prefix) if url.startswith(prefix) else url
        return url.rstrip("/")

    items = []
    if SITE.get("email"):
        items.append(item("E-mail", f"mailto:{SITE['email']}", SITE["email"]))
    if SITE.get("phone"):
        items.append(item("Telefoon", "tel:" + SITE["phone"].replace(" ", ""), SITE["phone"]))
    if SITE.get("linkedin"):
        items.append(item("LinkedIn", SITE["linkedin"], SITE.get("linkedin_label") or short(SITE["linkedin"]), external=True))
    if SITE.get("github"):
        items.append(item("GitHub", SITE["github"], short(SITE["github"]), external=True))
    return "\n".join(items)


def build_index():
    cards = "\n\n".join(competentie_card(c) for c in COMPETENTIES)
    body = f"""    <!-- Hero -->
    <section class="hero" id="home" aria-labelledby="hero-title">
      <div class="container hero__inner">
        <div class="hero__content">
          <p class="hero__greeting">{escape(SITE['hero_greeting'])}</p>
          <h1 class="hero__title" id="hero-title">
            {hero_title()}
          </h1>
          <p class="hero__text">
            {escape(SITE['hero_text'])}
          </p>
          <div class="hero__actions">
            <a class="button button--primary" href="#competenties">Bekijk mijn werk</a>
            <span class="has-tooltip">
              <span class="button button--outline button--disabled" role="link" aria-disabled="true" tabindex="0" aria-describedby="hero-tooltip-reflectie">Reflectie</span>
              <span class="tooltip" id="hero-tooltip-reflectie" role="tooltip">Binnenkort beschikbaar</span>
            </span>
          </div>
        </div>
        <figure class="hero__image">
          <img src="{escape(hero_image_src())}" alt="{escape(SITE['hero_image_alt'])}" width="800" height="1000">
        </figure>
      </div>
    </section>

    <!-- Competenties overview -->
    <section class="section" id="competenties" aria-labelledby="competenties-title">
      <div class="container">
        <p class="section__eyebrow">Mijn werk</p>
        <h2 id="competenties-title">Competenties</h2>
        <p class="section__intro">Mijn portfolio is opgebouwd rond vier competenties. Kies een competentie om de leerdoelen en de bijbehorende projecten te bekijken.</p>

        <ul class="project-grid theme-grid">
{cards}
        </ul>
      </div>
    </section>

{timeline()}

    <!-- Contact -->
    <section class="section contact" id="contact" aria-labelledby="contact-title">
      <div class="container">
        <p class="section__eyebrow">Contact</p>
        <h2 id="contact-title">Laten we samenwerken</h2>
        <p class="section__intro">Op zoek naar een stagiair, een samenwerking of gewoon benieuwd naar mijn werk? Neem gerust contact op.</p>

        <address>
          <ul class="contact__list">
{contact_items()}
          </ul>
        </address>
      </div>
    </section>"""
    html = page(
        title="Shena | Portfolio bouwkunde",
        description="Portfolio van Shena, student bouwkunde, opgebouwd rond vier competenties.",
        prefix="", body=body,
    )
    # The home page links to its own sections
    html = html.replace('href="index.html#', 'href="#')
    write("index.html", html)


def diagram_figure(c):
    d = c.get("diagram")
    # No placeholder: the diagram only appears once a real image is set
    if not d or not d.get("image"):
        return ""
    return f"""
        <figure class="project-detail__image competentie-diagram">
          <img src="../images/{escape(d["image"])}" alt="{escape(d["alt"])}">
          <figcaption>{escape(d['caption'])}</figcaption>
        </figure>"""


TOELICHTING_PLACEHOLDER = "Licht toe hoe je dit leerdoel hebt aangetoond en wat je ervan hebt geleerd."


def leerdoel_accordion_item(code):
    """One leerdoel as a <details> accordion: explanation plus the projects that demonstrate it."""
    _, text, toelichting = LEERDOELEN[code]
    projects = [p for p in PROJECTS if code in p["leerdoelen"]]
    if projects:
        links = "\n".join(
            f'                <li><a href="../projects/{p["slug"]}.html">{escape(p["title"])}</a></li>'
            for p in projects
        )
        projects_html = f"""              <p class="leerdoel-accordion__label">Aangetoond in</p>
              <ul class="leerdoel-accordion__projects">
{links}
              </ul>"""
    else:
        projects_html = '              <p class="leerdoel-accordion__empty">Nog geen projecten gekoppeld aan dit leerdoel.</p>'
    starr = LEERDOEL_STARR.get(code)
    if starr:
        # STARR-reflectie for this leerdoel; ids get the code, as all accordions share one page
        title = f'\n                <p class="leerdoel-starr__titel">{escape(starr["titel"])}</p>' if starr.get("titel") else ""
        steps = starr_steps(starr, f"starr-{code.replace('.', '-')}", "h3", "                ", "leerdoel-starr__step")
        explanation = f"""              <div class="leerdoel-starr">{title}
{steps}
              </div>"""
    else:
        explanation = f"              <p>{escape(toelichting or TOELICHTING_PLACEHOLDER)}</p>"
    return f"""          <li>
            <details class="leerdoel leerdoel-accordion" id="leerdoel-{code.replace('.', '-')}">
              <summary class="leerdoel-accordion__summary">
                <span class="leerdoel__code">{code}</span>
                <span class="leerdoel__text">{escape(text)}</span>
                <span class="leerdoel-accordion__icon" aria-hidden="true"></span>
              </summary>
              <div class="leerdoel-accordion__body">
{explanation}
{projects_html}
              </div>
            </details>
          </li>"""


def starr_steps(starr, id_prefix, tag, indent, extra_class="starr__step"):
    """The STARR parts of one reflectie as <section>s with a letter badge; empty parts are left out."""
    steps = []
    for key, letter, heading in STARR_PARTS:
        if not starr.get(key):
            continue
        paragraphs = "\n".join(f"{indent}  <p>{escape(par)}</p>" for par in starr[key])
        steps.append(f"""{indent}<section class="star-step {extra_class}" aria-labelledby="{id_prefix}-{key}-title">
{indent}  <{tag} class="star-step__title" id="{id_prefix}-{key}-title"><span class="star-step__letter" aria-hidden="true">{letter}</span> {heading}</{tag}>
{paragraphs}
{indent}</section>""")
    return "\n\n".join(steps)


def link_leerdoel_codes(text, c):
    """Escape text and turn each known leerdoel code ("1.2") into a link to its accordion.
    Codes of this competentie link within the page; other codes link to their own competentie page."""
    def link(match):
        code = match.group(0)
        if code not in LEERDOELEN:
            return code
        target = comp_of(code)
        page_ = "" if target is c else f"{target['slug']}.html"
        return f'<a class="starr__leerdoel-link" href="{page_}#leerdoel-{code.replace(".", "-")}" aria-label="Leerdoel {code}">{code}</a>'
    return re.sub(r"(?<![\d.])\d+\.\d+(?![\d.])", link, escape(text))


def starr_section(c):
    """The competentie's STARR-reflectie (from STARR), or nothing if it has none."""
    starr = STARR.get(c["number"])
    if not starr:
        return ""
    intro = f'\n        <p class="starr__leerdoelen">{link_leerdoel_codes(starr["leerdoelen"], c)}</p>' if starr.get("leerdoelen") else ""
    steps_html = starr_steps(starr, "starr", "h3", "        ")
    return f"""
      <section class="starr" id="starr" aria-labelledby="starr-title">
        <h2 id="starr-title">STARR-reflectie</h2>{intro}

{steps_html}
      </section>
"""


def competentie_toc(c):
    """The sticky "Op deze pagina" menu on a competentie page, linking to each section below."""
    def item(href, label, sub=""):
        return f'          <li class="toc__item"><a class="toc__link" href="#{href}">{escape(label)}</a>{sub}</li>'

    def sublist(links):
        rows = "\n".join(
            f'              <li><a class="toc__link toc__link--sub" href="#{href}">{escape(label)}</a></li>'
            for href, label in links
        )
        return f'\n            <ol class="toc__sublist">\n{rows}\n            </ol>\n          '

    leerdoelen = []
    for i in range(1, len(c["leerdoelen"]) + 1):
        code = f"{c['number']}.{i}"
        titel = (LEERDOEL_STARR.get(code) or {}).get("titel")
        leerdoelen.append((f"leerdoel-{code.replace('.', '-')}", f"{code} {titel}" if titel else f"Leerdoel {code}"))
    items = [item("leerdoelen", "Leerdoelen", sublist(leerdoelen))]
    starr = STARR.get(c["number"])
    if starr:
        steps = [(f"starr-{key}-title", heading) for key, _, heading in STARR_PARTS if starr.get(key)]
        items.append(item("starr", "STARR-reflectie", sublist(steps)))
    items.append(item("projecten", "Projecten"))
    items.append(item("andere-competenties", "Andere competenties"))
    rows = "\n".join(items)
    return f"""      <nav class="toc" aria-labelledby="toc-title" data-toc>
        <h2 class="toc__title" id="toc-title">Op deze pagina</h2>
        <ol class="toc__list">
{rows}
        </ol>
      </nav>"""


def build_competentie(c):
    prefix = "../"
    leerdoelen = "\n".join(
        leerdoel_accordion_item(f"{c['number']}.{i}") for i in range(1, len(c["leerdoelen"]) + 1)
    )
    projects = projects_for(c)
    if projects:
        cards = "\n\n".join(project_card(p, prefix, c) for p in projects)
        project_html = f"""        <ul class="project-grid">
{cards}
        </ul>"""
    else:
        project_html = '        <p class="section__intro">Er zijn nog geen projecten aan deze competentie gekoppeld.</p>'
    others = "\n".join(
        f'          <li><a class="button button--outline" href="{o["slug"]}.html">Competentie {o["number"]}</a></li>'
        for o in COMPETENTIES if o is not c
    )
    body = f"""    <div class="container">
      <nav class="breadcrumb" aria-label="Kruimelpad">
        <ol>
          <li><a href="../index.html">Home</a></li>
          <li><a href="../index.html#competenties">Competenties</a></li>
          <li><span aria-current="page">Competentie {c['number']}</span></li>
        </ol>
      </nav>

      <header class="theme-header">
        <p class="section__eyebrow">Competentie {c['number']}</p>
        <h1>{escape(c['name'])}</h1>
      </header>

      <div class="competentie-layout">
{competentie_toc(c)}

      <div class="competentie-layout__content">
      <section class="leerdoelen" id="leerdoelen" aria-labelledby="leerdoelen-title">
        <h2 id="leerdoelen-title">Leerdoelen</h2>
        <ol class="leerdoel-list">
{leerdoelen}
        </ol>{diagram_figure(c)}
      </section>
{starr_section(c)}
      <section class="competentie-projects" id="projecten" aria-labelledby="projects-title">
        <h2 id="projects-title">Projecten</h2>
{project_html}
      </section>

      <nav class="theme-nav" id="andere-competenties" aria-labelledby="other-title">
        <h2 class="theme-nav__title" id="other-title">Andere competenties</h2>
        <ul class="theme-nav__list">
{others}
        </ul>
      </nav>
      </div>
      </div>
    </div>"""
    write(f"competenties/{c['slug']}.html", page(
        title=f"Competentie {c['number']}: {c['name']} | Shena",
        description=f"Leerdoelen en projecten van Shena voor competentie {c['number']}: {c['name']}.",
        prefix=prefix, body=body, current="competenties",
    ))


def detail_image(p):
    src = image_src(p, "../", 1200, 675)
    alt = p.get("image_alt") if p.get("image") else "Voorbeeldfoto (placeholder)"
    return f'<img src="{escape(src)}" alt="{escape(alt or "")}" width="1200" height="675">'


def paragraphs(value):
    """A text field as <p>s: one string, or a list of strings (one per paragraph)."""
    items = [value] if isinstance(value, str) else value
    return "\n            ".join(f"<p>{escape(t)}</p>" for t in items)


def media_item(m):
    """One picture, video or video link inside a "Werk in detail" step."""
    caption = f"\n                  <figcaption>{escape(m['caption'])}</figcaption>" if m.get("caption") else ""
    if m.get("image"):
        return f"""                <figure class="project-media__item">
                  <img src="../images/{escape(m['image'])}" alt="{escape(m.get('alt', ''))}" loading="lazy">{caption}
                </figure>"""
    if m.get("video"):
        poster = f' poster="../images/{escape(m["poster"])}"' if m.get("poster") else ""
        label = f' aria-label="{escape(m["alt"])}"' if m.get("alt") else ""
        return f"""                <figure class="project-media__item project-media__item--video">
                  <video controls preload="none" playsinline{poster}{label}>
                    <source src="../videos/{escape(m['video'])}" type="video/mp4">
                    <a href="../videos/{escape(m['video'])}">Download de video</a>
                  </video>{caption}
                </figure>"""
    return f"""                <p class="project-media__link"><a href="{escape(m['url'])}" rel="noopener noreferrer" target="_blank">{escape(m.get('label', 'Bekijk de video'))}<span class="visually-hidden"> (opent in een nieuw tabblad)</span></a></p>"""


def detail_steps(p):
    """The optional "Werk in detail" section: steps with text, labelled points and media."""
    if not p.get("details"):
        return ""
    steps = []
    for i, step in enumerate(p["details"], start=1):
        sid = f"detail-{i}-title"
        date = f'\n              <p class="project-step__date">{escape(step["date"])}</p>' if step.get("date") else ""
        text = "".join(f"\n              <p>{escape(t)}</p>" for t in step.get("text", []))
        points = ""
        if step.get("points"):
            rows = "\n".join(
                f"""                <div>
                  <dt>{escape(label)}</dt>
                  <dd>{escape(value)}</dd>
                </div>"""
                for label, value in step["points"]
            )
            points = f'\n              <dl class="project-step__points">\n{rows}\n              </dl>'
        media = ""
        if step.get("media"):
            items = "\n".join(media_item(m) for m in step["media"])
            media = f'\n              <div class="project-media">\n{items}\n              </div>'
        steps.append(f"""            <section class="project-step" aria-labelledby="{sid}">
              <h3 id="{sid}">{escape(step['title'])}</h3>{date}{text}{points}{media}
            </section>""")
    body = "\n\n".join(steps)
    return f"""
          <section class="project-details" aria-labelledby="details-title">
            <h2 id="details-title">Werk in detail</h2>
{body}
          </section>
"""


def feedback_section(p):
    """Feedback from FEEDBACK that this project links to."""
    if not p.get("feedback"):
        return ""
    items = []
    for key in p["feedback"]:
        f = FEEDBACK[key]
        paras = "\n".join(f"                <p>{escape(t)}</p>" for t in f["paragraphs"])
        meta = ", ".join(x for x in (f.get("from"), f.get("date")) if x)
        items.append(f"""            <figure class="feedback">
              <h3 class="feedback__title">{escape(f['title'])}</h3>
              <blockquote class="feedback__quote">
{paras}
              </blockquote>
              <figcaption class="feedback__from">{escape(meta)}</figcaption>
            </figure>""")
    body = "\n\n".join(items)
    return f"""
          <section class="project-feedback" aria-labelledby="feedback-title">
            <h2 id="feedback-title">Feedback</h2>
{body}
          </section>
"""


def build_project(p):
    c = {**CONTENT_DEFAULTS, **p}
    steps = "\n".join(f"              <li>{escape(s)}</li>" for s in c["steps"])
    steps_html = f"\n            <ul>\n{steps}\n            </ul>" if c["steps"] else ""
    comp = comp_of(p["leerdoelen"][0])  # primary competentie drives breadcrumb and navigation
    siblings = projects_for(comp)
    nxt = siblings[(siblings.index(p) + 1) % len(siblings)]
    next_link = (
        f'\n        <a class="button button--primary" href="{nxt["slug"]}.html">Volgende: {escape(nxt["title"])} &rarr;</a>'
        if nxt is not p else ""
    )
    comp_links = ", ".join(
        f'<a href="../competenties/{x["slug"]}.html">Competentie {x["number"]}</a>' for x in comps_of(p)
    )
    leerdoelen = "\n".join(
        f"""            <li class="leerdoel">
              <a class="leerdoel__code" href="../competenties/{comp_of(code)['slug']}.html" aria-label="Leerdoel {code}, competentie {comp_of(code)['number']}">{code}</a>
              <p class="leerdoel__text">{escape(LEERDOELEN[code][1])}</p>
            </li>"""
        for code in sorted(p["leerdoelen"], key=code_key)
    )
    body = f"""    <div class="container container--narrow">
      <nav class="breadcrumb" aria-label="Kruimelpad">
        <ol>
          <li><a href="../index.html">Home</a></li>
          <li><a href="../index.html#competenties">Competenties</a></li>
          <li><a href="../competenties/{comp['slug']}.html">Competentie {comp['number']}</a></li>
          <li><span aria-current="page">{escape(p['title'])}</span></li>
        </ol>
      </nav>

      <article class="project-detail">
        <header class="project-detail__header">
          <p class="section__eyebrow">Project</p>
          <h1>{escape(p['title'])}</h1>
          <p class="project-detail__lead">{escape(p['lead'])}</p>
{tag_list(p)}

          <dl class="project-detail__meta">
            <div>
              <dt>Rol</dt>
              <dd>{escape(p['role'])}</dd>
            </div>
            <div>
              <dt>Periode</dt>
              <dd>{format_month(p['date'])}</dd>
            </div>
            <div>
              <dt>Software &amp; tools</dt>
              <dd>{escape(p['tools'])}</dd>
            </div>
            <div>
              <dt>Competenties</dt>
              <dd>{comp_links}</dd>
            </div>
          </dl>
        </header>

        <figure class="project-detail__image">
          {detail_image(p)}
          <figcaption>{escape(c['caption'])}</figcaption>
        </figure>

        <div class="project-detail__content">
          <section aria-labelledby="opgave-title">
            <h2 id="opgave-title">De opgave</h2>
            {paragraphs(c['challenge'])}
          </section>

          <section aria-labelledby="proces-title">
            <h2 id="proces-title">Het proces</h2>
            {paragraphs(c['process'])}{steps_html}
          </section>
{detail_steps(p)}
          <section aria-labelledby="resultaat-title">
            <h2 id="resultaat-title">Het resultaat</h2>
            {paragraphs(c['result'])}
          </section>
{feedback_section(p)}
          <section aria-labelledby="leerdoelen-title">
            <h2 id="leerdoelen-title">Aangetoonde leerdoelen</h2>
            <ol class="leerdoel-list">
{leerdoelen}
            </ol>
          </section>
        </div>
      </article>

      <nav class="project-nav" aria-label="Projectnavigatie">
        <a class="button button--outline" href="../competenties/{comp['slug']}.html">&larr; Terug naar competentie {comp['number']}</a>{next_link}
      </nav>
    </div>"""
    write(f"projects/{p['slug']}.html", page(
        title=f"{p['title']} | Shena",
        description=f"Project van Shena: {p['title']}.",
        prefix="../", body=body, current="competenties",
    ))


def code_key(code):
    return [int(n) for n in code.split(".")]


def timeline_projects():
    """Projects dated within the TIMELINE range, oldest first.

    Dates are zero-padded "YYYY-MM" strings (checked by parse_month), so they sort correctly as text.
    sorted() is stable: projects from the same month keep their order in PROJECTS.
    """
    in_range = [p for p in PROJECTS if TIMELINE["start"] <= p["date"] <= TIMELINE["end"]]
    return sorted(in_range, key=lambda x: x["date"])


def timeline():
    """Home-page slider of projects in the TIMELINE range, with cumulative leerdoel progress."""
    total = len(LEERDOELEN)
    shown = set()
    items = []
    for p in timeline_projects():
        new = sorted((code for code in p["leerdoelen"] if code not in shown), key=code_key)
        shown.update(p["leerdoelen"])
        percent = round(len(shown) / total * 100)
        when = escape(format_month(p["date"]))
        new_html = (
            f'\n              <p class="timeline-card__new">Nieuw: {", ".join(new)}</p>' if new else ""
        )
        items.append(f"""          <li class="timeline__item">
            <p class="timeline__date">{when}</p>
            <article class="project-card timeline-card">
              <div class="project-card__media">
                {card_image(p, "")}
              </div>
              <div class="project-card__body">
                <h3 class="project-card__title">
                  <a class="project-card__link" href="projects/{p['slug']}.html">{escape(p['title'])}</a>
                </h3>
{tag_list(p)}
                <div class="timeline-card__progress">
                  <p class="timeline-card__progress-label">{len(shown)} van {total} leerdoelen aangetoond</p>
                  <div class="progress-bar" aria-hidden="true"><span style="width: {percent}%"></span></div>
                </div>{new_html}
              </div>
            </article>
          </li>""")
    cards = "\n".join(items)
    period = f"{format_month(TIMELINE['start'])} – {format_month(TIMELINE['end'])}"
    return f"""    <!-- Timeline -->
    <section class="section timeline" id="tijdlijn" aria-labelledby="timeline-title" data-slider>
      <div class="container">
        <div class="timeline__header">
          <div>
            <p class="section__eyebrow">Tijdlijn · {period}</p>
            <h2 id="timeline-title">Mijn ontwikkeling</h2>
            <p class="timeline__intro">Mijn projecten van {period}, met de groei in aangetoonde leerdoelen. Klik op een project voor de details.</p>
          </div>
          <div class="timeline__controls" hidden>
            <button class="timeline__button" type="button" data-slider-prev aria-controls="timeline-track">
              <span aria-hidden="true">&larr;</span><span class="visually-hidden">Vorige projecten</span>
            </button>
            <button class="timeline__button" type="button" data-slider-next aria-controls="timeline-track">
              <span aria-hidden="true">&rarr;</span><span class="visually-hidden">Volgende projecten</span>
            </button>
          </div>
        </div>

        <ol class="timeline__track" id="timeline-track" data-slider-track>
{cards}
        </ol>
      </div>
    </section>"""


def build_reflectie():
    sections = "\n\n".join(
        f"""          <section class="star-step" aria-labelledby="reflectie-{i}-title">
            <h2 class="star-step__title" id="reflectie-{i}-title"><span class="star-step__letter" aria-hidden="true">{escape(s['letter'])}</span> {escape(s['heading'])}</h2>
""" + "\n".join(f"            <p>{escape(par)}</p>" for par in s["paragraphs"]) + """
          </section>"""
        for i, s in enumerate(REFLECTIE["sections"], start=1)
    )
    body = f"""    <div class="container container--narrow">
      <nav class="breadcrumb" aria-label="Kruimelpad">
        <ol>
          <li><a href="index.html">Home</a></li>
          <li><span aria-current="page">{escape(REFLECTIE['title'])}</span></li>
        </ol>
      </nav>

      <header class="project-detail__header">
        <p class="section__eyebrow">Reflectie</p>
        <h1>{escape(REFLECTIE['title'])}</h1>
        <p class="project-detail__lead">{escape(REFLECTIE['lead'])}</p>
      </header>

      <section class="project-detail__content" aria-label="STAR-reflectie">
{sections}
      </section>

      <nav class="project-nav" aria-label="Paginanavigatie">
        <a class="button button--outline" href="index.html#competenties">&larr; Naar de competenties</a>
      </nav>
    </div>"""
    write("reflectie.html", page(
        title=f"{REFLECTIE['title']} | Shena",
        description="Reflectie van Shena op de eigen ontwikkeling en het portfolio.",
        prefix="", body=body, current="reflectie",
    ))


build_index()
build_reflectie()
for comp in COMPETENTIES:
    build_competentie(comp)
for proj in PROJECTS:
    build_project(proj)

# Pages left over from renamed or removed projects/competenties are not deleted automatically
expected = {f"competenties/{x['slug']}.html" for x in COMPETENTIES} | {f"projects/{x['slug']}.html" for x in PROJECTS}
for folder in ("competenties", "projects", "themes"):
    folder_path = os.path.join(ROOT, folder)
    if not os.path.isdir(folder_path):
        continue
    for name in sorted(os.listdir(folder_path)):
        if name.endswith(".html") and f"{folder}/{name}" not in expected:
            print(f"warning: {folder}/{name} is not in build.py anymore; delete it if it is no longer needed")

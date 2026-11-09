# The wine guides on gobletai.app/guides/. Each one answers a question people
# actually type into Google, in full, and only then shows how Goblet does it
# in one photo. build_guides.py turns these into pages.
#
# Rules the copy keeps to, because they are what search engines and AI
# assistants reward and what keeps the site honest:
#  - answer the question in the first paragraph, then go deeper;
#  - facts that can be checked, no invented numbers about Goblet;
#  - other apps described fairly, by what they are known for;
#  - every FAQ answer stands on its own (it is lifted into search results).

GUIDES = [
# ─────────────────────────────────────────────────────────────────────────────
dict(
slug='best-wine-apps',
title='Best Wine Apps (2026): Scanners, Ratings & AI Sommeliers',
description='The best wine apps compared: label scanners, crowd ratings, cellar trackers, price finders and AI sommeliers that learn your taste. Which one is for you.',
h1='The best wine apps, and what each one is for',
kicker='Wine apps compared',
intro='There is no single “best wine app”, because wine apps do different jobs. Some read a label and show you what the crowd thinks, some manage a cellar, some find the cheapest shop, and a newer kind learns your own palate and tells you what <em>you</em> will like. Here is how they differ, so you can pick the right one, or the right two.',
body='''
<h2>The five kinds of wine app</h2>
<table>
<thead><tr><th>What you want</th><th>Kind of app</th><th>Best known example</th></tr></thead>
<tbody>
<tr><td>Point at a label and see what other drinkers think</td><td>Scanner with community ratings</td><td>Vivino</td></tr>
<tr><td>Follow what sommeliers and friends are drinking</td><td>Social tasting notes</td><td>Delectable</td></tr>
<tr><td>Track the bottles in your cellar and when to open them</td><td>Cellar manager</td><td>CellarTracker</td></tr>
<tr><td>Find where a wine is sold and the going price</td><td>Price search</td><td>Wine-Searcher</td></tr>
<tr><td>Know which wine <em>you</em> will like, on a list or a shelf</td><td>Personal AI sommelier</td><td>Goblet</td></tr>
</tbody>
</table>

<h2>Scanner apps with crowd ratings</h2>
<p>The most downloaded wine apps work the same way: photograph a label, the app recognises the wine and shows an average star rating from its community, often with a price and a place to buy it. <strong>Vivino</strong> is the best known, with a very large database of wines and user reviews and a marketplace in many countries.</p>
<p>Crowd ratings are good at one thing: telling you whether lots of people liked a wine. They are not good at telling you whether <em>you</em> will. An average of thousands of palates flattens out exactly the differences that matter: if you love crisp, high-acid whites and the crowd loves soft, oaky ones, the top-rated bottle is the wrong bottle for you.</p>

<h2>Social and tasting-note apps</h2>
<p><strong>Delectable</strong> also scans labels, but leans social: you follow people, including sommeliers and wine professionals, and see what they are drinking and their notes. It is a good way to discover wines through people whose taste you trust.</p>

<h2>Cellar managers</h2>
<p>If you own more than a few dozen bottles, a cellar manager keeps the inventory, where each bottle sits and when it should be drunk. <strong>CellarTracker</strong> is the long-standing choice among collectors and has a deep archive of community tasting notes.</p>

<h2>Price search</h2>
<p><strong>Wine-Searcher</strong> answers “where can I buy this and for how much?”. It lists shops and prices for a given wine and is the quickest way to check whether a price in front of you is fair.</p>

<h2>Personal AI sommeliers</h2>
<p>The newest kind of app starts from you rather than the crowd. <strong>Goblet</strong> learns your palate from a short taste quiz and from every wine you rate, then scores any wine, out of 10, for how much you personally will enjoy it. It works on the three places people actually choose wine:</p>
<ul>
<li><strong>A single bottle</strong>: scan the label for a fit score and a plain-English reason.</li>
<li><strong>A restaurant wine list</strong>: photograph the menu and every bottle on it is ranked for your palate and your budget.</li>
<li><strong>A shop shelf</strong>: photograph the whole display and Goblet picks the three worth taking home.</li>
</ul>
<p>It also has Vinum, an AI sommelier you can ask anything (“what goes with lamb chops?”), a Taste Profile with a Wine ID card you can show a waiter, and a table mode that picks a bottle that suits everyone at dinner.</p>

<h2>How to choose</h2>
<ul>
<li><strong>You want to know what is popular</strong>: a crowd-rating scanner.</li>
<li><strong>You collect</strong>: a cellar manager, plus a price search for buying.</li>
<li><strong>You want to stop guessing and drink more wine you love</strong>: an app that learns your own taste.</li>
</ul>
<p>Many wine lovers keep two: one to track or buy, and one to decide what to drink. The deciding one is where a personal palate matters most.</p>
''',
faq=[
('What is the best app to scan wine labels?', 'Vivino, Delectable and Goblet all read a wine label from a photo. Vivino and Delectable show what other people thought of the wine; Goblet scores the wine for your own palate, out of 10, and explains why. Goblet also scans whole restaurant wine lists and shop shelves, not just single bottles.'),
('Is there a wine app that tells you what wine you will like?', 'Yes. Goblet is built for exactly that. It learns your taste from a short quiz and from the wines you rate, then predicts how much you personally will enjoy any wine you scan, instead of showing a crowd average.'),
('Is there a free wine scanner app?', 'Most wine scanner apps are free to download. Goblet is free with a monthly allowance of bottle scans plus wine list and shelf scans; Goblet Premium makes scanning unlimited.'),
('Can an app read a restaurant wine list?', 'Yes. In Goblet you switch the scanner to Wine List, photograph the menu, and every bottle on it is ranked for your palate and your budget, with a recommendation of what to order and why.'),
('What is a good alternative to Vivino?', 'It depends what you use Vivino for. For tracking a collection, CellarTracker; for prices, Wine-Searcher; for picks based on your own taste rather than crowd ratings, Goblet.'),
],
related=['how-to-find-wine-you-like', 'how-to-choose-wine-from-a-wine-list', 'wine-ratings-explained'],
),
# ─────────────────────────────────────────────────────────────────────────────
dict(
slug='how-to-choose-wine-from-a-wine-list',
title='How to Choose Wine From a Restaurant Wine List',
description='A calm, step-by-step way to order wine at a restaurant: set a budget, read the list, match the food, ask the sommelier and check the bottle.',
h1='How to choose wine from a restaurant wine list',
kicker='Ordering wine',
intro='To choose wine from a restaurant list: decide your budget first, find the section that matches your food (or the style you like), pick two or three candidates in your price range, and ask the sommelier or server to choose between them. You do not need to know the wines; you need to know your budget and what you like.',
body='''
<h2>1. Set the budget before you open the list</h2>
<p>Decide the most you want to spend on the bottle before you start reading. It stops the list from deciding for you. Restaurant prices usually include a sizeable markup over shop prices, so a bottle that looks expensive is often a modest wine; that is normal and not a reason to panic-order the cheapest line.</p>
<p>A standard 750 ml bottle pours about five 150 ml (5 oz) glasses. If two or more people will have two glasses each, a bottle is usually better value than wine by the glass.</p>

<h2>2. Understand how the list is laid out</h2>
<p>Most lists are grouped by colour and style (sparkling, white, rosé, red, dessert), then by country or region, sometimes by grape. Within each group, wines are often listed from lighter to fuller, or from cheaper to dearer. Read the headings first; they tell you more than the wine names do.</p>

<h2>3. Match the food, roughly</h2>
<p>You do not need a perfect pairing. Two rules cover most dinners:</p>
<ul>
<li><strong>Match weight with weight.</strong> Light dishes (fish, salads, chicken) want lighter wines; rich dishes (steak, braises, cream sauces) want fuller ones.</li>
<li><strong>Tannic reds love fat and protein</strong>, and clash with delicate fish. If the table is ordering everything, a lighter red like Pinot Noir or a dry rosé goes with almost anything.</li>
</ul>
<p>Our <a href="/guides/wine-and-food-pairing.html">wine and food pairing guide</a> has a table for common dishes.</p>

<h2>4. Look for value in the right places</h2>
<ul>
<li><strong>Lesser-known regions</strong> often give more wine for the money than famous names: Portugal, the Loire Valley, southern Italy, Spain beyond Rioja, Austria, Chile.</li>
<li><strong>The second-cheapest bottle</strong> is famously what nervous diners order. It is not a trap everywhere, but it is not automatically good value either.</li>
<li><strong>Grapes over glamour.</strong> A Gamay from Beaujolais or a Cabernet Franc from the Loire can drink far above its price.</li>
</ul>

<h2>5. Ask the sommelier, the easy way</h2>
<p>Point at a price on the list rather than saying it out loud, and say what you like: “something like this, not too heavy, we are having the lamb.” A good sommelier hears the budget and stays within it. Describing what you enjoyed before (“I liked a Rioja last time”) helps more than any wine vocabulary.</p>

<h2>6. When the bottle arrives</h2>
<p>The server shows you the label: check it is the wine and vintage you ordered. They pour a taste: you are checking the wine is not faulty, not whether you love it. A corked wine smells musty, like wet cardboard or a damp cellar. If it does, say so, and it will be replaced. If it is sound, a nod is enough.</p>

<h2>The shortcut</h2>
<p>Goblet does steps 2 to 4 in one photo. Switch the scanner to <strong>Wine List</strong>, photograph the menu, and every bottle is ranked for your palate and your budget, with the one to order and why, in plain English.</p>
''',
faq=[
('How do you pick a wine at a restaurant if you know nothing about wine?', 'Set a budget, tell the server or sommelier what you are eating and what you usually like, and point to a price on the list. Or photograph the list with Goblet, which ranks every bottle for your palate and budget and tells you which to order.'),
('Is it rude to order the cheapest wine on the list?', 'No. Ordering within your budget is never rude, and sommeliers are used to it. Asking which inexpensive bottle they would choose often gets you a well-chosen wine.'),
('How many glasses are in a bottle of wine?', 'A standard 750 ml bottle holds about five 150 ml (5 oz) glasses, or about six smaller 125 ml pours.'),
('Can you send back a bottle of wine at a restaurant?', 'You can send back a faulty bottle, for example one that is corked and smells musty or of wet cardboard. A bottle that is sound but not to your taste is usually not returnable, which is why asking for advice before ordering helps.'),
('What does the sommelier want when they pour a little wine to taste?', 'They want you to confirm the wine is sound, not faulty. A quick sniff and sip is enough; a nod means it is fine to pour.'),
],
related=['wine-and-food-pairing', 'how-to-find-wine-you-like', 'best-wine-apps'],
),
# ─────────────────────────────────────────────────────────────────────────────
dict(
slug='how-to-read-a-wine-label',
title='How to Read a Wine Label: A Plain-English Guide',
description='What every part of a wine label means: producer, region, grape, vintage and alcohol, plus terms like Reserva, Grand Cru, Brut and Trocken.',
h1='How to read a wine label',
kicker='Wine labels',
intro='A wine label tells you five main things: who made it (the producer), where the grapes grew (the region or appellation), what it is made from (the grape, if stated), when the grapes were picked (the vintage) and how strong it is (alcohol by volume). European labels usually name the place; New World labels usually name the grape. Once you know that, most labels make sense.',
body='''
<h2>The five things on almost every label</h2>
<table>
<thead><tr><th>On the label</th><th>What it tells you</th></tr></thead>
<tbody>
<tr><td><strong>Producer</strong> (Château, Domaine, Bodega, Weingut, winery name)</td><td>Who made the wine. The single best predictor of quality once you know a few names.</td></tr>
<tr><td><strong>Region or appellation</strong> (Bordeaux, Rioja DOCa, Napa Valley AVA)</td><td>Where the grapes grew, often with legal rules about grapes and methods.</td></tr>
<tr><td><strong>Grape variety</strong> (Pinot Noir, Sauvignon Blanc)</td><td>What the wine is made from. Common on New World labels, rarer on Old World ones.</td></tr>
<tr><td><strong>Vintage</strong> (a year)</td><td>The year the grapes were harvested. No year usually means a blend of years.</td></tr>
<tr><td><strong>Alcohol (ABV)</strong></td><td>Roughly, how full-bodied the wine will feel: under 12.5% tends to be lighter, over 14% fuller and warmer.</td></tr>
</tbody>
</table>

<h2>Old World labels name the place</h2>
<p>In France, Italy and Spain the place is the point: the rules of each appellation largely decide which grapes may be used. So the label says <em>Chablis</em>, not Chardonnay; <em>Chianti Classico</em>, not Sangiovese; <em>Rioja</em>, not Tempranillo. A quick map in your head helps:</p>
<ul>
<li><strong>Burgundy</strong> red is Pinot Noir; white is Chardonnay (Chablis included).</li>
<li><strong>Bordeaux</strong> red is mostly Cabernet Sauvignon and Merlot blends.</li>
<li><strong>Sancerre</strong> white is Sauvignon Blanc.</li>
<li><strong>Chianti</strong> and <strong>Brunello di Montalcino</strong> are Sangiovese; <strong>Barolo</strong> and <strong>Barbaresco</strong> are Nebbiolo.</li>
<li><strong>Rioja</strong> red is mostly Tempranillo.</li>
</ul>

<h2>New World labels name the grape</h2>
<p>In the US, Australia, New Zealand, Chile, Argentina and South Africa the grape is usually front and centre. In the US, a wine labelled with one grape must contain at least 75% of it under federal rules (some states require more), and a vintage date means at least 85% of the grapes came from that year (95% for wines labelled with an AVA). EU rules for a named grape and vintage are generally 85%.</p>

<h2>Quality and ageing terms</h2>
<ul>
<li><strong>Reserva, Gran Reserva</strong> (Spain): legally defined minimum ageing; Gran Reserva is aged the longest.</li>
<li><strong>Riserva</strong> (Italy): longer ageing than the standard wine of that appellation.</li>
<li><strong>Grand Cru, Premier Cru</strong> (Burgundy): classified vineyards; Grand Cru is the top tier. In Bordeaux, “Grand Cru Classé” refers to classified estates.</li>
<li><strong>Reserve</strong> (US, Australia and others): usually not legally defined; it means whatever the producer wants.</li>
<li><strong>Old vines, Vieilles Vignes</strong>: older vines, often more concentrated wine; not regulated in most places.</li>
<li><strong>Estate bottled</strong>: grown and bottled by the same producer.</li>
</ul>

<h2>Sweetness words</h2>
<ul>
<li><strong>Sparkling wine</strong>, from driest: Brut Nature, Extra Brut, Brut, Extra Dry, Dry (Sec), Demi-Sec, Doux. Yes, Extra Dry is <em>sweeter</em> than Brut.</li>
<li><strong>German Riesling</strong>: “Trocken” means dry; Kabinett, Spätlese and Auslese describe grape ripeness at harvest, often (not always) meaning more sweetness up the scale.</li>
<li><strong>Sec, Demi-Sec, Moelleux, Doux</strong> (France): dry, off-dry, sweet, very sweet.</li>
</ul>

<h2>The back label</h2>
<p>Back labels carry the importer, the legally required warnings (in the US, “Contains sulfites”) and often a tasting note. Tasting notes are marketing, but useful marketing: “crisp”, “bright”, “zesty” mean high acid; “rich”, “velvety”, “opulent” mean full and soft.</p>

<h2>Skip the decoding</h2>
<p>Point Goblet at any label, in any language, and it reads the producer, region, grape and vintage for you, explains the wine in plain English and scores it out of 10 for your palate.</p>
''',
faq=[
('What is the most important thing on a wine label?', 'The producer. Region, grape and vintage tell you the style, but who made the wine is the best single guide to quality once you know a few names you trust.'),
('Why do French wine labels not say the grape?', 'Because French appellation rules largely decide which grapes may be used in each place, so the place name implies the grape: red Burgundy is Pinot Noir, Sancerre is Sauvignon Blanc, Chablis is Chardonnay.'),
('What does the year on a wine bottle mean?', 'It is the vintage: the year the grapes were harvested, not the year the wine was bottled. Wine with no year is usually a blend of several harvests.'),
('Is Extra Dry Champagne sweeter than Brut?', 'Yes. On sparkling wine labels Extra Dry is slightly sweeter than Brut. From driest to sweetest: Brut Nature, Extra Brut, Brut, Extra Dry, Dry or Sec, Demi-Sec, Doux.'),
('What does Reserva mean on a Spanish wine?', 'Reserva and Gran Reserva are legally defined ageing categories in Spain. Gran Reserva wines spend the longest time ageing in barrel and bottle before release.'),
],
related=['wine-grapes-explained', 'how-to-buy-wine-at-a-store', 'how-to-taste-wine'],
),
# ─────────────────────────────────────────────────────────────────────────────
dict(
slug='how-to-find-wine-you-like',
title='How to Find Out What Wine You Like (and Why)',
description='Discover your wine taste: the five traits that make wines different, side-by-side tastings, and rating what you drink until your palate shows.',
h1='How to find out what wine you like',
kicker='Your palate',
intro='The fastest way to learn what wine you like is to taste a few very different wines side by side, notice what you prefer about each (sweetness, acidity, tannin, body, flavour), and rate every wine you drink on one simple question: would I buy this again? After a dozen honest ratings, a pattern appears, and that pattern is your palate.',
body='''
<h2>The five things that make wines different</h2>
<p>Most of what makes you love or dislike a wine comes down to five things. Learn to notice them and you can say what you like in words any sommelier understands.</p>
<table>
<thead><tr><th>Trait</th><th>What it feels like</th><th>Low</th><th>High</th></tr></thead>
<tbody>
<tr><td><strong>Sweetness</strong></td><td>Sugar on the tip of the tongue</td><td>Brut Champagne, Sauvignon Blanc</td><td>Moscato, Port</td></tr>
<tr><td><strong>Acidity</strong></td><td>Mouth-watering, crisp, zesty</td><td>Viognier, many warm-climate reds</td><td>Riesling, Sauvignon Blanc, Chianti</td></tr>
<tr><td><strong>Tannin</strong></td><td>Drying grip on gums and teeth, like strong tea</td><td>Pinot Noir, Gamay, most whites</td><td>Cabernet Sauvignon, Nebbiolo</td></tr>
<tr><td><strong>Body</strong></td><td>Weight in the mouth: skimmed milk to cream</td><td>Pinot Grigio, Beaujolais</td><td>Oaked Chardonnay, Shiraz, Malbec</td></tr>
<tr><td><strong>Flavour</strong></td><td>Fruit, floral, earthy, spicy, oaky</td><td colspan="2">Red fruit vs black fruit, fresh vs ripe, oak (vanilla, toast) vs none</td></tr>
</tbody>
</table>

<h2>Taste side by side</h2>
<p>You learn far more from two wines tasted together than from twenty tasted weeks apart. Open two contrasting bottles with a friend, or order two glasses, and compare:</p>
<ul>
<li>Pinot Noir against Cabernet Sauvignon: light and silky against firm and tannic.</li>
<li>Unoaked Chablis against oaked California Chardonnay: the same grape, with and without oak.</li>
<li>New Zealand Sauvignon Blanc against a dry Riesling: two high-acid whites with different fruit.</li>
</ul>
<p>Each pair teaches you one dimension. Note which side you preferred, not which seemed “better”.</p>

<h2>Rate everything, simply</h2>
<p>Elaborate tasting notes are hard to keep up. One number works: <strong>would you buy it again, out of 10?</strong> Rate every wine you drink, including the cheap ones and the ones you did not like. The dislikes are as useful as the favourites: they tell you what to avoid.</p>

<h2>Look for the pattern</h2>
<p>After ten or twelve ratings, look at your top and bottom wines together. Common patterns:</p>
<ul>
<li>Your favourites are all high-acid: look for cool-climate wines (Loire, Burgundy, northern Italy, Germany, New Zealand).</li>
<li>Your favourites are ripe and full: warm regions (Napa, Barossa, Mendoza, southern Italy).</li>
<li>You dislike every tannic red: stay with Pinot Noir, Gamay, Grenache and lighter Italian reds.</li>
</ul>

<h2>Clues from what you already eat and drink</h2>
<p>Your other tastes can be a starting hint, not a rule. People who like bitter dark chocolate or strong black coffee are often comfortable with tannic reds; people who love lemon and green apple often enjoy crisp whites; people who take their coffee sweet sometimes start happier with off-dry wines.</p>

<h2>Let the pattern do the choosing</h2>
<p>This is exactly what Goblet does for you. A short taste quiz gives it a starting point, then every wine you rate out of 10 sharpens its picture of your palate. Scan any bottle, wine list or shelf and it predicts how much <em>you</em> will like each wine, and explains why in terms of wines you already rated.</p>
''',
faq=[
('How do I figure out what kind of wine I like?', 'Taste contrasting wines side by side, notice which you prefer on sweetness, acidity, tannin, body and flavour, and rate every wine you drink on whether you would buy it again. After about a dozen ratings a clear pattern usually appears.'),
('What wine is good for beginners?', 'Approachable, fruity wines with soft tannins are easiest to enjoy at first: Pinot Noir, Merlot, Grenache or Beaujolais for reds; Pinot Grigio, Sauvignon Blanc or an off-dry Riesling for whites. The best beginner wine is still the one you personally enjoy.'),
('What is the difference between dry and sweet wine?', 'Dry wine has little or no sugar left after fermentation; sweet wine has noticeable sugar. Fruity is not the same as sweet: a wine can taste of ripe fruit and still be completely dry.'),
('What are tannins in wine?', 'Tannins are compounds from grape skins, seeds and oak barrels that cause a drying, gripping feeling on your gums, like strong black tea. They are high in Cabernet Sauvignon and Nebbiolo and low in Pinot Noir and most white wines.'),
('Is there an app that learns my wine taste?', 'Yes. Goblet learns your palate from a short quiz and the wines you rate out of 10, then scores any wine you scan for how much you personally will enjoy it.'),
],
related=['how-to-taste-wine', 'wine-grapes-explained', 'best-wine-apps'],
),
# ─────────────────────────────────────────────────────────────────────────────
dict(
slug='wine-and-food-pairing',
title='Wine and Food Pairing Guide: What Wine Goes With What',
description='Simple wine pairing rules and a quick table for steak, chicken, salmon, pasta, pizza, cheese, spicy food and dessert, plus the pairings to avoid.',
h1='Wine and food pairing: what wine goes with what',
kicker='Food and wine',
intro='Good wine pairing comes down to a few rules: match the weight of the wine to the weight of the dish, pair acid with acid, let tannic reds meet fat and protein, use a touch of sweetness against spice, and make dessert wine sweeter than the dessert. Use the table below for common dishes, then trust what you enjoy.',
body='''
<h2>The six rules that cover most meals</h2>
<ol>
<li><strong>Weight with weight.</strong> Delicate food wants a lighter wine; rich food wants a fuller one.</li>
<li><strong>Acid with acid.</strong> Tomato sauces, vinaigrettes and citrus need a wine with at least as much acidity, or the wine tastes flat.</li>
<li><strong>Tannin with fat and protein.</strong> Steak softens a tannic red; the same wine with delicate fish can taste metallic.</li>
<li><strong>Sweetness against heat.</strong> Spicy food makes alcohol and tannin feel harsher; an off-dry white cools it down.</li>
<li><strong>Dessert wine sweeter than dessert.</strong> Otherwise the wine tastes thin and sour.</li>
<li><strong>What grows together goes together.</strong> Regional food and wine evolved side by side: Chianti with Tuscan food, Muscadet with Loire oysters.</li>
</ol>

<h2>Quick pairing table</h2>
<table>
<thead><tr><th>Dish</th><th>Try</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Steak, grilled red meat</td><td>Cabernet Sauvignon, Malbec, Syrah</td><td>Tannin and fat soften each other</td></tr>
<tr><td>Lamb</td><td>Rioja, Bordeaux blends, Syrah</td><td>Savoury reds for a rich, gamey meat</td></tr>
<tr><td>Burgers, barbecue</td><td>Zinfandel, Malbec, Shiraz</td><td>Ripe fruit for smoky, sweet sauces</td></tr>
<tr><td>Roast chicken</td><td>Chardonnay, Pinot Noir</td><td>Medium weight, flexible</td></tr>
<tr><td>Salmon, tuna</td><td>Pinot Noir, dry rosé, oaked Chardonnay</td><td>Light red with oily fish works</td></tr>
<tr><td>White fish, shellfish</td><td>Sauvignon Blanc, Albariño, Chablis</td><td>Crisp acidity, like a squeeze of lemon</td></tr>
<tr><td>Oysters</td><td>Muscadet, Chablis, Champagne</td><td>Saline, mineral, high acid</td></tr>
<tr><td>Tomato pasta, pizza</td><td>Chianti (Sangiovese), Barbera</td><td>High acid matches tomato</td></tr>
<tr><td>Creamy pasta</td><td>Chardonnay, Pinot Grigio</td><td>Body matches cream</td></tr>
<tr><td>Mushrooms, truffle</td><td>Pinot Noir, Nebbiolo</td><td>Earthy with earthy</td></tr>
<tr><td>Spicy Thai, Indian, Sichuan</td><td>Off-dry Riesling, Gewürztraminer</td><td>Sweetness tames heat</td></tr>
<tr><td>Goat cheese</td><td>Sancerre (Sauvignon Blanc)</td><td>Classic regional match</td></tr>
<tr><td>Aged hard cheese</td><td>Cabernet Sauvignon, Rioja Reserva</td><td>Fat and salt soften tannin</td></tr>
<tr><td>Blue cheese</td><td>Port, Sauternes</td><td>Sweet against salty</td></tr>
<tr><td>Chocolate, dessert</td><td>Port, late-harvest wines</td><td>Wine sweeter than the dessert</td></tr>
</tbody>
</table>

<h2>Pairings to avoid</h2>
<ul>
<li>Very tannic reds with delicate fish: the combination can taste metallic.</li>
<li>Dry wine with a sweet dessert: the wine turns sour.</li>
<li>High-alcohol, tannic reds with very spicy food: the burn gets worse.</li>
<li>Oaky wines with vinegar-heavy dishes: the oak tastes bitter.</li>
</ul>

<h2>When the table orders everything</h2>
<p>Pick a versatile wine: dry rosé, Champagne or another dry sparkling wine, Pinot Noir, or a dry Riesling. All four have enough acidity to handle a wide range of dishes without overpowering any.</p>

<h2>Ask for a pairing</h2>
<p>In Goblet, ask Vinum, the built-in AI sommelier: “lamb chops with rosemary tonight, what should I open?”. It answers from the bottles in your own Winery first, then suggests what to buy, scored for your palate.</p>
''',
faq=[
('What wine goes with steak?', 'Full-bodied reds with firm tannin: Cabernet Sauvignon, Malbec or Syrah. The fat and protein in the steak soften the tannin, and the wine cuts through the richness.'),
('What wine goes with salmon?', 'Pinot Noir is the classic red for salmon; a dry rosé or a lightly oaked Chardonnay also work. Avoid very tannic reds, which can taste metallic with fish.'),
('What wine goes with pasta?', 'For tomato sauces, a high-acid Italian red like Chianti (Sangiovese) or Barbera. For cream sauces, Chardonnay or Pinot Grigio. For pesto, a crisp white such as Vermentino or Sauvignon Blanc.'),
('What wine goes with spicy food?', 'An off-dry white such as Riesling or Gewürztraminer. A little sweetness and lower alcohol calm the heat, while high-alcohol tannic reds make it burn more.'),
('What is the safest wine to bring to dinner?', 'A dry sparkling wine, a dry rosé or a Pinot Noir. All three pair with a wide range of food and suit most guests.'),
],
related=['how-to-choose-wine-from-a-wine-list', 'wine-grapes-explained', 'how-to-buy-wine-at-a-store'],
),
# ─────────────────────────────────────────────────────────────────────────────
dict(
slug='how-to-buy-wine-at-a-store',
title='How to Pick a Good Bottle of Wine at the Store',
description='How to choose a good bottle in a shop or supermarket: set a price, shop by grape or region, find value regions, read shelf tags and ask staff.',
h1='How to pick a good bottle of wine at the store',
kicker='Buying wine',
intro='To pick a good bottle at the store: set your price, decide the style (light or full, red or white), head for a grape or region you know you like, look for value regions that over-deliver for the money, and ask the staff. In a good shop, “what would you drink at this price?” is the most useful question you can ask.',
body='''
<h2>1. Decide price and style first</h2>
<p>Pick a price and a style before you walk in: red or white, light or full, for drinking tonight or for a dinner. Standing in front of five hundred bottles with no plan is how people buy by label art.</p>

<h2>2. Shop by grape or region you already like</h2>
<p>If you liked a Malbec, the Argentina section is a good start. If a crisp Sauvignon Blanc was a hit, try New Zealand, Sancerre or Chile. Our guide to <a href="/guides/wine-grapes-explained.html">wine grapes</a> lists what each one tastes like and what to try next.</p>

<h2>3. Go where the value is</h2>
<p>Famous regions charge for their names. These usually give more for the money:</p>
<ul>
<li><strong>Portugal</strong> (Douro and Dão reds, Vinho Verde whites)</li>
<li><strong>Spain beyond Rioja</strong> (Garnacha from Campo de Borja or Calatayud, Monastrell, Albariño)</li>
<li><strong>Southern France</strong> (Languedoc, Côtes du Rhône) and the <strong>Loire</strong> (Chenin Blanc, Cabernet Franc)</li>
<li><strong>Southern Italy</strong> (Montepulciano d’Abruzzo, Primitivo, Nero d’Avola)</li>
<li><strong>Chile, Argentina, South Africa</strong> for ripe, generous styles</li>
</ul>

<h2>4. Read the shelf, carefully</h2>
<ul>
<li><strong>Shelf talkers</strong> (the little cards with scores) are a starting point. A 90-point score says a critic liked it, not that you will. See <a href="/guides/wine-ratings-explained.html">what wine scores mean</a>.</li>
<li><strong>Vintage</strong>: for everyday whites and rosés, the youngest available vintage is usually the freshest.</li>
<li><strong>Screw caps</strong> are not a sign of cheap wine; many excellent wines use them, and they avoid cork taint.</li>
<li><strong>Heavy bottles and deep punts</strong> mean nothing about what is inside.</li>
</ul>

<h2>5. Ask, and buy by the case</h2>
<p>In an independent shop, staff taste the stock. Tell them a wine you liked and your price. Many shops discount mixed cases of twelve, which is an easy way to try a range and learn what you like.</p>

<h2>6. Rate it when you drink it</h2>
<p>The bottle you buy today is only half the value; remembering what you thought of it is the other half. A quick rating out of 10 turns every bottle into a better next pick.</p>

<h2>Scan the whole shelf</h2>
<p>With Goblet, photograph the whole shelf. It reads every label in the picture and pulls out the three bottles most worth taking home for your palate, with a reason for each.</p>
''',
faq=[
('How do I choose a good wine at the supermarket?', 'Set a price, choose a style, start from a grape or region you have liked before, and favour value regions such as Portugal, southern France, southern Italy, Spain and Chile. Or photograph the shelf with Goblet, which picks the three bottles that best suit your palate.'),
('How much should I spend on a good bottle of wine?', 'There is no fixed answer, but in many markets quality rises noticeably from the cheapest tier into the mid-teens in US dollars, and value regions give the most for the money. Above that, you are often paying for rarity and reputation as much as taste.'),
('Are screw cap wines worse than cork?', 'No. Many high-quality wines use screw caps, especially in New Zealand and Australia. Screw caps keep wine fresh and avoid cork taint.'),
('Does an older vintage mean a better wine?', 'Not usually. Most wines, especially everyday whites and rosés, are made to be drunk young. Only some wines improve with years of ageing.'),
('What does a 90-point wine mean?', 'It means a critic rated the wine outstanding on the 100-point scale. It is a judgement of quality by one taster, not a prediction of whether you will enjoy it.'),
],
related=['wine-grapes-explained', 'wine-ratings-explained', 'how-to-read-a-wine-label'],
),
# ─────────────────────────────────────────────────────────────────────────────
dict(
slug='wine-grapes-explained',
title='Red and White Wine Types: 16 Grapes Explained',
description='The 16 wine grapes worth knowing, red and white: what each tastes like, how full it is, where it grows, and what to try next if you like it.',
h1='Red and white wine types: 16 grapes explained',
kicker='Wine grapes',
intro='Most wine you will meet is made from a handful of grapes. Learn these sixteen, ten red and six white, and you can read almost any wine list: what each tastes like, how full it is, where it grows best, and what to try next if you like it.',
body='''
<h2>Red wine grapes</h2>
<table>
<thead><tr><th>Grape</th><th>Tastes like</th><th>Body</th><th>Classic regions</th><th>If you like it, try</th></tr></thead>
<tbody>
<tr><td><strong>Cabernet Sauvignon</strong></td><td>Blackcurrant, cedar, firm tannin</td><td>Full</td><td>Bordeaux, Napa, Coonawarra</td><td>Bordeaux blends, Malbec</td></tr>
<tr><td><strong>Merlot</strong></td><td>Plum, cherry, soft and round</td><td>Medium to full</td><td>Bordeaux (Right Bank), Washington</td><td>Cabernet Franc, Carmenère</td></tr>
<tr><td><strong>Pinot Noir</strong></td><td>Red cherry, raspberry, earth, silky</td><td>Light to medium</td><td>Burgundy, Oregon, Central Otago</td><td>Gamay (Beaujolais), Nebbiolo</td></tr>
<tr><td><strong>Syrah / Shiraz</strong></td><td>Blackberry, pepper, smoke</td><td>Full</td><td>Northern Rhône, Barossa</td><td>Grenache blends, Mourvèdre</td></tr>
<tr><td><strong>Malbec</strong></td><td>Plum, blackberry, cocoa, plush</td><td>Full</td><td>Mendoza, Cahors</td><td>Shiraz, Zinfandel</td></tr>
<tr><td><strong>Tempranillo</strong></td><td>Cherry, leather, vanilla from oak</td><td>Medium to full</td><td>Rioja, Ribera del Duero</td><td>Sangiovese, Garnacha</td></tr>
<tr><td><strong>Sangiovese</strong></td><td>Sour cherry, tomato leaf, high acid</td><td>Medium</td><td>Chianti, Brunello di Montalcino</td><td>Barbera, Tempranillo</td></tr>
<tr><td><strong>Nebbiolo</strong></td><td>Rose, tar, cherry, high tannin and acid</td><td>Medium to full</td><td>Barolo, Barbaresco</td><td>Pinot Noir, Sangiovese</td></tr>
<tr><td><strong>Grenache / Garnacha</strong></td><td>Strawberry, raspberry, spice, warm</td><td>Medium</td><td>Southern Rhône, Spain, Sardinia (Cannonau)</td><td>Pinot Noir, Syrah blends</td></tr>
<tr><td><strong>Zinfandel / Primitivo</strong></td><td>Jammy blackberry, spice, ripe</td><td>Full</td><td>California, Puglia</td><td>Malbec, Shiraz</td></tr>
</tbody>
</table>

<h2>White wine grapes</h2>
<table>
<thead><tr><th>Grape</th><th>Tastes like</th><th>Body</th><th>Classic regions</th><th>If you like it, try</th></tr></thead>
<tbody>
<tr><td><strong>Chardonnay</strong></td><td>Apple and citrus (unoaked) or butter, vanilla, toast (oaked)</td><td>Medium to full</td><td>Burgundy (incl. Chablis), California</td><td>Chenin Blanc, Viognier</td></tr>
<tr><td><strong>Sauvignon Blanc</strong></td><td>Grapefruit, gooseberry, cut grass, zesty</td><td>Light to medium</td><td>Marlborough, Sancerre</td><td>Albariño, Grüner Veltliner</td></tr>
<tr><td><strong>Riesling</strong></td><td>Lime, green apple, petrol with age; bone dry to sweet</td><td>Light</td><td>Mosel, Alsace, Clare Valley</td><td>Chenin Blanc, Grüner Veltliner</td></tr>
<tr><td><strong>Pinot Grigio / Pinot Gris</strong></td><td>Pear, lemon, light (Italy) or richer, spicy (Alsace)</td><td>Light to medium</td><td>North-east Italy, Alsace, Oregon</td><td>Albariño, Vermentino</td></tr>
<tr><td><strong>Chenin Blanc</strong></td><td>Quince, honey, apple; dry to sweet</td><td>Medium</td><td>Loire (Vouvray), South Africa</td><td>Riesling, Chardonnay</td></tr>
<tr><td><strong>Albariño</strong></td><td>Peach, lemon, saline</td><td>Light to medium</td><td>Rías Baixas, Vinho Verde (Alvarinho)</td><td>Sauvignon Blanc, Vermentino</td></tr>
</tbody>
</table>

<h2>How to use this</h2>
<p>Find a grape you already like, then try the “if you like it” column. That is the fastest way to grow your range without buying blind. Notice whether you lean to the light or full end of each table; that tells you as much about your palate as any single favourite.</p>

<h2>Your own grape map</h2>
<p>Goblet builds this for you from your ratings: its Taste Profile shows the grapes, regions and flavours you score highest, and its Compass maps every bottle you have drunk on a world map with suggestions of where to explore next.</p>
''',
faq=[
('What are the main types of red wine?', 'The red grapes you will see most are Cabernet Sauvignon, Merlot, Pinot Noir, Syrah or Shiraz, Malbec, Tempranillo, Sangiovese, Nebbiolo, Grenache and Zinfandel. They range from light and silky (Pinot Noir) to full and tannic (Cabernet Sauvignon, Nebbiolo).'),
('What are the main types of white wine?', 'Chardonnay, Sauvignon Blanc, Riesling, Pinot Grigio or Pinot Gris, Chenin Blanc and Albariño cover most white wine. They range from light and zesty (Sauvignon Blanc, Albariño) to full and creamy (oaked Chardonnay).'),
('What is the smoothest red wine?', 'Wines with soft tannins and ripe fruit feel smoothest: Merlot, Grenache, Malbec and many Pinot Noirs. Very tannic grapes such as Cabernet Sauvignon and Nebbiolo feel firmer.'),
('Is Syrah the same as Shiraz?', 'Yes, it is the same grape. Shiraz is the name used in Australia and often signals a riper, fuller style; Syrah is used in France and often signals a more peppery, savoury one.'),
('Is Pinot Grigio the same as Pinot Gris?', 'Yes, the same grape. Pinot Grigio, the Italian name, is usually light and crisp; Pinot Gris, the French name, is usually richer and rounder.'),
],
related=['how-to-find-wine-you-like', 'wine-and-food-pairing', 'how-to-read-a-wine-label'],
),
# ─────────────────────────────────────────────────────────────────────────────
dict(
slug='how-to-taste-wine',
title='How to Taste Wine and Describe It Like a Pro',
description='How to taste wine step by step: look, swirl, smell, sip, finish. Plus words to describe wine, how to spot a faulty bottle and serving temperatures.',
h1='How to taste wine, and describe it',
kicker='Tasting',
intro='To taste wine properly: look at its colour, swirl it to release aromas, smell it with short sniffs, take a small sip and move it round your mouth, then notice how long the flavour lasts after you swallow. You are checking five things: sweetness, acidity, tannin, body and flavour. That is all a professional tasting is.',
body='''
<h2>The five steps</h2>
<ol>
<li><strong>Look.</strong> Tilt the glass against something white. Pale, watery whites tend to be light and young; deep gold suggests oak or age. Purple-edged reds are young; brick or orange edges mean age.</li>
<li><strong>Swirl.</strong> A few turns on the table releases the aromas. The “legs” running down the glass show alcohol and sugar, not quality.</li>
<li><strong>Smell.</strong> Short sniffs. Most of what you call taste is smell. Try to name one fruit, then one non-fruit thing (flowers, herbs, earth, spice, vanilla, toast).</li>
<li><strong>Sip.</strong> A small sip, moved round the whole mouth. Notice sweetness on the tip of the tongue, acidity making your mouth water, tannin drying your gums, and the weight of the wine.</li>
<li><strong>Finish.</strong> After swallowing, count how long the flavour lasts. A long finish is one of the surest signs of a well-made wine.</li>
</ol>

<h2>Words that describe wine</h2>
<table>
<thead><tr><th>If the wine is</th><th>People say</th></tr></thead>
<tbody>
<tr><td>High in acid</td><td>Crisp, fresh, zesty, bright, lively</td></tr>
<tr><td>Low in acid</td><td>Soft, round, flabby (if too low)</td></tr>
<tr><td>Tannic</td><td>Firm, grippy, structured, astringent</td></tr>
<tr><td>Low in tannin</td><td>Silky, smooth, supple</td></tr>
<tr><td>Full-bodied</td><td>Rich, big, weighty, opulent</td></tr>
<tr><td>Light-bodied</td><td>Delicate, elegant, light</td></tr>
<tr><td>Oaked</td><td>Vanilla, toast, coconut, smoke, spice</td></tr>
<tr><td>Aged</td><td>Leather, mushroom, dried fruit, tobacco, honey (whites)</td></tr>
</tbody>
</table>

<h2>How to tell if a wine is faulty</h2>
<ul>
<li><strong>Corked</strong> (cork taint): musty, wet cardboard, damp basement; the fruit seems muted.</li>
<li><strong>Oxidised</strong>: flat, brown-tinged, smells of bruised apple or sherry when it should not.</li>
<li><strong>Heat-damaged</strong>: stewed, jammy, cooked fruit; the cork may have pushed up.</li>
</ul>
<p>Sediment and tartrate crystals (“wine diamonds”) are harmless.</p>

<h2>Serving temperatures</h2>
<table>
<thead><tr><th>Wine</th><th>Serve at</th></tr></thead>
<tbody>
<tr><td>Sparkling, light whites, rosé</td><td>6–10 °C (43–50 °F)</td></tr>
<tr><td>Full whites (oaked Chardonnay)</td><td>10–13 °C (50–55 °F)</td></tr>
<tr><td>Light reds (Pinot Noir, Beaujolais)</td><td>12–15 °C (54–59 °F)</td></tr>
<tr><td>Full reds (Cabernet, Syrah)</td><td>15–18 °C (59–65 °F)</td></tr>
</tbody>
</table>
<p>“Room temperature” for reds means a cool room. A warm red tastes alcoholic; twenty minutes in the fridge helps.</p>

<h2>Keep what you learn</h2>
<p>Tasting only teaches you something if you remember it. In Goblet you rate each wine out of 10 and keep notes in your Winery; every rating sharpens the next recommendation.</p>
''',
faq=[
('What are the steps of wine tasting?', 'Look at the colour, swirl the glass, smell with short sniffs, take a small sip and move it around your mouth, then notice the finish: how long the flavour lasts after you swallow.'),
('What does it mean when wine has legs?', 'Legs or tears are the streams that run down the glass after swirling. They show the alcohol and sugar content, not the quality of the wine.'),
('How can you tell if wine has gone bad?', 'A corked wine smells musty, like wet cardboard. An oxidised wine tastes flat and smells of bruised apple or sherry, and may look brownish. Heat-damaged wine tastes stewed or cooked.'),
('What temperature should red wine be served at?', 'Light reds such as Pinot Noir at about 12 to 15 °C (54 to 59 °F); full reds such as Cabernet Sauvignon at about 15 to 18 °C (59 to 65 °F). Most reds are served too warm.'),
('What does a long finish mean in wine?', 'The finish is how long the flavour lingers after you swallow. A long finish, of several seconds or more, is generally a sign of a well-made, concentrated wine.'),
],
related=['how-to-find-wine-you-like', 'wine-grapes-explained', 'wine-ratings-explained'],
),
# ─────────────────────────────────────────────────────────────────────────────
dict(
slug='wine-ratings-explained',
title='What Wine Scores Mean: 90 Points, Stars and 10/10',
description='What a 90-point wine score means, how critic scores and crowd star ratings work, why they disagree, and how a score for your own palate differs.',
h1='What wine scores mean',
kicker='Wine ratings',
intro='Wine scores come in three kinds. Critic scores, usually out of 100, are one expert’s judgement of quality: 90 and above means outstanding. Crowd ratings, usually out of 5 stars, average many drinkers’ opinions. A personal score predicts how much you in particular will enjoy the wine. They answer different questions, which is why they often disagree.',
body='''
<h2>Critic scores: the 100-point scale</h2>
<p>The 100-point scale was popularised in the 1980s by the critic Robert Parker and is used by publications such as Wine Spectator and Wine Enthusiast. In practice only the top part of the scale is used:</p>
<table>
<thead><tr><th>Score</th><th>What it generally means</th></tr></thead>
<tbody>
<tr><td>95–100</td><td>Classic, extraordinary</td></tr>
<tr><td>90–94</td><td>Outstanding</td></tr>
<tr><td>85–89</td><td>Very good</td></tr>
<tr><td>80–84</td><td>Good, sound</td></tr>
<tr><td>Below 80</td><td>Rarely published</td></tr>
</tbody>
</table>
<p>Exact bands vary by publication. A score is a judgement of quality and typicity by an experienced taster. It is not a prediction of whether you will like the wine: a 96-point, very tannic young Barolo is a superb wine that many people will not enjoy tonight.</p>

<h2>Crowd ratings: stars out of 5</h2>
<p>Scanner apps show the average star rating of everyone who rated a wine. Averages are useful for spotting duds and crowd-pleasers, but they bunch together in a narrow band, and they reward wines that please the most people. If your taste is anywhere off the middle, the crowd’s favourite is not yours.</p>

<h2>Why scores disagree</h2>
<ul>
<li><strong>Different questions.</strong> Critics judge quality; crowds report enjoyment; both are averaged over people who are not you.</li>
<li><strong>Different palates.</strong> Some critics prefer ripe, powerful wines; others fresh and restrained.</li>
<li><strong>Bottle and context.</strong> Vintage, storage and food change how the same wine shows.</li>
</ul>

<h2>A score for your palate</h2>
<p>Goblet’s score answers the only question that matters at the moment of choosing: <em>how much will I like this?</em> It is out of 10, on the same scale you rate wines with, and it comes from your own ratings rather than critics or crowds. A famous bottle that does not suit you scores low, and it should. Each pick comes with a plain-English reason, in terms of wines you have already rated.</p>
''',
faq=[
('What does a 90-point wine mean?', 'On the 100-point scale used by critics, 90 to 94 means outstanding. It is one expert’s judgement of the wine’s quality, not a guarantee that you will enjoy it.'),
('Who invented the 100-point wine rating scale?', 'The critic Robert Parker popularised the 100-point scale in the 1980s through his newsletter The Wine Advocate. Publications such as Wine Spectator and Wine Enthusiast use similar scales.'),
('Is a 4-star wine on a wine app good?', 'A high crowd rating means many people enjoyed the wine. Because crowd averages bunch in a narrow range and favour crowd-pleasing styles, it does not tell you whether you personally will like it.'),
('Why do wine critics and apps give different scores?', 'They answer different questions. Critics judge quality and typicity; app ratings average the enjoyment of many drinkers. Neither is built around your own palate.'),
('Is there a wine rating based on my own taste?', 'Yes. Goblet scores wines out of 10 for your palate, learned from a short quiz and the wines you rate, and explains each score in plain English.'),
],
related=['best-wine-apps', 'how-to-find-wine-you-like', 'how-to-buy-wine-at-a-store'],
),
]

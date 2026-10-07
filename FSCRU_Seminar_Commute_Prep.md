# FSCRU hop seminar — commute prep and speaker notes

**Wed 7 Oct 2026 · Hamilton Hall, WSU IAREC, Prosser, WA · seminar 8:30** · Sections 1–4 are a ~10 min read for the first flight. Section 5 has the speaker notes plus a spoken script for each slide (~25 min, second flight). Section 6 is what the web check on 6 Oct changed.

_The bullet lines under each slide heading in section 5 **are** the deck's speaker notes. Edit here, then run `make sync` (or `python3 tools/speaker_notes.py update --from FSCRU_Seminar_Commute_Prep.md`); or edit in the deck and run `python3 tools/speaker_notes.py extract --into FSCRU_Seminar_Commute_Prep.md`. Only the lines directly under a heading are notes — the quoted script below them is not._

---

## 1. Today and tomorrow

**Tue 6 Oct — getting there**

| Time | What |
|---|---|
| 12:43 | Alaska 3006 EUG → PDX, seat 13A (conf. EIBRXU). Read sections 1–4 |
| 1:35 → 2:30 | PDX layover, 55 min |
| 2:30 | Alaska 2108 PDX → PSC, seat 20A. Read section 5 |
| 3:24 | Land Pasco. Hertz compact (conf. L715E790554), return Thu 6:01 AM |
| Evening | Drive to Prosser (~50 min). **Run the deck once, out loud, with a timer** (`s` for the speaker view). Check the videos play from disk |

**Wed 7 Oct — interview day** (from Dr. Hayes)

| Time | What |
|---|---|
| 8:15 | Meet Dr. Hayes at the Hamilton Hall reception desk, 24106 N Bunn Rd. Set up. **Ask who is in the room and who is remote** (the panel is known — §4c) |
| **8:30–10:00** | **Seminar: 45–50 min talk + 20–30 min questions** (audience: ARS, WSU, industry) |
| 10:00–11:00 | Q&A with the evaluation panel |
| 11:00–12:00 | Facilities tour (Hayes, Gonzalez Tapia) |
| 12:00–1:30 | Lunch with industry stakeholders |
| 1:30–2:00 | Dr. Naidu Rayapati, IAREC Director |
| 2:00–3:00 | USDA hop research team (Gent, Gonzalez Tapia, Altendorf) |
| 3:00–4:00 | FSCRU scientists (virtual and in person) |
| 4:00–5:00 | Wrap-up with Dr. Hayes |

**Thu 8 Oct** — Alaska 2314 PSC 6:01 AM → SEA (10A) → Alaska 2176 SEA 8:00 → EUG 9:17 (13D). Car back by ~5:15.

## 2. Eight things to get right

1. **This hire is the cultivar developer.** The posting's first objective is cultivars and its last is adoption. Every method in the talk ends with "and that's how more good hops reach growers and brewers sooner."
2. **Water is the Yakima abiotic stress.** 2025: junior water rights got **40%** of a full supply. 2026 is the **fourth drought year**; junior supply was 52% in June and 60% by September. Don't quote 40% as this year.
3. **Aroma moves under stress; bitterness doesn't.** Dr. Gonzalez Tapia's lapse trials: alpha and beta stable, oil down, monoterpenes down and sesquiterpenes up. Brewers buy aroma. It's his result — cite it to him, don't explain it to him.
4. **Team, not rival.** Genomics, HopBox, DArTag and the 2026 GWAS are Dr. Altendorf's group; mildew races are Dr. Gent's; water physiology is Dr. Gonzalez Tapia's. Say "with your program," never "instead of." HopBox already images cones — plug in.
5. **The fit is close — say it, then say the three differences.** Hop and cranberry are both clonal, highly heterozygous perennials mapped in F1 full-sib families. Differences: dioecy (half of each family is male), North American vs European chromosome structure (suppressed recombination, the chr 6 inversion), and the 18-ft trellis.
6. **Your abiotic work is escape by timing, not tolerance physiology.** The LMI selects for late-but-fast spring greening. Say "the method transfers, not the stress."
7. **Only disease trait: cranberry fruit rot** (a fungal complex). Don't claim mildew work. R6 broke in 2012 — durability is the lesson.
8. **Half the room is industry — and four of the seven panel seats** (Coleman, Stevens, Elliot, Adler). Lead every aim with the grower or brewer outcome; use grower units (pounds per acre, per acre-foot); define QTL, h² and genomic prediction once (`qtl-plain`).

## 3. Pacing (46 min timed · totalTime 2760 s)

| Checkpoint | Minute |
|---|---|
| End of opening (`scale`) | ≈ 4.5 |
| End of model system (`frost`) | ≈ 7.75 |
| End of meta-QTL block (`ch2-takeaways`) | ≈ 15.75 |
| End of UAV block (`ch3-takeaways`) | ≈ 26.25 |
| End of LMI genetics (`ch4-takeaways`) | ≈ 33.25 |
| Outreach done → vision starts | **34.75** |
| Five-year deliverables | 45 |
| Summary + thanks | 46 |

The brief says the vision is the **last 5–10 minutes**; it's timed at 10.25 with the summary. **If the room starts late:** skip `vision-not-claiming` (keep its lines for questions) and take `vision-adoption` in one sentence → ~8.5 min vision. If behind in the research half: one sentence each on `ch3-indices`, `ch4-qtl`, `ch2-vaccap`. Never cut into the 20–30 minutes of questions.

## 4. Numbers to have ready

| Topic | Number | Why it matters | Source |
|---|---|---|---|
| U.S. industry 2025 | 41,654 acres · 83.1 M lb · $447.5 M · $5.38/lb · 1,996 lb/acre | Scale; acreage down 23% since 2023 | USDA NASS via Capital Press, Dec 2025 |
| Washington | 31,198 acres (75%) · 62.1 M lb · $329.1 M | Prosser is the center of U.S. hops | same |
| Water | 2025: junior supply 40% · 2026: fourth drought year, 52% (June) → 60% (Sept) | Abiotic stress = water | USBR forecasts; Capital Press Aug 2025 |
| Late-season lapse | 15 d: −9.5% yield, total oil −19%, geraniol −20.8%, linalool −11.4%, humulene +9.1%, caryophyllene +12.4% · 30 d: −28.8% yield · alpha/beta stable | Aroma is the stress-sensitive quality trait | Gonzalez Tapia 2025, *JASHS* 150:136 |
| Deficit irrigation | 60% of crop water: yield −19% Chinook, −25% Columbus, −30% Mt. Hood, −33% Willamette; alpha/beta unchanged · 80%: Columbus +2% | Cultivars differ almost twofold — genetic opening | Nakawuka, Peters, Kenny & Walsh 2017, *Ind. Crops Prod.* 98:82 |
| Physiology | stomata close early · bine growth stops below ~−0.8 MPa · P<sub>50</sub> ≈ −1.6 MPa | Why canopy temperature is the proxy | Gloser et al. 2024 |
| Europe and heat | 1995–2018 vs 1971–1994: yield −9.5 to −19.4%, alpha −10.5 to −34.8%, ripening ~20 d earlier · 2050: yield −4–18%, alpha −20–31% | The warming signal | Mozny et al. 2023, *Nat. Commun.* |
| Seedling prediction | cone traits predictive 75–85% of the time; agronomic 38–56%; Spearman 0.78–0.82 vs 0.52–0.64; dense nursery +717% individuals; only plots represent yield | Why plots are the bottleneck | Altendorf, Heineck & Tawril 2025, *Crop Sci.* 65:e70024 |
| GWAS | 529 females · 20,861 SNPs · 49 MTAs at 43 loci · 5 traits · H² 0.32–0.71 · NIR R 0.54–0.94 · allele stacks | Training set for prediction | Clare, Schmuker & Altendorf 2026, *Plant Genome* 19:e70238 |
| Sex marker | SM1 PACE assay, 96% accurate; GWAS on 765 hops | Sex at the seedling | Clare et al. 2024, *G3* |
| Apollo genome | NA + EU haplotypes · 52,593 presence + 41,990 absence variants · 4,438 translocations · 215 inversions · ~85 Mb chr 6 inversion (~500 genes) from Brewer's Gold (wild Manitoba female, 1916) · recombination suppressed · additive NA + EU bitter-acid alleles | Two ancestries in every U.S. hop | Kale … Braumann 2026, *Nat. Commun.* |
| Cascade genome | 3.71 Gb assembled · 10 pseudochromosomes · 30,404 genes · 64% repeats · heterozygosity 4.6–5.5% | HopBase coordinates (named in the posting) | Padgitt-Cobb … Hendrix 2023 |
| Powdery mildew | R genes Rb, R1–R6 · V6 strains WA/ID 2012 · Comet chr 6 308–314 Mb (~140 genes, 27 R-related) · 7 multi-race lines from 102 WSU genotypes | Durability; what's already in hand | Gent 2017; Henning 2024; Altendorf 2025 |
| Releases | Cascade 1972 · Chinook 1985 · Vista 2021 (3x) · Vera 2025 · Thora Oct 2025 (Wye Northdown × USDA 21327M; collaboration from 2015) · EdleFrucht 2025 | The program's own history | primer; HGA release |
| Program | ARS project 2072-21000-061-000D (from Mar 2023) · 10 acres of hop yard · ~5,500 sq ft lab, greenhouse, picking and drying space | What the job comes with | posting; ARS |
| Your meta-QTL | 235 F1 seedlings (168 + 67), 3 seasons each · 40 traits · 1,542 QTL → 22 meta-QTL | Large populations, multiple years | Maule et al. 2024 |
| Your Flex-Seq | 17,502 loci · 99.8% recovery · 192 accessions · fruit rot 1 → 4 QTL · flagged a likely mislabelled parent | Markers + identity | Clare et al. 2026 |
| Your UAV | 597 genotypes · 3 populations · 2 sites · 8 dates · RF R² 0.95 · median CV 3.9% (n = 10,489) | Repeatable plot phenotype | under review |
| Your LMI | h² 0.74 · 11 QTL, 1.8–9.1% each | Heritable timing trait | in prep, *G3* |

## 4b. Don't say (couldn't confirm, or wrong)

- **"40%" as this year's water.** That was 2025. 2026: 52% → 60%, fourth drought year.
- **"Braumann et al." for the Apollo genome.** First author is **Sandip Kale**; Ilka Braumann (Carlsberg) is last. Say "the Carlsberg-led Apollo genome." (Hopsteiner's Pitra and Matthews are co-authors.)
- **That Altendorf works in Prosser.** The Brewers Association 2026 pre-harvest roundup says she moved to Corvallis to oversee both stations after Henning retired. Confirm at 8:15 or at 2:00.
- **Shaun Clare's current employer** (LinkedIn may say Carlsberg). Ask, don't assert.
- **A release year, a "drought-proof" hop, a DArTag marker count or a genotyping price.**
- **That you've worked on mildew, drought physiology or hop**, or called a triploid. Your disease trait is cranberry fruit rot; your polyploid tools were used on diploid data.
- **"Hallertau 736 AD"** or other folklore dates. Details of the hop FT-like flowering paper, Gonzalez Tapia 2026 *HortScience*, or the PLOS One KASP fingerprinting set (none read in full).
- **Chinook or Centennial breeding details** beyond "Chinook, 1985, from Prosser."
- **The thesis R² 0.886** (the paper's is 0.95). **"Leaf" vs "late" maturity index:** the deck says *late*; ⚠ the manuscript may say *leaf* — pick one before the room and stick to it.
- **Walt Mahaffee's or Zhiwu Zhang's roles** (from memory, not checked).
- **"Colemen."** The brief misspells it; every public source says **Coleman** (Max Coleman, Coleman Agriculture).
- **Diane Gooding as HRC vice president** — she is **President** (2026 officer list). **Ann George as WHC director** — Jessica Stevens is executive director (George's successor; confirm).
- **Pronouns for Dr. Liu** — sources differ. Say "Dr. Liu."
- **Dr. Gonzalez Tapia's 2025 firing and reinstatement** — know it, don't raise it. **Labor or immigration politics** with Coleman or anyone — stay on harvest efficiency.
- **Weeds as a hop breeding priority.** Two honest links only: early vigor and canopy closure; cultivar sensitivity to stripping herbicides as a pre-release check.

## 4c. People you might meet

Full profiles: `../../people/` (one file per person); day overview: `../../people/_Panel_and_Audience_Overview.md`. The deck names them on `vision-fit` (roles on the slide, names aloud) and by name on `backup-partners`; one line per panelist on the hidden `prep-panel` slide.

**Evaluation panel, 10:00–11:00** — 2 ARS, 1 WSU, 4 industry. No hop breeder, pathologist or genomicist on it.

- **Francisco "Paco" Gonzalez Tapia** — ARS Research Horticulturist, Prosser (FSCRU); hop water and heat stress. Your closest collaborator; also leads the tour. G × water on his lapse plots; credit his *JASHS* 2025 lapse paper.
- **Max Feldman** — ARS Research Geneticist (potato), Prosser (TTFVRU); machine-vision tuber phenotyping (with Rippner); earlier *Setaria* WUE-components genetics (*Plant Physiol.* 2018). Will test whether an image trait is real and which WUE component you mean. Background: `../../prep/WUE_Components_Literature_Review.md`.
- **Rui Liu** — WSU Assistant Professor and Extension Weed Specialist, IAREC (since Nov 2022). The WSU voice: partners by name, on-farm trials, co-advised students, field days. "Dr. Liu."
- **Max Coleman** — seventh-generation grower, director of farm operations, Coleman Agriculture (St. Paul, OR; Yakima Chief grower-owner). Would he plant it? Yield parity, mildew, picking date, kiln drying, Oregon testing. Plain field language.
- **Jessica Stevens** — Executive Director, Washington Hop Commission (also HGW/HGA). Grower engagement (Obj. 6), grower value, follow-through. Ask: "What would success look like in three years?"
- **Maggie Elliot** — Science & Communications Director, WHC/HGA. Plain language; resistance → fewer sprays → fewer MRL problems; water.
- **Alicia Adler** — Executive Technical Director, Hop Research Council (Bryant Christie); leads the Hill Climb. The PHBAC → grow-out → Hopsource pipeline; year-three milestones funders can see.

**Everyone else**

- **Ryan Hayes** — FSCRU Research Leader (Corvallis), your contact, runs the tour and the wrap-up. Sits on the Public Hop Breeding Advisory Committee.
- **Kayla Altendorf** — Research Geneticist, FSCRU; HopBox, single-hill prediction, the 2026 GWAS, 'Vera', the seven multi-race mildew lines; now in Corvallis overseeing both stations (⚠ confirm). Your closest partner.
- **David Gent** — Research Plant Pathologist, Corvallis; powdery and downy mildew races, risk models, fungicide/MRL economics.
- **Francisco "Paco" Gonzalez Tapia** — Research Horticulturist, ARS Prosser (since 2022); late-season irrigation lapses, hop stress physiology. Co-located with you.
- **Naidu Rayapati** — IAREC Director (grape virologist). 30 minutes at 1:30: the WSU partnership question.
- **Also at Prosser (ARS):** Devin Rippner (soil CT and deep learning; HopBox co-author), Phil Miklas (dry bean breeder — he breeds *cranberry* beans), Brian Irish (WRPIS forage-legume curator; germplasm mechanics). With Feldman and Gonzalez Tapia: a shared imaging core.
- **WSU IAREC:** Lav Khot (UAV sensing; AgWeatherNet; CPAAS), Troy Peters (irrigation; CPAAS director; **co-author of the deficit-irrigation hop paper**), Doug Walsh (mites and aphids; state IPM coordinator; **also a co-author**), David James (biocontrol), Scott Harper (viroids), Sudarsana Poojari (Clean Plant Center Northwest director), Markus Keller (grape cold hardiness and water), Per McCord (cherry breeding; ex-ARS sugarcane), Gwen Hoheisel (Benton County Extension; precision spraying with Khot). Sindhuja Sankaran (phenomics, VOC sensing) is in Pullman.
- **FSCRU scientists, 3:00 (Corvallis, partly virtual):** Hannah Rivedal (pathology: grass seed, hemp — Cannabaceae link), Kristin Trippe (soil microbiology), Joseph Gallagher (cool-season grass genetics; title to confirm), Seth Dorman (entomology; title to confirm).
- **Lineage:** John Henning (retired Jan 2026; Cascade genome, HopBase, Thora; courtesy OSU) — credit him. Stephen Kenny (former WSU hop breeder) — credit his program for the WSU females.
- **Stephen Kenny** — former WSU hop breeder; bred the material behind 'Vera'; co-author on the deficit-irrigation paper.
- **Industry (lunch, 12:00):** the four industry panelists plus possibly Diane Gooding (HRC **President**; Gooding Farms, Parma ID — offer Idaho as a third site), Chuck Skypeck (Brewers Association; runs Hopsource; PHBAC), Eric Desmarais (CLS Farms; Thora grower), Jason Perrault (Select Botanicals; Simcoe/Citra/Mosaic — talk shared problems, not competition); Ann George (former WHC/HGA executive director). Private programs: Hop Breeding Company, Yakima Chief Ranches, Hopsteiner, Select Botanicals.
- **OSU:** Shaun Townsend (Indie Hops aroma breeding, 'Strata'), Tom Shellhammer (brewing chemistry), David Hendrix (Cascade genome, HopBase).
- **Shared colleague:** Shaun J. Clare — first author of your Flex-Seq paper *and* of the hop sex-marker and 2026 GWAS papers with Altendorf.

## 4d. Q&A — short answers

- **Hayes — "What does year one look like?"** Plant out and evaluate the WSU females and the multi-race lines; put a thermal camera and an RGB cart on Dr. Gonzalez Tapia's irrigation plots; write the hop meta-QTL synthesis on Cascade/Apollo coordinates; meet growers, brewers and the HRC. And learn the picking and drying line.
- **Hayes — "How will you run a breeding program with one technician?"** Automation first; genotyping as a service; pipelines that rerun without a bioinformatician; dense seedling nurseries plus the sex marker so labor goes to females that matter.
- **Altendorf — "HopBox already images cones. What do you add?"** The plot and the season: canopy, timing and water response, measured weekly, at plot scale. HopBox stays the cone instrument.
- **Altendorf — "How would you handle segregation distortion and the NA × EU structure?"** Map distortion as biology; build parental maps; check order against both Apollo haplotypes; expect suppressed recombination around the chr 6 inversion and choose parents with matching arrangements to fine-map. (`backup-cp-mapping`, `backup-hop-genome`)
- **Altendorf — "Genomic prediction with what training data?"** DArTag on every seedling family, the 529-female GWAS panel as a base, plot data from Prosser and Corvallis. Start with cone chemistry (high H²), add yield and water use as plots accumulate.
- **Altendorf — "How would you choose males?"** Sex marker at the seedling; genomic values for cone traits from female relatives; validate with progeny tests; fit the X separately. (`backup-dioecy`)
- **Gent — "How do you think about mildew resistance?"** Stack major genes on a quantitative background (Comet, the multi-race lines) with markers; never deploy a single R gene alone; screen with his races. Measure severity continuously only if it helps his program.
- **Gonzalez Tapia — "How would you phenotype water-use efficiency at scale?"** Genotype × water design on his lapse plots; canopy temperature in fixed midday windows with wet/dry references; bine growth and top-wire date from imagery; yield and oil per acre-foot. Check repeatability before heritability.
- **Gonzalez Tapia — "Isn't canopy temperature confounded by vigor and trellis position?"** Yes — fit vigor (cover, LiDAR volume) and time of day as covariates; use the full-vs-reduced water contrast within a genotype, not raw temperature.
- **Rayapati / Liu — "How would you work with WSU?"** Khot on sensing and AgWeatherNet covariates; Peters on irrigation; Walsh on mites; Harper and Poojari on viroids and clean stock for releases; Hoheisel for field days; co-advise WSU students through an adjunct appointment. (`backup-partners`)
- **Feldman — "How do you know an image-derived trait means anything?"** Ground truth against manual scores; repeatability across flights and dates (median CV 3.9%); h² (LMI 0.74); genetic correlation with the target; QTL near plausible biology. Report what failed too.
- **Feldman — "Which component of WUE are you selecting on?"** Not instantaneous WUE. In field plots: the stress response — when each line's canopy warms during a lapse, how far, how fast it recovers — plus yield and quality stability, each line against its own full-water plot. Components have different genetics (his *Setaria* paper), so keep transpiration and growth terms separate where possible.
- **Feldman — "How do you handle spatial and temporal noise in UAV data?"** Spatial mixed models, flight-date effects, radiometric panels, fixed solar time, growth-curve parameters rather than single dates.
- **Liu — "How will you run on-farm trials and keep management from confounding them?"** Shared protocols, a check cultivar at every site, randomized and replicated plots with spatial correction, management records as covariates; results to cooperators first.
- **Coleman — "What would you breed that I'd actually plant?"** Mildew-resistant aroma and dual-purpose hops at yield parity that cut sprays; spread harvest dates so picking and kiln capacity aren't jammed; confirmed brewer demand before acres.
- **Coleman — "Will it work in Oregon?"** Multi-environment testing is central: Prosser, Corvallis and grower sites in Oregon (and Idaho). The Willamette's downy mildew pressure is a selection environment the Yakima can't give.
- **Stevens — "How will you engage Washington growers?"** The commission's annual meeting and research committee, IAREC field days, on-farm cooperators, results back to cooperators first.
- **Elliot — "How does breeding help with residues and MRLs?"** Resistant cultivars mean fewer fungicide applications and less EU residue risk; Gent's group has quantified the savings from host resistance.
- **Adler — "How would you work with the advisory committee and HRC?"** Bring lines to PHBAC with full agronomic, disease, chemistry and stress data; use grow-outs and Hopsource as formal selection stages; feed brewer scores into selection indices.
- **Adler — "How will we know you're succeeding at year three?"** Crosses and seedlings evaluated, lines advanced, a heritable stress phenotype published, germplasm deposited, outreach events held.
- **Industry — "When will growers get a drought-tolerant variety?"** Years, not months; public releases take about a decade. The first deliverable is a ranking of existing advanced lines under reduced water — usable sooner.
- **Industry — "Can a public program compete with Citra and Mosaic?"** It doesn't have to: the public role is mildew resistance, water resilience, open germplasm and brewer-defined aroma (Thora's thiols) that private programs won't prioritise.
- **Industry — "How do brewers fit in?"** Hopsource ratings, pilot brews on advanced lines, and a standing panel modelled on the Hop Quality Group's.
- **"Why leave cranberry for hops?"** Same breeding structure, a bigger industry with a public mission, and a stress problem — water — where measurement is the bottleneck I've worked on.
- **"Why so much phenotyping?"** Markers and prediction are only as good as the phenotypes they're trained on.
- **"Triploid seedless cultivars?"** Dosage-aware calling (updog, polyRAD) and polymapR/MAPpoly for the 4x × 2x side — tools I've used on diploid data, ready for that work.
- **"What do you need?"** A technician, a thermal camera, a cart I can build, genotyping as a service, and greenhouse and nursery space for seedlings.

---

## 5. Slide-by-slide cues (= speaker notes in index.html) and what to say

*Bullets are the current speaker notes. The quoted block under each is a fuller spoken version; italics in brackets are stage directions.*

### A. Opening

**[`title-new`](http://localhost:8000/presentation/#/title-new)** · 0.5 min
- **Say:** "Thank you to Dr. Hayes and the panel for the invitation." Cranberry is the case study; the title is the whole talk.
- "Bog to bine" — say what a bine is once, for the non-hop people in the room.
- Don't read the title. Advance.

> Good morning, and thank you to Dr. Hayes, the panel, and everyone from ARS, WSU and the industry for being here. The title is the shape of the talk: I work on cranberry, a bog crop, and I'll spend most of my time showing what I've built there — and the last ten minutes on what it would mean for the bines here in the Yakima Valley. *[Advance.]*

**[`path`](http://localhost:8000/presentation/#/path)** · 1 min
- The brief asks for a biographical sketch — this is it. Four steps, left to right.
- **Say:** "I treat phenotyping and genotyping as engineering problems; breeding gives them a purpose."
- Ten years of avionics = instruments characterized before they are trusted — and rigs that keep running.

> A brief sketch, since many of you haven't seen my CV. I studied computer engineering at Georgia Tech and spent about ten years building embedded and avionics software — real-time systems, sensors, certification. My interest in plants took me to a PhD in Plant Breeding and Plant Genetics at UW–Madison, in Juan Zalapa's lab with the USDA-ARS Vegetable Crops Research Unit, finished last December. I'm now a research associate across the Digman and Zalapa labs. That background is why I treat phenotyping and genotyping as engineering problems: an instrument gets characterized before anyone trusts its numbers, and a field rig has to keep running after the person who built it goes home.

**[`cycle`](http://localhost:8000/presentation/#/cycle)** · 1 min
- **Say:** "The clone doesn't grow faster. What changes is how many seedlings you can afford to judge, and how early you know."
- Walk the bar: seedlings → nursery (sex, chemistry) → replicated plots at two stations → grow-outs and brewing trials → release. ~10 years; Thora 2015 → Oct 2025. Phase lengths illustrative — invite Dr. Altendorf and Dr. Hayes to correct them.
- Three levers: markers at the seedling · plot traits that are numbers · brewers and growers earlier.

> Let me be precise about what can go faster in hop breeding. *[Walk the bar.]* A cross, greenhouse seedlings, a seedling nursery where you learn sex and cone chemistry, replicated plots at two stations for yield and mildew, then grower grow-outs and brewing trials before release. Thora took from 2015 to last October. These phase lengths are illustrative — please correct me. The clone doesn't grow faster. What changes is how many seedlings you can afford to judge, and how early you know: markers at the seedling, plot traits that are numbers, and brewers and growers seeing advanced lines sooner. *[Point at the green loop.]* And that data decides which parents — and which males — you cross next.

**[`map`](http://localhost:8000/presentation/#/map)** · 1 min
- Left: the posting's six research objectives, in its words. Right: where I've done something comparable. State publication status once.
- Point at row 3 — the phenotyping objective is "almost word for word" what my UAV work did.
- Row 6 is outreach — there's a slide on it before the vision.

> Here's the map for the talk. On the left are the six research objectives in the announcement, in its own words; on the right, where I've already done something comparable. The meta-QTL study is published; the spring-greening paper is under review; the LMI genetics paper is in preparation; and I'm a co-author on a genotyping platform, a flavonoid review, and BerryPortraits with Breeding Insight. *[Point at row 3.]* This one — phenotyping that increases the precision, frequency, type and volume of data at the plot scale — describes what my drone work did almost word for word.

**[`scale`](http://localhost:8000/presentation/#/scale)** · 1 min
- The brief's first ask: "trait data on large populations … across multiple environments." Four numbers, left to right.
- 235 F1 seedlings (168 + 67), three seasons each · 40 traits · 597 genotypes, 3 populations, 2 sites, 8 dates · 10,489 repeated plot images.
- Markers: GBS, then the 17,502-locus Flex-Seq panel across 192 accessions.

> The brief asked about collecting trait data on large populations across environments, so here's the scale up front. Two F1 mapping families — 235 seedlings — phenotyped for three seasons each. Forty traits per plant and plot. In the drone work, 597 genotypes from three populations, at two sites, on eight dates across two years. And more than ten thousand repeated plot images, scored again specifically to test whether a phenotype repeats. On the marker side: genotyping-by-sequencing, then a 17,502-locus targeted panel validated across 192 accessions.

### B. Cranberry as a model system

**[`background`](http://localhost:8000/presentation/#/background)** · 0.75 min
- Perennial, clonal, slow — say the hop word with each ("like a hop yard, you wait years").
- Cranberry is diploid like hop; it's self-compatible but bred from outcrossed, heterozygous clones.

> Briefly, the crop. Cultivated cranberry is a perennial of acidic bogs, native to eastern North America. What matters for this room: it's clonally propagated, it takes three to five years to establish a bed, and six to eight years to evaluate a selection. Like a hop yard, you wait years to see what you've got — and you're selecting a clone, not a seed line.

**[`why-hops`](http://localhost:8000/presentation/#/why-hops)** · 1.25 min
- Left: shared problems. **Say:** "The population genetics of my PhD crop and of hop are nearly the same." Then the three differences: dioecy, NA × EU structure, the trellis.
- Right: Altendorf 2025 — seedling hills predict cone traits 75–85% of the time, agronomic 38–56%; only plots represent yield.
- **Say:** "The traits that pay live in plots, where measuring is most expensive."
- **⚠** Your disease trait is cranberry fruit rot, a fungal complex. Don't claim mildew work.

> Why should a hop audience care about cranberry? *[Left.]* The breeding problems are shared: a clonal perennial; highly heterozygous parents, so mapping happens in F1 full-sib families — the same design; value set by chemistry as much as yield; wild North American germplasm in the pedigrees; and clone identity in growers' fields. The population genetics of my PhD crop and of hop are nearly the same. The honest differences are three: hop is dioecious, so half of every family is male and never makes a cone; the North American and European chromosome sets differ in structure, so recombination is suppressed; and the canopy is an eighteen-foot hedgerow. *[Right.]* And there's a shared measurement problem. Dr. Altendorf's group showed seedling hills predict plot performance for cone traits most of the time — but not for yield. The traits that pay live in plots, where measuring is most expensive. Cranberry taught me to make plot traits cheap and repeatable.

**[`qtl-plain`](http://localhost:8000/presentation/#/qtl-plain)** · 0.5 min
- For the industry half of the room. One sentence per term; point at the two clouds.
- QTL · heritability · genomic prediction ("rank a male on cones he'll never make"). Then don't define them again.

> Three terms I'll use, in plain words. *[Point at the picture.]* A QTL is a stretch of chromosome where the DNA differs between plants and the trait differs with it — so its marker can be read on a seedling years before the hill is harvested. Heritability is the share of the differences between plants that's genetic. And genomic prediction estimates a plant's breeding value from DNA across many small QTL — which means you can rank a male on cones he will never make.

**[`frost`](http://localhost:8000/presentation/#/frost)** · 0.75 min
- **Say:** "When is the crop exposed, and can genetics move the window?"
- **Hop:** the Yakima exposure windows are water cut off before harvest and heat while the cones fill.

> Here's the abiotic problem in grower terms for cranberry. Buds are hardy in winter and vulnerable once they swell, so growers flood or sprinkle on frost nights — and every night costs water, energy, labor and sleep. Genetics could shorten that window or shift it. The Yakima Valley asks the same question of water and heat: irrigation cut off before harvest, heat while the cones fill. When is the crop exposed, and can genetics move the window?

### C. Meta-QTL synthesis — Maule et al. 2024 + Clare et al. 2026

**[`ch2-title`](http://localhost:8000/presentation/#/ch2-title)** · 0.25 min
- **Say:** "My most polished work and the least hop-specific — so I'll sell the method, not the loci."

> The first study is my meta-QTL paper, published in Frontiers in Plant Science in 2024. It's my most polished work and the least hop-specific, so I'll sell the method, not the loci.

**[`populations-map`](http://localhost:8000/presentation/#/populations-map)** · 0.75 min
- CNJ02 (168) and CNJ04 (67); three seasons each; composite map, 12 LGs, 1,560 bins.
- Hop parallel: Newport × 21110M and Comet × a susceptible male are the same F1 design. One minute max.

> We used two mapping populations: CNJ02, Mullica Queen by Crimson Queen, 168 seedlings, and CNJ04, Mullica Queen by Stevens, 67 — each phenotyped over three seasons and placed on one composite map of 12 linkage groups and about 1,560 bins. These are F1 families from two heterozygous parents — the same design as your Newport and Comet mildew populations. *[One minute, then move on.]*

**[`ch2-workflow`](http://localhost:8000/presentation/#/ch2-workflow)** · 0.75 min
- Phenotypes + markers → mixed models → BLUPs and h² → QTL → meta-QTL. Give Mermaid a beat to render.
- In hop the same pipe runs with CP-F1 tools (OneMap, Lep-MAP3) — parental maps first.

> *[Give the diagram a second to render.]* Here's the workflow in one picture. Trait phenotypes and markers go into mixed models, which give breeding values and heritabilities. We map QTL on the breeding values, then combine them with QTL from other studies to find meta-QTL. In hop the same pipeline runs with the standard cross-pollinated F1 tools — parental maps first, then an integrated map.

**[`plot-traits-pics`](http://localhost:8000/presentation/#/plot-traits-pics)** · 0.75 min
- 21 upright + 8 plot + 11 derived = the hand-measured ground truth.
- **Hop equivalent:** dry cone yield, alpha and beta, oil, HopBox cone shape, harvest date.

> These are the traits: 21 measured on individual uprights, 8 at the plot level, and 11 derived from images. They're the hand measurements breeders have trusted for a century — the ground truth any image trait has to earn its place against. In hop, that's dry cone yield, alpha and beta acids, oil, cone shape from HopBox, and harvest date.

**[`ch2-h2-corr`](http://localhost:8000/presentation/#/ch2-h2-corr)** · 0.5 min
- Left: roundness and TAcy highly heritable; yield modest. Right: upright ≈ plot berry weight; TAcy vs rot trade-off.
- Same shape as hop: chemistry H² 0.32–0.71 in the 2026 GWAS; yield the hard trait. Don't read the figures.

> Two takeaways. *[Left.]* Berry roundness and anthocyanin are highly heritable — easy selection targets — while total yield is only modestly heritable. That's the same shape as hop, where cone chemistry is moderately to highly heritable and yield is the hard trait. *[Right.]* Upright berry weight tracks plot berry weight, and there's a trade-off between anthocyanin and fruit rot.

**[`ch2-metaqtl-concept`](http://localhost:8000/presentation/#/ch2-metaqtl-concept)** · 1.25 min
- Stable = across years, across traits, across studies.
- **Say:** "Consensus, not p-values, is what a breeder can act on."
- Hop: the Teamaker downy mildew study found different QTL in Oregon and Washington — exactly why "stable" matters.

> What counts as a stable QTL? Three kinds of stability. Across years: the same QTL in two or more seasons. Across related traits: upright and plot berry weight sharing an interval. And across studies and populations: agreement with published QTL on one composite map — that's the meta-QTL. Consensus, not p-values, is what a breeder can act on. Hop has the textbook case for why: in the Teamaker downy mildew population, the QTL differed by environment — five from the Oregon field, twelve from Washington, five from the greenhouse.

**[`ch2-results`](http://localhost:8000/presentation/#/ch2-results)** · 0.75 min
- Land on 22. (1,542 QTL · 470 major · 13 multi-year · 8 multi-trait.)
- If asked about "92" from the thesis: that counted single-study projections; 22 is the strict cross-study consensus.

> The results. We mapped 1,542 QTL, 470 of them major. Only 13 were stable across years, and 8 across related traits within a study. Twenty-two held up across studies as meta-QTL. *[Pause on 22.]* Yield and quality QTL are everywhere; stable ones are rare.

**[`ch2-why`](http://localhost:8000/presentation/#/ch2-why)** · 0.75 min
- Image traits anchored to traits breeders already trust; deposited on vaccinium.org, code public.
- Hop equivalents: HopBase (the posting links the Cascade assembly), GRIN-Global, BrAPI / Breeding Insight.

> Why does this matter to a breeder? The meta-QTL anchored image-derived traits to the traditional ones, so high-throughput phenotyping is validated against what breeders already trust. The markers and maps are deposited on vaccinium.org, and the code is public. The method is crop-agnostic: populations plus a composite map. For hop, HopBase — which the announcement links — is the natural home.

**[`ch2-vaccap`](http://localhost:8000/presentation/#/ch2-vaccap)** · 0.5 min
- 30 s: the meta-QTL synthesis became a community deliverable (cranberry half of Fig. 1B).
- My role: cross-population synthesis and anchoring. The MYB biology is Albert's and Espley's.
- Light bridge: flavonoid chemistry in a fruit ↔ prenylated chemistry in the lupulin gland.

> The meta-QTL work also became a community deliverable. For this Plant Physiology review on flavonoids across Vaccinium, I contributed the cross-population synthesis and genome anchoring of cranberry anthocyanin, proanthocyanidin and color QTL — including a stable chromosome 3 hotspot where MYBA-like genes sit. The MYB biology is Albert's and Espley's; the QTL synthesis was mine. *[~30 seconds.]*

**[`ch2-flexseq`](http://localhost:8000/presentation/#/ch2-flexseq)** · 1.25 min
- My role: formal analysis, software, validation — not panel design.
- 17,502 loci · 99.8% recovery · fruit rot 1 → 4 QTL · parent–offspring checks flagged a likely mislabelled parent.
- **Hop bridges:** the posting's "new DArTag marker platform"; clone identity for nursery stock and germplasm transfers. Shaun Clare led this paper *and* the hop sex-marker and GWAS papers — say it if Altendorf is in the room.
- **Lesson:** 160 QTL targets → 36 survived the design. Validate trait markers in the panel.

> That work fed a genotyping platform. Shaun Clare and colleagues built Flex-Seq for cranberry, published this year in The Plant Genome: 17,502 loci, 99.8% recovery, haplotypes rather than single SNPs. Stable QTL from my study went in as design targets; my role was the formal analysis, software and validation. *[Point at the figure.]* Mapping the same populations with GBS and then Flex-Seq, fruit rot went from one QTL to four. And parent–offspring checks flagged a likely mislabelled parent — the same identity problem as checking nursery stock or a germplasm transfer in a clonal crop. Shaun, of course, also led your sex-marker and GWAS papers. One lesson: of 160 QTL targets we supplied, 36 survived the design, so trait markers have to be validated in the panel — the same will be true on DArTag.

**[`ch2-takeaways`](http://localhost:8000/presentation/#/ch2-takeaways)** · 0.5 min
- Last bullet is the forward line: hop's mildew, Verticillium and cone-chemistry loci on one reference = a year-one paper, no field season.
- **⏱** ≈ minute 15.75.

> To sum up: over 1,500 QTL, 13 stable across years, 8 across traits, 22 across studies and populations. *[Last bullet.]* And the forward point: hop's mapped loci — mildew on chromosome 6, Verticillium on LG3, the 43 cone-chemistry loci — sit on different maps and references. One synthesis on the Cascade and Apollo coordinates is a year-one paper that needs no field season. *[Near minute 15¾.]*

### D. Image phenomics — UAV, the LMI (under review) & BerryPortraits

**[`ch3-title`](http://localhost:8000/presentation/#/ch3-title)** · 0.25 min
- **Say:** "Can a camera see the trait a breeder wants to select on?" Under review, Smart Agricultural Technology.

> The second study asks a simple question: can a camera see the trait a breeder wants to select on? It's under review at Smart Agricultural Technology.

**[`ch3-video`](http://localhost:8000/presentation/#/ch3-video)** · 0.25 min
- **Say:** "This is what dormancy exit looks like from 30 m." Then pause.

> This is what dormancy exit looks like from 30 meters. *[Pause and let the video play.]*

**[`ch3-biology`](http://localhost:8000/presentation/#/ch3-biology)** · 1 min
- Red → green is a visible proxy for dormancy exit.
- **Hop:** emergence from the crown, bine growth up the string, top-wire arrival, burr — each visible from above or from the alley.

> The biology in one slide. Cranberry's evergreen leaves turn red with anthocyanin in winter and green up in spring, and that transition coincides with the bud changes where cold hardiness is lost. So a camera can potentially see the trait a breeder wants to select on. A hop yard has its own visible calendar: emergence from the crown, bines climbing the strings, arrival at the top wire, and burr.

**[`ch3-objectives`](http://localhost:8000/presentation/#/ch3-objectives)** · 0.75 min
- Hypothesis: late-but-rapid greeners avoid frost without losing the season.
- Say "late maturity index" (⚠ check against the manuscript's wording before the room).

> The objectives: use a low-cost drone as a phenotyping tool; monitor spring greening in breeding populations; predict leaf anthocyanin from image indices; and build an index — the late maturity index, or LMI — that favors genotypes that green late but fast. Late-but-rapid greeners should avoid the frost window without losing the season.

**[`ch3-parameters`](http://localhost:8000/presentation/#/ch3-parameters)** · 0.75 min
- 3 populations · 2 sites · 8 dates, 2018–19 · 597 genotypes.
- Repeated sessions per date are deliberate — they become the CV metric. Hop version: two passes of the cart, same morning.

> Three populations at two Wisconsin sites, eight flight dates across 2018 and 2019, about 600 genotypes, ground truth on about 10% of plots each date, and a consumer RGB camera. We flew several sessions per date on purpose, to measure whether a phenotype stays the same when the drone flies again. In a hop yard, that's two passes down the same alley on the same morning.

**[`ch3-pipeline`](http://localhost:8000/presentation/#/ch3-pipeline)** · 1 min
- Automated plots, segmentation, 23 indices, containerized.
- **Say:** "Numbers that come out the same when a different person or day collects them."

> The pipeline goes from flights, to an orthomosaic, to plots, to 23 vegetation indices per plot per session. Plot finding and segmentation are automated, and everything runs in containers. That's the avionics habit: characterize the instrument before the germplasm. The goal is numbers that come out the same when a different person, or a different day, collects them.

**[`ch3-berryportraits`](http://localhost:8000/presentation/#/ch3-berryportraits)** · 0.5 min
- Built with Breeding Insight; segmentation precision and recall ≥ 0.99.
- **Hop:** HopBox is the program's version for cones (Altendorf et al. 2023 — Dr. Rippner, ARS Prosser, is a co-author). Say "plug in, not rebuild." Next slide is the bridge.

> Here's the same toolkit, post-harvest. BerryPortraits, built with Breeding Insight, segments berries from images and measures color, size, shape and uniformity, with precision and recall above 0.99. My role was conceptualization, design, analysis and software testing. Your program already has the cone version in HopBox — Dr. Altendorf's, with Dr. Rippner here at Prosser — so for cones I'd plug in, not rebuild. Where I'd add something is the plot and the season.

**[`ch3-trellis`](http://localhost:8000/presentation/#/ch3-trellis)** · 1.25 min
- **Say:** "Same pipeline, new geometry."
- Left: overhead sees a whole cranberry bed. Right: overhead sees only the top of an 18-ft hedgerow — good for emergence, top-wire date and closure.
- A cart down the alley sees the canopy face: cones, canopy temperature (thermal), structure (LiDAR).
- **⚠** Illustrative. Check for published side-view or LiDAR hop work before calling it new; the Žatec group has a 2025 UAV preprint.
- Off the slide: Dr. Khot (WSU CPAAS, AgWeatherNet) is the person to build the cart with — ask him later whether his group has flown hop yards. Your avionics years mean you can co-build it, not just specify it.

> *[Slow down.]* This is the bridge. On the left, a cranberry bed: a drone overhead sees the whole canopy, and that's why my work could be done from the air. On the right, a hop yard. From overhead you see only the top of an eighteen-foot hedgerow — which is still useful for emergence, the date bines reach the top wire, and canopy closure. But the canopy face, the cones and the canopy temperature are seen from the alley. So the hop version is a sensing cart driven down the rows — RGB, thermal, and LiDAR for structure — plus flights for timing. Same pipeline, new geometry: segment, measure, repeat through the season, and end with one heritable number per plot.

**[`ch3-indices`](http://localhost:8000/presentation/#/ch3-indices)** · 0.75 min
- Anthocyanin absorbs green; chlorophyll absorbs blue/red — that's why RGB works.
- **If asked:** A535 vs top index r ≈ 0.93.

> Which indices carry the signal? The relationships follow pigment optics: anthocyanin absorbs green light, chlorophyll absorbs blue and red. That's why an ordinary RGB camera works at all.

**[`ch3-models`](http://localhost:8000/presentation/#/ch3-models)** · 1.25 min
- **Say:** "A phenotype that changes when the drone changes angle is not a breeding phenotype."
- RF R² 0.95; median CV 3.9% vs ≥ 6% for linear models. Never quote the thesis 0.886.

> We compared four linear models with random forest across 50 resampled splits. Random forest wins on accuracy, R-squared 0.95, and on stability: its predictions varied about 3.9% across repeated views of the same plot, versus 6% or more for the linear models. A phenotype that changes when the drone changes angle is not a breeding phenotype — and a canopy temperature that changes with the time of the pass isn't either.

**[`ch3-lmi`](http://localhost:8000/presentation/#/ch3-lmi)** · 1.25 min
- SLOW DOWN. A time series → one selectable number.
- Late-and-fast genotypes score high.
- **Hop:** the same construction on a bine-height curve, a canopy-temperature curve under a water cut, or cone dry matter toward harvest.

> *[Slow down — this is the key idea.]* For each genotype we fit an exponential decay of predicted anthocyanin against growing degree days and compare it with the population curve. The LMI is the signed area between them, with the sign flipped at about 200 degree days. A genotype that stays red late and greens fast scores high. A whole time series becomes one selectable number. The same construction works on a bine-growth curve, on canopy temperature after the water is cut, or on cone dry matter heading into harvest.

**[`ch3-validation`](http://localhost:8000/presentation/#/ch3-validation)** · 0.5 min
- Top vs bottom LMI through the season. Let the picture work.

> Top row, a high-LMI genotype; bottom row, a low one; each column is a flight date. *[Pause and let the picture work.]*

**[`ch3-takeaways`](http://localhost:8000/presentation/#/ch3-takeaways)** · 1 min
- Say the limits yourself: RGB resolution; sparse 75–150 GDD window; CNJ04/GRYG didn't converge.
- **Lesson for hop:** measure densely in the window where genotypes separate — for water, the days after the cut.
- **⏱** ≈ minute 26.25.

> The takeaways: random forest is accurate and stable; one index carries most of the signal; the LMI is a new, general selection index. And the honest limits: RGB spectral resolution; too few flights in the window where genotypes separate; and the models didn't converge for the two smaller populations. For a water trial, that lesson is direct: measure densely in the days after the water is cut, when genotypes pull apart. *[Near minute 26¼.]*

### E. Genetics of the LMI — in preparation

**[`ch4-title`](http://localhost:8000/presentation/#/ch4-title)** · 0.25 min
- **Say:** "Is LMI heritable, and where does it live?" In preparation for G3.

> The third study asks whether the LMI is heritable, and where it lives in the genome. It's in preparation for G3.

**[`ch4-objectives`](http://localhost:8000/presentation/#/ch4-objectives)** · 0.75 min
- Four objectives. Markers for frost resilience are the breeder deliverable.
- The same four steps for a water-use trait in hop: heritability → QTL → markers → candidates (ARS sub-objective 3.A).

> Four objectives: characterize the genetic basis of the LMI, map QTL, develop markers for spring frost resilience — the breeder's deliverable — and look at candidate genes. They're the same four steps your project plan lays out for water-use efficiency.

**[`ch4-dist-blups`](http://localhost:8000/presentation/#/ch4-dist-blups)** · 1.25 min
- One number: h² = 0.74 (GBLUP, CNJ02).
- **If asked:** Ch. IV uses the thesis-era anthocyanin predictor, so its LMI scale differs from the paper's.

> The LMI segregates in CNJ02, and its genomic heritability is 0.74 — high for a timing trait — from a mixed model with spatial terms and a genomic relationship matrix. An image-derived abiotic-stress trait can be as heritable as the chemistry.

**[`ch4-qtl`](http://localhost:8000/presentation/#/ch4-qtl)** · 1.25 min
- 11 QTL on LG 6–12, each 1.8–9.1% — polygenic, as expected.
- **Hop:** expect water use to be polygenic too — and expect coarse intervals inside non-recombining NA × EU blocks.

> Eleven QTL, on linkage groups 6 through 12, each explaining 1.8 to 9.1% of the genetic variance: a polygenic timing trait. I'd expect water use in hop to look similar — many small effects — with one hop-specific twist: inside the blocks where North American and European chromosomes don't recombine, intervals will stay coarse.

**[`ch4-genes`](http://localhost:8000/presentation/#/ch4-genes)** · 1.5 min
- Clock, photoperiod, dormancy MADS and flowering families. Say "preliminary" once.
- **Hop translation (on the slide):** short-day plant with juvenility; emergence, top-wire, burr and cone maturity are timing traits; harvest maturity sets picker and kiln schedules.
- Off the slide: Europe's hops already ripen ~20 days earlier than in the 1970s (Mozny 2023). EdleFrucht was released partly as an early-harvest type.

> The candidates are the dormancy regulators you'd expect: clock genes like LHY and PRR95, photoperiod genes like CRY1 and COL12, the MADS-box genes SVP and AGL24, and flowering genes. These are preliminary — hypotheses for functional work. Hop runs its own version: it's a short-day plant with a juvenility requirement, so bines need enough nodes before burr. Emergence, top-wire arrival, burr and cone maturity are all timing traits under the same gene families — and harvest maturity is what sets the picker and kiln schedule.

**[`ch4-breeder`](http://localhost:8000/presentation/#/ch4-breeder)** · 1.5 min
- LMI is independent of harvest window. Small effects → genomic prediction, not MAS.
- **Hop:** timing that escapes late-season water cuts and heat without moving harvest maturity; predicted from DNA, trained on plots.
- MAS for big-effect loci (sex, mildew R genes); prediction for the rest.

> So what does a breeder do with this? The LMI doesn't correlate with harvest window, so you can select for frost resilience without pushing ripening later. Small effects mean genomic prediction rather than marker-assisted selection. And the QTL prioritize functional work. *[Last bullet.]* For hop, the same logic: look for timing that escapes a late-season water cut or heat during cone fill without moving harvest maturity — and because the effects will be small, predict it from DNA, trained on plots. Markers for the big loci, like sex and the mildew R genes; prediction for everything else.

**[`ch4-takeaways`](http://localhost:8000/presentation/#/ch4-takeaways)** · 0.5 min
- **Say:** "The method transfers to a hop yard." Then: "Before the vision, one more thing the brief asked about — outreach."
- **⏱** ≈ minute 33.25.

> So: the signal showed up in CNJ02; the LMI is highly heritable; 11 QTL, none major; independent of harvest window; candidates in clock, photoperiod and flowering pathways. *[Pause.]* A time series, to a heritable index, to QTL, to candidate genes — the method transfers to a hop yard. Before the vision, one more thing the brief asked about. *[Minute 33¼.]*

### F. Outreach and adoption

**[`outreach`](http://localhost:8000/presentation/#/outreach)** · 1.5 min
- **Say:** "Show the result in the grower's units."
- Left: Wisconsin Cranberry School 2024 (meta-QTL, with a gene-mapping primer for growers) and 2025 (drone monitoring); VacCAP meeting 2025; open tools and data.
- Off the slide: grower partners are on the acknowledgments slide (Valley Corporation, Cranberry Creek; WSCGA, Ocean Spray). ⚠ GRYG is likely named for Ed Grygleski's planting — confirm before saying it.
- Right: brewers as the assay (Hopsource, pilot brews, the Hop Quality Group model behind Thora); HRC grow-outs, on-farm trials through the hop commissions, IAREC field days with WSU Extension (Hoheisel); grower units; public by default.
- Room: Stevens and Elliot (Washington Hop Commission) and Adler (HRC) are on the panel — this slide is their Objective 6. Don't name them; name their channels.

> The brief asked how I approach outreach. *[Left.]* In cranberry it's been the growers' own meeting: at Wisconsin Cranberry School in 2024 I presented the meta-QTL results with a short primer on what gene mapping is, and in 2025 the drone monitoring work. I've presented to the VacCAP project, which brings blueberry and cranberry breeders and industry together, and the tools are public — BerryPortraits with Breeding Insight, the code, the maps. *[Right.]* For hop, the industry has already built the channels. Brewers are the assay — Hopsource, pilot brews, and the Hop Quality Group model that produced Thora. Growers are the test sites, through Hop Research Council grow-outs, on-farm trials organized with the hop commissions, and field days here at IAREC with WSU Extension. And the rule I'd hold to is to report results in the grower's units — pounds per acre, per acre-foot of water, alpha and oil — not LOD scores.

### G. Vision for hop breeding in Prosser

**[`vision-headline`](http://localhost:8000/presentation/#/vision-headline)** · 0.75 min
- **Say:** "A breeding program that delivers hops that hold yield and aroma on less water — bred here, measured here, and proven with growers and brewers."
- Three aims: breed · measure · predict. Speak to the room (and the camera if anyone is remote).

> *[Face the room.]* So here's what I'd bring to Prosser: a breeding program that delivers hops that hold yield and aroma on less water — bred in the Yakima Valley, measured on the IAREC hop yard, and proven with growers and brewers. Three aims: breed, measure, predict. All of them built on germplasm, genomics and trials this program already has.

**[`vision-why-now`](http://localhost:8000/presentation/#/vision-why-now)** · 1.25 min
- Four numbers, left to right: 75% of acres in WA · 40% junior water in 2025 (2026: fourth drought year, 52–60%) · −29% yield after a 30-day lapse · alpha −20 to −31% by 2050 in Europe.
- **Say:** "Under late-season water stress, yield and aroma move — bitterness doesn't. Brewers buy aroma."
- The lapse numbers are Dr. Gonzalez Tapia's — cite him by name (he's on the panel). Deficit-irrigation paper: Nakawuka, Peters, Kenny & Walsh — all IAREC.

> Why now? Three-quarters of U.S. hop acres are in Washington, almost all of them irrigated from the Yakima. Last year junior water-right holders got 40% of a full supply, and this year is the fourth drought year in a row. Dr. Gonzalez Tapia's trials here show what a late-season cut does: thirty days without water before harvest cost almost 29% of the yield, and even fifteen days cut the oil by nearly a fifth — while the alpha and beta acids didn't move. And in Europe, warming has already moved ripening about twenty days earlier, with alpha acids projected to fall by up to a third by 2050. Under late-season water stress, yield and aroma move, and bitterness doesn't. Brewers buy aroma.

**[`vision-fit`](http://localhost:8000/presentation/#/vision-fit)** · 1 min
- One clause per partner — don't recite the grid. Say names aloud; the slide says roles.
- ARS Prosser: Gonzalez Tapia (water), with Feldman (potato phenomics) and Rippner (soil imaging) down the hall · Altendorf (genomics, HopBox, the second station) · Gent (races) · NCGR (Reinhold) · WSU (Khot sensing and AgWeatherNet, Peters irrigation, Liu weeds and on-farm trials, Walsh mites, Harper and Poojari clean plants, Hoheisel Extension; Sankaran in Pullman) · OSU (Townsend, Shellhammer, Hendrix) · Washington Hop Commission, HRC, brewers, growers · Oregon and Idaho farms and other test sites.
- Every panelist's program is in this grid: Gonzalez Tapia, Feldman, Liu by name; Stevens and Elliot (the commission), Adler (HRC), Coleman (growers, Oregon farms) by channel. Say their programs, not "as the panel knows". Full list by name: `backup-partners`.
- **Say:** "The middle is the job: breed, measure, predict."

> Here's where that fits. *[Top row.]* Dr. Gonzalez Tapia's stress physiology here, which defines the water treatments, with Dr. Feldman's and Dr. Rippner's imaging down the hall; Dr. Altendorf's genomics and the Corvallis station; Dr. Gent's mildew races. *[Sides.]* The national collection in Corvallis; WSU here on campus — sensing with Dr. Khot, irrigation with Dr. Peters, weeds and on-farm trials with Dr. Liu, mites with Dr. Walsh, Extension, and the Clean Plant Center for releases. *[Bottom.]* Oregon State for breeding peers, chemistry and the genome; the growers, the Hop Commission, the Hop Research Council and brewers, who decide what succeeds; and Oregon and Idaho farms for more environments. *[Middle.]* The middle is the job: breed, measure, predict.

**[`vision-aim1`](http://localhost:8000/presentation/#/vision-aim1)** · 1.5 min
- This is the job description — cultivars. Grower and brewer outcome first.
- Start with what's in hand: WSU females transferred to ARS (sub-objective 1.B), the seven multi-race PM lines.
- Dense seedling nurseries (+717% individuals) + the SM1 sex marker; plots for yield and water at both stations, then grower trials in WA, OR (Willamette downy mildew pressure — Coleman's question) and ID (Parma); brewers early via Hopsource and pilot brews.
- Credit the lineage: the WSU material is Stephen Kenny's program; Thora and the genome are Henning's.
- **⚠** Don't give a release year.

> Aim one is breeding — the main job. For growers and brewers, the target is aroma hops with multi-race mildew resistance that hold yield and oil on less water. I'd start with what's in hand: the advanced WSU females transferred to ARS, and the seven multi-race mildew-resistant lines that came out of that collection. New crosses would go into dense seedling nurseries — Dr. Altendorf's work shows a dense layout evaluates about eight times as many individuals — with the sex marker at the seedling, so space goes to females. Then plots here and in Corvallis for yield and water, and grower trials in Washington, Oregon and Idaho — the Willamette gives us mildew pressure the Yakima can't. And brewers early: Hopsource ratings and pilot brews on advanced lines, not just at the end.

**[`vision-aim2`](http://localhost:8000/presentation/#/vision-aim2)** · 1.5 min
- The posting's "abiotic stress emphasis" and Objective 3. Grower outcome first: rank varieties when the water is cut.
- Genotype × water design on Gonzalez Tapia's lapse plots, with WSU's irrigation engineering (Peters, CPAAS); canopy temperature as a time series (early stomatal closure → warmer canopy before yield loss); cart + flights with Khot's engineers and the ARS imaging on site (Feldman, Rippner); → h² → the first WUE QTL (ARS 3.A).
- **Components, not one ratio** is Dr. Feldman's point (*Setaria*, 2018: WUE components have distinct genetic signatures). Credit it in one clause; the traits are the timing and size of each line's stress response, not instantaneous WUE. Background: `../../prep/WUE_Components_Literature_Review.md`.
- Off the slide: no hop water-use QTL is published; the ARS plan has WUE in 2.A, 3.A and 4.A — the phenotype is the gap.

> Aim two is measurement — the abiotic-stress emphasis in the announcement. For growers, it means ranking varieties by yield and aroma when the water is cut, not only on full water. I'd run breeding lines in a genotype-by-water design on Dr. Gonzalez Tapia's irrigation-lapse plots, with the irrigation engineering WSU already has here. Hop closes its stomata early as the soil dries, so a stressed canopy runs warmer before it loses yield, and thermal imaging can see that if you measure it as a time series. A sensing cart down the alleys and flights overhead — built with the imaging and engineering people already on this campus — would give emergence, bine growth and top-wire date every week. And water use has components with different genetics — Dr. Feldman showed that in *Setaria* — so the traits are the timing and size of each line's response, not one ratio. Then the cranberry recipe: heritability, and the first water-use QTL in hop — which your project plan already calls for.

**[`vision-aim3`](http://localhost:8000/presentation/#/vision-aim3)** · 1.25 min
- Grower outcome: choose parents, males included, before they've been through a plot.
- Train on DArTag + the 2026 GWAS allele stacks + Aim 2 phenotypes. Males: the dairy-bull problem — validate against progeny tests.
- Map hop like cranberry (CP-F1); distortion mapped, not filtered; call against Cascade and both Apollo haplotypes.
- This is Objective 4's "concepts applicable to … dioecious crops." It's Altendorf's genomics — say "with."

> Aim three is prediction, with Dr. Altendorf's group. The breeding payoff is choosing parents — males included — before they've been through a plot. Train on the DArTag genotypes and the allele stacks from the 2026 GWAS, plus the plot data from Aim two. Males are the interesting part: they carry alleles for cone chemistry they never express, so their breeding values have to come from relatives and DNA — the dairy-bull problem — checked against progeny tests. That's the dioecious-crop concept the announcement asks for. And I'd map hop the way I mapped cranberry, as a cross-pollinated F1, calling against both the Cascade and Apollo haplotypes so neither ancestry gets lost.

**[`vision-adoption`](http://localhost:8000/presentation/#/vision-adoption)** · 1 min
- Objective 6. Walk the table top to bottom in one breath: team → growers at field days (WSU Extension) → HRC and brewers → grower cooperators through the commissions → advisory committee and clean plants.
- "Drying" and "sprays saved" are for Coleman (kiln behavior) and Elliot (MRLs). Results go back to cooperators first, then the commission's annual meeting.
- **Say the bottom line** — it's for the industry half of the room.

> Adoption is built into each stage. Seedlings and hills are for the breeding team. Plots under full and reduced water are what growers see at field days here, with WSU Extension — yield and oil per acre and per acre-foot. Advanced lines go to Hop Research Council grow-outs and to brewers through Hopsource, and onto growers' farms in Washington, Oregon and Idaho through the hop commissions — where the questions are yield, picking date, how it dries and how many sprays it saves. And releases go through the Public Hop Breeding Advisory Committee and the Clean Plant Center. The question a grower asks isn't "what's the LOD score?" It's "what does it yield on 60% water, and will brewers buy it?"

**[`vision-not-claiming`](http://localhost:8000/presentation/#/vision-not-claiming)** · 0.75 min
- Say the limits yourself, quickly: not a pathologist, not a stress physiologist, not the hop genomicist, not a brewer; no drought-proof hop on a date; no faster clone.
- **Cut this slide first** if the room started late — keep the lines for questions.

> To be clear about limits: I'm not a pathologist — mildew resistance rests on Dr. Gent's races. I'm not a stress physiologist — the water treatments are Dr. Gonzalez Tapia's; I make them heritable at plot scale. I'm not the hop genomicist. I'm not a brewer. And I'm not promising a drought-proof hop on a date, or a faster clone — what changes is the accuracy of selection and how early it happens.

**[`vision-deliverables`](http://localhost:8000/presentation/#/vision-deliverables)** · 1.25 min
- Five deliverables, then the year-one footer — that's the answer to "what would you do first?"
- **Say:** "Year one: plant out the WSU females, instrument the irrigation plots, write the meta-QTL paper, and meet the growers, the commissions and the brewers."
- **⏱** minute 45.

> In five years I'd aim for five things. Advanced selections from the WSU collection and new crosses in grower and brewer trials. Water and heat phenotypes on the IAREC hop yard, measured every week. The first QTL for water-use efficiency and crop timing in hop. Genomic prediction in routine use, including males. And a public pipeline that growers and brewers trust. *[Footer.]* In year one: plant out the WSU females, instrument the irrigation plots, write the hop meta-QTL paper, and meet the growers, the hop commissions, brewers and the Hop Research Council. *[Minute 45.]*

### H. Close

**[`summary`](http://localhost:8000/presentation/#/summary)** · 0.75 min
- Land the last line and stop talking.

> In summary: six papers — the meta-QTL synthesis and the flavonoid review, a genotyping platform, BerryPortraits, drone phenomics and the LMI, and the genetics of dormancy exit. The announcement's six objectives, each met by a method I've used in another clonal perennial. And three aims: breed, measure, predict. Cranberry was the case study. Water is the Yakima problem. Cultivars are the deliverable. *[Stop talking.]*

**[`acks`](http://localhost:8000/presentation/#/acks)** · 0.25 min
- Zalapa, Digman, committee, growers (Valley Corporation, Cranberry Creek), funders; Dr. Hayes, the panel, ARS, WSU, the Washington Hop Commission and HRC. 15 s.

> Thank you to Juan Zalapa, Matthew Digman and Amaya Atucha, the lab, the growers and funders on this slide — and to Dr. Hayes, the panel, ARS, WSU, the Hop Commission and the Hop Research Council for the invitation. I'm happy to take questions.

**[`references`](http://localhost:8000/presentation/#/references)**
- Untimed. Press `o` to jump to any backup.

**[`questions`](http://localhost:8000/presentation/#/questions)**
- Repeat each question for the room (and anyone remote). Two or three sentences, then offer a backup.
- Year one? WSU females · instrument the lapse plots · meta-QTL paper · meet growers and brewers.
- HopBox? Plug in; I add the plot and the season. Canopy temperature confounded? Fit vigor and time; use the within-genotype water contrast.
- Males? Sex marker; genomic values; progeny tests (`backup-dioecy`). Distortion / Apollo? `backup-cp-mapping`, `backup-hop-genome`.
- Drought-tolerant variety when? Years; ranking existing lines under reduced water comes first.
- Panelists will likely ask here too: Feldman (is the image trait real? which WUE component?) · Liu (WSU partners) → `backup-partners` · Coleman (would I plant it? Oregon?) · Stevens, Elliot (growers, MRLs, water) · Adler (the advisory-committee pipeline; year-three milestones). One line each: `prep-panel`.
- Full answers: Prep section at the end of the deck, or the commute prep doc.

> *[Open the floor.]* Thank you — I'm happy to take questions. *[Listen to the whole question, repeat it for the room, answer in two or three sentences, and offer a backup slide if one fits.]*

### Backup — Q&A

**[`backup-title`](http://localhost:8000/presentation/#/backup-title)**
- Hop backups first (how/funding, who I'd work with, genomes, F1 mapping, males, mildew, water, sensors, trait evaluation), then rhAmpSeq vs Flex-Seq and the cranberry material.

**[`backup-how`](http://localhost:8000/presentation/#/backup-how)**
- Pipelines · data · funding. Year one needs a thermal camera, a cart, a technician share and genotyping as a service — not a sensor fleet.

> *If asked what you'd need:* Open, containerised pipelines that rerun the same way every season; data in a hop trait dictionary with BrAPI-compatible records on Cascade and Apollo coordinates, deposited to GRIN-Global; and a lean funding path — the CRIS base, the Hop Research Council and the Washington, Oregon and Idaho hop commissions, state specialty-crop grants and SCRI. Year one needs a thermal camera, a cart I can build, part of a technician and genotyping as a service.

**[`backup-partners`](http://localhost:8000/presentation/#/backup-partners)**
- For "Who would you work with?" (Liu's likely question; Rayapati's at 1:30). Pick one partner per row and one joint project — don't read the table.
- ARS at Prosser is five research units on one campus: Gonzalez Tapia (FSCRU), Feldman (TTFVRU), Rippner (HCRU), Miklas (Grain Legume unit), Irish (WRPIS). Feldman + Rippner + Gonzalez Tapia + you = a shared imaging core.
- ⚠ Altendorf's Corvallis move is from the 2026 BA roundup (IAREC still lists her in Prosser) · Gooding is HRC President (2026) · Stevens is WHC executive director (Ann George's successor — confirm) · Gallagher's and Dorman's titles unconfirmed.

> *If asked who you'd work with:* Here on campus, Dr. Gonzalez Tapia on water, and Dr. Feldman and Dr. Rippner on a shared imaging and compute setup. In Corvallis, Dr. Altendorf's genomics and selections, and Dr. Gent's races. At WSU, Dr. Khot and Dr. Peters for the sensing cart and managed deficits, Dr. Liu for on-farm trials, the Clean Plant Center for releases, and Extension for field days — and I'd want to co-advise WSU students. Oregon State for a peer breeding program and brewing chemistry. And the Hop Commission, the Hop Research Council and the Brewers Association for priorities, grower trials and brewer evaluation. The rule is to extend their programs, not duplicate them.

**[`backup-hop-genome`](http://localhost:8000/presentation/#/backup-hop-genome)**
- Cascade 2023 vs Apollo 2026. Kale is first author; Braumann (Carlsberg) last; Hopsteiner co-authors.
- Two rules: call against both haplotypes; can't break a block that doesn't recombine — choose parents.

> *If asked which reference:* Cascade is the coordinate system most U.S. QTL use, and HopBase serves it. The 2026 Apollo assembly separates a North American and a European chromosome set and shows tens of thousands of structural differences between them — including an 85-megabase inversion on chromosome 6 from Brewer's Gold — with recombination suppressed between ancestries. So I'd call NA-by-EU families against both haplotypes, and for a QTL inside a non-recombining block I'd choose parents with the same arrangement rather than try to break it.

**[`backup-cp-mapping`](http://localhost:8000/presentation/#/backup-cp-mapping)**
- Segregation types; parental maps; phase-aware QTL; distortion as biology; triploid/tetraploid tools.
- Honest line: the polyploid tools I've used on diploid data.

> *If asked how you'd map in hop:* Exactly as in cranberry — a cross-pollinated F1 with up to four alleles per locus, segregating 1:1, 1:2:1 or 1:1:1:1. Parental maps first, then an integrated map, with phase-aware QTL on breeding values. Hop's distortion is biology — chromosome 2's centromere, the translocations, the chromosome 6 inversion — so I'd map it rather than filter it. For triploid and tetraploid lines, the dosage tools from potato apply; I've used them on diploid data.

**[`backup-dioecy`](http://localhost:8000/presentation/#/backup-dioecy)**
- SM1 PACE 96% (765-hop GWAS) · the dairy-bull problem · fit the X separately · other dioecious crops.

> *If asked how you'd choose males:* Sex them as seedlings with the SM1 marker, so no one waits a year or two for flowers. Then rank them on cone chemistry from their relatives and their DNA — the dairy-bull problem — and check those predictions against progeny tests. Loci on the X are hemizygous in males, so the X gets its own term in the model. The same approach would serve asparagus, kiwifruit, spinach, pistachio and hemp.

**[`backup-pm`](http://localhost:8000/presentation/#/backup-pm)**
- R6 broke in 2012 — durability is the lesson. Comet's chr 6 interval; the seven multi-race lines. Gent's program owns races and screens.
- ⚠ Is the Comet interval inside the Brewer's Gold inversion? Ask, don't assert.
- Last bullet is for the commission (Elliot): resistance → fewer sprays → fewer residue problems in EU markets. Gent's group showed cultivar susceptibility is one of the drivers of how many fungicides growers apply and what they spend (Hwang et al. 2024, Phytopathology).

> *If asked about powdery mildew:* There are seven named R genes; V6 strains appeared here in 2012 and overcame R6, and Cascade's partial resistance eroded too. The durable route is stacking major genes on a quantitative background — Comet's chromosome 6 region, the seven multi-race lines from the WSU collection — selected with markers and screened with Dr. Gent's races. For growers, that also means fewer fungicide sprays and less residue risk in export markets.

**[`backup-water`](http://localhost:8000/presentation/#/backup-water)**
- Physiology (early stomatal closure; −0.8 MPa; P50 −1.6) · Nakawuka 2017 cultivar range · Gonzalez Tapia 2025 lapse numbers. No WUE QTL published.

> *If asked what's known about hop and water:* Hop closes its stomata early and stops bine growth at fairly mild soil drying. In the Yakima deficit trials, cutting to 60% of crop water cost 19% of the yield in Chinook and 33% in Willamette, with alpha and beta unchanged — almost a twofold difference between cultivars. And the late-season lapse trials show oil, not bitterness, is the quality that moves. No water-use QTL is published, which is the opening.

**[`backup-sensing`](http://localhost:8000/presentation/#/backup-sensing)**
- RGB first (your experience); multispectral with red-edge; thermal with a calibration budget; LiDAR for structure. Repeatability test before genetics.

> *If asked which sensors:* RGB first — it's what my cranberry work used and it covers emergence, cover, top-wire date and color. Multispectral with red-edge for vigor and nitrogen. Thermal for water stress, but only with wet and dry references and a fixed midday window. LiDAR from the cart for canopy volume. And every trait passes the repeat-measurement test before it goes to the genetics.

**[`backup-trait-evaluation`](http://localhost:8000/presentation/#/backup-trait-evaluation)**
- Repeatable → heritable → holds across environments → changes a decision.

> *If asked how you evaluate a trait:* Is it repeatable — the same number from a different pass or scorer? Is it heritable on the unit I select — hills for cone traits, plots for yield and water? Does it hold across full and reduced water, Prosser and Corvallis? And does it change a decision — save water, keep the aroma, cut a spray? If not, it isn't worth measuring.

**[`backup-rhampseq-flexseq`](http://localhost:8000/presentation/#/backup-rhampseq-flexseq)**
- rhAmpSeq = transferable across a genus; Flex-Seq = density within a species. In hop, wild *neomexicanus*/*lupuloides* segments and NA vs EU structural variants are where the transferability lesson applies.

> *If asked which kind of panel:* rhAmpSeq was designed to transfer across a genus; Flex-Seq for density within a species. In hop, the wild American segments and the North American versus European structural variants are where transferability matters — markers designed on one ancestry can drop out in the other.

### Prep — not presented

**[`prep-top`](http://localhost:8000/presentation/#/prep-top)**
- Prep only — not presented. Full version: FSCRU_Seminar_Commute_Prep.md.

**[`prep-dont-say`](http://localhost:8000/presentation/#/prep-dont-say)**
- Prep only — not presented.

**[`prep-panel`](http://localhost:8000/presentation/#/prep-panel)**
- Prep only — not presented. Full profiles: `../../people/`; overview: `../../people/_Panel_and_Audience_Overview.md`.

**[`prep-qa`](http://localhost:8000/presentation/#/prep-qa)**
- Prep only — not presented.

---

## 6. What the 6 Oct web check changed

Checked against primary sources the day before; the deck and notes already use the corrected versions.

- **Water, 2026.** The primer's 40% junior supply is **2025** (Capital Press, Aug 2025). Reclamation's 2026 forecasts: **52%** in June, **60%** in September; Reclamation calls 2026 the **fourth consecutive drought year**. The deck says "40% … 2025" and "2026: fourth drought year, 52–60%."
- **Apollo authorship.** *Nature Communications*, May 2026: first author **Sandip M. Kale**, last author **Ilka Braumann** (Carlsberg); co-authors include Pitra and Matthews (Hopsteiner) and Horáková. Numbers (corrected 7 Oct against the full text): 52,593 presence + 41,990 absence variants, 4,438 translocations, 215 inversions; ~85 Mb chr 6 inversion, ~500 genes, traced to Brewer's Gold from a wild Manitoba female collected in 1916; suppressed recombination; additive NA + EU bitter-acid alleles. The primer's "Braumann et al." is corrected everywhere.
- **Gonzalez Tapia 2025** (*JASHS* 150(3):136): 15-d lapse −9.5% yield (1,961 kg/ha); 30-d −28.8% (1,654 kg/ha); alpha 4.3% and beta 6.4% means, no lapse effect; total oil −19% at 15 d; geraniol −20.8%, linalool −11.4%, humulene +9.1%, caryophyllene +12.4%.
- **Nakawuka et al. 2017** (*Ind. Crops Prod.* 98:82–92) — authors **Nakawuka, Peters, Kenny and Walsh**, three of them IAREC. 60% water: Mt. Hood −30%, Willamette −33%, Columbus −25%, Chinook −19%; 80%: Mt. Hood −14%, Willamette −10%, Chinook −3%, Columbus +2%. The primer's "2.4-fold water productivity" is the top of each range; the deck uses the yield-loss range instead.
- **Altendorf, Heineck & Tawril 2025** (*Crop Sci.*): predictive for 44–75% of trait combinations; cone traits 75–85%, agronomic 38–56%; Spearman 0.78–0.82 vs 0.52–0.64; +717% individuals; only plots adequately represent yield.
- **Clare, Schmuker & Altendorf 2026** (*Plant Genome*): 529 females, 20,861 SNPs, 49 MTAs, 43 loci, 5 traits, H² 0.32–0.71, NIR R 0.54–0.94 — confirmed.
- **NASS 2025** (via Capital Press): 41,654 acres, 83.1 M lb, $447.5 M, $5.38/lb, 1,996 lb/acre; Washington 31,198 acres, 62.1 M lb, $329.1 M (~75%); production −20% and acreage −23% vs 2023 — confirmed.
- **Mozny et al. 2023**: 1995–2018 vs 1971–1994 — yield −19.4% Celje, −19.1% Spalt, −13.7% Hallertau, −9.5% Tettnang; alpha −34.8% Celje … −10.5% Žatec; ripening ~20 d earlier; 2050 yield −4–18%, alpha −20–31% — confirmed.
- **Outreach.** Your 2024 Cranberry School deck ("Of Buds and Bits", with a "Gene Mapping Primer") and 2025 deck ("Drone-Based Phenological Monitoring of Spring Leaf Coloration in Cranberry Breeding Populations") and an April 2025 VacCAP deck are in your Documents — the outreach slide is built on those. ⚠ Confirm the event names as you'd say them.
- **Still ⚠:** where Altendorf sits now; Shaun Clare's employer; whether the Comet chr 6 interval lies inside the Brewer's Gold inversion; DArTag panel size; published side-view/LiDAR hop phenotyping; "late" vs "leaf" maturity index.

## 6b. What the 7 Oct people update changed

Built from the per-person files in `../../people/` and the panel named in `../../documents/Overview.md` (updated 7 Oct).

- **`vision-fit`:** ARS Prosser cell now covers the potato phenomics and soil imaging next door (Feldman, Rippner); WSU cell adds weeds and Extension (Liu, Hoheisel); the industry cell names the commissions; other sites lead with Oregon and Idaho farms. Notes and script name the people.
- **`vision-adoption`:** a new "On farms" row (grower cooperators in WA, OR, ID through the hop commissions — yield, picking date, drying, sprays saved); WSU Extension at field days.
- **`outreach`, `vision-aim1`, `vision-deliverables`, `acks`, `backup-how`:** hop commissions, on-farm trials in WA/OR/ID, WSU Extension, and the Washington Hop Commission and HRC in the thanks.
- **`vision-aim2`:** irrigation engineering (Peters) and the campus imaging groups (Feldman, Rippner, Khot) on the slide; "components, not one ratio" with Feldman et al. 2018 cited.
- **`backup-pm`:** a grower line — fewer sprays, less residue risk (Elliot's issue).
- **New `backup-partners`:** who you'd work with, by name, for ARS Prosser, ARS Corvallis, WSU, OSU and industry.
- **New hidden `prep-panel`;** `prep-top` and `prep-dont-say` updated for the panel.
- Timing unchanged: 46 min, `totalTime` 2760. Deck now 101 slides.

## 6c. What the 7 Oct source check changed

Every cited number was checked against the full-text PDFs (now in `../../publications/`; full report: `../../publications/_Source_Verification_2026-10-07.md`). Fixed in the deck and notes:

- **Apollo structural variants:** 52,593 presence + 41,990 absence variants, **4,438 translocations, 215 inversions** (the earlier "41,990 translocations · 4,438 inversions" shifted the list by one).
- **Comet chr 6 paper** is Henning et al. 2024 *Crop Science* 64:2823 (not *J. Genet. Genomics*). Numbers unchanged.
- **Hwang et al.** is 2024 *Phytopathology* 114:2287: cultivar susceptibility drives fungicide use and cost. Don't say "quantified savings".
- **"Strongly isohydric"** is not Gloser's wording; say "closes its stomata early, at mild soil drying".
- **Teamaker downy mildew** (Henning et al. 2015, not 2016): QTL differed by environment (5 Oregon, 12 Washington, 5 greenhouse).
- **rhAmpSeq ">80,000 vines / KASP"** removed (not in Zou 2020).
- Know, don't necessarily say: Flex-Seq's 160 → 36 targets came from all collaborators; the "mislabelled parent" is 9 of 22 trios flagged, 5 sharing McFarlin; Altendorf 2025 tested 7 cultivars across spacings; Gonzalez Tapia's lapse trials were Cascade in John I. Haas fields.
- **Still ⚠:** UAV/LMI numbers from your own unpublished manuscripts (not reachable for the check).

## Sources checked

- Posting, seminar brief and schedule: `../../documents/` · crop primer: `../../prep/FSCRU_Humulus_Genetics_Primer.md` · people: `../../people/` (per-person files, `_Panel_and_Audience_Overview.md`, `Prosser Hop Breeding — Potential Collaborators.md`)
- U.S. Bureau of Reclamation, Yakima basin June 2026 forecast: https://www.usbr.gov/newsroom/news-release/5348 · September 2026 forecast: https://www.usbr.gov/newsroom/news-release/5405 · 2025 rationing at 40%: https://capitalpress.com/2025/08/08/yakima-river-basin-water-rationing-stays-at-40-of-full-supply/
- Gonzalez Tapia 2025, *JASHS*: https://journals.ashs.org/view/journals/jashs/150/3/article-p136.xml · Nakawuka et al. 2017: https://www.usahops.org/img/blog_pdf/87.pdf
- Apollo genome (Kale … Braumann 2026): https://www.nature.com/articles/s41467-026-72379-8
- Clare, Schmuker & Altendorf 2026: https://www.ars.usda.gov/research/publications/publication/?seqNo115=429180 · Altendorf, Heineck & Tawril 2025: https://www.ars.usda.gov/research/publications/publication/?seqNo115=419394
- U.S. hops 2025 (NASS via Capital Press): https://capitalpress.com/2025/12/30/u-s-hops-production-acreage-continue-drop-in-2025-but-yield-price-and-value-improve/
- Mozny et al. 2023: https://www.nature.com/articles/s41467-023-41474-5
- Everything else on the slides is cited in the primer's source list.

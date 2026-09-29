# TPGRDRU coffee seminar — prep and speaker notes

**Wed 30 Sep 2026 · DKI-USPBARC, Hilo, Hawaiʻi · seminar 8:30** · Sections 1–4 are a ~10 min read. Section 5 has the speaker notes plus a spoken script for each slide (~25 min). Section 6 is what the web check on 29 Sep changed.

_The bullet lines under each slide heading in section 5 **are** the deck's speaker notes. Edit here, then run `python3 tools/speaker_notes.py update --from TPGRDRU_Seminar_Prep.md`; or edit in the deck and run `python3 tools/speaker_notes.py extract --into TPGRDRU_Seminar_Prep.md`. Only the lines directly under a heading are notes — the quoted script below them is not._

---

## 1. Today

| Time | What |
|---|---|
| 7:45 | Pick-up at the hotel |
| 8:00 | Center Director, Dr. Marisa Wall |
| 8:15 | Seminar prep. **Ask: who is in the room, who is on Teams, who chairs the panel.** Load the deck from disk, check the videos play, open the speaker view (`s`) |
| **8:30** | **Seminar: 45–50 min talk + 15 min questions** |
| 9:40 | Technicians and admin |
| 10:15 | PBARC scientists |
| 10:45 | Facility tour |
| 11:15 | Dr. Lisa Keith (pathology) |
| 11:45 | Lunch |
| 1:15 | Germplasm tour with curator Dr. Ryan Domingo |
| 2:30 | Dr. Jon Suzuki (molecular biology) |
| 3:30 | Dr. Melissa Johnson (TCCPRU) |
| 4:00 | Dr. Roxana Myers (nematology) |
| 4:30 | Dr. Qingyi Yu (genomics) |
| 6:00 | Dinner with Tracie Matsumoto (Research Leader) |
| Thu | Kona: Kraig Lee (Kona Direct Farms) 9:00 · Tommy Greenwell (Greenwell Farms — ‘Mamo’) 10:30 |

## 2. Seven things to get right

1. **Yu owns the genomic half of 3.A.** The assemblies, the bulked-segregant analysis and an ORISE postdoc on rust QTL are hers. Everything in Aim 2 is "with your group, on your assembly." You bring the phenotype and the map her genomics is waiting for.
2. **The leaf-disc assay already scores latency, % lesions and reaction type** (HARC SCRI report). Say *instrument*, never *invent*. Your addition is continuous, blind, repeated measurement — and splitting the 939-plant "tolerant" class.
3. **Kona, not Hawaiʻi.** Kona Typica is "over 90% of coffee produced in Kona" (Lyu et al. 2025). Yu is the senior author.
4. **Allo, not auto.** Arabica is disomic: two diploid subgenomes. The hard parts are homoeolog collapse and Timor Hybrid introgression, not dosage. Cranberry is diploid; say so once.
5. **Not a pathologist, not the genome group, not yet a coffee breeder.** Nagai and HARC have carried this material since 1992. Say it on `vision-not-claiming`, plainly, and move on.
6. **Quality is a gate.** Sub-objective 3.A says "maintain high cupping quality." Nothing resistant goes anywhere without cupping against Kona Typica.
7. **Half the panel is industry** (Long, Shriner, Falconer, plus Nagai as breeder). Lead every aim with the grower outcome; define QTL, h² and AUDPC once (`qtl-plain`).

## 3. Pacing (47 min timed · totalTime 2820 s)

| Checkpoint | Minute |
|---|---|
| End of opening + model system (`frost`) | ≈ 6.5 |
| End of meta-QTL block (`ch2-takeaways`) | ≈ 15.5 |
| End of UAV block (`ch3-takeaways`) | ≈ 26.5 |
| Pivot to vision (`ch4-takeaways`) | **35** |
| Five-year deliverables | 46 |
| Summary + mahalo | 47 |

**10-min vision (if the room starts late):** skip `vision-how` and `vision-not-claiming` (keep their lines for Q&A), and take Aim 3 in one sentence. **15-min vision (if asked for more):** add `backup-stacking` after Aim 3. Never cut into the 15 minutes of questions.

If behind in the research half: one sentence each on `ch3-indices`, `ch4-qtl`, `ch2-vaccap`.

## 4. Numbers to have ready

| Topic | Number | Why it matters | Source |
|---|---|---|---|
| Hawaiʻi industry | 7,000 bearing acres · 5.26 M lb parchment · $53.0 M · $14.80/lb (2024–25) | Scale of what rust threatens | USDA NASS, Jan 2026 |
| CLR arrival | 2020, Maui; now Hawaiʻi Island, Maui, Oʻahu, Lānaʻi, Molokaʻi | Five years in, no resistant Kona variety yet | HDOA; Keith et al. 2023 |
| Invasion genetics | 434 isolates · 17 countries · 11 SSRs · MLG 10 | One Latin American lineage, human-moved | Ramírez-Camejo et al. 2022 |
| Race | XXIV (v2,4,5) in every sample from three islands | Defeats SH5 — Kona Typica's only factor | Keith et al. 2023 |
| Kona Typica | > 90% of coffee produced in Kona; ~1.13 Gb; 22 chr; BUSCO 99.1%; 65,458 genes | The unit's own reference | Lyu … Yu 2025 |
| Field epidemic | < 4% early season → 36% at harvest; 30 lots, 204–875 m | Rust peaks when growers are busiest | Aristizábal & Johnson 2022 |
| Spray cost | Priaxor < 2% for 12 wk, $140/acre · copper < 5% for 6–8 wk, $126/acre · biologicals failed, $138–198/acre | The recurring cost genetics could remove | Aristizábal, Maeda, Matsumoto & Johnson 2025 |
| Parental genomes | T5175, T8667 (resistant) · Typica, Mokka (susceptible) · 222,771 SNPs + 557,623 indels | Discovery tier already exists | ARS FY2024 |
| The F2 | Mokka × Catimor 5175 · leaf-disc screened · 8 R + 8 S sequenced (34 / 39 Gb HiFi) → differential SNPs | Next step is quantitative mapping on every plant | ARS FY2025 |
| HARC pipeline | Catimor F2s 210 R / 939 T / 894 S (14 crosses; parentage confirmed for 11) · Obatã F1s 183 / 243 / 162 (25 crosses; 21 confirmed) | "Tolerant" is the biggest class; parentage checks are already a need | HARC SCRI 2023–24 |
| First arabica map | Pearl, Nagai … Ming 2004: Mokka hybrid × Catimor pseudo-F2, 60 trees, 456 AFLP + 8 co-dominant, 1,802.8 cM, 68% of markers from Catimor | Credit Nagai; same design, better tools | TAG 108:829 |
| Breeding cycle | 'Mamo': crosses 1999 → planted in Kona 2009 → F5–F6 → market 2017 | ~18 years; the cycle slide | Big Island Video News 2018 |
| Latency | ~21 d Caturra vs ~37 d F1 hybrids (warm regime) | Latency is heritable and big | Toniutti et al. 2017 |
| WCR global trial | 29 varieties · 23 sites · 15 countries in the rust analysis (from 2015) · introgressed 1.47 vs pure 2.03 (1–5) · 4 mega-environments | G×E is real; a shared scale matters | Berny Mier y Terán et al. 2025; WCR |
| Introgression | Timor Hybrid = 7–11% of the genome, mostly subgenome C; polyploidy 350–610 ka | Where the polymorphism in the F2 will be | Salojärvi et al. 2024 |
| CBB harvesting | 4.6% vs 9.0% infestation; +3,024 lb cherry/acre; 55% lower chemical cost; 48% higher net benefit | Why synchrony (Aim 3) is worth money | Aristizábal, Johnson, Shriner & Wall 2023 |
| Ripening | Anthesis → ripe 220–243 d (180–330); cultivars differ by 30+ d; 5–10 mm rain breaks bud dormancy | Timing is genetic and unmapped | Unigarro et al. 2025 |
| Nematode | E17, E25, E52 Rf < 1 · Tupi-HI 7.12 · Obatã 2.33 | The stacking cross | Myers et al. 2023 |
| Variety ID | WCR 45-SNP KASP panel; 1,424 reference samples; validated on 30,000+; ARS a partner | Deployment tier exists for identity | WCR 2023 |
| Innovea | ARS joined 28 Mar 2023; access to 300+ samples/evaluations | Long's network | ARS news |
| Your meta-QTL | 1,542 QTL; 22 cross-study meta-QTL | Stable QTL are rare | Maule et al. 2024 |
| Your Flex-Seq | 17,502 loci; 99.8% recovery; fruit rot 1 → 4 QTL; parent checks caught mislabels | Identity + disease + markers | Clare et al. 2026 |
| Your UAV | RF R² 0.95; median CV 3.9% | A repeatable image trait | Under review |
| Your LMI | h² 0.74; 11 QTL, 1.8–9.1% each | A heritable timing trait | In prep, G3 |

## 4b. Don't say (couldn't confirm, or wrong)

- "90% of Hawaiʻi's coffee is Typica" — the figure is for **Kona**.
- A month for CLR's arrival. Lyu et al. and Ramírez-Camejo say spores in Feb 2020; HDOA and the first report say Oct 2020 (Haʻikū, Maui). Say "2020, on Maui."
- "18 countries" — the invasion study sampled **17**; WCR's rust analysis covered **15** (18 was the network).
- Johnson as first author of the harvesting paper — it is **Aristizábal**, Johnson, Shriner & Wall 2023.
- The 8 + 8 bulks as FY2024 — they are in the **FY2025** report (FY2024 is the four genomes).
- "Ten RPP8 genes on chr 4" — Salojärvi reports tandem arrays of RPP8- (5), CPR1- (10) and LRK10L-like (3) genes; say "a cluster of resistance-gene arrays."
- Any F1-hybrid heterosis percentage (not verified), any genotyping price, any release year.
- That MauiGrown is the world's only Mokka grower as fact (their claim). Nagai's pronouns until you meet.
- That you have run a leaf-disc assay, called variants in a polyploid, or worked on pathogen-specific resistance. Your disease trait is cranberry fruit rot, a multi-fungus complex.
- The thesis R² 0.886 (the paper's is 0.95).

## 4c. People you might meet

- **Panel:** Lisa Keith (pathology; race XXIV, qPCR, urediniospore storage) · Qingyi Yu (genomics; Kona Typica senior author; polyploidy) · Chifumi Nagai (HARC breeder; 'Mamo'; 2004 map) · Michael Muszynski (UH Mānoa; maize flowering, editing) · Jennifer "Vern" Long (WCR CEO; Innovea; likely remote) · Suzanne Shriner (SHAC; Board of Agriculture; CBB co-author) · James "Kimo" Falconer (MauiGrown; Mokka; 28-variety trial).
- **Hiring manager:** Tracie Matsumoto (Research Leader, TPGRDRU) — the F2, genomes, genebank and ID panel are her program.
- **Around the building:** Marisa Wall (Center Director) · Melissa Johnson (TCCPRU; CLR monitoring, CBB) · Roxana Myers (nematodes, grafting) · Ryan Domingo (curator) · Jon Suzuki · Haomin Lyu and Jinjin Song (Yu group) · Lionel Sugiyama and Eva Brill (Keith lab) · Ming-Li Wang (HARC SCRI PI) · Andrea Kawabata (CTAHR Kona) · Luis Aristizábal (SHAC).
- **Thursday:** Tommy Greenwell grew out Nagai's crosses and brought 'Mamo' to market — a good person to ask what a grower needs to see before planting a new variety.

## 4d. Q&A — short answers

- **Yu — "We're already mapping rust resistance. What do you add?"** A phenotype with more than three values on every F2 plant. The bulks find the major locus; latency and sporulation need everyone measured on a scale. Then the tiers that get markers to HARC and growers.
- **Yu — "How do you handle an allotetraploid?"** Disomic, so two diploids. Map to both subgenomes of Kona Typica; a het call in a pure-line parent is a homoeolog artifact until proven otherwise; keep markers polymorphic between parents and single-copy in their subgenome; KASP primers homoeolog-specific. Cranberry was diploid — the discipline transfers, the filtering I'd build with your group. (`backup-allo-calling`)
- **Yu — "Why not GWAS on the collection?"** Too little diversity and too much structure; the F2 first. Ethiopian and Innovea material for allele discovery later.
- **Keith — "How do you separate resistance from escape or inoculum variation?"** Check cultivars (Kona Typica, a Catimor) in every run, blind duplicates, spore load and viability recorded per run (her storage work), and qPCR on discs to catch infection that never sporulates.
- **Keith — "Race-specific or quantitative?"** Both. Race-specific loci to fix and stack; quantitative components for durability. XXIV already beat SH5.
- **Nagai — "What generation do you select at? Can markers replace field evaluation?"** Markers at F2/F3 in the nursery reduce what goes to the field; they don't replace yield and cup evaluation. Ask what segregated in the Mokka crosses behind 'Mamo'.
- **Nagai — "Linkage drag and cup quality?"** Background selection with the operational panel: keep the resistance block, recover Mokka/Typica elsewhere. Cupping is the release gate.
- **Muszynski — "Mechanism? Would you edit?"** Candidates come from the assemblies once intervals narrow. Editing needs the regeneration work in the -019/-024-A objective; validate first, edit in partnership.
- **Long — "How does this plug into Innovea?"** A shared image-based rust protocol and a marker panel sites can run the same way; Hawaiʻi lines as entries; Hawaiʻi as a site with a characterized race. (`backup-f1-hybrids` if F1s come up.)
- **Long — "Isn't the OSU/WCR hyperspectral project doing this?"** It measures leaf physiology and reflectance; this measures lesions and canopy loss. Complementary — share genotyped material.
- **Shriner / Falconer — "When does a grower get a resistant tree that tastes like Kona?"** Years, not months — 'Mamo' took ~18. Markers and the screen shorten the list of trees that go to the field; cupping against Kona Typica gates release. Don't give a year.
- **Shriner — "Can growers use the on-farm assay?"** Yes: a phone protocol on lower-canopy leaves, the same leaves already sampled for monitoring.
- **Falconer — "Mokka?"** It's the susceptible parent of the F2, so Mokka-background resistant lines are a natural product to discuss with HARC. Ask what he sees in Mokka under rust in Kāʻanapali.
- **Matsumoto — "Year one?"** Image the leaf-disc runs; map the F2 with Yu's group; the meta-QTL coordinate paper; walk the monitoring farms with TCCPRU and SHAC; learn HARC's populations.
- **"What do you need?"** A camera rig and growth-room time, a share of a technician, genotyping as a service. Not a drone fleet.
- **"Why so much phenotyping?"** Markers are only as good as the phenotypes they're trained on.

---

## 5. Slide-by-slide cues (= speaker notes in index.html) and what to say

*Bullets are the current speaker notes. The quoted block under each is a fuller spoken version; italics in brackets are stage directions.*

### A. Opening

**[`title-new`](http://localhost:8000/presentation/#/title-new)** · 0.5 min
- **Say:** "Thank you, and mahalo for the invitation." Then: cranberry is the case study; the title is the vision half.
- **Resolve the tension early:** "I haven't run a leaf-disc assay. The first 35 minutes are how I went from field imagery to loci in cranberry."
- Don't read the title. Advance.

> Good morning, and mahalo for the invitation — to Tracie, Dr. Wall, and the panel. I work on cranberry, a perennial with the same breeding problems coffee has: years before you see yield or resistance, a narrow cultivated base, and quality that decides the price. The title is the vision half of the talk. I haven't run a leaf-disc assay; the first 35 minutes are how I went from field imagery to loci in cranberry, and the last 12 are how that would work here. *[Advance.]*

**[`path`](http://localhost:8000/presentation/#/path)** · 0.75 min
- **Say:** "I treat phenotyping and genotyping as engineering problems; breeding gives them a purpose."
- Ten years of avionics = instruments characterized before they are trusted.

> My path wasn't a straight line. I studied computer engineering at Georgia Tech and spent about ten years building embedded and avionics software — real-time systems, sensors, certification. My interest in plants took me to a PhD in Plant Breeding and Plant Genetics at UW–Madison, in the Zalapa lab with the USDA-ARS Vegetable Crops Research Unit, and I'm now a research associate across the Digman and Zalapa labs. That's why I treat phenotyping and genotyping as engineering problems: an instrument gets characterized before anyone trusts its numbers.

**[`cycle`](http://localhost:8000/presentation/#/cycle)** · 1 min
- **Say:** "The generation stays about three years. What changes is how many trees you carry and how early you know."
- 'Mamo': HARC crosses 1999 → F5–F6 → market 2017. Phase lengths illustrative — invite Nagai to correct them.
- Three levers: markers in the nursery · leaf-disc numbers instead of waiting for an epidemic · growers' farms as trial sites.

> Let me be precise about what can go faster. *[Walk the bar.]* A pure-line arabica goes from cross, to an F1 that takes about three years to fruit, through F2 to F5 or F6 at roughly three years a generation, then multi-site trials and cupping. 'Mamo' — Dr. Nagai's crosses from 1999 — reached the market in 2017. These phase lengths are illustrative; Dr. Nagai, correct me. The generation doesn't get shorter. What changes is how many trees you carry and how early you know: markers in the nursery, leaf-disc numbers instead of waiting for an epidemic, and growers' farms as trial sites. *[Point at the green loop.]* And those data decide which families to advance.

**[`map`](http://localhost:8000/presentation/#/map)** · 0.75 min
- Left: the project plans' own words. Right: where I've done something comparable. State publication status once.
- Point at row 2 — the on-farm assay is written into the plan "almost in my words."
- Row 1 is Yu's genomics too — "alongside," not "instead of."

> Here's the map for the talk. On the left is what your coffee projects commit to, in their own words; on the right, where I've done something comparable. The meta-QTL study is published, the spring-greening paper is under review and the LMI genetics paper is in preparation, plus co-authored work on a genotyping platform, a flavonoid review, and BerryPortraits with Breeding Insight. *[Point at row 2.]* This one — a high-throughput, on-farm rust susceptibility assay — is written into the plan almost in my words.

### B. Cranberry as a model system

**[`background`](http://localhost:8000/presentation/#/background)** · 0.75 min
- Perennial, slow, quality-priced — say the coffee word with each.
- **Honest difference (say it here or on the next slide):** cranberry is diploid; arabica is an allotetraploid.

> Briefly, the crop. Cultivated cranberry is a perennial of acidic bogs, native to eastern North America. What matters for this room: it takes three to five years to establish a bed and six to eight years to evaluate a selection — like coffee, you wait years to see what you've got.

**[`why-coffee`](http://localhost:8000/presentation/#/why-coffee)** · 1.5 min
- Left: shared problems. Say the honest difference: cranberry is a diploid outcrossing clone; arabica is a selfing allotetraploid bred as pure lines → an F2 design.
- Right: the leaf-disc assay already scores latency, % lesions and reaction type — the output is three classes. **939 of 2,043 are "tolerant."**
- **⚠** Your disease trait is fruit rot, a multi-fungus complex. Don't claim rust or pathogen-specific resistance work.

> Why should a coffee audience care? *[Left.]* The problems are shared: a perennial; a quantitative fungal resistance — for me, cranberry fruit rot, which is a complex of fungi, not one pathogen; a narrow cultivated base with variation in wild relatives; quality setting the price; and identity in growers' fields. One honest difference: cranberry is a diploid outcrossing clone, and arabica is a self-pollinating allotetraploid bred as pure lines. That makes an F2 design — simpler to map, harder to genotype. *[Right.]* And there's a shared measurement problem. HARC's leaf-disc bioassay already scores latency, lesions and reaction type, and the output is three classes. Across 14 Catimor crosses, the biggest class — 939 seedlings — is "tolerant." The biggest class is the least defined.

**[`qtl-plain`](http://localhost:8000/presentation/#/qtl-plain)** · 0.5 min
- For the industry half of the panel. One sentence per term; point at the two clouds.
- QTL · heritability · AUDPC. Then don't define them again.

> Three terms I'll use, in plain words. *[Point at the picture.]* A QTL is a stretch of chromosome where the DNA differs between plants and the trait differs with it — so a marker there can be read on a seedling, years before the tree is scored. Heritability is the share of the differences between plants that's genetic. And AUDPC — the area under the disease progress curve — turns a whole epidemic, or a whole leaf-disc time series, into one number.

**[`frost`](http://localhost:8000/presentation/#/frost)** · 0.75 min
- **Say:** "When is the crop exposed, and can genetics move the window?"
- **Coffee:** no frost in Hawaiʻi — the same question applies to flowering after rain, ripening spread, and how long a leaf is open to rust.

> Here's the problem in grower terms for cranberry. Buds are hardy in winter and vulnerable once they swell, so growers sprinkle on frost nights — and every night costs water, energy, labor and sleep. Genetics could shorten or shift that window. Hawaiʻi has no frost night, but coffee asks the same question of flowering after the rain, of ripening spread over months, and of how long a leaf is open to rust: when is the crop exposed, and can genetics move the window?

### C. Meta-QTL synthesis — Maule et al. 2024 + Clare et al. 2026

**[`ch2-title`](http://localhost:8000/presentation/#/ch2-title)** · 0.25 min
- **Say:** "My most polished work and the least coffee-specific — so I'll sell the method, not the loci."

> The first study is my meta-QTL paper, published in Frontiers in Plant Science in 2024. It's my most polished work and the least coffee-specific, so I'll sell the method, not the loci.

**[`populations-map`](http://localhost:8000/presentation/#/populations-map)** · 1 min
- CNJ02 (168) and CNJ04 (67); composite map, 12 LGs, 1,560 bins.
- Coffee contrast: these are F1 families from heterozygous parents; the unit's Mokka × Catimor 5175 is an F2 from inbred parents — simpler segregation. One minute max.

> We used two mapping populations: CNJ02, Mullica Queen by Crimson Queen, 168 individuals, and CNJ04, Mullica Queen by Stevens, 67. They were phenotyped over several years and placed on one composite map — 12 linkage groups, about 1,560 bins. These are F1 families from two heterozygous parents; your Mokka by Catimor 5175 is an F2 from inbred parents, which segregates more simply. *[One minute, then move on.]*

**[`ch2-workflow`](http://localhost:8000/presentation/#/ch2-workflow)** · 0.75 min
- Phenotypes + markers → mixed models → BLUPs and h² → QTL → meta-QTL. Give Mermaid a beat to render.
- The coffee F2 runs the same pipe with standard diploid tools, once markers are subgenome-specific.

> *[Give the diagram a second to render.]* Here's the workflow in one picture. Trait phenotypes and markers go into mixed models, which give breeding values and heritabilities. We map QTL on the breeding values, then combine them with QTL from other studies to find meta-QTL. For the coffee F2, the same pipeline runs with standard diploid tools, once each marker is assigned to its subgenome.

**[`plot-traits-pics`](http://localhost:8000/presentation/#/plot-traits-pics)** · 0.75 min
- 21 upright + 8 plot + 11 derived = the hand-measured ground truth.
- **Coffee equivalent:** the three-class leaf-disc score, field severity, yield, bean size, cup score.

> These are the traits: 21 measured on individual uprights, 8 at the plot level, and 11 derived. They're the hand measurements breeders have trusted for a century — the ground truth any image trait has to earn its place against. In coffee, that's the leaf-disc class, field severity, yield, bean size and the cup.

**[`ch2-h2-corr`](http://localhost:8000/presentation/#/ch2-h2-corr)** · 0.75 min
- Left: roundness and TAcy highly heritable; yield modest. Right: upright ≈ plot berry weight; TAcy vs rot trade-off.
- The TAcy–rot trade-off is the cranberry version of resistance vs cup quality. Don't read the figures.

> Two takeaways. *[Left.]* Berry roundness and anthocyanin are highly heritable — easy selection targets — while total yield is only modestly heritable. *[Right.]* Upright berry weight tracks plot berry weight, and there's a trade-off between anthocyanin and fruit rot — our version of resistance against cup quality.

**[`ch2-metaqtl-concept`](http://localhost:8000/presentation/#/ch2-metaqtl-concept)** · 1.25 min
- Stable = across years, across traits, across studies.
- **Say:** "Consensus, not p-values, is what a breeder can act on."
- Coffee: published rust loci (SH3, Timor Hybrid QTL, the chr 4 region) sit on different maps — the same synthesis is waiting.

> What counts as a stable QTL? Three kinds of stability. Across years: the same QTL in two or more seasons. Across related traits: upright and plot berry weight sharing an interval. And across studies and populations: agreement with published QTL on one composite map — that's the meta-QTL. Consensus, not p-values, is what a breeder can act on. For coffee rust, the published loci — SH3, the Timor Hybrid QTL, the chromosome 4 region — sit on different maps and marker systems. The same synthesis is waiting.

**[`ch2-results`](http://localhost:8000/presentation/#/ch2-results)** · 0.75 min
- Land on 22. (1,542 QTL · 470 major · 13 multi-year · 8 multi-trait.)
- If asked about "92" from the thesis: that counted single-study projections; 22 is the strict cross-study consensus.

> The results. We mapped 1,542 QTL, 470 of them major. Only 13 were stable across years, and 8 across related traits within a study. Twenty-two held up across studies as meta-QTL. *[Pause on 22.]* Yield and quality QTL are everywhere; stable ones are rare.

**[`ch2-why`](http://localhost:8000/presentation/#/ch2-why)** · 0.75 min
- Image traits anchored to traits breeders already trust; deposited on vaccinium.org, code public.
- Coffee equivalents: the Kona Typica assembly as the coordinate system; GRIN-Global; BrAPI.

> Why does this matter to a breeder? The meta-QTL anchored image-derived traits to the traditional ones, so high-throughput phenotyping is validated against what breeders already trust. The markers and maps are deposited on vaccinium.org, and the code is public. The method is crop-agnostic: populations plus a composite map. Here, the Kona Typica assembly would be that map.

**[`ch2-vaccap`](http://localhost:8000/presentation/#/ch2-vaccap)** · 0.5 min
- 30 s: the meta-QTL synthesis became a community deliverable (cranberry half of Fig. 1B).
- My role: cross-population synthesis and anchoring. The MYB biology is Albert's and Espley's.
- Quality chemistry as a trait — the cup-quality bridge, lightly.

> The meta-QTL work also became a community deliverable. For this Plant Physiology review on flavonoids across Vaccinium, I contributed the cross-population synthesis and genome anchoring of cranberry anthocyanin, proanthocyanidin and color QTL — including a stable chromosome 3 hotspot where MYBA-like genes sit. The MYB biology is Albert's and Espley's; the QTL synthesis was mine. *[~30 seconds.]*

**[`ch2-flexseq`](http://localhost:8000/presentation/#/ch2-flexseq)** · 1.5 min
- My role: formal analysis, software, validation — not panel design.
- 17,502 loci · 99.8% recovery · fruit rot 1 → 4 QTL · parent–offspring checks caught mislabels.
- **Coffee bridges:** HARC confirmed parentage for 11 of 14 Catimor crosses; the unit's SNP panel helps growers identify cultivars. Identity is a grower product.
- **Lesson:** 160 QTL targets → 36 survived the design. Validate trait markers in the panel.

> That work fed a genotyping platform. Clare and colleagues built Flex-Seq for cranberry, published this year in The Plant Genome: 17,502 loci, 99.8% recovery, haplotypes rather than single SNPs. Stable QTL from my study went in as design targets; my role was the formal analysis, software and validation. *[Point at the figure.]* Mapping the same populations with GBS and then Flex-Seq, fruit rot went from one QTL to four. And parent–offspring checks caught mislabelled parents. That's the same problem as identifying cultivars in growers' fields, or confirming parentage in a breeding cross — HARC could confirm 11 of 14 Catimor crosses. One lesson: of 160 QTL targets we supplied, 36 survived the design, so trait markers have to be validated in the panel.

**[`ch2-takeaways`](http://localhost:8000/presentation/#/ch2-takeaways)** · 0.75 min
- Last bullet is the forward line: published rust loci on the Kona Typica coordinates = a year-one paper, no field season.
- **⏱** ≈ minute 15.5.

> To sum up: over 1,500 QTL, 13 stable across years, 8 across traits, 22 across studies and populations. *[Last bullet.]* And the forward point: two decades of published rust-resistance loci sit on different maps. Bringing them onto the Kona Typica coordinates is a year-one paper that needs no field season. *[You should be near minute 15½.]*

### D. Image phenomics — UAV, the LMI (under review) & BerryPortraits

**[`ch3-title`](http://localhost:8000/presentation/#/ch3-title)** · 0.25 min
- **Say:** "Can a camera see the trait a breeder wants to select on?" Under review, Smart Agricultural Technology.

> The second study asks a simple question: can a camera see the trait a breeder wants to select on? It's under review at Smart Agricultural Technology.

**[`ch3-video`](http://localhost:8000/presentation/#/ch3-video)** · 0.25 min
- **Say:** "This is what dormancy exit looks like from 30 m." Then pause.

> This is what dormancy exit looks like from 30 meters. *[Pause and let the video play.]*

**[`ch3-biology`](http://localhost:8000/presentation/#/ch3-biology)** · 1 min
- Red → green is a visible proxy for dormancy exit.
- **Coffee:** rust shows as chlorotic flecks on top of the leaf and orange sporulation underneath; defoliation shows from above. A camera sees different parts of the same disease at different scales.

> The biology in one slide. Cranberry's evergreen leaves turn red with anthocyanin in winter and green up in spring, and that transition coincides with the bud changes where cold hardiness is lost. So a camera can potentially see the trait a breeder wants to select on. Coffee rust is the same kind of problem at different scales: yellow flecks on top of the leaf, orange spores underneath, and leaf loss you can see from above.

**[`ch3-objectives`](http://localhost:8000/presentation/#/ch3-objectives)** · 0.75 min
- Hypothesis: late-but-rapid greeners avoid frost without losing the season.
- Say "late maturity index," never "leaf."

> The objectives: use a low-cost drone as a phenotyping tool; monitor spring greening in breeding populations; predict leaf anthocyanin from image indices; and build an index — the late maturity index, or LMI — that favors genotypes that green late but fast. Late-but-rapid greeners should avoid the frost window without losing the season.

**[`ch3-parameters`](http://localhost:8000/presentation/#/ch3-parameters)** · 0.75 min
- 3 populations · 2 sites · 8 dates, 2018–19 · 597 genotypes.
- Repeated sessions per date are deliberate — they become the CV metric. The leaf-disc version: repeated images of the same disc, blind duplicates.

> Three populations at two Wisconsin sites, eight flight dates across 2018 and 2019, about 600 genotypes, ground truth on about 10% of plots each date, and a consumer RGB camera. We flew several sessions per date on purpose, to measure whether a phenotype stays the same when the drone flies again. On a leaf disc, that's imaging the same disc twice, and blind duplicates.

**[`ch3-pipeline`](http://localhost:8000/presentation/#/ch3-pipeline)** · 1 min
- Automated plots, segmentation, 23 indices, containerized.
- **Say:** "Numbers that come out the same when a different person or day collects them."

> The pipeline goes from flights, to an orthomosaic, to plots, to 23 vegetation indices per plot per session. Plot finding and segmentation are automated, and everything runs in containers. That's the avionics habit: characterize the instrument before the germplasm. The goal is numbers that come out the same when a different person, or a different day, collects them.

**[`ch3-berryportraits`](http://localhost:8000/presentation/#/ch3-berryportraits)** · 0.75 min
- Built with Breeding Insight; segmentation precision and recall ≥ 0.99.
- This is the template for leaf-disc imaging — next slide.

> Here's the same toolkit, post-harvest. BerryPortraits, built with Breeding Insight, segments berries from images and measures color, size, shape and uniformity, with precision and recall above 0.99. My role was conceptualization, design, analysis and software testing. And it's the template for what I'd do with a leaf disc.

**[`ch3-leafdisc`](http://localhost:8000/presentation/#/ch3-leafdisc)** · 1.25 min
- **Say:** "Same pipeline, new object."
- Left: berry → count, size, color. Right: disc → lesion count, area, sporulating area, latency, AUDPC.
- **⚠** The right panel is an illustrative mock, not data. Say so.
- Latency ~21 d Caturra vs ~37 d F1 hybrids (Toniutti 2017) — the component is big and genetic.

> *[Slow down.]* This is the bridge. On the left, a berry: segment it, count it, measure its size and color. On the right — and this is an illustrative mock, not data — a leaf disc imaged every few days after inoculation. Segment the flecks and the orange sporulation, count lesions, measure sporulating area, find the day sporulation starts — the latency — and integrate the curve into an AUDPC. Latency alone is a big, genetic difference: in one growth-chamber study, about 21 days for Caturra and 37 for F1 hybrids. Same pipeline, new object: one heritable number per plant.

**[`ch3-indices`](http://localhost:8000/presentation/#/ch3-indices)** · 0.75 min
- Anthocyanin absorbs green; chlorophyll absorbs blue/red — that's why RGB works.
- **If asked:** A535 vs top index r ≈ 0.93.

> Which indices carry the signal? The relationships follow pigment optics: anthocyanin absorbs green light, chlorophyll absorbs blue and red. That's why an ordinary RGB camera works at all.

**[`ch3-models`](http://localhost:8000/presentation/#/ch3-models)** · 1.25 min
- **Say:** "A phenotype that changes when the drone changes angle is not a breeding phenotype."
- RF R² 0.95; median CV 3.9% vs ≥ 6% for linear models. Never quote the thesis 0.886.

> We compared four linear models with random forest across 50 resampled splits. Random forest wins on accuracy, R-squared 0.95, and on stability: its predictions varied about 3.9% across repeated views of the same plot, versus 6% or more for the linear models. A phenotype that changes when the drone changes angle is not a breeding phenotype — and a rust score that changes with the scorer isn't either.

**[`ch3-lmi`](http://localhost:8000/presentation/#/ch3-lmi)** · 1.5 min
- SLOW DOWN. A time series → one selectable number.
- Late-and-fast genotypes score high.
- **Coffee:** the same construction on a leaf-disc sporulation curve, or on a flowering / ripening curve per tree.

> *[Slow down — this is the key idea.]* For each genotype we fit an exponential decay of predicted anthocyanin against growing degree days and compare it with the population curve. The LMI is the signed area between them, with the sign flipped at about 200 degree days. A genotype that stays red late and greens fast scores high. A whole time series becomes one selectable number. The same construction works on a sporulation curve from a leaf disc, or a flowering and ripening curve from a tree.

**[`ch3-validation`](http://localhost:8000/presentation/#/ch3-validation)** · 0.5 min
- Top vs bottom LMI through the season. Let the picture work.

> Top row, a high-LMI genotype; bottom row, a low one; each column is a flight date. *[Pause and let the picture work.]*

**[`ch3-takeaways`](http://localhost:8000/presentation/#/ch3-takeaways)** · 1 min
- Say the limits yourself: RGB resolution; sparse 75–150 GDD window; CNJ04/GRYG didn't converge.
- **Lesson for the leaf disc:** image densely in the window where genotypes separate (around latency).
- **⏱** ≈ minute 26.5.

> The takeaways: random forest is accurate and stable; one index carries most of the signal; the LMI is a new, general selection index. And the honest limits: RGB spectral resolution; too few flights in the window where genotypes separate; and the models didn't converge for the two smaller populations. For a leaf disc, that lesson is direct: image densely around latency. *[Near minute 26½.]*

### E. Genetics of the LMI — in preparation

**[`ch4-title`](http://localhost:8000/presentation/#/ch4-title)** · 0.25 min
- **Say:** "Is LMI heritable, and where does it live?" In preparation for G3.

> The third study asks whether the LMI is heritable, and where it lives in the genome. It's in preparation for G3.

**[`ch4-objectives`](http://localhost:8000/presentation/#/ch4-objectives)** · 0.75 min
- Four objectives. Markers for frost resilience are the breeder deliverable.
- Same four steps for a leaf-disc trait in the F2: heritability → QTL → markers → candidates.

> Four objectives: characterize the genetic basis of the LMI, map QTL, develop markers for spring frost resilience — the breeder's deliverable — and look at candidate genes. They're the same four steps I'd take with a leaf-disc trait in your F2.

**[`ch4-dist-blups`](http://localhost:8000/presentation/#/ch4-dist-blups)** · 1.25 min
- One number: h² = 0.74 (GBLUP, CNJ02).
- **If asked:** Ch. IV uses the thesis-era anthocyanin predictor, so its LMI scale differs from the paper's.

> The LMI segregates in CNJ02, and its genomic heritability is 0.74 — high for a timing trait — from a mixed model with spatial terms and a genomic relationship matrix.

**[`ch4-qtl`](http://localhost:8000/presentation/#/ch4-qtl)** · 1.5 min
- 11 QTL on LG 6–12, each 1.8–9.1% — polygenic, as expected.
- **Coffee contrast:** rust resistance in the F2 may be one large Timor Hybrid block plus small modifiers — map both, with the block fitted first.

> Eleven QTL, on linkage groups 6 through 12, each explaining 1.8 to 9.1% of the genetic variance: a polygenic timing trait. Rust resistance in your F2 may look different — one large Timor Hybrid block plus smaller modifiers — so the block gets fitted first, and the modifiers are what continuous phenotypes let you see.

**[`ch4-genes`](http://localhost:8000/presentation/#/ch4-genes)** · 1.75 min
- Clock, photoperiod, dormancy MADS and flowering families. Say "preliminary" once.
- **Coffee translation (on the slide):** buds dormant for weeks to months, open ~1–2 weeks after rain; ripening ~220–245 d; cultivars differ by 30+ d.
- **For Muszynski:** flowering-time genetics is his field — one sentence, not a promise.

> The candidates are the dormancy regulators you'd expect: clock genes like LHY and PRR95, photoperiod genes like CRY1 and COL12, the MADS-box genes SVP and AGL24, and flowering genes. These are preliminary — hypotheses for functional work. Coffee runs its own version of this: floral buds sit dormant for weeks to months and open a week or two after rain, ripening runs seven to eight months, and cultivars differ by a month. The same gene families are where a coffee flowering-synchrony QTL would be tested first.

**[`ch4-breeder`](http://localhost:8000/presentation/#/ch4-breeder)** · 2 min
- LMI is independent of harvest window. Small effects → genomic prediction, not MAS.
- **Coffee:** "What does a breeder do with a QTL for latent period? Fix it if it's large, predict it if it's small — decide before the tree is planted."
- Arabica: MAS for the big introgressed blocks (SH genes); prediction for the partial components.

> So what does a breeder do with this? The LMI doesn't correlate with harvest window, so you can select for frost resilience without pushing ripening later. Small effects mean genomic prediction rather than marker-assisted selection. And the QTL prioritize functional work. *[Last bullet.]* The same question for your F2: what does a breeder do with a QTL for latent period? If it's large, fix it with a marker. If it's small, predict it. Either way, decide before the tree is planted.

**[`ch4-takeaways`](http://localhost:8000/presentation/#/ch4-takeaways)** · 1 min
- **Pivot:** "The method transfers — here's how it would work in Hilo."
- **⏱** minute 35 here. If behind, cut research next rehearsal — never the vision, never Q&A.

> So: the signal showed up in CNJ02; the LMI is highly heritable; 11 QTL, none major; independent of harvest window; candidates in clock, photoperiod and flowering pathways. *[Pause.]* A time series, to a heritable index, to QTL, to candidate genes — the method transfers. Here's how it would work in Hilo. *[Minute 35.]*

### F. Vision for coffee at TPGRDRU

**[`vision-headline`](http://localhost:8000/presentation/#/vision-headline)** · 0.5 min
- **Say:** "A measurement-and-mapping program that turns the unit's leaf-disc screen and F2 into mapped, quantitative, durable rust resistance — and cultivars growers can verify in their own fields."
- Three aims: measure · map · time the crop. Speak to the room (and the camera, if Long is remote).

> *[Face the room.]* What I'd bring to Hilo is a measurement-and-mapping program: one that turns your leaf-disc screen and your F2 into mapped, quantitative rust resistance — and into cultivars growers can verify in their own fields. Three aims: measure resistance, map it to markers people can use, and time the crop.

**[`vision-why-now`](http://localhost:8000/presentation/#/vision-why-now)** · 1 min
- Four numbers, left to right: 2020 · race XXIV beats SH5 (Kona Typica, > 90% **of Kona**) · 36% at harvest · $126–140 per acre per spray.
- **Say:** "Every spray is a recurring cost that genetics could remove." — the line for Shriner and Falconer.
- Don't explain rust to Keith; cite her.

> Why now? Rust reached Maui in 2020 and is on five islands, from one Latin American lineage. It's race XXIV — Dr. Keith's typing — which defeats SH5, the only resistance factor in Kona Typica, and Kona Typica is over 90% of what Kona grows. On farms it stays under 4% early in the season and reaches 36% at harvest, with the lower canopy losing leaves first. And the answer today is spraying: 126 to 140 dollars an acre, every six to twelve weeks. Every spray is a recurring cost that genetics could remove.

**[`vision-fit`](http://localhost:8000/presentation/#/vision-fit)** · 0.5 min
- One clause per box; say the names, they aren't on the slide: Keith · Yu, Matsumoto · Nagai, Wang · Johnson · Myers · Shriner, Falconer, Aristizábal · Muszynski, Kawabata · Long.
- **Say:** "Pathology says which resistance matters, genomics gives the coordinates, I make the phenotype quantitative and map it, HARC advances the lines, growers check it."

> Here's where it fits. Dr. Keith's pathology decides which resistance matters. Dr. Yu's genomics and Tracie's genebank give the coordinates. *[Center.]* I make the phenotype quantitative and map it. HARC — Dr. Nagai and Dr. Wang — advance the lines; TCCPRU gives field ground truth; growers through SHAC and the coffee association run the on-farm check; and WCR's Innovea takes the best lines beyond Hawaiʻi.

**[`vision-aim1`](http://localhost:8000/presentation/#/vision-aim1)** · 1.75 min
- **Grower outcome first.** Then: time-lapse imaging of the discs the unit already runs — the components already scored by eye, now continuous and blind.
- Checks every run, blind duplicates, inoculum recorded, qPCR (Keith's assay) for latent infection.
- Why continuous: XXIV beat SH5; partial components last; they split the "tolerant" class.
- **⚠** Say "instrument," not "invent." Ask how inoculum is standardized today.

> Aim one: resistance you can measure. For growers, that's a screen that ranks seedlings by how resistant they are, so fewer susceptible trees ever reach a farm. In practice: time-lapse imaging of the leaf-disc runs you already do. Latency, lesion count and area, sporulating area and AUDPC — the components already scored by eye, now continuous, blind and repeatable. Repeatability is designed in: check cultivars in every run, blind duplicates, inoculum load and viability recorded, and Dr. Keith's qPCR to catch infection before it shows. Why continuous? Race-specific genes fail — XXIV already beats SH5. The partial components are what last, and they're exactly what splits the tolerant class.

**[`vision-aim1-field`](http://localhost:8000/presentation/#/vision-aim1-field)** · 1.25 min
- Phone protocol on lower-canopy leaves = Aristizábal & Johnson's sampling frame; a detector automates their ImageJ step.
- UAV for defoliation and greenness only — spores are on the underside.
- **The missing number:** genetic correlation, leaf disc ↔ field. That's what validates the screen.
- Complements the OSU–WCR hyperspectral project — don't imply rebuilding it.

> Then the farm — the on-farm assay the project plan asks for. A phone protocol on lower-canopy leaves, where rust starts, using the sampling frame and ImageJ severity already used on Hawaiʻi farms, with a detector doing the ImageJ step. A drone for what an overhead camera can actually see — defoliation and canopy greenness — not lesions, because the spores are on the underside. Growers run it, so the multi-site data start in the first season. And the one missing number: the genetic correlation between leaf-disc traits and field severity. That's what turns a lab screen into a validated one. It complements the OSU–WCR hyperspectral work rather than rebuilding it.

**[`vision-aim2`](http://localhost:8000/presentation/#/vision-aim2)** · 1.75 min
- **Grower outcome first:** HARC keeps only resistant seedlings in the nursery.
- The step after the bulks (8 R + 8 S, FY2025): every F2 plant measured → QTL for components, not just R vs S.
- Allotetraploid care in one line; the detail is for Yu's question (`backup-allo-calling`).
- **Credit Nagai:** Pearl, Nagai … Ming 2004 — Mokka hybrid × Catimor. "Same question, twenty years of better tools."

> Aim two: from bulked segregants to QTL, with your genomics. For growers, that means markers that let HARC keep only resistant seedlings in the nursery. Your FY2025 bulks — eight resistant and eight susceptible F2 plants — found differential SNPs. The next step is measuring every F2 plant with the Aim 1 traits, so we get QTL for latency, lesion number and sporulation, not just resistant versus susceptible. It's a simpler map than cranberry's: inbred parents segregate one-two-one per subgenome, and both parents are assembled. The care is in the calling — per subgenome, homoeolog false-hets stripped with the parental genomes, and coarse intervals inside the Timor Hybrid blocks. And this is where it started: Dr. Nagai, with Pearl and Ming, mapped a Mokka hybrid by Catimor population in 2004. Same question, twenty years of better tools.

**[`vision-aim2-markers`](http://localhost:8000/presentation/#/vision-aim2-markers)** · 1.25 min
- Three tiers: discovery (unit genomics) → operational panel with identity + parentage (every cross) → KASP (HARC, growers).
- Year-one paper: published rust loci on Kona Typica coordinates — **joint with Yu's group**.
- Payoff: homozygous resistance haplotypes at F2/F3 — fewer, better trees.

> Markers people can use. The discovery tier exists: your parental genomes. The operational tier is a panel that also checks identity and parentage on every cross — an extension of the grower cultivar-ID panel. And the deployment tier is KASP for the few validated loci, which HARC and growers can run, next to WCR's open variety-ID panel. The year-one paper needs no field season: published rust loci, on the Kona Typica assembly, as a joint paper with the genomics group. And the payoff: keep only seedlings homozygous for resistance at F2 or F3. The generation stays three years; the field holds fewer, better trees.

**[`vision-aim3`](http://localhost:8000/presentation/#/vision-aim3)** · 1.5 min
- Flushes → picking rounds → leftover berries → CBB. 4.6% vs 9.0% infestation; +48% net benefit (Aristizábal, Johnson, Shriner & Wall 2023) — Shriner is a co-author.
- Timing is genetic (30+ days between cultivars) and unmapped → the LMI construction.
- **Falconer:** one machine pass. **Muszynski:** a heritable flowering phenotype is what candidate-gene work needs.
- Quality is a gate — partner on the cup, don't lead it.

> Aim three: the timing traits no one has mapped in coffee. Several flowering flushes mean many picking rounds, and berries left behind feed the berry borer. Frequent harvesting cut infestation from 9 to under 5% and raised net benefit by almost half — Suzanne, that's your paper with Luis, Melissa and Marisa. Synchrony makes that cheaper, and lets one machine pass catch more ripe cherry. Cultivars differ by a month in ripening, but heritabilities and QTL are essentially unpublished — so the LMI construction applies directly, with drone time series over the resistant populations. Kona's slope is a natural gradient. And quality is a gate: resistant selections get cupped against Kona Typica before anyone talks release. I'd partner on the cup, not lead it.

**[`vision-how`](http://localhost:8000/presentation/#/vision-how)** · 0.5 min
- Pipelines · data · funding in one breath. Year one needs a camera rig and growth-room time, not a drone fleet.
- 10-min version: skip; keep for "what do you need?"

> How: open, reproducible pipelines; a coffee trait dictionary and BrAPI-compatible records deposited to GRIN-Global, so Innovea sites can compare; and a lean funding path — base funds, the HARC agreements, SCRI, state and industry rust funds, and Innovea. Year one needs a camera rig and growth-room time, not a drone fleet.

**[`vision-not-claiming`](http://localhost:8000/presentation/#/vision-not-claiming)** · 0.5 min
- Say the limits yourself, quickly: not a pathologist · not the genome group · not yet a coffee breeder · not permanent resistance · not a shorter generation.
- 10-min version: skip; use as Q&A answers.

> And what I'm not claiming. I'm not a pathologist, and I'm not the genome group. I'm not yet a coffee breeder — HARC has carried resistant material since 1992, and year one is learning it. I'm not promising permanent resistance: Catimor resistance has been overcome in Central America and Brazil. And I'm not shortening the generation — I'm raising accuracy and moving selection into the nursery.

**[`vision-deliverables`](http://localhost:8000/presentation/#/vision-deliverables)** · 0.5 min
- Five in 30 seconds; the footer is your answer to "year one?"
- **⏱** minute 46.

> In five years: an instrumented leaf-disc assay validated against the farm; QTL for quantitative resistance in the F2; tiered markers in HARC's and growers' hands; the first heritable flowering and ripening traits in Hawaiʻi coffee; and resistant selections, cup-checked, a decision earlier. *[Footer.]* Year one: image the leaf-disc runs, map the F2 with the genomics group, write the coordinate paper, and walk the farms. *[Minute 46.]*

### G. Close

**[`summary`](http://localhost:8000/presentation/#/summary)** · 0.75 min
- Land the last line and stop talking.

> In summary: six papers; three commitments in your project plans, each met by a method I've used once, in another perennial; and three aims — measure resistance, map it to markers people can use, and time the crop. Cranberry was the case study. The leaf disc is the next instrument. The locus is where it lands. *[Stop talking.]*

**[`acks`](http://localhost:8000/presentation/#/acks)** · 0.25 min
- Zalapa, Digman, committee, growers, funders; Tracie, Dr. Wall and the panel. 15 s. "Mahalo."

> Thank you to Juan Zalapa and the Digman lab, my committee, and the growers and funders behind this work — and mahalo to Tracie, Dr. Wall and the panel. I'm happy to take questions.

**[`references`](http://localhost:8000/presentation/#/references)**
- Untimed. Press o to jump to any backup.

**[`questions`](http://localhost:8000/presentation/#/questions)**
- What do you add to our QTL work? A phenotype with more than three values, on every F2 plant.
- Allotetraploid? Disomic → two diploids; map to C + E; parents filter false hets (`backup-allo-calling`).
- Escapes / inoculum? Checks every run, blind duplicates, spore viability, qPCR.
- When does a grower get a tree? Years, not months — 'Mamo' took ~18; cupping gates release.
- Innovea / F1 hybrids? Shared protocol and panel (`backup-f1-hybrids`).
- Year one? Leaf-disc imaging · map the F2 with Yu's group · coordinate paper · walk the farms.
- Full answers: Prep section at the end of the deck, or the prep document.

> *[Open the floor.]* Mahalo — I'm happy to take questions. *[Listen to the whole question, restate it for anyone remote, answer in two or three sentences, and offer a backup slide if one fits.]*

### Backup — Q&A

**[`backup-title`](http://localhost:8000/presentation/#/backup-title)**
- Coffee backups first (rust genetics, genomes, phenotyping, allotetraploid calls, stacking, F1 hybrids, trait evaluation), then rhAmpSeq vs Flex-Seq and the cranberry material.

**[`backup-clr-genetics`](http://localhost:8000/presentation/#/backup-clr-genetics)**
- SH1–SH9 / v1–v9; race XXIV = v2,4,5; not SH1 (Geisha) or SH3 (S.288). Keith's result — cite, don't explain.

> *If asked about rust genetics:* There are at least nine race-specific factors. Hawaiʻi's race XXIV beats SH2, SH4 and SH5 — Kona Typica, Bourbon and Catuaí — but not SH1 or SH3. The canephora-derived factors in Catimors still hold here as far as published, though they've been overcome elsewhere. That's why I'd measure the partial components underneath.

**[`backup-arabica-genome`](http://localhost:8000/presentation/#/backup-arabica-genome)**
- Allo, disomic; Kona Typica numbers; Timor Hybrid 7–11%, mostly subgenome C; unit genomes; Pearl 2004.

> *If asked about the genome:* Two diploid subgenomes from one hybridization; your Kona Typica assembly at chromosome scale; Timor Hybrid introgression covering 7 to 11% of the genome, mostly in the canephora subgenome, with clusters of resistance-gene arrays that respond to rust. In your F2, that's where the polymorphism will be.

**[`backup-clr-phenotyping`](http://localhost:8000/presentation/#/backup-clr-phenotyping)**
- Leaf disc → chamber → leaf on farm → tree across sites → UAV and sensors. The gap: continuous, heritable components on every plant of a mapping population.

> *If asked what exists already:* The leaf-disc method goes back to Eskes in 1982; growth-chamber work shows big latency differences; farm monitoring uses photos and ImageJ; WCR's global trial uses a 1-to-5 scale across 23 sites; and drone and hyperspectral work is mostly detection on small samples. What's missing is continuous, heritable measures on every plant of a mapping population.

**[`backup-allo-calling`](http://localhost:8000/presentation/#/backup-allo-calling)**
- Four rules: allo not auto · map to both subgenomes · filter with parents · expect blocks. Honest line last.

> *If Dr. Yu asks about the allotetraploid:* Arabica is disomic, so I'd treat it as two diploids. Map reads to both subgenomes so they find their true home; treat a het call in a pure-line parent as a homoeolog artifact; keep markers that are polymorphic between parents and single-copy in their subgenome; design KASP homoeolog-specific; and expect big blocks with little recombination inside the Timor Hybrid segments. Cranberry was diploid, so this filtering I'd build with your group, on your assembly.

**[`backup-stacking`](http://localhost:8000/presentation/#/backup-stacking)**
- Myers et al. 2023: Ethiopian E17/E25/E52 Rf < 1; Tupi-HI 7.12, Obatã 2.33. The authors suggest the cross. For Myers and Nagai.

> *If asked about nematodes:* Dr. Myers's screen found three Ethiopian accessions resistant to the Kona root-knot nematode, while the rust-resistant Tupi and Obatã are susceptible. The paper suggests crossing them. I'd build that cross as a mapping population from day one, so markers for both traits pay off in the same nursery.

**[`backup-f1-hybrids`](http://localhost:8000/presentation/#/backup-f1-hybrids)**
- Heterosis over pure lines (no percentages — unverified); deployment by somatic embryogenesis or male sterility; Mundo Maya most resistant in the WCR trial. Hilo's hook: the tissue-culture objective.

> *If Dr. Long or Dr. Muszynski asks about F1 hybrids:* They're where arabica breeding is heading — heterosis for yield, often longer rust latency — but they don't breed true, so they go out through somatic embryogenesis, cuttings or a male-sterile mother. Hilo's tissue-culture objective is the hook, and Innovea gives access to network hybrids. What I'd add is the same phenotypes, so hybrids and pure lines are compared on one scale.

**[`backup-trait-evaluation`](http://localhost:8000/presentation/#/backup-trait-evaluation)**
- Repeatable → heritable → holds across environments → changes a decision.

> *If asked how you evaluate a trait:* Is it repeatable — the same number from a different run or scorer? Is it heritable on the unit I select? Does it hold from lab to farm and across elevations? And does it change a decision — cut sprays, keep the cup, save a picking round? If not, it isn't worth measuring.

**[`backup-rhampseq-flexseq`](http://localhost:8000/presentation/#/backup-rhampseq-flexseq)**
- rhAmpSeq = transferable across a genus; Flex-Seq = density within a species. Coffee's introgressions (canephora, liberica segments) are where the rhAmpSeq lesson applies.

> *If asked which kind of panel:* rhAmpSeq was designed to transfer across a genus; Flex-Seq for density within a species. In coffee, the canephora and liberica segments are where transferability matters — markers designed on arabica can drop out inside introgressions.

### Prep — not presented

**[`prep-top`](http://localhost:8000/presentation/#/prep-top)**
- Prep only — not presented. Full version: TPGRDRU_Seminar_Prep.md.

**[`prep-dont-say`](http://localhost:8000/presentation/#/prep-dont-say)**
- Prep only — not presented.

**[`prep-qa`](http://localhost:8000/presentation/#/prep-qa)**
- Prep only — not presented.

---

## 6. What the 29 Sep web check changed

Checked against primary sources the night before; the deck and notes already use the corrected versions.

- **The leaf-disc assay is not just resistant/susceptible.** HARC's SCRI report says the bioassays measure "latency period, percentage of lesions, and reaction type," with ANOVA and Tukey tests, and report R / T / S classes. The pitch is now *instrument and quantify* what is scored by eye — not replace a binary call.
- **Parentage is already a problem they check:** 11 of 14 Catimor crosses and 21 of 25 Obatã crosses had parentage confirmed by genotyping. That's the Flex-Seq identity story's natural bridge.
- **FY2024 vs FY2025.** FY2024: four genomes (T5175, T8667, Typica, Mokka), 222,771 SNPs + 557,623 indels. FY2025: Mokka and Catimor 5175 assemblies (scaffold N50 48.84 / 50.57 Mb), leaf-disc screen of the F2, **8 R + 8 S** sequenced (34 / 39 Gb), differential SNPs "on chromosomes" (none named).
- **-019-008-S cooperator is HARC** (resolves the plan's ⚠). -024-A (Jun 2026 – Oct 2028) quotes "develop a high throughput, on farm, CLR susceptibility assay to more quickly identify susceptible genotypes."
- **Invasion study: 17 countries**, not 18. **WCR rust study: 15 countries** in the analysis (29 varieties, 23 sites; 18 was the network).
- **Kona Typica assembly ~1.13 Gb** (scaffold N50 50.5 Mb) — not 1.17.
- **Harvesting paper first author is Aristizábal** (Aristizábal, Johnson, Shriner & Wall 2023, *J. Econ. Entomol.* 116:513–519): 4.6% vs 9.0% infestation, +3,024 lb cherry/acre, −55% chemical cost, +48% net benefit, 10 farms.
- **Salojärvi chr-4 cluster:** tandem arrays of RPP8-like (5), CPR1-like (10) and LRK10L-like (3) genes, up-regulated after infection — not "ten RPP8s".
- **Pearl et al.:** the ARS record dates it 2003; the TAG issue is 2004 (108:829). Either is fine; the deck says 2004.
- **Marin et al. 2021** authors confirmed (Marin, Ferraz, Santana, Barbosa, Barata, Osco, Ramos, Guimarães; *Comput. Electron. Agric.* 190:106476).
- **Catimor breakdown** citation: Berny Mier y Terán et al. 2025 ("in Central America and Brazil, the resistance of Catimors has been overcome"), citing Capucho et al. 2012 and Brenes et al. 2025.
- **Mamo** confirmed: HARC crosses 1999, planted in Kona 2009, F5–F6, market spring 2017, cupped 84.5–85.5. The article credits "Kimo Faulkner" of the growers' association — possibly Kimo Falconer misspelled; ⚠ don't assert it.
- **Still ⚠:** exact F1-hybrid heterosis percentages (Bertrand et al. 2011) — not read; Eskes 1982 volume and pages; whether the unit uses BrAPI / Breeding Insight; who holds the ORISE rust-QTL postdoc.

## Sources checked

- ARS 2040-21000-018-000-D FY2024 and FY2025 reports: https://www.ars.usda.gov/research/project/?accnNo=444088 · -019-008-S: https://www.ars.usda.gov/research/project/?accnNo=444991 · -019-024-A: https://www.ars.usda.gov/research/project/?accnNo=448143
- HARC SCRI CLR pipeline (NIFA 1029149): https://portal.nifa.usda.gov/enterprise-search/cris_projects/1029149
- USDA NASS Coffee, Jan 2026: https://www.nass.usda.gov/Publications/Todays_Reports/reports/cafean26.pdf · HDOA CLR: https://dab.hawaii.gov/pi/main/clrinfo/
- Race XXIV (Keith et al. 2023): https://www.ars.usda.gov/research/publications/publication/?seqNo115=402712 · invasion genotyping (Ramírez-Camejo et al. 2022): https://www.mdpi.com/2309-608X/8/2/189
- Aristizábal & Johnson 2022: https://www.mdpi.com/2073-4395/12/5/1134 · fungicides 2025: https://www.sciencedirect.com/science/article/pii/S0261219425001619 · CBB harvesting 2023: https://academic.oup.com/jee/article/116/2/513/7070632
- Kona Typica genome: https://www.nature.com/articles/s41597-025-05658-6 · Salojärvi et al. 2024: https://www.nature.com/articles/s41588-024-01695-w · Pearl et al.: https://www.ars.usda.gov/research/publications/publication/?seqNo115=150010
- WCR global rust trial: https://www.frontiersin.org/articles/10.3389/fpls.2025.1583595/full · https://worldcoffeeresearch.org/news/2025/coffee-leaf-rust-knows-no-borders-neither-does-coffee-science · WCR KASP panel: https://worldcoffeeresearch.org/resources/arabica-ldp-snp-marker-panel · ARS joins Innovea: https://www.ars.usda.gov/news-events/news/research-news/2023/usda-ars-joins-wcr-global-coffee-breeding-network-adds-access-to-new-germplasm/
- Toniutti et al. 2017: https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2017.02025/full · Eskes leaf-disk method: https://www.semanticscholar.org/paper/The-use-of-leaf-disk-inoculations-in-assessing-to-Eskes/0949563d84d5f4c9c1b9ff7758f61a5248b9097d · Heller et al. 2025: https://link.springer.com/article/10.1007/s42161-025-01991-2
- Rodriguez-Gallo et al. 2023: https://www.mdpi.com/2624-7402/5/3/88 · Marin et al. 2021: https://researchr.org/publication/MarinFSBBORG21 · OSU–WCR AFRI project: https://portal.nifa.usda.gov/web/crisprojectpages/1030028-developing-field-based-high-throughput-phenotyping-for-coffee-yield-physiological-performance-and-disease-resistance.html
- Myers et al. 2023: https://www.mdpi.com/2077-0472/13/6/1168 · Unigarro et al. 2025: https://www.mdpi.com/2223-7747/14/21/3396 · Mamo: https://www.bigislandvideonews.com/2018/11/11/kona-farm-introduces-mamo-hawaiian-coffee-variety/

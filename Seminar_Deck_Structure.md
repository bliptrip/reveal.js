# TPGRDRU coffee seminar deck — structure, timing and references

_Drafted 2026-09-29 as the first coffee version, ported from the SGPG potato deck that `presentation/index.html` was copied from (branch `sgpgpotato_seminar_2026`). Every potato slide, note and citation was replaced with Hilo coffee content; the talk was retimed to 35 min research + 12 min vision/close (47 min, `totalTime: 2820`) + ~13–15 min questions; five new slides carry the coffee bridge (`why-coffee`, `qtl-plain`, `ch3-leafdisc`, a coffee `cycle` figure, and the whole vision block); the potato backups were replaced with seven coffee backups. The plan behind it is `../../prep/Maule_TPGRDRU_Seminar_Plan.md`; the crop background is `../../prep/TPGRDRU_Coffea_Genetics_Primer.md`. Lives beside the deck: `Maule_2026_10_TPGRDRUSeminar/presentation/index.html` (reveal.js port)._

**Companion files in this folder**

- `TPGRDRU_Seminar_Prep.md` — the morning-of prep doc. Its section 5 bullets **are** the speaker notes (with a spoken script under each).
- `tools/speaker_notes.py` — moves speaker notes between the deck and Markdown, and restamps timing. See "Working with the notes" below.

## Title and slot

**From Leaf Disc to Locus: High-Throughput Phenotyping and Genetic Mapping for Resistance and Resilience in Perennial Crops.** "Leaf disc" is the unit's own assay (ARS FY2025 report); "locus" is where Sub-objective 3.A has to land. The tension — CJ has never run a leaf-disc assay — is resolved in the first minute (`title-new` notes).

Venue and slot: **Wednesday 30 September 2026, 8:30**, DKI-USPBARC, Hilo (Tropical Plant Genetic Resources and Disease Research Unit). The schedule says "45 to 50 minutes presentation on background, research, vision for this position with 15 minutes of Q&A"; `documents/Overview.md` asks for ~35 min research + 10–15 min vision + 10–15 min Q&A. The deck is timed to **35 + 12 = 47 min**, leaving 13–15 min of questions. Evaluation panel (Overview): Keith, Yu, Nagai, Muszynski, Long, Shriner, Falconer — four scientists, three industry.

## Timing

| Block | Slides | Min | Ends ≈ |
|---|---|---|---|
| A. Opening (title, path, **coffee cycle**, map to the unit's commitments) | 4 | 3.0 | 3 |
| B. Cranberry as a model system (crop, **why a coffee audience should care**, **three terms in plain words**, exposure problem) | 4 | 3.25 | 6.25 |
| C. Meta-QTL and its deliverables: VacCAP review (Albert et al.) + Flex-Seq platform (Clare et al.) | 11 | 8.0 | 14.25 |
| D. Image phenomics: UAV & the LMI + BerryPortraits + **berry → leaf disc** | 13 | 10.5 | 24.75 |
| E. Genetics of the LMI | 7 | 7.0 | **31.75** |
| **Research subtotal** | **39** | **31.75** | |
| F. Vision for coffee at TPGRDRU (headline, why now, where it fits, Aim 1 ×2, Aim 2 ×2, Aim 3, not claiming, deliverables) | 10 | 12.25 | 44 |
| G. Close (summary, acks; References & Questions untimed) | 4 | 1.0 | 45 |
| **Vision + close** | | **13.25** | |
| Backup (how/funding + 7 coffee + rhAmpSeq vs Flex-Seq + 32 cranberry) | 42 | — | |
| Prep — not presented (`data-visibility="hidden"`) | 3 | — | |

**Retimed 30 Sep 2026 to the SHRS cacao deck's shape** (Cacao: 30 research / 13.5 vision / 1.5 close = 45). The first draft budgeted the vision at ~1 min per slide (Cacao ~1.5), so it would have run ~49 min against a hard 9:30 stop. Research padding went back to Cacao timings (why-coffee 1.25, populations-map 0.75, ch2-h2-corr 0.5, ch2-flexseq 1.25, ch2-takeaways 0.5, ch3-berryportraits 0.5, ch3-lmi 1.25, ch4-qtl 1.25, ch4-genes 1.5, ch4-breeder 1.5, ch4-takeaways 0.5); the coffee bridges (`qtl-plain`, `ch3-leafdisc`) kept their time; vision slides got realistic minutes (headline 0.75, why-now 1.25, fit 1.25, aim3 1.25, not-claiming 0.75, deliverables 1.0) and `vision-how` moved to backup as `backup-how`. `python3 tools/speaker_notes.py list` has the per-slide minutes.

**Vision cuts.** 10-min version: skip `vision-not-claiming` (its lines become Q&A answers; `backup-how` is already out) and give Aim 3 one sentence. 15-min version: add `backup-stacking` after Aim 3. Never cut Q&A.

## What changed from the SGPG deck

- **Replaced (body and notes):** `title-new` (title, subtitle, icons, footer), `cycle` (new inline-SVG coffee pipeline — 'Mamo' 1999 → 2017), `map` (the unit's commitments in their own words), `why-potato` → `why-coffee`, the whole vision block, `summary`, the "Cited on the slides" half of `references`, all Q&A notes, `backup-title`, `backup-trait-evaluation`, and the three prep slides.
- **New:** `qtl-plain` (QTL, h², AUDPC for the industry half of the panel, with an illustrative inline SVG), `ch3-leafdisc` (BerryPortraits figure beside an illustrative leaf-disc time series with latency and AUDPC — labelled "illustrative mock — not data"), `vision-why-now`, `vision-aim1-field`, `vision-aim2-markers`, and coffee backups `backup-clr-genetics`, `backup-arabica-genome`, `backup-clr-phenotyping`, `backup-allo-calling`, `backup-stacking`, `backup-f1-hybrids`.
- **Moved into the timed talk:** `vision-how` and `vision-not-claiming` (were backups `backup-how` / `backup-not-claiming` at Aberdeen).
- **Dropped:** `backup-potato-genotyping`, `backup-potato-phenomics`, `backup-how`, `backup-not-claiming`.
- **Kept verbatim (body):** all cranberry research slides. Small text edits where a slide carried a potato bridge: the last bullet of `frost`, `ch2-takeaways` and `ch4-takeaways`; the "translation" box in `ch4-genes`; one added bullet in `ch4-breeder`; the cite line on `ch2-why`; the thanks line on `acks`. All notes were rewritten for coffee.
- **Figures are inline SVG** (`cycle`, `qtl-plain`, `ch3-leafdisc`) so they are tracked in git — `static/images/` is git-ignored. No new media files are needed; the existing cranberry figures and videos in `static/` are the same set the Aberdeen deck used.

## Framing decisions

**The genomics is Yu's; the phenotype is the gap.** The unit (Matsumoto, Yu, HARC) has four parental genomes, the Mokka × Catimor 5175 F2, a leaf-disc screen and a bulked-segregant analysis on 8 + 8 plants; Yu mentors an ORISE postdoc on rust QTL. The vision is pitched as the phenotype and quantitative genetics her genomics needs — "with your group, on your assembly" — never as a second genomics program.

**Instrument, don't invent.** HARC's SCRI report shows the leaf-disc bioassay already scores latency, % lesions and reaction type, reported as resistant / tolerant / susceptible (210 / 939 / 894 across 14 Catimor crosses). Aim 1 is time-lapse imaging of that assay, so the components become continuous, blind and repeatable — and the 939-plant "tolerant" class gets split.

**The cycle slide.** Honest framing again: a pure-line arabica generation stays ~3 years; markers in the nursery, leaf-disc numbers and growers' farms change how many trees are carried and how early decisions are made. 'Mamo' (HARC 1999 → market 2017) is the sourced local example; phase lengths are illustrative and Nagai is invited to correct them.

**Allo, not auto.** Arabica is disomic. The deck says it once on `why-coffee` ("simpler to map, harder to genotype") and once on `vision-aim2`; the detail waits in `backup-allo-calling` for Yu's question. Cranberry being diploid is stated plainly.

**Stakeholder panel.** Every aim leads with the grower outcome; `qtl-plain` defines QTL, h² and AUDPC once; `vision-why-now` puts the spray cost on the slide for Shriner and Falconer; `vision-fit` names roles, not people (say the names aloud).

**Honesty lines to volunteer.** Not a pathologist; not the genome group; not yet a coffee breeder (HARC since the late 1990s — ARS -019 project text); not permanent resistance (Catimor resistance overcome in Central America and Brazil); not a shorter generation. Only disease trait: cranberry fruit rot, a multi-fungus complex.

## Verification pass, 30 Sep 2026

Fixed on the slides: Kauaʻi added to the island list (Ramírez-Camejo 2022: every coffee island by July 2021); "since 1992" → "since the late 1990s"; Obatã "slightly susceptible"; map row 1 no longer claims fruit rot for the meta-QTL (moved to the Flex-Seq row, Clare 2026 1 → 4); "caught mislabelled parents" → "flagged a likely mislabelled parent"; qPCR "to confirm infection early"; ripening ~220–240 d; BerryPortraits r ≥ 0.94; WCR trial "23 sites on three continents"; prep slides `hidden` (were `uncounted`, which shows in the overview grid). Open: manuscript says **leaf** maturity index, deck says **late**.

## Verify before the room

- ⚠ Who is on Teams (Long likely remote), who chairs, whether Matsumoto attends and whether the position is new or a backfill.
- ⚠ CLR arrival month (Feb vs Oct 2020) — the deck says "2020, on Maui."
- ⚠ F1-hybrid heterosis percentages (Bertrand et al. 2011) — not on any slide; don't quote.
- ✓ Eskes 1982 = *Neth. J. Plant Pathol.* 88:127–141. ⚠ Whether the unit uses BrAPI / Breeding Insight; who holds the ORISE postdoc.
- ⚠ MauiGrown as the only commercial Mokka grower (their claim); Nagai's pronouns.
- ⚠ The 'Mamo' article's "Kimo Faulkner" — possibly Falconer; don't assert.

## Working with the notes (`tools/speaker_notes.py`)

The `Makefile` wraps every direction: `make` lists the targets; `make sync` pushes the prep doc (cues, minutes, scripts) into the deck and checks it; `make notes-to-prep` goes the other way. Each target's comment in the Makefile says which files it reads and which it overwrites.

```bash
python3 tools/speaker_notes.py list                                   # slides, minutes, note lengths, section end-times
python3 tools/speaker_notes.py extract -o Speaker_Notes.md            # all notes → Markdown
python3 tools/speaker_notes.py update --from TPGRDRU_Seminar_Prep.md  # prep-doc bullets → deck notes
python3 tools/speaker_notes.py extract --into TPGRDRU_Seminar_Prep.md # deck notes → prep-doc bullets (scripts untouched)
python3 tools/speaker_notes.py update --from X.md --apply-minutes     # also apply "· N min" from headings, then restamp
python3 tools/speaker_notes.py restamp                                # after adding / moving / retiming slides
python3 tools/speaker_notes.py check                                  # HTML → Markdown → HTML round-trip test
python3 tools/speaker_notes.py scripts --from TPGRDRU_Seminar_Prep.md  # "> " spoken scripts → highlighted FULL SCRIPT box below the cues
python3 tools/speaker_notes.py scripts --remove                       # strip the script boxes again
```

A slide's notes are the lines directly under its `**[`id`](…)** · N min` heading, up to the first blank line: `- ` lines become `<li>`, other lines `<p>`; `**bold**`, `*italic*`, and `<sub>`/`<sup>`/`<br>` pass through. Slides not mentioned in the Markdown keep their notes. Since 30 Sep every timed slide (and the backups that have one) also carries its spoken script from the prep doc, after a dashed rule in an amber box; `list`, `extract` and `check` ignore that box and `update` preserves it, so after editing a script in the prep doc rerun `scripts --from`. The deck is edited as text, so nothing outside the `<aside class="notes">` (and, for restamp, the `<section>` timing attributes and `totalTime`) changes.

## References cited in the deck

Slide ids in brackets are where each reference appears (slide text or notes). ⚠ = verify before saying in the room. ✓ = checked against the source on 29 Sep 2026.

### CJ's own work and cranberry sources

- Maule, A. F., et al. (2024). Of buds and bits: a meta-QTL study identifies stable QTL for berry quality and yield traits in cranberry mapping populations. *Frontiers in Plant Science* 15:1294570. https://doi.org/10.3389/fpls.2024.1294570 · code: https://github.com/bliptrip/CNJ0x-Trait-Mapping [ch2-*, map, summary]
- Clare, S. J., …, Maule, A. F., Zalapa, J., …, Bassil, N. V. (2026). A high-recovery, high-density targeted genotyping platform for cranberry. *The Plant Genome* 19(1):e70153. https://doi.org/10.1002/tpg2.70153 [ch2-flexseq, map, backup-rhampseq-flexseq]
- Maule et al. — Modeling spring greening patterns among cranberry genotypes via aerial imaging of leaf color. Under review, *Smart Agricultural Technology* [ch3-*]
- Maule et al. — Mapping the genetic basis of temporal segregation of spring greening in cranberry. In preparation for *G3* [ch4-*]
- Maule, A. F. (2025). *Waders to Wings*. Ph.D. dissertation, UW–Madison [references]
- Albert, N. W., …, Maule, A., …, Espley, R. V. (2023). *Vaccinium* as a comparative system for understanding of complex flavonoid accumulation profiles and regulation in fruit. *Plant Physiology* 192(3):1696–1710. https://doi.org/10.1093/plphys/kiad250 [ch2-vaccap, map]
- Loarca, J., Wiesner-Hanks, T., Lopez-Moreno, H., Maule, A. F., et al. (2024). BerryPortraits. *Plant Methods* 20:172. https://doi.org/10.1186/s13007-024-01285-1 [ch3-berryportraits, ch3-leafdisc, map]
- Daverdin, G., et al. (2017). Fruit rot resistance QTL in cranberry. *Molecular Breeding* 37:38 — fruit rot is a fungal complex [references; why-coffee notes]
- Workmaster, B. A. A., & Palta, J. P. (2006). *J. Am. Soc. Hortic. Sci.* 131:327–337 [ch3-biology]
- Zou, C., et al. (2020). rhAmpSeq. *Nature Communications* 11:413 [backup-rhampseq-flexseq]

### Coffee leaf rust in Hawaiʻi

- ✓ Keith, L. M., Matsumoto Brower, T. K., Sugiyama, L. S., Fukada, M., Nagai, C., Pereira, A., Silva, M., & Várzea, V. (2023). First report of the physiological race XXIV of *Hemileia vastatrix* in Hawaiʻi. *Plant Disease*. https://doi.org/10.1094/PDIS-03-23-0460-PDN — v2,4,5 in every sample from Hawaiʻi Island, Maui and Molokaʻi; defeats SH5, SH2,5, SH4,5; not SH1,5 / SH3,5 / SH1 [vision-why-now, backup-clr-genetics]
- Keith, L. M., et al. First report of coffee leaf rust … in Hawaii. *Plant Disease*. https://doi.org/10.1094/PDIS-05-21-1072-PDN (⚠ page not readable here) [notes]
- ✓ Ramírez-Camejo, L. A., Keith, L. M., Matsumoto, T., …, Aime, M. C. (2022). *J. Fungi* 8(2):189. https://www.mdpi.com/2309-608X/8/2/189 — 434 isolates, 17 countries, 11 SSRs, MLG 10 [vision-why-now]
- ✓ Aristizábal, L. F., & Johnson, M. A. (2022). *Agronomy* 12(5):1134. https://www.mdpi.com/2073-4395/12/5/1134 — < 4% early → 36% at harvest; 30 lots, 204–875 m; ImageJ severity on the leaf underside [vision-why-now, vision-aim1-field]
- ✓ Aristizábal, L. F., Maeda, C. T., Matsumoto, T., & Johnson, M. A. (2025). *Crop Protection* 196:107269. https://www.sciencedirect.com/science/article/pii/S0261219425001619 — Priaxor < 2% / 12 wk / $140; copper < 5% / 6–8 wk / $126; biologicals failed ($138–198) [vision-why-now]
- ✓ Heller, W. P., Kissinger, K. R., Brill, E., Torres-Cruz, T. J., Aime, M. C., & Keith, L. M. (2025). Real-time PCR assay detection of *H. vastatrix*. *J. Plant Pathology*. https://link.springer.com/article/10.1007/s42161-025-01991-2 [vision-aim1]
- ✓ HDOA CLR page: https://dab.hawaii.gov/pi/main/clrinfo/ — first detected Oct 2020; Maui, Hawaiʻi Island, Oʻahu, Lānaʻi [vision-why-now]
- ✓ USDA NASS, Coffee (Jan 2026): https://www.nass.usda.gov/Publications/Todays_Reports/reports/cafean26.pdf — 2024–25: 7,000 bearing acres, 5.26 M lb parchment, $14.80/lb, $53.017 M [vision-why-now]

### Coffee genetics, genomics and breeding

- ✓ Lyu, H., Song, J., Yin, Y., Wang, M.-L., Matsumoto, T., …, Yu, Q. (2025). Kona Typica genome. *Scientific Data*. https://www.nature.com/articles/s41597-025-05658-6 — > 90% of coffee produced in Kona; ~1.13 Gb; 22 chr; BUSCO 99.1%; 65,458 genes; 65.16% repeats; Guatemala 1892 [vision-why-now, backup-arabica-genome]
- ✓ Salojärvi, J., et al. (2024). *Nature Genetics*. https://www.nature.com/articles/s41588-024-01695-w — 350–610 ka; Timor Hybrid 7–11% of the genome, mostly subgenome C; RPP8-, CPR1-, LRK10L-like arrays up-regulated after infection [vision-aim2, backup-arabica-genome]
- ✓ Pearl, H., Nagai, C., Moore, P. H., Steiger, D., Osgood, R., & Ming, R. (2004; ARS record 2003). Construction of a genetic map for arabica coffee. *Theor. Appl. Genet.* 108:829. https://www.ars.usda.gov/research/publications/publication/?seqNo115=150010 [cycle, vision-aim2, backup-arabica-genome]
- ✓ Myers, R. Y., Mello, C., Nagai, C., Sipes, B., & Matsumoto, T. (2023). *Agriculture* 13(6):1168. https://www.mdpi.com/2077-0472/13/6/1168 — Obatã Rf 2.33 "slightly susceptible"; rootstocks named are Dewevrei / Nemaya · 'Fukunaga': Bittenbender et al. 2001, CTAHR [backup-stacking]
- ✓ Berny Mier y Terán, J. C., et al. (2025). Global *C. arabica* variety trials reveal G×E in resistance to coffee leaf rust. *Front. Plant Sci.* 16:1583595. https://www.frontiersin.org/articles/10.3389/fpls.2025.1583595/full — 29 varieties, 23 sites on three continents in the rust analysis (country count only in Supp. Table S1A; 18 countries = whole network); 1.47 vs 2.03; EC16 most resistant; Catimor resistance overcome in Central America and Brazil (Capucho 2012; Brenes 2025) [vision-not-claiming, backup-clr-*, backup-f1-hybrids]
- ✓ WCR *C. arabica* KASP variety-ID panel (2023): https://worldcoffeeresearch.org/resources/arabica-ldp-snp-marker-panel — 45 SNPs; 1,424 samples; 30,000+ validation; ARS a partner [vision-aim2-markers]
- ✓ USDA-ARS joins WCR Innovea (28 Mar 2023): https://www.ars.usda.gov/news-events/news/research-news/2023/usda-ars-joins-wcr-global-coffee-breeding-network-adds-access-to-new-germplasm/ [vision-fit]
- Merot-L'Anthoene, V., et al. (2019). Coffee 8.5K SNP array. *Plant Biotechnol. J.* https://onlinelibrary.wiley.com/doi/10.1111/pbi.13066 [notes]
- Review: Exploring the genetic potential for multi-resistance to rust … (2025). *Plants* 14(3):391. https://www.mdpi.com/2223-7747/14/3/391 [backup-clr-genetics]
- ⚠ Bertrand, B., et al. (2011). Performance of *C. arabica* F1 hybrids … *Euphytica*. https://link.springer.com/article/10.1007/s10681-011-0372-7 (percentages not verified) · Georget, F., et al. (2019). Starmaya [backup-f1-hybrids]

### Rust phenotyping

- ✓ Eskes, A. B. (1982). The use of leaf disk inoculations in assessing resistance to coffee leaf rust (*Hemileia vastatrix*). *Netherlands Journal of Plant Pathology* 88:127–141 (leaf-disc scores explained 79% of field variation). https://link.springer.com/article/10.1007/BF01977270 [vision-aim1, backup-clr-*]
- ✓ Toniutti, L., et al. (2017). *Front. Plant Sci.* 8:2025. https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2017.02025/full — latency ~21 d Caturra vs ~37 d hybrids (27–22 °C) [ch3-leafdisc, vision-aim1, backup-clr-phenotyping]
- ✓ Rodriguez-Gallo, Y., Escobar-Benitez, B., & Rodriguez-Lainez, J. (2023). *AgriEngineering* 5(3):88. https://www.mdpi.com/2624-7402/5/3/88 — 96 UAV photos at 2.8 m [vision-aim1-field, backup-clr-phenotyping]
- ✓ Marin, D. B., Ferraz, G. A. S., Santana, L. S., Barbosa, B. D. S., Barata, R. A. P., Osco, L. P., Ramos, A. P. M., & Guimarães, P. H. S. (2021). *Comput. Electron. Agric.* 190:106476 [vision-aim1-field, backup-clr-phenotyping]
- ✓ OSU–WCR AFRI project, Developing field-based high-throughput phenotyping for coffee (2023–2027): https://portal.nifa.usda.gov/web/crisprojectpages/1030028-developing-field-based-high-throughput-phenotyping-for-coffee-yield-physiological-performance-and-disease-resistance.html [vision-aim1-field]

### Phenology and coffee berry borer

- ✓ Aristizábal, L. F., Johnson, M. A., Shriner, S., & Wall, M. (2023). Frequent and efficient harvesting as an economically viable strategy to regulate coffee berry borer on commercial farms in Hawaii. *J. Econ. Entomol.* 116(2):513–519. https://academic.oup.com/jee/article/116/2/513/7070632 [vision-aim3]
- ✓ Unigarro et al. (2025). Flowering and fruiting of *C. arabica*. *Plants* 14:3396. https://www.mdpi.com/2223-7747/14/21/3396 — 220–243 DAF (180–330); cultivars differ 30+ d; 5–10 mm rain breaks bud dormancy [ch4-genes, vision-aim3]

### Program and stakeholder sources

- ✓ ARS 2040-21000-018-000-D, FY2024 and FY2025 reports: https://www.ars.usda.gov/research/project/?accnNo=444088 [map, why-coffee, vision-*]
- ✓ ARS 2040-21000-019-008-S (HARC; Sep 2023 – Aug 2027): https://www.ars.usda.gov/research/project/?accnNo=444991 · ✓ -019-024-A (HARC; Jun 2026 – Oct 2028): https://www.ars.usda.gov/research/project/?accnNo=448143 [map, vision-aim1]
- ✓ HARC SCRI, Developing an efficient breeding pipeline for producing CLR-resistant coffee cultivars (PI Wang; 2022–2026): https://portal.nifa.usda.gov/enterprise-search/cris_projects/1029149 — leaf-disc bioassays scoring latency, % lesions, reaction type; 210/939/894 (14 crosses, 11 confirmed); 183/243/162 (25 crosses, 21 confirmed) [why-coffee, cycle, vision-aim1]
- ✓ 'Mamo' (Big Island Video News, 2018): https://www.bigislandvideonews.com/2018/11/11/kona-farm-introduces-mamo-hawaiian-coffee-variety/ [cycle]
- Panel and people background: `../../people/` and `../../prep/Maule_TPGRDRU_Seminar_Plan.md` §6, §9.

# FSCRU hop seminar deck — structure, timing and references

_Drafted 2026-10-06 as the first hop version, ported from the TPGRDRU coffee deck (`../../../HiloHI-Coffea-Interview/presentations/Maule_2026_10_TPGRDRUSeminar/presentation/index.html`). Every coffee slide, note and citation was replaced with Prosser hop content; the talk is timed to 34.75 min research and outreach + 10.25 min vision + 1 min close (46 min, `totalTime: 2760`), leaving 20–30 min of questions inside the 8:30–10:00 slot. New slides carry the hop bridge (`scale`, `why-hops`, a hop `cycle` figure, `ch3-trellis`, `outreach`, and the whole vision block); the coffee backups were replaced with seven hop backups (how/funding plus six topics). The crop background is `../../prep/FSCRU_Humulus_Genetics_Primer.md`; the people are in `../../people/` (one file per person, `_Panel_and_Audience_Overview.md`, and `Prosser Hop Breeding — Potential Collaborators.md`). Lives beside the deck: `Maule_2026_10_FSCRUSeminar/presentation/index.html` (reveal.js port)._

**Companion files in this folder**

- `FSCRU_Seminar_Commute_Prep.md` — the commute and morning-of prep doc. Its section 5 bullets **are** the speaker notes (with a spoken script under each). The `Makefile` finds it as `PREP` (first `*_Prep.md`).
- `tools/speaker_notes.py` — moves speaker notes between the deck and Markdown, and restamps timing. See "Working with the notes" below.

## Title and slot

**From Bog to Bine: High-Throughput Phenotyping and Quantitative Genetics for Resilient Perennial Crops.** "Bog" is the cranberry case study; "bine" is the hop shoot climbing the string, and the vision. "Resilient" carries the posting's abiotic-stress emphasis without claiming tolerance physiology CJ hasn't done.

Venue and slot: **Wednesday 7 October 2026, 8:30–10:00**, Hamilton Hall, WSU Irrigated Agriculture Research and Extension Center, Prosser (USDA-ARS Forage Seed and Cereal Research Unit hop program). The brief (`../../documents/Overview.md`, from Dr. Hayes) asks for **45–50 min plus 20–30 min of questions**, a mixed ARS / WSU / industry audience, and five things: a biographical sketch; research showing breeding ability and better breeding methods — large populations across environments, phenomics, abiotic stress, outreach and adoption; and **a vision for hop breeding in Prosser in the last 5–10 minutes**. The panel Q&A follows at 10:00.

## Timing

| Block | Slides | Min | Ends ≈ |
|---|---|---|---|
| A. Opening (title, **bio sketch**, **hop cycle**, map to the posting's six objectives, **research at breeding scale**) | 5 | 4.5 | 4.5 |
| B. Cranberry as a model system (crop, **why a hop audience should care**, **three terms in plain words**, exposure problem) | 4 | 3.25 | 7.75 |
| C. Meta-QTL and its deliverables: VacCAP review (Albert et al.) + Flex-Seq platform (Clare et al.) | 11 | 8.0 | 15.75 |
| D. Image phenomics: UAV & the LMI + BerryPortraits + **bed → hedgerow** | 13 | 10.5 | 26.25 |
| E. Genetics of the LMI | 7 | 7.0 | 33.25 |
| F. **Outreach and adoption** | 1 | 1.5 | **34.75** |
| **Research + outreach subtotal** | **41** | **34.75** | |
| G. Vision for hop breeding in Prosser (headline, why now, where it fits, Aim 1 breed, Aim 2 measure, Aim 3 predict, adoption, not claiming, deliverables) | 9 | 10.25 | 45 |
| H. Close (summary, acks; References & Questions untimed) | 4 | 1.0 | 46 |
| Backup (title, how/funding, who I'd work with, 6 hop topics, trait evaluation, rhAmpSeq vs Flex-Seq, 32 cranberry) | 43 | — | |
| Prep — not presented (`data-visibility="hidden"`: top, don't say, panel, Q&A) | 4 | — | |

Research timings are the TPGRDRU deck's (rehearsed); `ch3-trellis` takes `ch3-leafdisc`'s 1.25 min. The vision runs 10.25 min with `vision-not-claiming`, the top of the brief's 5–10 min window plus the summary.

**Vision cuts.** ~8.5-min version: skip `vision-not-claiming` (its lines become Q&A answers) and take `vision-adoption` in one sentence. Never cut Q&A — the brief reserves 20–30 min.

## What changed from the TPGRDRU deck

- **Replaced (body and notes):** `title-new` (title, subtitle, footer), `cycle` (new inline-SVG hop pipeline, ~10 years, Thora 2015 → Oct 2025), `map` (the posting's six research objectives in its own words, five rows), `why-coffee` → `why-hops`, `qtl-plain` (QTL · h² · **genomic prediction**, with an alpha-acid illustration), the last bullet of `frost`, the cite line on `ch2-why`, the forward bullet on `ch2-takeaways`, the translation box in `ch4-genes`, the last bullet of `ch4-breeder` and `ch4-takeaways`, the whole vision block, `summary`, `acks` thanks line, the "Cited on the slides" half of `references`, all Q&A notes, `backup-title`, `backup-how`, `backup-trait-evaluation`, the footnote on `backup-rhampseq-flexseq`, and the three prep slides.
- **New:** `scale` (the brief's "large populations across multiple environments" — 235 F1 seedlings × 3 seasons, 40 traits, 597 genotypes × 2 sites × 8 dates, 10,489 repeated plot images), `ch3-trellis` (inline-SVG: overhead sees all of a cranberry bed but only the top of an 18-ft hop hedgerow; a cart down the alley sees the canopy face — labelled "illustrative"), `outreach` (Wisconsin Cranberry School 2024 and 2025, VacCAP 2025, open tools → brewers as the assay, HRC grow-outs, grower units), `vision-adoption`, and hop backups `backup-hop-genome`, `backup-cp-mapping`, `backup-dioecy`, `backup-pm`, `backup-water`, `backup-sensing`.
- **Dropped:** `ch3-leafdisc`, `vision-aim1-field`, `vision-aim2-markers`, and the coffee backups (`backup-clr-genetics`, `backup-arabica-genome`, `backup-clr-phenotyping`, `backup-allo-calling`, `backup-stacking`, `backup-f1-hybrids`).
- **Kept verbatim (body):** all other cranberry research slides and the 32 cranberry backups. All notes on timed slides were rewritten for hop.
- **Figures are inline SVG** (`cycle`, `qtl-plain`, `ch3-trellis`) so they're tracked in git — `static/images/` is git-ignored. No new media files are needed.

## Framing decisions

**The fit is close; say it, then say three differences.** Coffee needed an "honest difference" opening; hop doesn't. Hop and cranberry are both clonally propagated, highly heterozygous perennials mapped in F1 full-sib (cross-pollinated) families. `why-hops` says so and names the three real differences — dioecy, North American × European structural divergence (Apollo, 2026), and the 18-ft trellis — which the vision then answers (Aim 3 for the first two, Aim 2 and `ch3-trellis` for the third).

**This hire is the cultivar developer.** The posting's Objectives 1 and 6 are cultivars and adoption, and the brief asks for "abilities as a plant breeder." So Aim 1 is breeding, it starts with germplasm already in hand (the WSU females, the seven multi-race mildew lines), and every aim leads with a grower or brewer outcome.

**Water is the abiotic stress.** The posting's emphasis is abiotic stress; in Yakima that means water (2025: 40% junior supply; 2026: fourth drought year) and heat. CJ's frost work is escape by timing, so the deck carries the *method* (time series → heritable index → QTL) to water, not the stress. Gonzalez Tapia's lapse data supply the punchline: aroma moves, bitterness doesn't.

**Team, not rival.** Altendorf's group owns HopBox, DArTag, the 2026 GWAS and the second station; Gent owns races; Gonzalez Tapia owns water physiology. The vision names roles on the slide (`vision-fit`) and people aloud; `backup-partners` has everyone by name for "Who would you work with?" Aim 3 is "with Dr. Altendorf's group." `ch3-berryportraits` says "plug in" to HopBox.

**Phenomics is Objective 3 almost word for word** — but the hop twist matters: a nadir UAV image of a hedgerow sees only the top. `ch3-trellis` shows the geometry so the proposal (a cart down the alleys plus flights) reads as thought about their crop.

**Outreach gets its own slide** (the brief asks for it and the coffee deck didn't have one). Built on CJ's own Cranberry School decks (2024 meta-QTL with a gene-mapping primer; 2025 drone monitoring) and the April 2025 VacCAP deck, all in `~/Documents`. The hop half uses channels the industry already has: Hopsource, HRC grow-outs, the Hop Quality Group model, the Public Hop Breeding Advisory Committee.

**Honesty lines to volunteer.** Not a pathologist; not a stress physiologist; not the hop genomicist; not a brewer; no drought-proof hop on a date; no faster clone. Only disease trait: cranberry fruit rot, a fungal complex. Polyploid tools used on diploid data only.

## Verification pass, 6 Oct 2026

Fixed against primary sources (details in the prep doc §6): 2026 water (52% → 60%, fourth drought year; 40% is 2025); Apollo first author Kale, last author Braumann; Gonzalez Tapia 2025 lapse numbers; Nakawuka et al. 2017 authors and per-cultivar losses (the "2.4-fold" water-productivity figure replaced by the yield-loss range); Altendorf 2025 predictive-ability numbers; Clare 2026 GWAS numbers; NASS 2025; Mozny 2023.

## Source check, 7 Oct 2026

All cited sources were downloaded to `../../publications/` and every number was checked against the full text (report: `../../publications/_Source_Verification_2026-10-07.md`). Fixed: Apollo SV counts (`backup-hop-genome`), Comet journal (`backup-pm`, `references`), Hwang 2024 (`backup-pm` notes), "isohydric" wording (`vision-aim2`, `backup-water`), Teamaker DM claim (`ch2-metaqtl-concept` notes), rhAmpSeq deployment row (`backup-rhampseq-flexseq`). Backup: `_backup_2026-10-07_source-check/`. Everything else ✓ except CJ's unpublished UAV/LMI numbers.

## People update, 7 Oct 2026

The deck was first built from the collaborators list alone. The per-person files in `../../people/` and the panel named in the 7 Oct brief (2 ARS, 1 WSU, 4 industry) changed these slides; details in the prep doc §6b.

- **Slide bodies:** `vision-fit` (ARS Prosser imaging; WSU weeds and Extension; the commissions; Oregon and Idaho farms), `vision-adoption` (new "On farms" row), `outreach`, `vision-aim1` (grower trials in WA, OR, ID), `vision-aim2` (irrigation and campus imaging groups; "components, not one ratio", Feldman 2018), `vision-deliverables`, `acks`, `backup-how`, `backup-pm` (fewer sprays, less residue risk), `backup-title`, `prep-top`, `prep-dont-say`.
- **New slides:** `backup-partners` (everyone by name, five rows: ARS Prosser, ARS Corvallis, WSU, OSU, industry) and hidden `prep-panel` (one line per panelist).
- **Notes and scripts:** every slide above, plus `ch3-berryportraits` (Rippner on HopBox), `ch3-trellis` (Khot for the cart), `vision-why-now`, `questions`.
- **Design choice kept:** the timed slides name roles and institutions, not people; names are spoken and live on `backup-partners`. Timing unchanged (46 min).
- Previous versions: `_backup_2026-10-07/`.

## Verify before the room

- Panel (from the 7 Oct brief): Gonzalez Tapia, Feldman (ARS); Liu (WSU); Coleman, Stevens, Elliot, Adler (industry). ⚠ Who is remote, and whether the panel sits in the seminar.
- ⚠ Where Altendorf sits now (2026 BA roundup: Corvallis, overseeing both stations) and how this hire divides breeding with her.
- ⚠ "Late" vs "leaf" maturity index — the deck says *late*; check the manuscript.
- ⚠ Event names as you'd say them: "Wisconsin Cranberry School" 2024 and 2025; "VacCAP project meeting" 2025.
- ⚠ Whether GRYG is named for Ed Grygleski / Valley Corporation (acks slide) before saying so.
- ⚠ Shaun Clare's current employer; whether the Comet chr 6 interval lies inside the Brewer's Gold inversion; DArTag panel size; any published side-view or LiDAR hop phenotyping.

## Working with the notes (`tools/speaker_notes.py`)

The `Makefile` wraps every direction: `make` lists the targets; `make sync` pushes the prep doc (cues, minutes, scripts) into the deck and checks it; `make notes-to-prep` goes the other way. Each target's comment in the Makefile says which files it reads and which it overwrites.

```bash
python3 tools/speaker_notes.py list                                            # slides, minutes, note lengths, section end-times
python3 tools/speaker_notes.py extract -o Speaker_Notes.md                     # all notes → Markdown
python3 tools/speaker_notes.py update --from FSCRU_Seminar_Commute_Prep.md     # prep-doc bullets → deck notes
python3 tools/speaker_notes.py extract --into FSCRU_Seminar_Commute_Prep.md    # deck notes → prep-doc bullets (scripts untouched)
python3 tools/speaker_notes.py update --from X.md --apply-minutes              # also apply "· N min" from headings, then restamp
python3 tools/speaker_notes.py restamp                                         # after adding / moving / retiming slides
python3 tools/speaker_notes.py check                                           # HTML → Markdown → HTML round-trip test
python3 tools/speaker_notes.py scripts --from FSCRU_Seminar_Commute_Prep.md    # "> " spoken scripts → FULL SCRIPT box below the cues
python3 tools/speaker_notes.py scripts --remove                                # strip the script boxes again
```

The deck as delivered was produced with `scripts --remove` → `update --apply-minutes` → `scripts --from` → `restamp` → `prettify`; `check` reports 0 round-trip problems on 101 slides (79 with notes) after the 7 Oct people update. Every timed slide and every hop backup carries its spoken script from the prep doc.

## References cited in the deck

Slide ids in brackets are where each reference appears (slide text or notes). ✓ = checked against the source on 6 Oct 2026; ⚠ = verify before saying in the room.

### CJ's own work and cranberry sources

- Maule, A. F., et al. (2024). Of buds and bits: a meta-QTL study identifies stable QTL for berry quality and yield traits in cranberry mapping populations. *Frontiers in Plant Science* 15:1294570. https://doi.org/10.3389/fpls.2024.1294570 · code: https://github.com/bliptrip/CNJ0x-Trait-Mapping [ch2-*, map, scale, summary]
- Clare, S. J., …, Maule, A. F., Zalapa, J., …, Bassil, N. V. (2026). A high-recovery, high-density targeted genotyping platform for cranberry. *The Plant Genome* 19(1):e70153. https://doi.org/10.1002/tpg2.70153 [ch2-flexseq, map, scale, backup-rhampseq-flexseq]
- Maule et al. — Modeling spring greening patterns among cranberry genotypes via aerial imaging of leaf color. Under review, *Smart Agricultural Technology* [ch3-*, scale]
- Maule et al. — Mapping the genetic basis of temporal segregation of spring greening in cranberry. In preparation for *G3* [ch4-*]
- Maule, A. F. (2025). *Waders to Wings*. Ph.D. dissertation, UW–Madison [references]
- Albert, N. W., …, Maule, A., …, Espley, R. V. (2023). *Plant Physiology* 192(3):1696–1710. https://doi.org/10.1093/plphys/kiad250 [ch2-vaccap, map]
- Loarca, J., …, Maule, A. F., et al. (2024). BerryPortraits. *Plant Methods* 20:172. https://doi.org/10.1186/s13007-024-01285-1 [ch3-berryportraits, map]
- Workmaster & Palta (2006) *J. Am. Soc. Hortic. Sci.* 131:327 [ch3-biology] · Daverdin et al. (2017) *Mol. Breed.* 37:38 [references] · Zou et al. (2020) *Nat. Commun.* 11:413 [backup-rhampseq-flexseq]
- Outreach decks in `~/Documents`: `Presentations/Maule_2024_CranSchool.pptx`, `Maule_2025_Cranschool.pptx`, `Presentations/Maule_2025_04_VacCap.pptx` [outreach]

### Hop genomics and breeding

- ✓ Kale, S. M., …, Pitra, …, Matthews, …, Braumann, I. (2026). Extensive variation between chromosomes of North American and European hop. *Nature Communications*. https://www.nature.com/articles/s41467-026-72379-8 [why-hops, vision-aim3, backup-hop-genome, references]
- Padgitt-Cobb, L. K., …, Henning, J. A., Hendrix, D. A. (2023). An improved assembly of the 'Cascade' hop genome… *Horticulture Research* 10:uhac281. https://academic.oup.com/hr/article/10/2/uhac281/6957044 [vision-aim3, backup-hop-genome]
- ✓ Clare, S. J., Schmuker, P., & Altendorf, K. R. (2026). Association mapping for hop cone chemistry and morphology identifies natural beneficial allele stacks. *The Plant Genome* 19:e70238. https://www.ars.usda.gov/research/publications/publication/?seqNo115=429180 [vision-aim3, ch2-takeaways]
- Clare, S. J., et al. (2024). A diagnostic marker to identify male and female hop plants. *G3* [cycle, vision-aim1, backup-dioecy]
- ✓ Altendorf, K., Heineck, G., & Tawril, A. (2025). Predictive ability of hop grown in single hills on plot environments. *Crop Science* 65:e70024. https://www.ars.usda.gov/research/publications/publication/?seqNo115=419394 [cycle, why-hops, vision-aim1]
- Altendorf, K. R., et al. (2023). HopBox. *Plant Phenome J.* [ch3-berryportraits notes] · Altendorf, K. R., et al. (2025). Seven hop genotypes with multi-race powdery mildew resistance. *J. Plant Regist.* https://www.ars.usda.gov/research/publications/publication/?seqNo115=411474 [vision-aim1, backup-pm]
- Henning, J. A., et al. (2017) *Euphytica* (Newport × 21110M) · Henning, J. A., et al. (2024) *Crop Sci.* 64:2823–2839 (Comet chr 6) · Henning et al. (2015) *Euphytica* 202:487–498 (Teamaker DM QTL) · Jakše et al. (2013) *TAG* (Verticillium LG03) [ch2-takeaways, ch2-metaqtl-concept notes, backup-cp-mapping, backup-pm]
- Gent, D. H., et al. (2017) *Plant Disease* 101:874 (Cascade partial resistance) · Wolfenbarger et al. (2016) *Plant Disease* 100:1212 (V6) · Hwang, J. Y., …, Gent, D. H. (2024) *Phytopathology* 114:2287 (cultivar susceptibility and fungicide use) [backup-pm]
- Zhang et al. (2017) *Plant Genome* (non-Mendelian inheritance) · Horáková et al. (2025) *New Phytologist* (centromeres) [backup-cp-mapping]
- ARS project 2072-21000-061-000D, Development of Superior Hops and Resilient Hop Production Systems: https://www.ars.usda.gov/research/project/?accnNo=445259&fy=2025 [vision-aim1, vision-aim2]

### Water, heat and the industry

- ✓ Gonzalez Tapia, F. (2025). Late-season irrigation lapses impact the physiology, yield, and metabolite production of Yakima Valley hops. *J. Am. Soc. Hortic. Sci.* 150(3):136. https://journals.ashs.org/view/journals/jashs/150/3/article-p136.xml [vision-why-now, vision-aim2, backup-water]
- ✓ Nakawuka, P., Peters, T. R., Kenny, S., & Walsh, D. (2017). Effect of deficit irrigation on … four cultivars of hops in the Yakima Valley. *Industrial Crops and Products* 98:82–92. https://www.usahops.org/img/blog_pdf/87.pdf [vision-aim2, backup-water]
- Feldman, M. J., Ellsworth, P. Z., Fahlgren, N., Gehan, M. A., Cousins, A. B., & Baxter, I. (2018). Components of water use efficiency have unique genetic signatures in the model C4 grass *Setaria*. *Plant Physiology* 178(2):699–715. https://doi.org/10.1104/pp.18.00146 [vision-aim2]
- Gloser, V., et al. (2024). High sensitivity of hop to limited soil water. *Irrigation Science*. https://link.springer.com/article/10.1007/s00271-024-00929-3 [vision-aim2, backup-water]
- ✓ Mozny, M., et al. (2023). Climate-induced decline in the quality and quantity of European hops. *Nature Communications*. https://www.nature.com/articles/s41467-023-41474-5 [vision-why-now]
- ✓ USDA NASS National Hop Report, Dec 2025, via Capital Press: https://capitalpress.com/2025/12/30/u-s-hops-production-acreage-continue-drop-in-2025-but-yield-price-and-value-improve/ [vision-why-now]
- ✓ U.S. Bureau of Reclamation, Yakima basin forecasts 2026: https://www.usbr.gov/newsroom/news-release/5348 (June, 52%) · https://www.usbr.gov/newsroom/news-release/5405 (September, 60%) · 2025 at 40%: https://capitalpress.com/2025/08/08/yakima-river-basin-water-rationing-stays-at-40-of-full-supply/ [vision-why-now]
- Thora release (Hop Quality Group / USDA-ARS, Oct 2025): https://www.usahops.org/img/blog_pdf/502.pdf [cycle]
- Hop Research Council, Public Hop Breeding Advisory Committee: https://www.hopresearchcouncil.org/page/Public-Hop-Breeding-Advisory-Committee [outreach, vision-adoption]
- Posting ARS-D26MWA-12958916-HCL and seminar brief: `../../documents/` [map, everywhere]

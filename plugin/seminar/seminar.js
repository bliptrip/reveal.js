/*!
 * seminar.js -- section grouping and pacing for the GGRU seminar deck.
 *
 * WebSlides had no speaker view, so the original deck carried presenter.js:
 * 60 KB implementing notes, a next-slide preview, a talk clock, per-slide and
 * per-section countdowns, an outline, and a slide grid.
 *
 * reveal.js ships most of that. Its built-in speaker view ('s') already gives
 * notes, the next-slide preview, a talk clock, per-slide budgets via
 * data-timing, and an ahead/behind pacing readout via totalTime. Its overview
 * ('o') replaces the slide grid, and #/slide-id links replace the outline.
 *
 * What reveal has no concept of is a *section*. This deck is built on them:
 * seven lettered blocks with minute budgets that sum to 45, and the whole
 * talk is rehearsed against those budgets. So that is what this plugin adds,
 * and nothing else:
 *
 *   1. A SECTION panel in the speaker view -- section name, position within
 *      the section, and a countdown of section time remaining, with the same
 *      green/amber/red behaviour presenter.js had.
 *   2. A heads-up when the next slide opens a new block, so a transition
 *      never arrives unannounced.
 *   3. revealTimings() -- where the time actually went, for rehearsal.
 *   4. revealOverflowingSlides() -- the successor to wsOverflowingSlides().
 *   5. 'h' to pin a section label on the audience screen (off by default).
 *
 * Section data comes from data-section / data-section-minutes /
 * data-section-index / data-section-count, stamped on every slide by
 * tools/ws2reveal.py from the original <ws-section> wrappers.
 */

window.RevealSeminar = function () {

  let deck;
  let speakerWindow = null;
  let speakerPanel = null;

  // ---- time accounting -------------------------------------------------
  // Charged per slide and summed per section, so bouncing back to re-explain
  // a slide bills its section correctly -- same rule presenter.js used.
  const spent = Object.create(null);     // slide id -> ms accumulated
  let currentKey = null;
  let lastStamp = null;
  let clockRunning = false;

  const slideKey = s => s.id || 'slide-' + deck.getSlides().indexOf(s);

  function charge() {
    if (currentKey !== null && lastStamp !== null && clockRunning) {
      spent[currentKey] = (spent[currentKey] || 0) + (Date.now() - lastStamp);
    }
    lastStamp = Date.now();
  }

  // ---- section model ---------------------------------------------------

  function sectionOf(slide) {
    if (!slide || !slide.dataset.section) return null;
    return {
      name:    slide.dataset.section,
      minutes: parseFloat(slide.dataset.sectionMinutes) || 0,
      index:   parseInt(slide.dataset.sectionIndex, 10) || 0,
      count:   parseInt(slide.dataset.sectionCount, 10) || 0
    };
  }

  function slidesInSection(name) {
    return deck.getSlides().filter(s => s.dataset.section === name);
  }

  function sectionSpentMs(name) {
    return slidesInSection(name)
      .reduce((total, s) => total + (spent[slideKey(s)] || 0), 0);
  }

  // ---- formatting ------------------------------------------------------

  function mmss(ms) {
    const over = ms < 0;
    let t = Math.round(Math.abs(ms) / 1000);
    const m = Math.floor(t / 60);
    const s = t % 60;
    return (over ? '\u2212' : '') + m + ':' + String(s).padStart(2, '0');
  }

  // Green, amber under 25% remaining, red once over -- presenter.js's scale.
  function pacingColour(remainingMs, budgetMs) {
    if (budgetMs <= 0) return '#8ea1b4';
    if (remainingMs < 0) return '#ff5e5e';
    if (remainingMs / budgetMs < 0.25) return '#ffc145';
    return '#7ed37e';
  }

  // ---- speaker-view panel ----------------------------------------------
  //
  // reveal's notes plugin keeps its window handle in module scope and does
  // not expose it, so we capture it at the moment it is opened. The speaker
  // view is same-origin, which means we can simply append to its DOM once it
  // has loaded. If reveal's internals ever change shape, every branch here
  // fails soft: the deck and the stock speaker view keep working, only the
  // section panel goes missing.

  function captureSpeakerWindow() {
    const nativeOpen = window.open;
    window.open = function (url, name, features) {
      const win = nativeOpen.apply(window, arguments);
      if (win && typeof name === 'string' && /notes/i.test(name)) {
        speakerWindow = win;
        speakerPanel = null;
        waitForSpeakerView(0);
      }
      return win;
    };
  }

  function waitForSpeakerView(attempt) {
    if (!speakerWindow || speakerWindow.closed) return;
    if (attempt > 100) return;                       // ~20 s, then give up
    let body = null;
    try {
      body = speakerWindow.document && speakerWindow.document.body;
    } catch (e) {
      return;                                        // cross-origin; bail out
    }
    if (body && speakerWindow.document.querySelector('.speaker-controls')) {
      injectSpeakerPanel();
      update();
    } else {
      setTimeout(() => waitForSpeakerView(attempt + 1), 200);
    }
  }

  function injectSpeakerPanel() {
    const doc = speakerWindow.document;
    if (doc.getElementById('seminar-section-panel')) {
      speakerPanel = doc.getElementById('seminar-section-panel');
      return;
    }

    const style = doc.createElement('style');
    style.textContent = `
      #seminar-section-panel {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        background: #1a1a1a;
        border-top: 1px solid #333;
        padding: 12px 16px 14px;
        color: #eee;
      }
      #seminar-section-panel .ss-label {
        font-size: 11px; letter-spacing: .12em; text-transform: uppercase;
        color: #888; margin-bottom: 6px;
      }
      #seminar-section-panel .ss-name {
        font-size: 19px; font-weight: 600; line-height: 1.25; margin-bottom: 8px;
      }
      #seminar-section-panel .ss-row {
        display: flex; align-items: baseline; gap: 18px; flex-wrap: wrap;
      }
      #seminar-section-panel .ss-time {
        font-size: 34px; font-weight: 600; font-variant-numeric: tabular-nums;
        line-height: 1;
      }
      #seminar-section-panel .ss-of { font-size: 14px; color: #888; }
      #seminar-section-panel .ss-pos { font-size: 14px; color: #bbb; }
      #seminar-section-panel .ss-next {
        margin-top: 10px; padding: 7px 10px; border-radius: 4px;
        background: rgba(255,193,69,.14); border: 1px solid rgba(255,193,69,.5);
        color: #ffc145; font-size: 13px; line-height: 1.35;
      }
      #seminar-section-panel .ss-bar {
        height: 4px; border-radius: 2px; background: #333;
        margin-top: 10px; overflow: hidden;
      }
      #seminar-section-panel .ss-bar > div { height: 100%; width: 0; }
      #seminar-section-panel.ss-empty { display: none; }
    `;
    doc.head.appendChild(style);

    const panel = doc.createElement('div');
    panel.id = 'seminar-section-panel';
    panel.innerHTML = `
      <div class="ss-label">Section</div>
      <div class="ss-name"></div>
      <div class="ss-row">
        <span class="ss-time"></span>
        <span class="ss-of"></span>
        <span class="ss-pos"></span>
      </div>
      <div class="ss-bar"><div></div></div>
      <div class="ss-next" hidden></div>
    `;

    // Sit directly under reveal's own timing block, above the notes pane.
    const controls = doc.querySelector('.speaker-controls');
    const notesPane = doc.querySelector('.speaker-controls-notes');
    if (notesPane && notesPane.parentNode) {
      notesPane.parentNode.insertBefore(panel, notesPane);
    } else if (controls) {
      controls.appendChild(panel);
    } else {
      doc.body.appendChild(panel);
    }
    speakerPanel = panel;
  }

  function update() {
    if (!speakerPanel || !speakerWindow || speakerWindow.closed) return;

    const slide = deck.getCurrentSlide();
    const sec = sectionOf(slide);

    if (!sec) {
      speakerPanel.classList.add('ss-empty');
      return;
    }
    speakerPanel.classList.remove('ss-empty');

    const budgetMs = sec.minutes * 60 * 1000;
    const usedMs = sectionSpentMs(sec.name);
    const leftMs = budgetMs - usedMs;

    speakerPanel.querySelector('.ss-name').textContent = sec.name;

    const timeEl = speakerPanel.querySelector('.ss-time');
    if (budgetMs > 0) {
      timeEl.textContent = mmss(leftMs);
      timeEl.style.color = pacingColour(leftMs, budgetMs);
      speakerPanel.querySelector('.ss-of').textContent =
        'left of ' + sec.minutes + ':00';
    } else {
      timeEl.textContent = mmss(usedMs);
      timeEl.style.color = '#8ea1b4';
      speakerPanel.querySelector('.ss-of').textContent = 'elapsed (no budget)';
    }

    speakerPanel.querySelector('.ss-pos').textContent =
      'slide ' + sec.index + ' of ' + sec.count + ' in this block';

    const bar = speakerPanel.querySelector('.ss-bar > div');
    const frac = budgetMs > 0 ? Math.min(usedMs / budgetMs, 1) : 0;
    bar.style.width = (frac * 100).toFixed(1) + '%';
    bar.style.background = pacingColour(leftMs, budgetMs);

    // Warn when the next slide crosses into a new block.
    const slides = deck.getSlides();
    const next = slides[slides.indexOf(slide) + 1];
    const nextSec = sectionOf(next);
    const warn = speakerPanel.querySelector('.ss-next');
    if (nextSec && nextSec.name !== sec.name) {
      warn.hidden = false;
      warn.textContent = 'Next slide opens: ' + nextSec.name +
        (nextSec.minutes ? '  (' + nextSec.minutes + ' min)' : '');
    } else {
      warn.hidden = true;
    }
  }

  // ---- optional on-screen section label ('h') ---------------------------

  function buildAudienceLabel() {
    const el = document.createElement('div');
    el.id = 'seminar-section-label';
    el.hidden = true;
    const css = document.createElement('style');
    css.textContent = `
      #seminar-section-label {
        position: fixed; top: 0; left: 0; right: 0; z-index: 40;
        padding: .8rem 2rem;
        font: 300 1.6rem/1.3 'Roboto', helvetica, arial, sans-serif;
        letter-spacing: .08em; text-transform: uppercase;
        color: rgba(255,255,255,.72);
        background: rgba(0,0,0,.42);
        pointer-events: none;
      }
    `;
    document.head.appendChild(css);
    document.body.appendChild(el);
    return el;
  }

  // ---- rehearsal helpers ------------------------------------------------

  function timings() {
    charge();
    return deck.getSlides().map((s, i) => {
      const budget = s.dataset.timing ? parseInt(s.dataset.timing, 10) : null;
      const used = (spent[slideKey(s)] || 0) / 1000;
      return {
        n: i + 1,
        id: s.id || '',
        section: s.dataset.section || '',
        title: (s.querySelector('h1, h2, h3') || {}).textContent
                 ? (s.querySelector('h1, h2, h3').textContent || '').trim().slice(0, 60)
                 : '',
        spent: Math.round(used) + 's',
        budget: budget !== null ? budget + 's' : '',
        over: budget !== null ? Math.round(used - budget) + 's' : ''
      };
    }).filter(r => r.spent !== '0s');
  }

  /*
   * The successor to wsOverflowingSlides().
   *
   * Under WebSlides this had to be re-run after every zoom change, because
   * the slide *was* the window. Under reveal the slide box is a fixed
   * 1920x1080 and the whole deck is scaled to fit, so overflow is now a
   * property of the deck rather than of the machine it is shown on: run this
   * once, fix what it lists, and it stays fixed on any projector.
   */
  function overflowing(tolerance) {
    tolerance = tolerance || 4;
    const cfg = deck.getConfig();
    const box = cfg.height;
    const out = [];
    deck.getSlides().forEach((s, i) => {
      const prevVisibility = s.style.visibility;
      const prevDisplay = s.style.display;
      s.style.visibility = 'hidden';
      s.style.display = 'block';
      const h = s.scrollHeight;
      s.style.visibility = prevVisibility;
      s.style.display = prevDisplay;
      if (h > box + tolerance) {
        out.push({
          n: i + 1,
          id: s.id || '',
          section: s.dataset.section || '',
          contentHeight: Math.round(h),
          slideHeight: box,
          overBy: Math.round(h - box) + 'px'
        });
      }
    });
    if (!out.length) console.log('No slides overflow the ' + box + 'px slide box.');
    return out;
  }

  // ---- plugin -----------------------------------------------------------

  return {
    id: 'seminar',

    init: function (reveal) {
      deck = reveal;

      captureSpeakerWindow();
      const label = buildAudienceLabel();

      // Start charging time the first time the speaker leaves slide 1,
      // matching presenter.js's behaviour.
      deck.on('slidechanged', () => {
        if (!clockRunning && !deck.isFirstSlide()) {
          clockRunning = true;
          lastStamp = Date.now();
        }
        charge();
        currentKey = slideKey(deck.getCurrentSlide());
        lastStamp = Date.now();

        const sec = sectionOf(deck.getCurrentSlide());
        label.textContent = sec ? sec.name : '';
        update();
      });

      deck.on('ready', () => {
        currentKey = slideKey(deck.getCurrentSlide());
        lastStamp = Date.now();
        const sec = sectionOf(deck.getCurrentSlide());
        label.textContent = sec ? sec.name : '';
      });

      // Keep the section countdown ticking while a slide is held.
      setInterval(update, 1000);

      deck.addKeyBinding(
        { keyCode: 72, key: 'H', description: 'Pin the section name on screen' },
        () => { label.hidden = !label.hidden; }
      );

      // Console helpers, on the deck window and mirrored where you actually
      // type during rehearsal -- the speaker window.
      window.revealTimings = timings;
      window.revealOverflowingSlides = overflowing;
      deck.on('slidechanged', () => {
        if (speakerWindow && !speakerWindow.closed) {
          try {
            speakerWindow.revealTimings = timings;
            speakerWindow.revealOverflowingSlides = overflowing;
          } catch (e) { /* window went away mid-talk; not worth reporting */ }
        }
      });
    },

    // exposed for testing and for anything else that wants the section model
    getSectionOf: () => sectionOf(deck.getCurrentSlide()),
    getTimings: () => timings()
  };
};

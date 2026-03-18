// root-builder.js — Interactive word builder for Tonesu CV primitive roots
// Three-panel UI: palette | chain builder | registry lookup

(function () {
  'use strict';

  // Only activate on the builder page
  var BUILDER_RE = /\/tonesu\/builder(\/|\.html)?$/;

  // Colour for each consonant family initial (16 consonants)
  var FAMILY_COLORS = {
    b: '#7bd88f', d: '#5ad4e6', f: '#fc618d', g: '#fd9353',
    h: '#e5c07b', k: '#c678dd', l: '#98c379', m: '#948ae3',
    n: '#61afef', p: '#d19a66', r: '#e06c75', s: '#56d0d0',
    t: '#fce566', v: '#b5cea8', w: '#e0a87e', z: '#88c0d0',
  };

  var SCOPE_MODS = [
    { prefix: 'a-', gloss: 'abstract / universal' },
    { prefix: 'i-', gloss: 'precise / particular' },
    { prefix: 'u-', gloss: 'interior / foundational' },
    { prefix: 'o-', gloss: 'collective' },
    { prefix: 'e-', gloss: 'emergent' },
  ];

  var SUFFIXES = [
    { sfx: '-li', gloss: 'person / agent' },
    { sfx: '-mu', gloss: 'tool / object' },
    { sfx: '-pa', gloss: 'place / domain' },
    { sfx: '-ge', gloss: 'event / moment' },
    { sfx: '-ki', gloss: 'transform / change' },
  ];

  var chain      = [];
  var prefixMod  = '';
  var suffixMod  = '';
  var allData    = null;
  var activeFamily = '';

  // ── Bootstrap ─────────────────────────────────────────────────────────────
  function init() {
    if (!BUILDER_RE.test(window.location.pathname)) return;

    var container = document.getElementById('root-builder');
    if (!container) return;

    // Reset state on each page visit (SPA navigation)
    chain = []; prefixMod = ''; suffixMod = ''; activeFamily = '';

    if (allData) {
      render(container);
      return;
    }

    container.innerHTML = '<p class="rb-loading">Loading root data\u2026</p>';

    var base = (typeof __md_get === 'function' && window.__md_config)
      ? window.__md_config.base : '';

    fetch(base + '/js/tonesu-data.json')
      .then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.json();
      })
      .then(function (data) {
        allData = data;
        container.innerHTML = '';
        render(container);
      })
      .catch(function (e) {
        container.innerHTML =
          '<p class="rb-error">Could not load root data (' + e.message + '). '
          + 'Try refreshing the page.</p>';
      });
  }

  // ── Top-level render ───────────────────────────────────────────────────────
  function render(container) {
    container.className = 'rb-container';

    var headerEl  = mk('div', 'rb-header');
    var mainEl    = mk('div', 'rb-main');
    var paletteEl = mk('div', 'rb-panel rb-panel--palette');
    var builderEl = mk('div', 'rb-panel rb-panel--builder');
    var lookupEl  = mk('div', 'rb-panel rb-panel--lookup');

    buildHeader(headerEl);
    buildPalette(paletteEl);
    buildChain(builderEl);
    buildLookup(lookupEl);

    mainEl.appendChild(paletteEl);
    mainEl.appendChild(builderEl);
    mainEl.appendChild(lookupEl);

    container.appendChild(headerEl);
    container.appendChild(mainEl);
  }

  // ── Header: scope/suffix controls + compound display ───────────────────────
  function buildHeader(node) {
    // Controls row
    var controls = mk('div', 'rb-controls');

    // Scope prefix buttons
    var scopeGrp = mk('div', 'rb-btn-group');
    var scopeLbl = mk('span', 'rb-group-label');
    scopeLbl.textContent = 'Prefix';
    scopeGrp.appendChild(scopeLbl);
    SCOPE_MODS.forEach(function (m) {
      var btn = mk('button', 'rb-ctrl-btn' + (prefixMod === m.prefix ? ' is-active' : ''));
      btn.textContent = m.prefix;
      btn.title = m.prefix + ' \u2014 ' + m.gloss;
      btn.addEventListener('click', function () {
        prefixMod = (prefixMod === m.prefix) ? '' : m.prefix;
        refresh();
      });
      scopeGrp.appendChild(btn);
    });

    // Suffix buttons
    var sfxGrp = mk('div', 'rb-btn-group');
    var sfxLbl = mk('span', 'rb-group-label');
    sfxLbl.textContent = 'Suffix';
    sfxGrp.appendChild(sfxLbl);
    SUFFIXES.forEach(function (s) {
      var btn = mk('button', 'rb-ctrl-btn' + (suffixMod === s.sfx ? ' is-active' : ''));
      btn.textContent = s.sfx;
      btn.title = s.sfx + ' \u2014 ' + s.gloss;
      btn.addEventListener('click', function () {
        suffixMod = (suffixMod === s.sfx) ? '' : s.sfx;
        refresh();
      });
      sfxGrp.appendChild(btn);
    });

    controls.appendChild(scopeGrp);
    controls.appendChild(sfxGrp);
    node.appendChild(controls);

    // Compound display row
    var display = mk('div', 'rb-display');
    var compound = buildCompound();

    if (compound) {
      var wordEl = mk('span', 'rb-word');
      wordEl.textContent = compound.written;

      var parseEl = mk('span', 'rb-parse');
      parseEl.textContent = '\u2009(' + compound.parse + ')';

      var copyBtn = mk('button', 'rb-icon-btn');
      copyBtn.innerHTML = '&#x29C9;';
      copyBtn.title = 'Copy written form';
      copyBtn.addEventListener('click', function () {
        if (navigator.clipboard) navigator.clipboard.writeText(compound.written);
      });

      display.appendChild(wordEl);
      display.appendChild(parseEl);
      display.appendChild(copyBtn);
    } else {
      var ph = mk('span', 'rb-placeholder');
      ph.textContent = 'Click roots below to start building \u2014\u2009';
      display.appendChild(ph);
    }

    var clearBtn = mk('button', 'rb-clear-btn');
    clearBtn.textContent = 'Clear';
    clearBtn.addEventListener('click', function () {
      chain = []; prefixMod = ''; suffixMod = '';
      refresh();
    });
    display.appendChild(clearBtn);
    node.appendChild(display);
  }

  // ── Palette panel: family filter + CV button grid ──────────────────────────
  function buildPalette(node) {
    var title = mk('div', 'rb-panel-title');
    title.textContent = 'Primitive roots';
    node.appendChild(title);

    // Family filter strip
    var families = [];
    allData.primitives.forEach(function (r) {
      if (r.status === 'active' && families.indexOf(r.family) === -1)
        families.push(r.family);
    });
    families.sort();

    var strip = mk('div', 'rb-family-strip');

    var allBtn = mk('button', 'rb-fam-btn' + (activeFamily === '' ? ' is-active' : ''));
    allBtn.textContent = 'all';
    allBtn.addEventListener('click', function () { setFamily('', strip); });
    strip.appendChild(allBtn);

    families.forEach(function (f) {
      var btn = mk('button', 'rb-fam-btn' + (activeFamily === f ? ' is-active' : ''));
      btn.textContent = f + '\u2013';
      btn.title = familyName(f);
      btn.style.setProperty('--fam-color', FAMILY_COLORS[f] || '#888');
      btn.addEventListener('click', function () { setFamily(f, strip); });
      strip.appendChild(btn);
    });
    node.appendChild(strip);

    // Root grid
    var grid = mk('div', 'rb-grid');
    node.appendChild(grid);
    fillGrid(grid);
  }

  function setFamily(fam, strip) {
    activeFamily = fam;
    strip.querySelectorAll('.rb-fam-btn').forEach(function (b) {
      b.classList.toggle('is-active',
        (fam === '' && b.textContent === 'all') ||
        b.textContent === fam + '\u2013');
    });
    var grid = strip.parentElement.querySelector('.rb-grid');
    if (grid) fillGrid(grid);
  }

  function fillGrid(grid) {
    grid.innerHTML = '';
    var roots = allData.primitives.filter(function (r) {
      return r.status === 'active' &&
             (activeFamily === '' || r.family === activeFamily);
    });
    roots.forEach(function (root) {
      var col = FAMILY_COLORS[root.family] || '#888';
      var btn = mk('button', 'rb-root-btn');
      btn.textContent = root.cv;
      btn.title = root.gloss + '\n' + familyName(root.family);
      btn.style.setProperty('--root-color', col);
      btn.addEventListener('click', function () {
        chain.push(root.cv);
        refresh();
      });

      var gloss = mk('span', 'rb-root-gloss');
      gloss.textContent = root.gloss;
      btn.appendChild(gloss);
      grid.appendChild(btn);
    });
  }

  // ── Chain builder panel ────────────────────────────────────────────────────
  function buildChain(node) {
    var title = mk('div', 'rb-panel-title');
    title.textContent = 'Chain';
    node.appendChild(title);

    if (chain.length === 0 && !prefixMod && !suffixMod) {
      var empty = mk('p', 'rb-empty');
      empty.textContent = 'No roots selected yet.';
      node.appendChild(empty);
      return;
    }

    var chipRow = mk('div', 'rb-chip-row');

    // Prefix chip
    if (prefixMod) {
      var pChip = mk('div', 'rb-chip rb-chip--modifier');
      var pLabel = mk('span', 'rb-chip-cv');
      pLabel.textContent = prefixMod;
      pChip.appendChild(pLabel);
      var pGloss = mk('span', 'rb-chip-gloss');
      var pMeta = SCOPE_MODS.find(function (m) { return m.prefix === prefixMod; });
      pGloss.textContent = pMeta ? pMeta.gloss : 'prefix';
      pChip.appendChild(pGloss);
      var pRm = mk('button', 'rb-chip-rm');
      pRm.textContent = '\xd7';
      pRm.title = 'Remove prefix';
      pRm.addEventListener('click', function () { prefixMod = ''; refresh(); });
      pChip.appendChild(pRm);
      chipRow.appendChild(pChip);
    }

    // Root chips
    chain.forEach(function (cv, i) {
      var col  = FAMILY_COLORS[cv[0]] || '#888';
      var root = allData.primitives.find(function (r) { return r.cv === cv; });

      var chip = mk('div', 'rb-chip');
      chip.style.setProperty('--chip-color', col);

      var cvEl = mk('span', 'rb-chip-cv');
      cvEl.textContent = cv;
      chip.appendChild(cvEl);

      if (root) {
        var glossEl = mk('span', 'rb-chip-gloss');
        glossEl.textContent = root.gloss;
        chip.appendChild(glossEl);
      }

      var rmBtn = mk('button', 'rb-chip-rm');
      rmBtn.textContent = '\xd7';
      rmBtn.title = 'Remove ' + cv;
      rmBtn.addEventListener('click', (function (idx) {
        return function () { chain.splice(idx, 1); refresh(); };
      })(i));
      chip.appendChild(rmBtn);

      chipRow.appendChild(chip);
    });

    // Suffix chip
    if (suffixMod) {
      var sChip = mk('div', 'rb-chip rb-chip--modifier');
      var sLabel = mk('span', 'rb-chip-cv');
      sLabel.textContent = suffixMod;
      sChip.appendChild(sLabel);
      var sGloss = mk('span', 'rb-chip-gloss');
      var sMeta = SUFFIXES.find(function (s) { return s.sfx === suffixMod; });
      sGloss.textContent = sMeta ? sMeta.gloss : 'suffix';
      sChip.appendChild(sGloss);
      var sRm = mk('button', 'rb-chip-rm');
      sRm.textContent = '\xd7';
      sRm.title = 'Remove suffix';
      sRm.addEventListener('click', function () { suffixMod = ''; refresh(); });
      sChip.appendChild(sRm);
      chipRow.appendChild(sChip);
    }

    node.appendChild(chipRow);

    // Gloss summary (roots only)
    if (chain.length > 0) {
      var glossLine = mk('p', 'rb-gloss-line');
      glossLine.textContent = chain.map(function (cv) {
        var r = allData.primitives.find(function (p) { return p.cv === cv; });
        return r ? r.gloss : cv;
      }).join(' + ');
      node.appendChild(glossLine);
    }
  }

  // ── Registry lookup panel ─────────────────────────────────────────────────
  function buildLookup(node) {
    var title = mk('div', 'rb-panel-title');
    title.textContent = 'Registry lookup';
    node.appendChild(title);

    if (chain.length === 0) {
      var empty = mk('p', 'rb-empty');
      empty.textContent = 'Build a word to search.';
      node.appendChild(empty);
      return;
    }

    var exact  = allData.entries.filter(function (e) { return arrEq(e.roots, chain); });
    var prefix = allData.entries.filter(function (e) {
      return !arrEq(e.roots, chain) && arrContains(e.roots, chain);
    });

    if (exact.length === 0 && prefix.length === 0) {
      var free = mk('div', 'rb-free');
      free.innerHTML = '\u2713 No existing entry \u2014 this combination is <strong>free&nbsp;to&nbsp;use</strong>.';
      node.appendChild(free);
      return;
    }

    if (exact.length > 0) {
      var h1 = mk('p', 'rb-subhead');
      h1.textContent = 'Exact match';
      node.appendChild(h1);
      exact.forEach(function (e) { node.appendChild(entryCard(e)); });
    }

    if (prefix.length > 0) {
      var h2 = mk('p', 'rb-subhead');
      h2.textContent = 'Contains this chain';
      node.appendChild(h2);
      prefix.slice(0, 12).forEach(function (e) { node.appendChild(entryCard(e)); });
    }
  }

  function entryCard(e) {
    var card = mk('div', 'rb-entry-card');

    var link = mk('a', 'rb-entry-word');
    link.href = '/tonesu/registry/words/' + e.wnum.toLowerCase() + '/';
    link.textContent = e.written || e.form;
    card.appendChild(link);

    var sep = mk('span', 'rb-entry-sep');
    sep.textContent = ' \u2014 ';
    card.appendChild(sep);

    var glossEl = mk('span', 'rb-entry-gloss');
    glossEl.textContent = e.gloss;
    card.appendChild(glossEl);

    var wnumEl = mk('span', 'rb-entry-wnum');
    wnumEl.textContent = e.wnum;
    card.appendChild(wnumEl);

    return card;
  }

  // ── Helpers ────────────────────────────────────────────────────────────────
  function buildCompound() {
    if (chain.length === 0 && !prefixMod && !suffixMod) return null;
    var base    = chain.join('-');
    var sfxCore = suffixMod ? suffixMod.slice(1) : '';   // strip leading '-'
    var parts   = [base, sfxCore].filter(Boolean);
    var full    = (prefixMod ? prefixMod : '') + parts.join('-');
    var written = full.replace(/-/g, '');
    return { parse: full, written: written };
  }

  function arrEq(a, b) {
    if (!Array.isArray(a) || a.length !== b.length) return false;
    for (var i = 0; i < b.length; i++) if (a[i] !== b[i]) return false;
    return true;
  }

  function arrContains(hay, needle) {
    if (!Array.isArray(hay) || hay.length < needle.length) return false;
    for (var i = 0; i <= hay.length - needle.length; i++) {
      var ok = true;
      for (var j = 0; j < needle.length; j++) {
        if (hay[i + j] !== needle[j]) { ok = false; break; }
      }
      if (ok) return true;
    }
    return false;
  }

  function mk(tag, cls) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    return e;
  }

  function familyName(f) {
    if (!allData || !allData.families) return f;
    // allData.families is an array from primitives.yaml
    var fam = allData.families.find
      ? allData.families.find(function (x) { return x.consonant === f; })
      : null;
    return fam ? fam.name : f;
  }

  function refresh() {
    var container = document.getElementById('root-builder');
    if (!container || !allData) return;
    container.innerHTML = '';
    render(container);
  }

  // ── Hook into Material SPA navigation ─────────────────────────────────────
  if (typeof document$ !== 'undefined') {
    document$.subscribe(init);
  } else {
    document.addEventListener('DOMContentLoaded', init);
  }
})();

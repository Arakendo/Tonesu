// learn-picker.js — Fill-in-the-blank chip selector for Tonesu learn pages
//
// ── Single-blank mode ────────────────────────────────────────────────────
//   data-answer   — form value of the correct chip (string)
//   data-items    — JSON array of {form, gloss}
//   data-template — text with one "___" blank: "la-___  ki  pa-li-pu"
//
// ── Multi-blank mode ─────────────────────────────────────────────────────
//   data-answers  — JSON array of correct forms in slot order: '["to","ki","mu"]'
//   data-items    — shared chip pool (JSON array of {form, gloss})
//   data-items-N  — (optional) per-slot override pool for slot N
//   data-template — text with N "___" blanks (for N answers): "___-___-___"
//                   The "'" juncture character is literal text between blanks,
//                   e.g. "___'___-su" → slot0 juncture slot1 -su
//
// ── Shared attributes ────────────────────────────────────────────────────
//   data-mode     — "form" | "gloss" | "both"
//   data-ok       — custom message when all slots are correct
//   data-nok      — custom wrong-attempt message

(function () {
  'use strict';

  // ── Helpers ──────────────────────────────────────────────────────────────

  function esc(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function chipHTML(item, mode) {
    var formPart  = '<code class="lp-chip-form">' + esc(item.form) + '</code>';
    var glossPart = '<span class="lp-chip-gloss">' + esc(item.gloss || '') + '</span>';
    var sep       = '<span class="lp-chip-sep" aria-hidden="true">·</span>';
    if (mode === 'form')  return formPart;
    if (mode === 'gloss') return glossPart;
    return formPart + sep + glossPart;
  }

  function makeUID() {
    return 'lp-' + Math.random().toString(36).slice(2, 8);
  }

  function shuffle(arr) {
    return arr.slice().sort(function () { return Math.random() - 0.5; });
  }

  // ── Single-blank picker ───────────────────────────────────────────────────

  function renderSinglePicker(el, uid) {
    var items    = JSON.parse(el.getAttribute('data-items')  || '[]');
    var answer   = (el.getAttribute('data-answer') || '').trim();
    var mode     = el.getAttribute('data-mode')    || 'both';
    var template = el.getAttribute('data-template') || '___';
    var okMsg    = el.getAttribute('data-ok')  || 'Correct \u2713';
    var nokMsg   = el.getAttribute('data-nok') || 'Not quite \u2014 try again.';

    var parts  = template.split('___');
    var before = parts[0] || '';
    var after  = parts[1] || '';
    var slotId = uid + '-slot';
    var fbId   = uid + '-fb';

    var chipsHTML = shuffle(items).map(function (item) {
      return '<button class="lp-chip" type="button"'
        + ' data-form="' + esc(item.form) + '"'
        + ' aria-label="' + esc(item.form) + (item.gloss ? ': ' + esc(item.gloss) : '') + '">'
        + chipHTML(item, mode) + '</button>';
    }).join('');

    el.innerHTML =
      '<div class="lp-template-line" aria-live="polite">'
      + '<span class="lp-tpl-seg">' + esc(before) + '</span>'
      + '<span class="lp-slot lp-slot--empty" id="' + slotId + '">___</span>'
      + '<span class="lp-tpl-seg">' + esc(after) + '</span>'
      + '</div>'
      + '<div class="lp-chips" role="group" aria-label="Choose a root">'
      + chipsHTML
      + '</div>'
      + '<div class="lp-feedback" id="' + fbId + '" role="status" hidden></div>';

    var slot   = document.getElementById(slotId);
    var fb     = document.getElementById(fbId);
    var chips  = el.querySelectorAll('.lp-chip');
    var locked = false;

    chips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        if (locked) return;
        var form = chip.dataset.form;
        chips.forEach(function (c) {
          c.classList.remove('lp-chip--selected', 'lp-chip--wrong', 'lp-chip--correct');
        });
        fb.hidden = true;
        fb.className = 'lp-feedback';
        slot.className = 'lp-slot lp-slot--filled';
        slot.textContent = form;
        chip.classList.add('lp-chip--selected');

        if (form === answer) {
          chip.classList.add('lp-chip--correct');
          slot.classList.add('lp-slot--correct');
          fb.textContent = okMsg;
          fb.classList.add('lp-feedback--correct');
          fb.hidden = false;
          locked = true;
          chips.forEach(function (c) { c.disabled = true; });
        } else {
          chip.classList.add('lp-chip--wrong');
          slot.classList.add('lp-slot--wrong');
          fb.textContent = nokMsg;
          fb.classList.add('lp-feedback--wrong');
          fb.hidden = false;
          setTimeout(function () {
            chip.classList.remove('lp-chip--selected', 'lp-chip--wrong');
            slot.className = 'lp-slot lp-slot--empty';
            slot.textContent = '___';
            fb.hidden = true;
            fb.className = 'lp-feedback';
          }, 5000);
        }
      });
    });
  }

  // ── Multi-blank picker ────────────────────────────────────────────────────
  //
  // Slots are filled sequentially: slot N only becomes active once slot N-1
  // has been correctly filled. A correctly used chip is disabled (greyed out)
  // so the learner cannot accidentally re-use it. Wrong guesses reset the slot
  // after 1.4 s without consuming the chip.
  //
  // If all slots share the same data-items pool, one chip row is rendered.
  // For per-slot overrides (data-items-0, data-items-1 …), each slot gets its
  // own chip row; only the active slot's row is visible at any time.

  function renderMultiPicker(el, uid) {
    var answers  = JSON.parse(el.getAttribute('data-answers'));
    var baseItems = JSON.parse(el.getAttribute('data-items') || '[]');
    var mode     = el.getAttribute('data-mode')     || 'both';
    var template = el.getAttribute('data-template') ||
                   answers.map(function () { return '___'; }).join('-');
    var okMsg    = el.getAttribute('data-ok')  || 'Correct \u2713';
    var nokMsg   = el.getAttribute('data-nok') || 'Try again.';

    var n        = answers.length;
    var segments = template.split('___');   // n+1 text segments

    // Resolve per-slot item pools
    var slotPools = answers.map(function (_, i) {
      var override = el.getAttribute('data-items-' + i);
      return override ? JSON.parse(override) : baseItems;
    });
    var perSlot = slotPools.some(function (pool, i) {
      return JSON.stringify(pool) !== JSON.stringify(slotPools[0]);
    });
    var shuffledPools = slotPools.map(shuffle);

    // ── Build template line ───────────────────────────────────────────────
    var tplHTML = '<div class="lp-template-line">';
    for (var i = 0; i < n; i++) {
      tplHTML += '<span class="lp-tpl-seg">' + esc(segments[i]) + '</span>';
      var cls = 'lp-slot ' + (i === 0 ? 'lp-slot--active' : 'lp-slot--inactive');
      tplHTML += '<span class="' + cls + '" id="' + uid + '-s' + i + '">___</span>';
    }
    tplHTML += '<span class="lp-tpl-seg">' + esc(segments[n] || '') + '</span>';
    tplHTML += '</div>';

    // ── Build chip row(s) ─────────────────────────────────────────────────
    var chipsHTML;
    if (!perSlot) {
      // Single shared chip row
      chipsHTML = '<div class="lp-chips" id="' + uid + '-chips" role="group" '
                + 'aria-label="Choose a root">'
                + shuffledPools[0].map(function (item) {
                    return '<button class="lp-chip" type="button"'
                      + ' data-form="' + esc(item.form) + '">'
                      + chipHTML(item, mode) + '</button>';
                  }).join('')
                + '</div>';
    } else {
      // Per-slot chip rows; only slot-0 visible initially
      chipsHTML = answers.map(function (_, i) {
        var vis = i === 0 ? '' : ' style="display:none"';
        return '<div class="lp-chips lp-chips-slot" id="' + uid + '-chips-' + i + '"'
               + vis + ' role="group" aria-label="Choose a root">'
               + shuffledPools[i].map(function (item) {
                   return '<button class="lp-chip" type="button"'
                     + ' data-form="' + esc(item.form) + '">'
                     + chipHTML(item, mode) + '</button>';
                 }).join('')
               + '</div>';
      }).join('');
    }

    el.innerHTML = tplHTML + chipsHTML
      + '<div class="lp-feedback" id="' + uid + '-fb" role="status" hidden></div>';

    // ── State ─────────────────────────────────────────────────────────────
    var current = 0;
    var placed  = new Array(n).fill(null);
    var done    = false;

    var slots = answers.map(function (_, i) {
      return document.getElementById(uid + '-s' + i);
    });
    var fb = document.getElementById(uid + '-fb');

    function getActiveChips() {
      if (!perSlot) {
        return Array.prototype.slice.call(
          document.getElementById(uid + '-chips').querySelectorAll('.lp-chip'));
      }
      var row = document.getElementById(uid + '-chips-' + current);
      return row ? Array.prototype.slice.call(row.querySelectorAll('.lp-chip')) : [];
    }

    function activateSlot(idx) {
      slots.forEach(function (s, i) {
        s.classList.remove('lp-slot--active', 'lp-slot--inactive',
                           'lp-slot--filled', 'lp-slot--wrong');
        if (placed[i] === answers[i]) {
          s.classList.add('lp-slot--correct');
        } else if (i === idx) {
          s.classList.add('lp-slot--active');
        } else {
          s.classList.add('lp-slot--inactive');
        }
      });
      if (perSlot) {
        for (var i = 0; i < n; i++) {
          var row = document.getElementById(uid + '-chips-' + i);
          if (row) row.style.display = (i === idx) ? '' : 'none';
        }
      }
    }

    function attachListeners(chips) {
      chips.forEach(function (chip) {
        chip.addEventListener('click', function () {
          if (done || chip.disabled) return;

          var form = chip.dataset.form;
          var expected = answers[current];
          var slot = slots[current];

          // Clear previous wrong state on this slot's chips
          getActiveChips().forEach(function (c) {
            c.classList.remove('lp-chip--selected', 'lp-chip--wrong');
          });
          fb.hidden = true;
          fb.className = 'lp-feedback';

          // Fill slot
          slot.classList.remove('lp-slot--active', 'lp-slot--wrong', 'lp-slot--inactive');
          slot.classList.add('lp-slot--filled');
          slot.textContent = form;
          placed[current] = form;
          chip.classList.add('lp-chip--selected');

          if (form === expected) {
            // ── Correct slot ─────────────────────────────────────────────
            slot.classList.remove('lp-slot--filled');
            slot.classList.add('lp-slot--correct');
            chip.classList.remove('lp-chip--selected');
            chip.classList.add('lp-chip--correct');
            chip.disabled = true;

            current++;
            if (current >= n) {
              done = true;
              fb.textContent = okMsg;
              fb.classList.add('lp-feedback--correct');
              fb.hidden = false;
              // Disable all chips
              Array.prototype.slice.call(
                el.querySelectorAll('.lp-chip')).forEach(function (c) { c.disabled = true; });
            } else {
              activateSlot(current);
            }
          } else {
            // ── Wrong guess ───────────────────────────────────────────────
            slot.classList.remove('lp-slot--filled');
            slot.classList.add('lp-slot--wrong');
            chip.classList.remove('lp-chip--selected');
            chip.classList.add('lp-chip--wrong');
            fb.textContent = nokMsg;
            fb.classList.add('lp-feedback--wrong');
            fb.hidden = false;
            setTimeout(function () {
              placed[current] = null;
              slot.className = 'lp-slot lp-slot--active';
              slot.textContent = '___';
              chip.classList.remove('lp-chip--wrong');
              fb.hidden = true;
              fb.className = 'lp-feedback';
            }, 5000);
          }
        });
      });
    }

    // Attach listeners to all chip rows upfront
    if (!perSlot) {
      attachListeners(getActiveChips());
    } else {
      for (var j = 0; j < n; j++) {
        var row = document.getElementById(uid + '-chips-' + j);
        if (row) {
          attachListeners(
            Array.prototype.slice.call(row.querySelectorAll('.lp-chip')));
        }
      }
    }

    activateSlot(0);
  }

  // ── Multiple-choice question widget ──────────────────────────────────────
  //
  //   data-options  — JSON array of {id, text}; `backtick` in text → <code>
  //   data-answer   — id of the correct option
  //   data-ok       — correct-answer feedback (plain text)
  //   data-nok      — wrong-answer feedback (plain text, optional)

  function mdInline(str) {
    return String(str).replace(/`([^`]+)`/g, '<code>$1</code>');
  }

  function renderMCQ(el) {
    var options = JSON.parse(el.getAttribute('data-options') || '[]');
    var answer  = (el.getAttribute('data-answer') || '').trim();
    var okMsg   = el.getAttribute('data-ok')  || 'Correct \u2713';
    var nokMsg  = el.getAttribute('data-nok') || 'Not quite \u2014 try again.';
    var uid     = makeUID();
    var fbId    = uid + '-fb';
    var labels  = ['A', 'B', 'C', 'D', 'E', 'F'];

    var optHTML = options.map(function (opt, i) {
      return '<button class="lp-mcq-option" type="button" data-id="' + esc(opt.id) + '">'
        + '<span class="lp-mcq-label">' + (labels[i] || String(i + 1)) + '</span>'
        + '<span class="lp-mcq-text">' + mdInline(opt.text) + '</span>'
        + '</button>';
    }).join('');

    el.innerHTML =
      '<div class="lp-mcq-options" role="group" aria-label="Choose an answer">'
      + optHTML + '</div>'
      + '<div class="lp-feedback" id="' + fbId + '" role="status" hidden></div>';

    var fb      = document.getElementById(fbId);
    var buttons = Array.prototype.slice.call(el.querySelectorAll('.lp-mcq-option'));
    var locked  = false;

    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        if (locked) return;
        var id = btn.getAttribute('data-id');
        buttons.forEach(function (b) {
          b.classList.remove('lp-mcq-option--selected',
                             'lp-mcq-option--wrong',
                             'lp-mcq-option--correct');
        });
        fb.hidden = true;
        fb.className = 'lp-feedback';
        btn.classList.add('lp-mcq-option--selected');

        if (id === answer) {
          btn.classList.add('lp-mcq-option--correct');
          fb.textContent = okMsg;
          fb.classList.add('lp-feedback--correct');
          fb.hidden = false;
          locked = true;
          buttons.forEach(function (b) { b.disabled = true; });
        } else {
          btn.classList.add('lp-mcq-option--wrong');
          fb.textContent = nokMsg;
          fb.classList.add('lp-feedback--wrong');
          fb.hidden = false;
          setTimeout(function () {
            btn.classList.remove('lp-mcq-option--selected', 'lp-mcq-option--wrong');
            fb.hidden = true;
            fb.className = 'lp-feedback';
          }, 5000);
        }
      });
    });
  }

  // ── Dispatcher ────────────────────────────────────────────────────────────

  function renderPicker(el) {
    if (el.dataset.lpInit) return;
    el.dataset.lpInit = '1';
    el.classList.add('lp-wrap');

    var uid = makeUID();
    if (el.getAttribute('data-answers')) {
      renderMultiPicker(el, uid);
    } else {
      renderSinglePicker(el, uid);
    }
  }

  // ── Page-level init ───────────────────────────────────────────────────────

  function init() {
    document.querySelectorAll('.tn-learn-picker').forEach(renderPicker);
    document.querySelectorAll('.tn-learn-mcq').forEach(function (el) {
      if (el.dataset.lpInit) return;
      el.dataset.lpInit = '1';
      renderMCQ(el);
    });
  }

  // MkDocs Material uses an RxJS document$ observable for SPA navigation.
  // Fall back to DOMContentLoaded in plain environments.
  if (typeof document$ !== 'undefined') {
    document$.subscribe(init);
  } else {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', init);
    } else {
      init();
    }
  }

}());

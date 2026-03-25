// learn-picker.js — Fill-in-the-blank chip selector for Tonesu learn pages
//
// Usage: place a div with class "tn-learn-picker" and data attributes:
//
//   data-items   — JSON array of {form, gloss} objects (the chips)
//   data-answer  — the `form` value of the correct chip
//   data-mode    — "form" | "gloss" | "both"  (what each chip displays)
//   data-template — sentence fragment with "___" marking the blank
//                   e.g.  "la-___  ki  pa-li-pu  ta-ti-be"
//   data-ok      — (optional) custom correct-answer message
//   data-nok     — (optional) custom wrong-answer message
//
// Example:
//   <div class="tn-learn-picker"
//        data-template="___-si"
//        data-answer="to"
//        data-mode="both"
//        data-items='[{"form":"to","gloss":"knowledge"},{"form":"ki","gloss":"motion"},{"form":"mu","gloss":"artifact"},{"form":"de","gloss":"decay"}]'>
//   </div>

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
    var glossPart = '<span class="lp-chip-gloss">' + esc(item.gloss) + '</span>';
    var sep       = '<span class="lp-chip-sep" aria-hidden="true">·</span>';
    if (mode === 'form')  return formPart;
    if (mode === 'gloss') return glossPart;
    return formPart + sep + glossPart;   // both
  }

  // ── Render a single picker element ───────────────────────────────────────

  function renderPicker(el) {
    if (el.dataset.lpInit) return;
    el.dataset.lpInit = '1';

    var items    = JSON.parse(el.getAttribute('data-items')  || '[]');
    var answer   = (el.getAttribute('data-answer') || '').trim();
    var mode     = el.getAttribute('data-mode')    || 'both';
    var template = el.getAttribute('data-template')|| '___';
    var okMsg    = el.getAttribute('data-ok')  || 'Correct \u2713';
    var nokMsg   = el.getAttribute('data-nok') || 'Not quite — try again.';

    // Shuffle chips so the first item isn't always the answer
    var shuffled = items.slice().sort(function () { return Math.random() - 0.5; });

    // Split template on ___
    var parts  = template.split('___');
    var before = parts[0] !== undefined ? parts[0] : '';
    var after  = parts[1] !== undefined ? parts[1] : '';

    // Unique IDs for ARIA
    var uid    = 'lp-' + Math.random().toString(36).slice(2, 8);
    var slotId = uid + '-slot';
    var fbId   = uid + '-fb';

    // Build chip buttons
    var chipsHTML = shuffled.map(function (item) {
      return '<button class="lp-chip" type="button"'
        + ' data-form="' + esc(item.form) + '"'
        + ' aria-label="' + esc(item.form) + (item.gloss ? ': ' + esc(item.gloss) : '') + '">'
        + chipHTML(item, mode)
        + '</button>';
    }).join('');

    el.className += ' lp-wrap';
    el.innerHTML =
      '<div class="lp-template-line" aria-live="polite">'
      + '<span class="lp-tpl-prefix">' + esc(before) + '</span>'
      + '<span class="lp-slot lp-slot--empty" id="' + slotId + '" aria-label="blank">___</span>'
      + '<span class="lp-tpl-suffix">' + esc(after) + '</span>'
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

        // Clear previous attempt
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
          // Auto-reset after a short delay so the learner sees the feedback
          setTimeout(function () {
            chip.classList.remove('lp-chip--selected', 'lp-chip--wrong');
            slot.className = 'lp-slot lp-slot--empty';
            slot.textContent = '___';
            fb.hidden = true;
            fb.className = 'lp-feedback';
          }, 1400);
        }
      });
    });
  }

  // ── Page-level init ───────────────────────────────────────────────────────

  function init() {
    document.querySelectorAll('.tn-learn-picker').forEach(renderPicker);
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

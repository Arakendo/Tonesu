// datatables-init.js
// Adds filter + sort to registry tables via DataTables 2.x
// DataTables CSS is intentionally not loaded — Material theme styling is used instead.

(function () {
  var TARGETS = [
    /\/tonesu\/registry\/?$/,
    /\/tonesu\/registry\/index\/?$/,
    /\/tonesu\/registry\/overview\/?$/,
    /\/tonesu\/registry\/english\/?$/,
    /\/tonesu\/registry\/colloquial\/?$/,
    /\/tonesu\/registry\/colloquial-english\/?$/,
    /\/tonesu\/registry\/words\/W\d+\/?$/,
  ];

  function isTargetPage() {
    return TARGETS.some(function (p) { return p.test(window.location.pathname); });
  }

  // Map header text → CSS class for column styling
  var COL_CLASSES = {
    'Word':      'col-word',
    'W#':        'col-wnum',
    'Status':    'col-status',
    'Gloss':     'col-gloss',
    'English':   'col-english',
    // Colloquial registry columns
    'CLQ ID':    'col-clqid',
    'Form':      'col-word',
    'Formal':    'col-formal',
    'Stub':      'col-word',
    'First use': 'col-firstuse',
    // Word detail page corpus table
    'S#':        'col-snum',
    'Tonesu':    'col-tonesu',
    'Natural':   'col-natural',
  };

  function applyColumnClasses(table) {
    var headers = table.querySelectorAll('thead th');
    var classMap = {};  // column index → class name
    headers.forEach(function (th, i) {
      var cls = COL_CLASSES[th.textContent.trim()];
      if (cls) {
        th.classList.add(cls);
        classMap[i] = cls;
      }
    });
    table.querySelectorAll('tbody tr').forEach(function (tr) {
      tr.querySelectorAll('td').forEach(function (td, i) {
        if (classMap[i]) td.classList.add(classMap[i]);
      });
    });
  }

  function initTables() {
    if (!isTargetPage()) return;
    if (!window.DataTable) return;
    try {
      document.querySelectorAll('.md-content__inner table').forEach(function (table) {
        // Skip tables whose first header isn't a known registry column — e.g. the
        // 2-column metadata table on word pages (Domain / Class / Type / …).
        var firstTh = table.querySelector('thead th');
        if (!firstTh || !COL_CLASSES[firstTh.textContent.trim()]) return;
        if (!window.DataTable.isDataTable(table)) {
          new window.DataTable(table, {
            paging: true,
            pageLength: 50,
            info: true,
            layout: {
              topStart: { search: { placeholder: 'Filter…' } },
              topEnd: null,
              bottomStart: 'info',
              bottomEnd: 'paging',
            },
          });
          applyColumnClasses(table);
        }
      });
    } catch (e) {
      console.error('[datatables-init]', e);
    }
  }

  // Material SPA observable — fires on initial load and each navigation
  if (typeof document$ !== 'undefined' && document$ && typeof document$.subscribe === 'function') {
    document$.subscribe(function () { setTimeout(initTables, 0); });
  }

  // Also handle direct page loads where document$ may not replay
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTables);
  } else {
    // DOM already parsed — run immediately
    initTables();
  }
})();

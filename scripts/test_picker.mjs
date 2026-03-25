// Quick test to trace multi-blank picker logic
function esc(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

// Exercise 1 data
const dataAnswers = '["to","li"]';
const dataTemplate = '___-___';
const dataItems = '[{"form":"to","gloss":"knowledge"},{"form":"li","gloss":"person"},{"form":"ki","gloss":"motion"},{"form":"ne","gloss":"relation"},{"form":"mu","gloss":"artifact"},{"form":"su","gloss":"structure"}]';

const answers = JSON.parse(dataAnswers);
const baseItems = JSON.parse(dataItems);
const template = dataTemplate;
const n = answers.length;
const segments = template.split('___');

console.log('=== Exercise 1 trace ===');
console.log('answers:', answers, 'n:', n);
console.log('segments:', segments, 'len:', segments.length, '(need n+1 =', n+1, ')');
console.log('segments match?', segments.length === n + 1);

// Check slotPools + perSlot
const slotPools = answers.map(() => baseItems);
const perSlot = slotPools.some((pool, i) => JSON.stringify(pool) !== JSON.stringify(slotPools[0]));
console.log('perSlot:', perSlot);  // expect false

// Simulate click on 'to' (correct)
let current = 0;
let done = false;

function simulateClick(chipForm) {
  if (done) { console.log('DONE, ignoring'); return; }
  console.log('\n--- Click:', chipForm, '| current:', current, '| expected:', answers[current]);
  const form = chipForm;
  const expected = answers[current];
  if (form === expected) {
    console.log('CORRECT slot', current);
    current++;
    if (current >= n) {
      done = true;
      console.log('ALL DONE - show ok feedback');
    } else {
      console.log('Advance to slot', current);
    }
  } else {
    console.log('WRONG: form="' + form + '" expected="' + expected + '"');
  }
}

simulateClick('to');   // should be correct
simulateClick('li');   // should complete

/**
 * Web Speech API wrapper for Tonesu pronunciation
 * Uses phonetic respelling so TTS engines produce correct CV syllables
 */

/**
 * Phonetic respelling map for Tonesu primitives.
 * Keys are Tonesu roots; values are strings a Spanish TTS voice
 * will pronounce correctly (Spanish has near-identical vowel values
 * and clean CV syllable structure).
 */
const PRONUNCIATION = {
  mu: 'moo',  ma: 'ma',   zo: 'zo',   li: 'lee',
  ki: 'kee',  ka: 'ka',   be: 'bay',  de: 'day',
  su: 'sue',  to: 'toe',  fe: 'fay',
  ne: 'nay',  pe: 'pay',  go: 'go',   du: 'do',   zi: 'zee',
  pa: 'pa',   di: 'dee',  ko: 'co',
  ti: 'tee',  re: 'ray',
  se: 'say',  so: 'so',   lu: 'loo',  si: 'see',
  ra: 'rah',  ha: 'ha',
  nu: 'gnu',  ru: 'roo',  pu: 'pooh',
  vo: 'voe',  wi: 'wee',  no: 'no',   fa: 'fa',
  mi: 'me',
};

class TonesuSpeaker {
  constructor() {
    this.synth = window.speechSynthesis;
    this.isSupported = !!this.synth;
  }

  speak(text, options = {}) {
    if (!this.isSupported) return;
    this.synth.cancel();

    // Use phonetic respelling if available, otherwise pass through
    const spoken = PRONUNCIATION[text.toLowerCase()] || text;

    const utterance = new SpeechSynthesisUtterance(spoken);
    utterance.rate = options.rate ?? 0.8;
    utterance.pitch = options.pitch ?? 1.0;
    utterance.volume = options.volume ?? 1.0;
    utterance.lang = 'en-US';

    // Prefer Microsoft Zira if available
    const voices = this.synth.getVoices();
    const zira = voices.find(v => v.name.includes('Zira'));
    if (zira) utterance.voice = zira;

    this.synth.speak(utterance);
  }

  stop() {
    if (this.isSupported) this.synth.cancel();
  }
}

// Global instance
const tonesuSpeaker = new TonesuSpeaker();

/**
 * Initialize speaker buttons on page load
 * Attach to elements with class "tonesu-speaker" and data-text attribute
 */
function initSpeakerButtons() {
  const buttons = document.querySelectorAll('.tonesu-speaker');
  
  buttons.forEach(button => {
    button.addEventListener('click', function(e) {
      e.preventDefault();
      const text = this.getAttribute('data-text') || this.textContent;
      tonesuSpeaker.speak(text);
      
      // Visual feedback
      this.classList.add('speaking');
      setTimeout(() => this.classList.remove('speaking'), 500);
    });
  });
}

// Initialize on every page load.
// MkDocs Material's navigation.instant replaces DOM on navigation without a full
// reload, so DOMContentLoaded only fires once. material exposes document$ which
// fires after every page transition — use it when available.
if (typeof document$ !== 'undefined') {
  document$.subscribe(initSpeakerButtons);
} else if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initSpeakerButtons);
} else {
  initSpeakerButtons();
}

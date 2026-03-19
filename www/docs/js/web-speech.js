/**
 * Web Speech API wrapper for Tonesu pronunciation
 * Speaks text using browser's native TTS engine
 * Quality varies by browser — Firefox and Chrome generally sound best
 */

class TonesuSpeaker {
  constructor() {
    this.synth = window.speechSynthesis;
    this.isSupported = !!this.synth;
    this.currentUtterance = null;
  }

  /**
   * Speak text with Tonesu-appropriate settings
   * @param {string} text - Text to pronounce
   * @param {object} options - Optional settings {rate, pitch, volume}
   */
  speak(text, options = {}) {
    if (!this.isSupported) {
      console.warn('Web Speech API not supported in this browser');
      return;
    }

    // Cancel any ongoing speech
    this.synth.cancel();

    const utterance = new SpeechSynthesisUtterance(text);
    
    // Default to slower rate so syllables are clear
    utterance.rate = options.rate ?? 0.85;
    utterance.pitch = options.pitch ?? 1.0;
    utterance.volume = options.volume ?? 1.0;

    this.currentUtterance = utterance;
    this.synth.speak(utterance);
  }

  /**
   * Stop current speech
   */
  stop() {
    if (this.isSupported) {
      this.synth.cancel();
    }
  }

  /**
   * Check if currently speaking
   */
  isSpeaking() {
    return this.isSupported && this.synth.speaking;
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

// Initialize when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initSpeakerButtons);
} else {
  initSpeakerButtons();
}

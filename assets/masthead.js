const slot = document.querySelector('.masthead-slot');
const masthead = slot.querySelector('.masthead');
const content = slot.querySelector('.masthead__content');
const name = slot.querySelector('h1');
const reduced = matchMedia('(prefers-reduced-motion: reduce)');
let range;
let start;
let lastY = scrollY;
let lastTime = performance.now();
let lastSpeed = 0;
let nudge = 0;
let pending = false;
let glintArmed = false;
masthead.addEventListener('animationend', event => {
  if (event.animationName === 'edge-glint') masthead.classList.remove('masthead--glint');
});

function render(now) {
  pending = false;
  const y = Math.max(0, scrollY);
  const ratio = Math.min(1, Math.max(0, (y - start) / range));
  slot.toggleAttribute('data-pinned', y >= start);
  const dt = Math.max(8, now - lastTime);
  const speed = (y - lastY) / dt;
  const acceleration = dt < 100 ? (speed - lastSpeed) / dt : 0;
  // Only the name responds to input dynamics. The header edges track position exactly.
  nudge = Math.min(.035, Math.abs(acceleration) * .08 + nudge * Math.exp(-dt / 55));
  const frame = reduced.matches ? Number(ratio >= .5) : ratio;
  // Width settles at 30%. Rearm below the opening phase to avoid flicker near that edge.
  if (reduced.matches) {
    glintArmed = false;
    masthead.classList.remove('masthead--glint');
  } else if (ratio <= .15) {
    glintArmed = true;
  } else if (glintArmed && ratio >= .30) {
    masthead.classList.add('masthead--glint');
    glintArmed = false;
  }
  const nameFrame = frame + nudge * 4 * frame * (1 - frame);
  slot.style.setProperty('--frame', -frame + 's');
  name.style.setProperty('--frame', -Math.min(1, nameFrame) + 's');
  lastY = y;
  lastTime = now;
  lastSpeed = speed;
  if (frame > 0 && frame < 1 && nudge > .0002) schedule();
}

function schedule() {
  if (!pending) {
    pending = true;
    requestAnimationFrame(render);
  }
}

function measure() {
  // The slot's document offset is fixed by the page padding, even when sticky.
  const main = slot.parentElement;
  start = main.getBoundingClientRect().top + scrollY;
  range = Number(getComputedStyle(slot).getPropertyValue('--scroll-range'));
  slot.style.setProperty('--content-width', main.clientWidth + 'px');
  slot.style.setProperty('--viewport-width', document.documentElement.clientWidth + 'px');
  main.style.setProperty('--open-height', content.offsetHeight + 'px');
  const rootSize = parseFloat(getComputedStyle(document.documentElement).fontSize);
  const nameRatio = Number(getComputedStyle(slot).getPropertyValue('--compact-name-ratio'));
  const compactScale = nameRatio * rootSize / parseFloat(getComputedStyle(name).fontSize);
  slot.style.setProperty('--compact-scale', compactScale);
  slot.style.setProperty('--compact-name-width', name.querySelector('a').offsetWidth * compactScale + 'px');
  slot.dataset.ready = '';
  schedule();
}

new ResizeObserver(measure).observe(content);
document.fonts.ready.then(measure);
addEventListener('resize', measure);
addEventListener('scroll', schedule, {passive: true});
reduced.addEventListener('change', schedule);
measure();

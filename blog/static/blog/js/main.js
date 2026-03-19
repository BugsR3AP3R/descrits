// Des Écrits et des Non-Écrits — JS

// Scroll to top
const scrollBtn = document.querySelector('.scroll-top');
if (scrollBtn) {
  window.addEventListener('scroll', () => {
    scrollBtn.classList.toggle('visible', window.scrollY > 400);
  });
  scrollBtn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
}

// Translation functionality (Google Translate style via URL param)
function translatePage(lang) {
  const current = window.location.href;
  if (lang === 'fr') {
    window.location.href = current.split('?')[0];
  } else {
    // Using Google Translate free widget
    window.open(`https://translate.google.com/translate?sl=fr&tl=${lang}&u=${encodeURIComponent(current)}`, '_blank');
  }
}

// Smooth reveal on scroll
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.post-card').forEach(card => {
  card.style.opacity = '0';
  card.style.transform = 'translateY(20px)';
  card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
  observer.observe(card);
});

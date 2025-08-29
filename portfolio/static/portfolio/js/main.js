window.addEventListener('DOMContentLoaded', () => {
  // Animación de inicio
  const intro = document.getElementById('intro-animation');
  const text = intro.querySelector('.intro-text');
  setTimeout(() => {
    text.style.opacity = 1;
  }, 400);
  setTimeout(() => {
    intro.classList.add('active');
  }, 1700);
  setTimeout(() => {
    intro.style.opacity = 0;
    intro.style.pointerEvents = 'none';
  }, 2400);
  setTimeout(() => {
    intro.remove();
    // Mostrar el contenido principal
    document.querySelectorAll('.hidden-after-intro').forEach(el => {
      el.classList.add('visible-after-intro');
    });
    // Ocultar solo la imagen de portada si es necesario
    const portada = document.querySelector('.ocultar-despues-intro');
    if (portada) portada.classList.add('ocultar');
  }, 3000);
});

// Pantalla completa para imágenes de Photoshop
document.querySelectorAll('.ps-thumb').forEach(img => {
  img.addEventListener('click', () => {
    const viewer = document.getElementById('fullscreen-viewer');
    const fullImg = document.getElementById('fullscreen-img');
    // Asigna el src y muestra el visor solo si hay imagen
    if (img.src) {
      fullImg.src = img.src;
      viewer.classList.remove('fullscreen-hidden');
      fullImg.style.display = 'block';
    }
  });
});

// Cerrar visor de pantalla completa
document.getElementById('fullscreen-viewer').addEventListener('click', () => {
  const viewer = document.getElementById('fullscreen-viewer');
  const fullImg = document.getElementById('fullscreen-img');
  viewer.classList.add('fullscreen-hidden');
  fullImg.style.display = 'none';
  fullImg.src = '';
});
// Carrusel para el proyecto Space Invaders
document.querySelectorAll('.slider').forEach(slider => {
  const imgs = slider.querySelectorAll('.slider-img');
  let idx = 0;

  function showImg(i) {
    imgs.forEach((img, j) => img.classList.toggle('active', j === i));
  }

  slider.querySelector('.slider-btn.prev').addEventListener('click', () => {
    idx = (idx - 1 + imgs.length) % imgs.length;
    showImg(idx);
  });

  slider.querySelector('.slider-btn.next').addEventListener('click', () => {
    idx = (idx + 1) % imgs.length;
    showImg(idx);
  });

  // Ampliar imagen activa al hacer clic
  imgs.forEach(img => {
    img.addEventListener('click', () => {
      if (img.classList.contains('active')) {
        const viewer = document.getElementById('fullscreen-viewer');
        const fullImg = document.getElementById('fullscreen-img');
        fullImg.src = img.src;
        fullImg.style.display = 'block'; // <-- Asegura que la imagen se muestre
        viewer.classList.remove('fullscreen-hidden');
      }
    });
  });
});

// Botón de modo oscuro/claro
document.getElementById('toggle-dark').addEventListener('click', () => {
  document.body.classList.toggle('dark-mode');
});

// Scroll manual hasta arriba para "Sobre mí"
document.getElementById('link-sobre-mi').addEventListener('click', function(e) {
  e.preventDefault();
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

document.addEventListener("DOMContentLoaded", () => {
  const posts = document.querySelectorAll(".post");
  posts.forEach((post, index) => {
    setTimeout(() => {
      post.classList.add("animate-in");
    }, index * 150); // secuencia: 0.15s entre cada post
  });
});
document.addEventListener('click', function(e) {
  // Mostrar formulario de crear post en el portfolio
  if (e.target.matches('.btn-crear-post')) {
    e.preventDefault();
    fetch(e.target.href, {headers: {'X-Requested-With': 'XMLHttpRequest'}})
      .then(r => r.text())
      .then(html => {
        document.getElementById('blog-container').innerHTML = html;
      });
  }
  // Volver al listado de posts
  if (e.target.matches('.btn-cancel')) {
    e.preventDefault();
    fetch('/blog/', {headers: {'X-Requested-With': 'XMLHttpRequest'}})
      .then(r => r.text())
      .then(html => {
        document.getElementById('blog-container').innerHTML = html;
      });
  }
});
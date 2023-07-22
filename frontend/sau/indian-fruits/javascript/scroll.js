function scrollToElement(element) {
    element.scrollIntoView({ behavior: "smooth" });
  }
  
  function scrollToAnchor() {
    const hash = window.location.hash;
    if (hash) {
      const targetElement = document.querySelector(hash);
      if (targetElement) {
        scrollToElement(targetElement);
      }
    }
  }

  window.onload = scrollToAnchor;
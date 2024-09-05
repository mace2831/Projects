const observer = new MutationObserver(() => {
    const rufusPopup = document.querySelector('.rufus-panel-container'); 
    if (rufusPopup) {
      rufusPopup.remove();
      console.log('Rufus AI pop-up blocked.');
    }
  });
  
  // Observe the entire document for changes
  observer.observe(document.body, { childList: true, subtree: true });
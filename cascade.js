const rows = document.querySelectorAll('tbody tr');
rows.forEach((row, index) => {
  row.style.setProperty('--delay', index);
  row.classList.add('visible');
});

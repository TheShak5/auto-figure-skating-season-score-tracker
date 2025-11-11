const rows = document.querySelectorAll('tbody tr');
rows.forEach((row, index) => {
  row.style.setProperty('--delay', index);
  row.classList.add('visible');
});

const rows = document.querySelectorAll('tbody tr');
rows.forEach(row => {
  const rankCell = row.querySelector('td'); // assuming rank is in the first <td>
  if (!rankCell) return;
  const rank = rankCell.textContent.trim();

  if (rank === "1") {
    row.classList.add('gold-row');
  } else if (rank === "2") {
    row.classList.add('silver-row');
  } else if (rank === "3") {
    row.classList.add('bronze-row');
  }
});
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

function sortTableAndHighlightMedals() {
  const tbody = document.querySelector('table tbody');
  const rows = Array.from(tbody.rows);

  // Sort rows by rank (assumed to be in first cell)
  rows.sort((a, b) => {
    const rankA = parseInt(a.cells[0].textContent.trim(), 10);
    const rankB = parseInt(b.cells[0].textContent.trim(), 10);
    return rankA - rankB;
  });

  // Clear and re-add rows in sorted order with highlight
  tbody.innerHTML = '';
  rows.forEach((row, index) => {
    row.classList.remove('gold-row', 'silver-row', 'bronze-row');
    if (index === 0) {
      row.classList.add('gold-row');
    } else if (index === 1) {
      row.classList.add('silver-row');
    } else if (index === 2) {
      row.classList.add('bronze-row');
    }
    tbody.appendChild(row);
  });
}

// Call this function after the table content is loaded or when sorting is triggered
window.onload = () => {
  sortTableAndHighlightMedals();
};

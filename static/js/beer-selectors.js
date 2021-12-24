const beerSelector = document.getElementById('beer-select');
const selectedInfo = document.getElementById('selected-beer-info');

selectedInfo.innerHTML = document.getElementById(`beer-id-${beerSelector.value}`).innerHTML

beerSelector.addEventListener('change', function(e) {
    const selectedId = e.target.value;
    const selectedInfo = document.getElementById('selected-beer-info');
    selectedInfo.innerHTML = document.getElementById(`beer-id-${selectedId}`).innerHTML
});

document.addEventListener('DOMContentLoaded', function() {
    const params = new URLSearchParams(window.location.search);
    const keywords = params.get('keywords') ? params.get('keywords').split(',') : [];
    console.log(keywords);
    const clothingItems = document.querySelectorAll('.panel');

    // Hide all items first
    //clothingItems.forEach(item => {
    //    item.style.display = 'none';
//});



// Display items that match the keywords

keywords.forEach(keyword => {
document.querySelectorAll(`.panel.${keyword}`).forEach(item => {
 item.style.display = 'none';
  });
  });
});
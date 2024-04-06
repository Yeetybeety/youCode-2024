const tags = document.querySelectorAll('.tag');
        tags.forEach(tag => {
            tag.addEventListener('change', () => {
                tag.nextElementSibling.classList.toggle('bg-blue-500');
                tag.classList.toggle('selected');
            });
        });

// Get the form element by its ID
var form = document.getElementById('bg-white rounded-lg shadow-md p-4');

// Add a submit event listener to the form
form.addEventListener('submit', function(event) {
  // Prevent the default form submission behavior
  event.preventDefault();
  
  // Get the selected tags
  var selectedTags = [];
  document.querySelectorAll('.tag.selected').forEach(function(selectedTag) {
    selectedTags.push(selectedTag.getAttribute('data-tag'));
  });
  
  // Set the selected tags as the value of the hidden input field
  document.getElementById('tags').value = selectedTags.join(',');
  
  // Optionally, submit the form data to a server or perform other actions
  console.log('Selected Tags:', selectedTags);

});
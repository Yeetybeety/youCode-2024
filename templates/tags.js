const tags = document.querySelectorAll('.tag');
        tags.forEach(tag => {
            tag.addEventListener('change', () => {
                tag.nextElementSibling.classList.toggle('bg-blue-500');
                tag.classList.toggle('selected');
            });
        });

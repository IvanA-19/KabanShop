const categoryItems = document.querySelectorAll('.category-item');

categoryItems.forEach(item => {
    const categoryId = item.parentElement.id.split('-')[1];
    const description = document.getElementById(`description-${categoryId}`);
    item.addEventListener('mouseover', () => {
        description.style.display = 'block';
    });
    item.addEventListener('mouseout', () => {
        description.style.display = 'none';
    });
});

const images = document.querySelectorAll('.category-image');
const maxHeight = 200; // Максимальная высота изображения

images.forEach(image => {
  image.onload = () => {
    let width = image.width;
    let height = image.height;

    if (height > maxHeight) {
      width *= maxHeight / height;
      height = maxHeight;
    }

    image.style.width = `${width}px`;
    image.style.height = `${height}px`;
  };
});
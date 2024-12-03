const images = document.querySelectorAll('.product-image');
const maxHeight = 200; // Максимальная высота изображения

images.forEach(image => {
    image.onload = () => {
        let width = image.width;
        let height = image.height;

        if (height > maxHeight) {
            const ratio = maxHeight / height;
            width *= ratio;
            height = maxHeight;
        }

        image.style.width = `${width}px`;
        image.style.height = `${height}px`;
    };
});

const productItems = document.querySelectorAll('.product-item');

productItems.forEach(item => {
    const productId = item.id.split('-')[1];
    const description = document.getElementById(`description-${productId}`);
    item.addEventListener('mouseover', () => {
        description.style.display = 'block';
    });
    item.addEventListener('mouseout', () => {
        description.style.display = 'none';
    });
});
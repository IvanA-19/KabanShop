const swiper = new Swiper('.mySwiper', {
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    mousewheel: true,
    autoplay: {
        delay: 3000,
        disableOnInteraction: false,
    },
    loop: true, // Добавлена опция loop: true
});
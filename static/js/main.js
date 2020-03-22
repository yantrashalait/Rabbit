(function($) {
'use strict'; 
$(document).ready(function(){
    $('.rabbit__footage__slider').owlCarousel({
            loop: true,
            rewind: true,
            responsiveClass: true,
            nav: true,
            smartSpeed: 500,
            dots: false,
            navText: ['<i class="fa fa-angle-left" aria-hidden="true"></i>', '<i class="fa fa-angle-right" aria-hidden="true"></i>'],
            responsive:{
                0:{
                    items:1
                },
                600:{
                    items:1
                },
                1000:{
                    items:1
                }
            }
        });    

    $('.story__yeller__caro').owlCarousel({
            loop: true,
            rewind: true,
            responsiveClass: true,
            nav: true,
            smartSpeed: 500,
            dots: false,
            navText: ['<i class="fa fa-angle-left" aria-hidden="true"></i>', '<i class="fa fa-angle-right" aria-hidden="true"></i>'],
            responsive:{
                0:{
                    items:1
                },
                600:{
                    items:1
                },
                1000:{
                    items:1
                }
            }
        });
    
    $('.success__stories__rabbit').owlCarousel({
            loop: true,
            rewind: true,
            responsiveClass: true,
            nav: true,
            smartSpeed: 500,
            dots: false,
            navText: ['<i class="fa fa-circle" aria-hidden="true"></i>', '<i class="fa fa-circle" aria-hidden="true"></i>'],
            responsive:{
                0:{
                    items:1
                },
                600:{
                    items:1
                },
                1000:{
                    items:1
                }
            }
        });

// Gallery page popup
$('.pdetails-imagezoom').lightGallery({
    selector: '.pdetails-singleimage',
    thumbnail:false,
    subHtmlSelectorRelative: true
});



// Height of story yellers video box
var hgt = $('.story__yeller__img').outerHeight();
$('.ply__vdo__story').css({'height' : hgt + 'px'});

 /* Product Details Image Slider */
    $('.pdetails-largeimages').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        dots: false,
        fade: true,
        asNavFor: '.pdetails-thumbs'
    });

    $('.pdetails-thumbs:not(.pdetails-thumbs-vertical)').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        asNavFor: '.pdetails-largeimages',
        arrows: true,
        dots: false,
        focusOnSelect: true,
        vertical: false
    });

});// document ready

// Masonry
$(window).load(function() {
    var $container = $('.portfolio-masonry');
    $container.masonry({
        columnWidth: 5,
        itemSelector: '.portfolio-masonry li'
    });
});
})(window.jQuery);  
 

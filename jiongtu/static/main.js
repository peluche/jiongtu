var canvas = document.querySelector("#jiong");
var ctx = canvas.getContext('2d');

function create_image(pixels) {
    // pixels are (x, y, r, g, b)
    var w = 100, h = 100;
    var imagedata = ctx.createImageData(w, h);
    pixels.forEach(function(pixel) {
        var x = pixel[0], y = pixel[1];
        imagedata.data[((w * y) + x) * 4] = pixel[2];
        imagedata.data[((w * y) + x) * 4 + 1] = pixel[3];
        imagedata.data[((w * y) + x) * 4 + 2] = pixel[4];
        imagedata.data[((w * y) + x) * 4 + 3] = 255;
    });
    return imagedata;
}

function draw(pixels) {
    ctx.putImageData(create_image(pixels), 0, 0);
}

function getData() {
    var request = new XMLHttpRequest();
    request.open('GET', '/i', true);
    request.onload = function() {
        var response = JSON.parse(request.responseText);
        images = response['images'];
        if (images.length > 0) {
            draw(images[0]);
        }
    }
    request.send();
}

var images = []
var frame = 0;

function animate() {
    frame++;
    console.log('frame: ', frame);
    window.requestAnimationFrame(animate);
    if (images.length > 0) {
        draw(images[frame % images.length]);
    }
}

animate();
getData();

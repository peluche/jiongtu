var canvas = document.querySelector("#jiong");
var ctx = canvas.getContext('2d');

function create_image(pixels) {
    // pixels are (x, y, r, g, b)
    var imagedata = ctx.createImageData(width, height);
    pixels.forEach(function(pixel) {
        var x = pixel[0], y = pixel[1];
        imagedata.data[((width * y) + x) * 4] = pixel[2];
        imagedata.data[((width * y) + x) * 4 + 1] = pixel[3];
        imagedata.data[((width * y) + x) * 4 + 2] = pixel[4];
        imagedata.data[((width * y) + x) * 4 + 3] = 255;
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
        width = response['width'];
        height = response['height'];
        images = response['images'];
        if (images.length == 1) {
            draw(images[0], width, height)
        } else if (images.length > 1) {
            animate();
        }
    }
    request.send();
}

function animate() {
    frame++;
    window.requestAnimationFrame(animate);
    draw(images[frame % images.length]);
}

var frame = 0, width = 0, height = 0, images = [];
getData();

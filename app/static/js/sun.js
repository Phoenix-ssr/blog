document.addEventListener("DOMContentLoaded", go);
function go() {
    "use strict";
    let canvas = document.querySelector('canvas');
    let ctx = canvas.getContext('2d');
    canvas.style = 'width: 100%; height: 100%; object-fit:contain; background:#000;';
    let frame = 0;
    function onFrame() {
        canvas.width = 512;
        canvas.height = 256;
        godraysCanvas.width = 128;
        godraysCanvas.height = 64;
        let sunY = Math.cos(frame++ / 512) * 24; // This is actually the offset from the middle of the canvas.
        let godraysCtx = godraysCanvas.getContext('2d');
        let emissionGradient = godraysCtx.createRadialGradient(
            godraysCanvas.width / 2, godraysCanvas.height / 2 + sunY, // The sun's center.
            0,                                                        // Start radius.
            godraysCanvas.width / 2, godraysCanvas.height / 2 + sunY, // Sun's center again.
            44                                                        // End radius.
        );
        godraysCtx.fillStyle = emissionGradient;
        emissionGradient.addColorStop(.1, '#0C0804'); // Color for pixels in radius 0 to 4.4 (44 * .1).
        emissionGradient.addColorStop(.2, '#060201'); // Color for everything past radius 8.8.
        godraysCtx.fillRect(0, 0, godraysCanvas.width, godraysCanvas.height);
        godraysCtx.fillStyle = '#000';
        let skyGradient = ctx.createLinearGradient(0, 0, 0, canvas.height);
        skyGradient.addColorStop(0, '#2a3e55'); // Blueish at the top.
        skyGradient.addColorStop(.7, '#8d4835'); // Reddish at the bottom.
        ctx.fillStyle = skyGradient;
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        function mountainHeight(position, roughness) {
            let frequencies = [1721, 947, 547, 233, 73, 31, 7];
            return frequencies.reduce((height, freq) => height * roughness - Math.cos(freq * position), 0);
        }
        for(let i = 0; i < 4; i++) {
            ctx.fillStyle = `hsl(7, 23%, ${23-i*6}%)`;
            for(let x = canvas.width; x--;) {
                let mountainPosition = (frame+frame*i*i) / 1000 + x / 2000;
                let mountainRoughness = i / 19 - .5;
                let y = 128 + i * 25 + mountainHeight(mountainPosition, mountainRoughness) * 45;
                ctx.fillRect(x, y, 1, 999); // 999 can be any large number...
                godraysCtx.fillRect(x/4, y/4+1, 1, 999);
            }
        }
        ctx.globalCompositeOperation = godraysCtx.globalCompositeOperation = 'lighter';
        for(let scaleFactor = 1.07; scaleFactor < 5; scaleFactor *= scaleFactor) {
            godraysCtx.drawImage(
                godraysCanvas,
                (godraysCanvas.width - godraysCanvas.width * scaleFactor) / 2,
                (godraysCanvas.height - godraysCanvas.height * scaleFactor) / 2 - sunY * scaleFactor + sunY,
                godraysCanvas.width * scaleFactor,
                godraysCanvas.height * scaleFactor
            );
        }
        ctx.drawImage(godraysCanvas, 0, 0, canvas.width, canvas.height);
        requestAnimationFrame(onFrame);
    }
    let godraysCanvas = canvas.cloneNode();
    onFrame();
    let encodedMelody = "!!----,*,(444420/20/-0/---,,--//((4444202/;;;;986986420/00--//,,";
    let voiceBuffer = []; // M = [...]
    let ksDelayBuffer = []; // Y = [...]
    let sampleOffset = 0; // V = 0 (used later)
    let J = 0; // What the hell is J????
}


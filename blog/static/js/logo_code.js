function randomInt(min, max){
    num = min + (max-min)*Math.random();
    return Math.floor(num);
}

function randomSign(){
    if(Math.random()<0.5){
        return 1;
    }
    else{
        return -1;
    }
}

class Ring{
    constructor(sAng, eAng, r, width, color="#FFFFFF", rotationSpeed=0){
        this.sAng =sAng;
        this.eAng = eAng;
        this.r = r;
        this.width = width;
        this.color = color;
        this.rotSpeed= rotationSpeed/2000/Math.PI; //Umdrehungen pro Sekunde
        this.time = Date.now();
        this.active = false;
    }

    draw(){
        this.rotate((Date.now()-this.time));
        this.time = Date.now();
        ctx.beginPath();
        ctx.lineCap ="round";
        ctx.strokeStyle = this.color;
        ctx.lineWidth = this.width;
        ctx.arc(xcenter,ycenter, this.r,this.sAng, this.eAng);
        ctx.stroke();
    }

    rotate(timePassed){
        this.sAng += timePassed*this.rotSpeed;
        this.eAng += timePassed*this.rotSpeed;
        this.sAng = this.sAng%(2*Math.PI);
        this.eAng = this.eAng%(2*Math.PI);
    }
}

class floatingThing{
    constructor(url, r, angle, speed, smallSpeed, radialSpeed, width, height){
        this.r =r;
        this.start= [r, angle, height, width];
        this.angle = angle;
        this.speed = speed/2/Math.PI;
        this.smallSpeed = smallSpeed/2000/Math.PI;
        this.radialSpeed = radialSpeed/1000; //px per second
        this.image = new Image();
        this.image.src = url;
        this.time = Date.now();
        this.loaded =false;
        this.width=width;
        this.height = height;
        this.smallAngle=0;
/*
        this.image.addEventListener("load", function() {
            this.loaded=true;
          }, false);*/
    }

    draw(){
        if(true){//this.loaded){
            
            this.angle += this.speed/this.r*(Date.now()-this.time);
            this.smallAngle += this.smallSpeed*(Date.now()-this.time);
            this.r -= this.radialSpeed*(Date.now()-this.time);
            this.time = Date.now();
            
            let x = Math.cos(this.angle)*this.r + xcenter;
            let y = Math.sin(this.angle)*this.r+ycenter;

            if(this.r<200){
                this.height = this.start[2]*Math.sqrt(this.r/200)
                this.width = this.start[3]*Math.sqrt(this.r/200)
            }
            //ctx.drawImage(this.image,xcenter-this.width/2,ycenter-this.height/2, this.width, this.height);
            //x =xcenter;
            //y= ycenter;
            ctx.save();
            ctx.translate(x,y);
            //this.smallAngle =Math.PI/3;
            ctx.rotate(this.smallAngle);
            ctx.drawImage(this.image, -this.width/2,-this.height/2, this.width, this.height);
            ctx.restore();

            if (this.r<20){
                this.r = this.start[0];
                this.angle = this.start[1];
                this.height = this.start[2];
                this.width = this.width[3];
            }
        }
        
    }

}
var width = 3000;
var height = 850;

var xcenter = width/2;
var ycenter = height/2;
var rings = 12;

// displays the same rings in one session
sessionStorage.setItem("ringList", null);
console.log(sessionStorage.getItem("ringList")=="null");
if (sessionStorage.getItem("ringList")==null || sessionStorage.getItem("ringList")=="null"){
    console.log("ringList undefined");
    ringList = new Array();
    let saveArray = new Array();
    //this generates random rings

    var blueColors =["32,178,170", "47,79,79", "0,206,209", "100,149,237", "25,25,112", "25,25,112",
                    "0,0,205", "0,255,255", "123,104,238", "153,50,204", "0,191,255", "0,0,128"]
    let i=0;
    while(i<rings){
        let sAng = Math.random()*2*Math.PI;
        let eAng = Math.random()*2*Math.PI;
        let r = Math.random()*330;
        let ring_width = Math.random()*60+30;
        let alpha = Math.random()*0.3 + 0.7;
        let color = "rgba("+blueColors[i]+","+alpha+")";//"rgb("+randomInt(0,256)+","+randomInt(0,256)+","+randomInt(0,256)+")";
        let speed = (r/100 +Math.random()*5)*randomSign();
        console.log(sAng, eAng, r, width, color, speed);
        if(ring_width<r){
            ringList[i] = new Ring(sAng, eAng, r, ring_width, color, speed);
            saveArray[i] = [sAng, eAng, r, ring_width, color, speed];
            i++;
        }
    }
    ringList[rings]= new Ring(0, Math.PI*2/3, 20, 30, "rgba(51, 102, 153,0.7)",10);
    ringList[rings+1]= new Ring(1.96, 0.41, 360, 34, 'rgba(0,191,255,0.7)', 10);

    sessionStorage.setItem("ringList",JSON.stringify(saveArray));
    console.log(sessionStorage.getItem("ringList"));
    console.log(JSON.parse(sessionStorage.getItem("ringList")));
}
else{
    let ringListString = sessionStorage.getItem("ringList");
    let arr = JSON.parse(ringListString);
    ringList = new Array();
    for (let i =0; i<arr.length; i++){
        let a=arr[i];
        ringList[i] = new Ring(a[0], a[1], a[2], a[3], a[4], a[5]);
    }
    ringList[rings]= new Ring(0, Math.PI*2/3, 20, 30, "rgba(51, 102, 153,0.7)",10);
    ringList[rings+1]= new Ring(1.96, 0.41, 410, 34, 'rgba(0,191,255,0.7)', 10);
}

if(sessionStorage.getItem('activeSite') =="about"){
    var sheep = new floatingThing("/Blog/pics/blog_sheep_adrift_transparent_background.png",
                             1000, Math.PI/2, 5,0, 10,140,160);
}


//function to draw all rings
function drawAll(){
    ctx.clearRect(0,0,width,height);
    for(let i=0; i<ringList.length; i++){
        ringList[i].draw();
    }
    //if(sessionStorage.getItem('activeSite') =="about"){
    //    sheep.draw();
    //}

    ctx.font = "200px 'Rubik Moonrocks'";
    ctx.fillText("Delve", xcenter- m.width/2, ycenter- height*0.01);
    ctx.fillText("Deeper", xcenter - m2.width/2, ycenter+text_height+ height*0.01 );
    ctx.font = "60px 'Ubuntu'";
    ctx.fillText("Quips, Quirks & Questions", xcenter-m3.width/2, ycenter + text_height*2);
    window.requestAnimationFrame(drawAll);
}


window.onload =function() {
    var canvasBox = document.getElementById("canvasBox");
    canvasBox.innerHTML= `<canvas id='logoCanvas' width=${width} height=${height}></canvas>`; //feeling fancy

    canvas = document.getElementById("logoCanvas"); //global variable
    canvasBox.appendChild(canvas);
    ctx = canvas.getContext("2d"); //global variable

    //specify location of heading
    ctx.fillStyle = "#FFFFFF";
    ctx.font = "200px 'Rubik Moonrocks'";
    m = ctx.measureText("Delve");
    m2 = ctx.measureText("Deeper");
    text_height = m.actualBoundingBoxAscent + m.actualBoundingBoxDescent;

    ctx.font = "60px 'Ubuntu'";
    m3= ctx.measureText("Quips, Quirks & Questions");

    drawAll();
}
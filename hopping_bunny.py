//variables defining
var bodyX = 36;
var bodyY = 316;
var bodyW = 107;
var bodyH = 86;
var faceW = bodyW/2.5;
var faceH = bodyW - 65;
var earW = 10;
var earH = earW*3;
var eyeSize = 5;
var tailWH = bodyW-93;
var cloudX1 =192;
var cloudY1 = 106;
var cloudX2 = 325;
var cloudY2 = 75;

draw = function() {
  
    
    background(228, 240, 240);
    stroke (207, 207, 207);
    
//background
    //hill
    noStroke ();
    fill (209, 235, 212);
    arc (201,426,531,196,182,402);
    
    //sun
    fill (255, 251, 212);
    ellipse (289,88,100,100);
 
    
    //clouds

    fill (252, 252, 252);
    ellipse (cloudX1,cloudY1,40,40);
    ellipse (cloudX1+33,cloudY1,60,60);
    ellipse (cloudX1+67,cloudY1,40,40);


    ellipse (cloudX2,cloudY2,40,40);
    ellipse (cloudX2+31,cloudY2,60,60);
    ellipse (cloudX2+64,cloudY2,40,40);

cloudX1-=1;
cloudX2+=1;

//body
    fill(252, 252, 252);
    ellipse (bodyX-55, bodyY-(-15),tailWH,tailWH); //tail
    ellipse(bodyX, bodyY, bodyW, bodyH); //main body
  
  //body,ears,head,whiskers,teeth,tail,eyes x's and y's are all dependent on bodyX and bodyY
  
//face
    
    //ears
    fill (250, 250, 250);
    ellipse (bodyX+57, bodyY-40, earW, earH); //ear 1
    fill (250, 227, 227);
    ellipse (bodyX+57, bodyY-39, earW-5, earH-12); 
    fill (255, 255, 255);
    ellipse (bodyX+50, bodyY-40, earW, earH); //ear 2
    fill (255, 227, 227);
    ellipse (bodyX+50, bodyY-39, earW-5, earH-12); 
    
    //head
    fill (255, 255, 255);
    ellipse(bodyX+56, bodyY-10, faceW, faceH);
    
    //eyes
    fill (0, 0, 0);
    ellipse (bodyX+63, bodyY-13,eyeSize,eyeSize);
    
    //nose
    fill (191, 185, 138);
    triangle (bodyX+75,bodyY-5,bodyX+73,bodyY-2,bodyX+72,bodyY-5);

    //mouth
    stroke (232, 204, 204);
    line (70+bodyX,0+bodyY,73+bodyX,-3+bodyY);
    line (74+bodyX,-3+bodyY,77+bodyX,0+bodyY);
        
        //teeth
        fill (230, 230, 230);
        rect (72+bodyX,-2+bodyY,1,1,4);
    
if(bodyY <= 317) {
    
bodyY = bodyY +1.5;
bodyX = bodyX +0.5;



}

else {
bodyY-=90;
bodyX +=50;
} 



};

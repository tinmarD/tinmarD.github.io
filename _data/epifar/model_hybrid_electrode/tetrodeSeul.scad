scale       = 100;
lMacro      = 6*scale;
rMacro      = 0.4*scale;
lMacroPlot  = 2*scale;
lMicro      = 0.5*scale;
rMicro      = 0.07*scale;
rMicroContact = 0.02*scale;
angleMicroY = 30;
microColor   = (1/255)*[220,193,171];
//microColor          = (1/255)*[255,255,0];
macroPlotColor      = (1/255)*[78,80,83];
macroNoPlotColor    = (1/255)*[238,225,213];
microContactColor   = (1/255)*[186,104,25];



module drawTetrode(){
    rotate([0,0,0]){
        difference(){
            color(microColor)
            cylinder(h=lMicro+rMicro,r1=rMicro,r2=rMicro,center=false,$fn=300);
            translate([0,0,lMicro+rMicro]){
                rotate([0,-60,0]){
                    cube(size=[10*rMicro,10*rMicro,1.75*rMicro],center=true);
                }
            }
        }
        difference(){
        for (angleMicroContact = [45,135,225,315]){
            rotate([0,0,angleMicroContact]){
                translate([0.035*scale,0,0]){
                    color(microContactColor)
                    cylinder(h=lMicro+rMicro,r1=rMicroContact,r2=rMicroContact,center=false,$fn=300);
                }
            }
        }
        translate([0,0,lMicro+rMicro]){
            rotate([0,-60,0]){
                cube(size=[10*rMicro,10*rMicro,1.6*rMicro],center=true);
                }
            }
        }
    }
}


drawTetrode();

//for (angleMicroX = [0,120,240]){
//    rotate([angleMicroX,0,0])
//    translate([0,0,rMacro-rMicro])
//    rotate([0,90-angleMicroY,0]){
//        difference(){
//            drawTetrode();
//        }
//    }
//                
//}


